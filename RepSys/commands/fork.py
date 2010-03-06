#!/usr/bin/python
from RepSys import Error
from RepSys.command import *
from RepSys.rpmutil import fork
import getopt
import sys

HELP = """\
Usage: repsys fork [OPTIONS] URL [LOCALPATH]

Checkout the package source from the Mandriva repository.

If the 'mirror' option is enabled, the package is obtained from the mirror
repository.

You can specify the distro branch to checkout from by using distro/pkgname.

Options:
    -d      The distribution branch to checkout from
    -b      The package branch
    -M      Do not use the mirror (use the main repository)
    -h      Show this message

Examples:
    repsys fork pkgname
    repsys fork -d 2009.0 pkgname
    repsys fork 2009.0/pkgame
    repsys fork http://repos/svn/cnc/snapshot/foo
    repsys fork http://repos/svn/cnc/snapshot/foo foo-pkg
"""

def parse_options():
    parser = OptionParser(help=HELP)
    parser.add_option("--distribution", "-d", dest="distro", default=None)
    parser.add_option("--branch", "-b", dest="branch", default=None)
    opts, args = parser.parse_args()
    if len(args) not in (1, 2):
        raise Error, "invalid arguments"
    # here we don't use package_url in order to notify the user we are
    # using the mirror
    opts.pkgdirurl = args[0]
    if len(args) == 2:
        opts.path = args[1]
    else:
        opts.path = None
    return opts

def main():
    do_command(parse_options, fork)

# vim:et:ts=4:sw=4
