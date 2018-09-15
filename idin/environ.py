"""Environment variables specified by the application Quantumfile."""
import os

import yaml


DEFAULT_SECRET_KEY = "70422360908e67dbbe1ac7bcf98f16b194ae51e779f690d9598c2d596c6e4bb4"

# Set up some variables serving as hints to the Quantum framework.
os.environ['SQ_ENVIRON_PREFIX'] = 'IDIN'


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


# Provide some defaults to the environment prior to assigning the
# module-level constants.
os.environ.setdefault('IDIN_SECRET_KEY',
    "70422360908e67dbbe1ac7bcf98f16b194ae51e779f690d9598c2d596c6e4bb4")
os.environ.setdefault('IDIN_DEBUG',
    "1")
os.environ.setdefault('IDIN_IOC_DEFAULTS',
    "/etc/idin/ioc.conf")
os.environ.setdefault('IDIN_IOC_DIR',
    "/etc/idin/ioc.conf.d/")
os.environ.setdefault('IDIN_RDBMS_DSN',
    "postgresql+psycopg2://idin:idin@rdbms:5432/idin")


SECRET_KEY = os.getenv('IDIN_SECRET_KEY')
DEBUG = os.getenv('IDIN_DEBUG', '').lower() in ('yes', '1', 'true')
IOC_DEFAULTS = os.getenv('IDIN_IOC_DEFAULTS')
IOC_DIR = os.getenv('IDIN_IOC_DIR')
RDBMS_DSN = os.getenv('IDIN_RDBMS_DSN')
GIT_COMMIT = os.getenv('IDIN_GIT_COMMIT')
CM_MERCHANT_TOKEN = os.getenv('IDIN_CM_MERCHANT_TOKEN')
DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'
CONFIG_DIR = os.getenv('QUANTUM_CONFIG_DIR')
TEST_PHASE = os.getenv('SQ_TESTING_PHASE')
