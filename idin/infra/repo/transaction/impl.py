"""Declares :class:`TransactionRepository`."""
from .base import BaseTransactionRepository

from ...orm import Transaction


class TransactionRepository(BaseTransactionRepository):

    def persist_tx(self, dto):
      """Persists a Data Transfer Object (DTO) representing an
      iDIN transaction.
      """
      dao = self.dao_factory(Transaction, dto)
      self.session.add(dao)
      self.session.flush()
      return dao
