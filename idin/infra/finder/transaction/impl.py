from .base import BaseTransactionFinder


class TransactionFinder(BaseTransactionFinder):

    def reference(self):
        raise NotImplementedError("Subclasses must override this method.")

    def result(self):
        raise NotImplementedError("Subclasses must override this method.")
