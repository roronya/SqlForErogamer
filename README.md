# sqlforerogamer

[![Build Status](https://travis-ci.org/roronya/sqlforerogamer.svg?branch=master)](https://travis-ci.org/roronya/sqlforerogamer)

## installation

    $ pip install sqlforerogamer

## usage
    >>> import sqlforerogamer
    >>> sqlforerogamer.read("select id, brandname, brandfurigana, url from brandlist where id = 1")
    index id brandname brandfurigana                         url
    0      1  1       age          アージュ  http://www.age-soft.co.jp/
