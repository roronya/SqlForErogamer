sqlforerogamer
==============

|Build Status|

installation
------------

::

    $ pip install sqlforerogamer

usage
-----

::

    >>> import sqlforerogamer
    >>> sqlforerogamer.read_sql("SELECT id  FROM brandlist WHERE id = '1'")
    id
    0  1

.. |Build Status| image:: https://travis-ci.org/roronya/sqlforerogamer.svg?branch=master
   :target: https://travis-ci.org/roronya/sqlforerogamer
