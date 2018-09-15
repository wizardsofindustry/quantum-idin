import ioc
from sq.service import Service


class BaseIdinService(Service):
    repo = ioc.class_property('TransactionRepository')
    finder = ioc.class_property('TransactionFinder')

    def issuers(self):
        raise NotImplementedError("Subclasses must override this method.")

    def transaction(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def result(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def update(self, dto):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
