"""The validation schema for ``#/components/schema/Transaction`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class Transaction(sq.schema.Schema):
    """Specifies the properties for a new iDIN transaction.
    """

    #: Retrieve a uniquely identifying token with the bank for this
    #: consumer that is consistent across multiple sessions.
    identity = sq.schema.fields.Boolean(
        allow_none=False,
        missing=True
    )

    #: Retrieve the name information associated with this consumer.
    name = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: Retrieve the gender of this consumer.
    gender = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: Retrieve address information associated with this consumer.
    address = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: Retrieve the birthdate of the user.
    date_of_birth = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: Retrieve if this user is known to be 18 years or older.
    legal_age = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: Retrieve the email address associated with this consumer.
    email_address = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: Retrieve the telephone number associated with this consumer.
    telephone_number = sq.schema.fields.Boolean(
        allow_none=False,
        missing=False
    )

    #: An identifier for the bank which the customer has chosen.
    issuer_id = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    #: The 2 character language code in which to return the results. Can
    #: be either ‘nl’ or ‘en’ for Dutch or English. This is a preferred
    #: language, not all banks support all languages.
    language = sq.schema.fields.String(
        allow_none=False,
        missing='en'
    )

    #: The URI where the issuing bank should redirect the user to at the
    #: end of the flow. The bank will append two query parameters to this
    #: URL when returning the user to you, ``trxid`` and ``ec``. The
    #: latter will contain the value of ``ec`` (generated and stored
    #: internally), ``trxid`` is the ``txid`` that you will receive in
    #: this request.
    redirect_uri = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
