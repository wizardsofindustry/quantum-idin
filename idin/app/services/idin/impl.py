"""Declares :class:`IdinService`."""
import os

import requests
import quantum.lib.timezone

import idin.environ
from .base import BaseIdinService


class IdinService(BaseIdinService):
    """Provides an API to the CM Telecom iDIN gateway."""
    base_url = 'https://idin.cmtelecom.com/idin/v1.0'

    def update(self, dto):
        """Returns the result of an iDIN transaction."""
        # Get the status from CM telecom.
        status = self._request('POST', '/status', json={
            'transaction_id': dto.txid,
            'merchant_reference': self.finder.get_reference(dto.txid)
        })
        return status

    def transaction(self, dto):
        """Create a new iDIN transaction and return the redirect
        URL.
        """
        dto = self.dto(**dto)
        ec = bytes.hex(os.urandom(20))
        params = dict(dto)
        params.update({
            '18y_or_older': params.pop('18y_or_older', False),
            'merchant_token': idin.environ.CM_MERCHANT_TOKEN,
            'merchant_return_url': params.pop('redirect_uri'),
            'entrance_code': ec
        })
        result = self._request('POST', '/transaction', json=params)
        dto.storage_class = 'tx'
        dto.created = quantum.lib.timezone.now()
        dto.ec = ec
        dto.txid = result['transaction_id']
        dto.ref = result['merchant_reference']
        self.repo.persist(dto)

        return self.dto(
            url=result['issuer_authentication_url'],
            txid=dto.txid
        )

    def issuers(self, country=None):
        """Return a list containing all issuers."""
        dto = self._request('POST', '/directory')
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
        response = requests.request(method, f'{self.base_url}{url}', *args, **kwargs)
        if response.status_code != 200:
            raise RuntimeError(response.text)
        return response.json()
