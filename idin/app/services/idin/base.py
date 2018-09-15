import ioc
from sq.service import Service


class BaseIdinService(Service):
    repo = ioc.class_property('TransactionRepository')

    def issuers(self):
        raise NotImplementedError("Subclasses must override this method.")

    def transaction(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def result(self, dto):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
