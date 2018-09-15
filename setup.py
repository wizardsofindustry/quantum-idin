#!/usr/bin/env python3
from setuptools import find_packages
from setuptools import setup

import idin

setup(
    name='idin',
    version=idin.__version__,
    packages=find_packages()
)

# pylint: skip-file
