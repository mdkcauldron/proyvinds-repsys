from RepSys import Error, config
from RepSys.util import execcmd, get_auth
from RepSys.VCS import *
import sys
import re
import time

__all__ = ["SVN", "SVNLook", "SVNLogEntry"]

class SVNLogEntry(VCSLogEntry):
    def __init__(self, revision, author, date):
        VCSLogEntry.__init__(self, revision, author, data)

class SVN(VCS):
    def __init__(self):
        VCS.__init__(self)
        self.vcs_name = "svn"
        self.vcs_command = config.get("global", "svn-command",
                        "SVN_SSH='ssh -o \"BatchMode yes\"' svn")

class SVNLook(VCSLook):
    def __init__(self, repospath, txn=None, rev=None):
        VCSLook.__init__(self, repospath, txn, rev)
        self.execcmd = "svnlook"

# vim:et:ts=4:sw=4
