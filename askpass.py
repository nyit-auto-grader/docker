#!/usr/bin/env python3

from sys import argv
from os import environ

if argv[1] == "Username for 'https://github.com': ":
    print(environ['GIT_USERNAME'])
    exit()

if argv[1] == "Password for 'https://%(GIT_USERNAME)s@github.com': " % environ:
    print(environ['GIT_PASSWORD'])
    exit()

exit(1)
