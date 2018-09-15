"""Declares :class:`IdinService`."""
import requests

from .base import BaseIdinService

import idin.environ


class IdinService(BaseIdinService):
    """Provides an API to the CM Telecom iDIN gateway."""
    base_url = 'https://idin.cmtelecom.com/idin/v1.0'

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
