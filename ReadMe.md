bookshelf.py
============

This tool takes a list of ISBNs and converts them to a html bookshelf. Jinja2 is used as the templating engine and isbnlib as the library for the actual lookup..

It reads either a given file or from stdin and outputs to stdout

Commandline switches
--------------------

-s, --service: the service to use for the lookup (default: openl)
-t, --template: the template to use (default: shelf.j2)

Usage
-----

from commandline:
$ ./bookshelf.py isbnlist.txt > output.html

or from within vim:
:read !./bookshelf.py isbnlist.txt
