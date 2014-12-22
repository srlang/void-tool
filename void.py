#
# void.py
#   Python-written helper tool to Void Linux's xbps-* tools
#   Written for personal ease of use, not robustness.
#
# Copyright (c) 2014Sean R. Lang <srlang@ncsu.edu>
#

from subprocess import call     # for external shell calls
from sys import argv            # for command line arguments


##########################################################################
# xbps subcommands
def void_install(args):
    '''Install the specified package atoms.'''
    pass

def void_remove(args):
    '''Remove the specified package atoms.'''
    pass

def void_query(args):
    '''Perform a search operation for a package atom'''
    pass

def find_command(cmd):
    if "-I" in cmd:
        return void_install
    elif "-Q" in cmd:
        return void_query
    elif "-R" in cmd:
        return void_remove
    else:
        return usage()
##########################################################################

##########################################################################
# Usage handling items
USAGE_MESSAGE="""
Usage: void <operation>[flags] [package]
    operation: -I, -Q, -R
        -I: Install
        -Q: Query
        -R: Remove
"""

def usage(args=None):
    '''Display a usage message to the user.'''
    print USAGE_MESSAGE
##########################################################################


def main(argv):
    '''Main program logic'''
    if len(argv) > 1:
        cmd = argv[1]
        func = find_command(cmd)
        func(argv[1:])
    else:
        usage()

if __name__ == '__main__':
    main(argv)
