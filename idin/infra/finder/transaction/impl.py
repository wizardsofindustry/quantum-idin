from .base import BaseTransactionFinder


class TransactionFinder(BaseTransactionFinder):

    def reference(self, txid):
        raise NotImplementedError("Subclasses must override this method.")

    def result(self, txid, ec):
        raise NotImplementedError("Subclasses must override this method.")
