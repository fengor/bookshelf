#! /usr/bin/python2

import isbnlib
import argparse
import sys

from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser()
parser.add_argument('isbnfile', type=file,
                    help='file to load ISBNs from',
                    nargs='?')
parser.add_argument('-t', '--template',
                    help='Choose template to use',
                    default='shelf.j2')
parser.add_argument('-s', '--service',
                    help='Choose service to use',
                    choices=['merge', 'wcat', 'goob', 'openl'],
                    default='openl')
args = parser.parse_args()

print args

env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
template = env.get_template(args.template)

booklist = []

if args.isbnfile is not None:
    for line in args.isbnfile:
        booklist.append(isbnlib.meta(line, args.service))
else:
    for line in sys.stdin:
        booklist.append(isbnlib.meta(line, args.service))

print template.render(books=booklist),
