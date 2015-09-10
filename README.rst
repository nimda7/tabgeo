tabgeo: Geolocation database
====================================

Overview
--------

TabGeo - a special geolocation database to determine country of the user according to his IP-address.
Due to the unique architecture of the database and the binary format, TabGeo performs 2-4 times faster on real projects than similar free alternatives

TabGeo - the best solution for the IP-geolocation live.

This module based on origial PHP version from http://tabgeo.com
This python implementation licensed under `GNU Affero General Public License v3.0 <http://choosealicense.com/licenses/agpl-3.0/>`_, available from `PyPI <https://pypi.python.org/pypi/tabgeo/>`_, the source code can be found on `GitHub <https://github.com/nimda7/tabgeo>`_.

In case of issues please open ticket here https://github.com/nimda7/tabgeo/issues

Installation
------------

Through PyPI::

    $ pip install tabgeo


Usage:
------
Example usage::

    >>> from tabgeo import getbyip
    >>> print getbyip('8.8.4.4')
    US
