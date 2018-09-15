"""Declares :class:`TransactionFinder`."""
from ...orm import Transaction
from .base import BaseTransactionFinder


class TransactionFinder(BaseTransactionFinder):

    def reference(self, txid):
        """Returns the merchant reference for the transaction identified
        by `txid`.
        """
        return self.session.query(Transaction.ref)\
            .filter(Transaction.txid == txid)\
            .scalar()

    def result(self, txid, ec):
        raise NotImplementedError("Subclasses must override this method.")
