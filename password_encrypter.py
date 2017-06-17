#!/usr/bin/env python
import crypt
import sys
import string
import random


def usage():
    print "Usage: %s <username> <password> <optional:salt>" % sys.argv[0]
    exit()

def randomsalt():
	return random.choice(string.letters) + random.choice(string.letters)


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        usage()
    elif len(sys.argv) == 3:
		salt = randomsalt()
    else:
		salt = sys.argv[3]
    #print "%s:%s" % (sys.argv[1], crypt.crypt(sys.argv[2],salt)
    print sys.argv[1] + ":" + crypt.crypt(sys.argv[2],salt)
main()
