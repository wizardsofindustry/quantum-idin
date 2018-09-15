from werkzeug.routing import Map

from .health import HealthEndpoint
from .version import VersionEndpoint
from .countryissuer import CountryIssuerEndpoint
from .issuer import IssuerEndpoint


urlpatterns = Map([
    HealthEndpoint.as_rule(),
    VersionEndpoint.as_rule(),
    CountryIssuerEndpoint.as_rule(),
    IssuerEndpoint.as_rule(),
])


# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
