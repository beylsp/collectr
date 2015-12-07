#!/usr/bin/env python

install_requires = ['Flask']

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    # only available from py27
    import importlib  # noqa
except ImportError:
    install_requires.append('importlib')

setup(
    name='collectr',
    version='1.0',
    packages=['collectr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires
)
