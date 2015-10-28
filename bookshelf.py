#! /usr/bin/python2

import isbnlib
import fileinput

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
template = env.get_template('shelf.j2')

booklist = []

for line in fileinput.input():
    booklist.append(isbnlib.meta(line, 'openl'))

print template.render(books=booklist),
