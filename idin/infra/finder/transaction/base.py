import ioc
from sq.readmodel import Finder


class BaseTransactionFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')

    def reference(self):
        raise NotImplementedError("Subclasses must override this method.")

    def result(self):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
