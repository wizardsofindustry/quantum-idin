import ioc
from sq.persistence import Repository


class BaseTransactionRepository(Repository):
    session = ioc.class_property('DatabaseSessionFactory')

    def persist_tx(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_result(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def setstatus(self, txid, status):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
