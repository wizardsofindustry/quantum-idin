"""The validation schema for ``#/components/schema/TransactionIdentifier`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class TransactionIdentifier(sq.schema.Schema):
    """Identifies an iDIN transaction.
    """

    #: The transaction identifier.
    txid = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: The entrance code as returned by the iDIN acquirer.
    ec = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
