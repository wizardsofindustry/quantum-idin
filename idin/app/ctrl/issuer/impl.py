"""Contains the concrete implementation of :class:`BaseIssuerCtrl`."""
from .base import BaseIssuerCtrl


class IssuerCtrl(BaseIssuerCtrl):

    async def get(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
