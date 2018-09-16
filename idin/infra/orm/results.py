""""Declares a Python object mapping to the ``results`` relation."""
import sqlalchemy

from .base import Relation
from .transactions import Transaction


class Result(Relation):
    """Maintains the results of successful iDIN transactions.
    """

    __tablename__ = 'results'

    #: Identifies the transaction of this result.
    txid = sqlalchemy.Column(
        sqlalchemy.ForeignKey(Transaction.txid),
        name='txid',
        primary_key=True,
        nullable=False
    )

    #: Identifies the issuer.
    issuer_id = sqlalchemy.Column(
        sqlalchemy.String,
        name='issuer_id',
        nullable=False
    )

    #: The Bank Identification Number (BIN) identifying the customer, as
    #: returned by the iDIN issuer.
    bin = sqlalchemy.Column(
        sqlalchemy.String,
        name='bin',
        nullable=False
    )

    #: The data yielded by the iDIN transaction, serialized as JSON with
    #: sorted keys.
    data = sqlalchemy.Column(
        sqlalchemy.String,
        name='data',
        nullable=False
    )

    #: A SHA-256 hash of the transaction identifier and the result.
    checksum = sqlalchemy.Column(
        sqlalchemy.LargeBinary,
        name='checksum',
        nullable=False
    )

    #: The date/time at which the result was retrieved, in milliseconds
    #: since the UNIX epoch.
    retrieved = sqlalchemy.Column(
        sqlalchemy.BigInteger,
        name='retrieved',
        nullable=False
    )

    #: Specifies if a secure time stamp is requested and persisted for the
    #: checksum of this result.
    timestamped = sqlalchemy.Column(
        sqlalchemy.Boolean,
        name='timestamped',
        nullable=False,
        default=False
    )


# pylint: skip-file
