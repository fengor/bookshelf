bookshelf.py
============

This tool takes a list of ISBNs and converts them to a html bookshelf. Jinja2 is used as the templating engine.

It reads either a given file or from stdin and outputs to stdout

Usage
-----

from commandline:
$ ./bookshelf.py isbnlist.txt > output.html

or from within vim:
:read !./bookshelf.py isbnlist.txt
