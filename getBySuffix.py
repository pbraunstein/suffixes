#!/usr/bin/env python

from sys import exit
from sys import argv
import re
from sys import getfilesystemencoding

# CONSTANTS
INPUT = "cbbkfmfonb-2096231156-e9e6io.txt"
PREF_FILE = "preps.txt"
CODE = "utf-8"

def main():
    if len(argv) != 2:
        print "USAGE", argv[0], "SUFFIX_TO_SEARCH"
        exit(0)

    prefs = getPrefs()

    test = argv[1].decode(getfilesystemencoding()).strip().lower()

    found = {}

    # Generate potential list of words
    potentials = [x + test for x in prefs]

    with open(INPUT, 'r') as filer:
        for line in filer:
            line = line.decode(CODE)
            listL = line.strip().split("\t")
            # remove () {} [] ""
            word = re.sub(ur'\{.*\}|\[.*\]|\(.*\)|\".*\"', ur'', listL[0],
                    re.UNICODE).strip().lower()
                

            # Only interested in one word things
            if " " in word or word.strip() == '':
                continue
            if word in potentials:
                if word in found.keys():
                    found[word].append(listL[1])
                else:
                    found[word] = [listL[1]]

    writeOut(test, found)


# Returns a list of the prefixes for testing
def getPrefs():
    toReturn = []
    with open(PREF_FILE, 'r') as filer:
        for line in filer:
            line = line.decode(CODE)
            toReturn.append(line.strip())

    return toReturn



def writeOut(test, found):
    keys = found.keys()
    keys.sort()

    with open(test + "_words.txt", 'w') as filew:
        for key in keys:
            defs = found[key]

            filew.write(key.encode(CODE) + ":")
            filew.write(",".join([x.encode(CODE) for x in defs]) + "\n")

if __name__ == '__main__':
    main()
