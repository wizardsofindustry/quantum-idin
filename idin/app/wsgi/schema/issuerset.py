"""The validation schema for ``#/components/schema/IssuerSet`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema

from .issuer import Issuer


class IssuerSet(sq.schema.Schema):
    """Contains all iDIN Acquirers per country.
    """

    #: The readable name of the country
    country = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: Array of `Issuer` objects.
    issuers = sq.schema.fields.Nested(
        nested=Issuer(many=True),
        required=True,
        allow_none=False
    )


#pylint: skip-file
