#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     wikiIdStrToInt.py
# ROLE:     TODO (some explanation)
# CREATED:  2015-11-28 11:29:25
# MODIFIED: 2015-11-28 11:44:31


import sys
import os

def strToInt(inputFile, outputFile):
    result = open(outputFile, "w+")
    try:
        with open(inputFile, 'r') as fin:
            for line in fin:
                freebaseId, wikiIdStr = line.strip().split("\t")
                array = wikiIdStr.strip().split("\"")
                if(len(array) == 3):
                    wikiIdInt = array[1]
                    result.write(freebaseId + "\t" + wikiIdInt + "\n")
                else:
                    print "wikiIdStr split error!"
                    exit()
        result.close()
    except IOError, e:
        print 'Could not open file:', e
        exit()
        

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "sys.argv[1]: input wikiIdStr file"
        print "sys.argv[2]: output file"

    
    strToInt(sys.argv[1], sys.argv[2])
