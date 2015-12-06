#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='collectr',
    version='1.0',
    packages=['collectr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)