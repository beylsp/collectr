#!/usr/bin/env python
"""Distutils scripts to build, distribute and install the collectr package."""

requirements = ['Flask']

test_requirements = []

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    # only available from py27
    import importlib  # noqa
except ImportError:
    requirements.append('importlib')

setup(
    name='collectr',
    version='1.0',
    packages=['collectr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements
)
