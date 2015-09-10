# tabgeo
Geolocation database to determine country code (ISO 3166-1 alpha-2) by IP


Installation
------------

Through PyPI::

    $ pip install tabgeo
 
From the project root directory::

    $ python setup.py install


Usage:
------
Example usage::

    >>> from tabgeo import getbyip
    >>> print getbyip('8.8.4.4')
    US
