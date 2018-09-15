"""Contains the concrete implementation of :class:`BaseTransactionCtrl`."""
from .base import BaseTransactionCtrl


class TransactionCtrl(BaseTransactionCtrl):
    """Exposes handlers for ``GET`` and ``POST`` requests on the ``/transactions``
    endpoint.
    """

    async def post(self, request, *args, **kwargs):
        return 201, self.idin.transaction(request.payload)

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
