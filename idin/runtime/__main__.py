"""Start the main :mod:`idin` application using the
specified command-line parameters.
"""
import argparse
import logging
import os
import sys

import yaml

import sq.runtime


DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'

# This is a hook to load secrets or other environment variables
# from YAML-encoded file, for example when using Docker Swarm
# secrets.
if os.getenv('IDIN_SECRETS'):
    with open(os.getenv('IDIN_SECRETS')) as f:
        secrets = yaml.safe_load(f.read()) #pylint: disable=invalid-name
    for key, value in secrets.items():
        if not key.startswith('IDIN'):
            continue
        os.environ[key] = str(value)

    del secrets


os.environ['SQ_ENVIRON_PREFIX'] = 'IDIN'
DEFAULT_SECRET_KEY = "70422360908e67dbbe1ac7bcf98f16b194ae51e779f690d9598c2d596c6e4bb4"
os.environ.setdefault('IDIN_SECRET_KEY', "70422360908e67dbbe1ac7bcf98f16b194ae51e779f690d9598c2d596c6e4bb4")
os.environ.setdefault('IDIN_DEBUG', "1")
os.environ.setdefault('IDIN_IOC_DEFAULTS', "/etc/idin/ioc.conf")
os.environ.setdefault('IDIN_IOC_DIR', "/etc/idin/ioc.conf.d/")
os.environ.setdefault('IDIN_RDBMS_DSN', "postgresql+psycopg2://idin:idin@rdbms:5432/idin")
os.environ.setdefault('IDIN_HTTP_ADDR', "0.0.0.0")
os.environ.setdefault('IDIN_HTTP_PORT', "8443")


class MainProcess(sq.runtime.MainProcess):
    """The main :mod:`idin` process manager."""
    framerate = 10
    components = [
        sq.runtime.HttpServer,
    ]


parser = argparse.ArgumentParser() #pylint: disable=invalid-name
parser.add_argument('-c', dest='config',
    default='./etc/idin.conf',
    help="specifies the runtime configuration file (default: %(default)s)")
parser.add_argument('--loglevel',
    help="specifies the logging verbosity (default: %(default)s)",
    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], default='INFO')


if __name__ == '__main__':
    logger = logging.getLogger('idin') #pylint: disable=invalid-name
    args = parser.parse_args() #pylint: disable=invalid-name
    p = MainProcess(args, logger=logger) #pylint: disable=invalid-name

    if DEFAULT_SECRET_KEY == os.getenv('IDIN_SECRET_KEY'):
        logger.critical("The application is started using the default secret key")
        if DEPLOYMENT_ENV == 'production':
            logger.critical("DEFAULT_SECRET_KEY may not be used in production")
            sys.exit(128)


    try:
        sys.exit(p.start() or 0)
    except Exception: #pylint: disable=broad-except
        logger.exception("Fatal exception caused program termination")
        sys.exit(1)


# !!! SG MANAGED FILE -- DO NOT EDIT !!!
