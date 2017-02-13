#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013:
#     Sébastien Pasche, braoru@gmail.com
#
#
# iJPermission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

author = "Sebastien Pasche"
maintainer = "Sebastien Pasche"
version = "0.0.1"

import argparse
import sys
import logging
import traceback

# Settings
# -------

# Logging
logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)
logger = logging.getLogger("test")

# OPT parsing
# -----------
prog_name = sys.argv[0]
parser = argparse.ArgumentParser(prog="{pn} {v}".format(pn=prog_name, v=version))
usage = """{pn} [options]

God dammit .. this is a test

""".format(
    pn=prog_name
)

parser = argparse.ArgumentParser(
    usage=usage
)

##args
parser.add_argument(
    '--username',
    default=None,
    dest="user_name",
    help='what do you think ?',
    type=str
)

parser.add_argument(
    '--password',
    default=None,
    dest="user_password",
    help='In the name of pasta',
    type=str
)

# Debug
##
parser.add_argument(
    '--debug',
    dest="debug",
    default=False,
    action="store_true",
    help='Enable debug'
)

if __name__ == '__main__':

    # Ok first job : parse args
    ##
    args = parser.parse_args()

    # debug
    ##
    debug = args.debug

    # Set Debug Level
    ##
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.CRITICAL)

    # settings
    ##
    if args.user_name is None:
        parser.error("You must specify a user name")
    user_name = args.user_name

    if args.user_password is None:
        parser.error("What the hell i'm suposed to do with that ...")
    user_password = args.user_password

    try:
        logger.info(
            "{username}:{password}".format(
                username=user_name,
                password=user_password
            )
        )

    except Exception as e:
        logger.debug(e)
        the_type, value, tb = sys.exc_info()
        if debug:
            traceback.print_tb(tb)
        print("Error: {m}".format(m=e))
        sys.exit(2)
