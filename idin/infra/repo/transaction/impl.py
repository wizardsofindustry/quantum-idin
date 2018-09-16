"""Declares :class:`TransactionRepository`."""
import hashlib

from ...orm import Result
from ...orm import Transaction
from .base import BaseTransactionRepository


class TransactionRepository(BaseTransactionRepository):
    """Exposes an interface to mutate the state of iDIN transactions."""

    def persist_result(self, dto):
        """Persists the result of a succesful iDIN transaction."""
        dao = self.dao_factory(Result, dto)
        dao.checksum = self._calculate_checksum(dao)
        self.session.add(dao)
        self.session.flush()

    @staticmethod
    def _calculate_checksum(dao):
        h = hashlib.sha256()
        h.update(int.to_bytes(dao.retrieved, 8, 'big'))
        h.update(str.encode(dao.txid))
        h.update(str.encode(dao.issuer_id))
        h.update(str.encode(dao.bin))
        h.update(str.encode(dao.data))
        return h.digest()

    def setstatus(self, txid, status):
        """Sets the status of the transaction identified by `txid`."""
        self.session.query(Transaction)\
            .filter(Transaction.txid == txid)\
            .filter(Transaction.status == 'open')\
            .update({'status': status})

    def persist_tx(self, dto):
        """Persists a Data Transfer Object (DTO) representing an
        iDIN transaction.
        """
        dao = self.dao_factory(Transaction, dto)
        self.session.add(dao)
        self.session.flush()
        return dao
