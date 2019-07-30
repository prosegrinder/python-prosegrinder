# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

# Version
with open(path.join(path.dirname(__file__), 'prosegrinder', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()


setup(
    version=VERSION,
)
