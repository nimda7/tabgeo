#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


PACKAGE_VERSION = '0.1'

setup(
    name='tabgeo',
    version=PACKAGE_VERSION,
    description='Geolocation database to determine country code (ISO 3166-1 alpha-2) by IP',
    long_description=read('README.rst'),
    author='Alex Klimenka',
    author_email='nimda7@gmail.com',
    license='GNU Affero General Public License v3',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    keywords=[
        'geo',
        'geoip',
        'geolocation',
        'ISO 3166-1',
    ]
)
