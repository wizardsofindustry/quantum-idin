"""Contains the concrete implementation of :class:`BaseTransactionCtrl`."""
from .base import BaseTransactionCtrl


class TransactionCtrl(BaseTransactionCtrl):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
