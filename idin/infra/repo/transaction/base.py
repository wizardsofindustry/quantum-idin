import ioc
from sq.persistence import Repository


class BaseTransactionRepository(Repository):
    session = ioc.class_property('DatabaseSessionFactory')

    def persist_tx(self):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
