from subprocess import call     # for external shell calls
from sys import argv            # for command line arguments


##########################################################################
# xbps subcommands
def void_install(args):
    pass

def void_remove(args):
    pass

def void_query(args):
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
    print USAGE_MESSAGE
##########################################################################

def main(argv):
    if len(argv) > 1:
        cmd = argv[1]
        func = find_command(cmd)
        func(argv[1:])
    else:
        usage()

if __name__ == '__main__':
    main(argv)