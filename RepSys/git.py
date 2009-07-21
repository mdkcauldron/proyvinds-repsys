from RepSys import Error, config
from RepSys.util import execcmd, get_auth
from RepSys.VCS import *
import sys
import re
import time

class GITLogEntry(VCSLogEntry):
    def __init__(self, revision, author, date):
        VCSLogEntry.__init__(self, revision, author, data)

class GIT(VCS):
    def __init__(self):
        VCS.__init__(self)
        self.vcs_name = "git"
        self.vcs_command = config.get("global", "git-command",
                        "GIT_SSH='ssh -o \"BatchMode yes\"' git")
        self.vcs_supports['clone'] = True

    def clone(self, url, targetpath, **kwargs):
        if url.split(':')[0].find("svn") < 0:
            return VCS.clone(self, url, targetpath, **kwargs)
        else:
            cmd = ["svn", "clone", "'%s'" % url, targetpath]
            return self._execVcs_success(*cmd, **kwargs)


class SVNLook(VCSLook):
    def __init__(self, repospath, txn=None, rev=None):
        VCSLook.__init__(self, repospath, txn, rev)

# vim:et:ts=4:sw=4
