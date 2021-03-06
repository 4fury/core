#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

WorkDir = "jinja-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto(examples, "examples/*")

    #Create docs with python-Sphinx
    #shelltools.cd("docs")
    #autotools.make("html")
    #shelltools.cd("..")
    #pisitools.dohtml("Jinja2-%s/docs/_build/html/*" % get.srcVERSION())
    pisitools.dodoc("CHANGES*", "README*")