from sq.service import Service


class BaseIdinService(Service):

    def issuers(self):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
