"""The validation schema for ``#/components/schema/IdinAssertion`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class IdinAssertion(sq.schema.Schema):
    """The successful result of an iDIN transaction.
    """

    #: The Bank Identification Code (BIN), identifying the customer.
    bin = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
