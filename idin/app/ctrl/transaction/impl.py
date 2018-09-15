"""Contains the concrete implementation of :class:`BaseTransactionCtrl`."""
from .base import BaseTransactionCtrl


class TransactionCtrl(BaseTransactionCtrl):
    """Exposes handlers for ``GET`` and ``POST`` requests on the ``/transactions``
    endpoint.
    """

    async def patch(self, request, *args, **kwargs):
        """Returns the results of the transaction identified by the request
        payload.
        """
        return self.idin.result(request.payload)

    async def post(self, request, *args, **kwargs):
        """Creates a new iDIN transaction with the parameters specified in the
        request payload.
        """
        return 201, self.idin.transaction(request.payload)

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
