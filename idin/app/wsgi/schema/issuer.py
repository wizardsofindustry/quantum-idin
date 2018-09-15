"""The validation schema for ``#/components/schema/Issuer`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class Issuer(sq.schema.Schema):
    """An organization that is an iDN Acquirer
    """

    #: An identifier for the bank. Used as the value of the in bank
    #: selector dropdowns. The end user selects a value and iDIN will
    #: direct the end user to that bank, so that the user can identify
    #: himself. Has the pattern
    #: `/[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}/`.
    issuer_id = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: A human-readable name of the issuer.
    issuer_name = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
