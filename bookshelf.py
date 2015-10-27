#! /usr/bin/python2

import isbnlib
import fileinput

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('shelf.j2')

booklist = []

for line in fileinput.input():
    print "Looking up ISBN: %s" % line
    booklist.append(isbnlib.meta(line, 'openl'))

with open('shelf.html', 'wb') as output_file:
    output_file.write(template.render(books=booklist))
