#!/usr/bin/python
from RepSys import Error
from RepSys.command import *
from RepSys.rpmutil import get_spec
import getopt
import sys

HELP = """\
Usage: repsys getspec [OPTIONS] REPPKGURL

Options:
    -t DIR  Use DIR as target for spec file (default is ".")
    -h      Show this message

Examples:
    repsys getspec http://repos/svn/cnc/snapshot/foo
"""

def parse_options():
    parser = OptionParser(help=HELP)
    parser.add_option("-t", dest="targetdir", default=".")
    opts, args = parser.parse_args()
    if len(args) != 1:
        raise Error, "invalid arguments"
    opts.pkgdirurl = default_parent(args[0])
    return opts

def main():
    do_command(parse_options, get_spec)

# vim:et:ts=4:sw=4
