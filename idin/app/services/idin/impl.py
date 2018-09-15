"""Declares :class:`IdinService`."""
import os

import requests

import idin.environ
from .base import BaseIdinService


class IdinService(BaseIdinService):
    """Provides an API to the CM Telecom iDIN gateway."""
    base_url = 'https://idin.cmtelecom.com/idin/v1.0'

    def transaction(self, dto):
        """Create a new iDIN transaction and return the redirect
        URL.
        """
        ec = bytes.hex(os.urandom(20))
        params = dict(dto)
        params.update({
            '18y_or_older': params.pop('18y_or_older', False),
            'merchant_token': idin.environ.CM_MERCHANT_TOKEN,
            'merchant_return_url': params.pop('redirect_uri'),
            'ec': ec
        })
        response = self._request('POST', '/transaction', json=params)
        if response.status_code != 200:
            raise RuntimeError(response.text)
        result = response.json()
        txid = result['transaction_id']
        ref = result['merchant_reference']

        return self.dto(
            url=result['merchant_return_url'],
            txid=txid
        )

    def issuers(self, country=None):
        """Return a list containing all issuers."""
        response = self._request('POST', '/directory')
        dto = response.json()
        if country is None:
            return dto

        # Return the issuers per country, but only Dutch is supported now
        # so simply return the issuers list
        assert len(dto) == 1, dto
        return dto[0]['issuers']

    def _request(self, method, url, *args, **kwargs):
        json = kwargs.setdefault('json', {})
        if 'merchant_token' not in json:
            json['merchant_token'] = idin.environ.CM_MERCHANT_TOKEN
        return requests.request(method, f'{self.base_url}{url}',
            *args, **kwargs)
