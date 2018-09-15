""""Declares a Python object mapping to the ``transactions`` relation."""
import sqlalchemy

from .base import Relation


class Transaction(Relation):
    """Maintains information about iDIN transactions.
    """

    __tablename__ = 'transactions'

    #: Transaction ID as specified by the intermediary.
    txid = sqlalchemy.Column(
        sqlalchemy.String,
        name='txid',
        primary_key=True,
        nullable=False
    )

    #: Current status of the transaction, may be one of ``open``,
    #: ``success``, ``cancelled``, ``failure`` or ``expired``.
    status = sqlalchemy.Column(
        sqlalchemy.String,
        name='status',
        nullable=False,
        default=open
    )

    #: Entrance code to be included in the response from the iDIN
    #: acquirer.
    ec = sqlalchemy.Column(
        sqlalchemy.String,
        name='ec',
        nullable=False
    )

    #: Reference at the intermediary for accounting purposes.
    reference = sqlalchemy.Column(
        sqlalchemy.String,
        name='reference',
        nullable=False
    )


# pylint: skip-file
