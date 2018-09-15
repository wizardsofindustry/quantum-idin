from .base import BaseTransactionRepository


class TransactionRepository(BaseTransactionRepository):

    def persist_tx(self):
        raise NotImplementedError("Subclasses must override this method.")
