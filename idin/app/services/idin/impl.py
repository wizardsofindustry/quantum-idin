from .base import BaseIdinService


class IdinService(BaseIdinService):

    def issuers(self):
        raise NotImplementedError("Subclasses must override this method.")
