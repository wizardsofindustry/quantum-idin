"""Contains the concrete implementation of :class:`BaseIssuerCtrl`."""
from .base import BaseIssuerCtrl


class IssuerCtrl(BaseIssuerCtrl):
    """Exposes a handler for ``GET`` requests."""

    async def get(self, request, *args, **kwargs):
        """Handle an incoming ``GET`` request and return the available
        iDIN acquirers.
        """
        return 200, self.idin.issuers(country=kwargs.pop('country', None))
