sqlforerogamer
==============

installation
------------

::

    $ pip install sqlforerogamer

usage
-----

::

    >>> import sqlforerogamer
    >>> sqlforerogamer.read("SELECT id  FROM brandlist WHERE id = '1'")
    id
    0  1
