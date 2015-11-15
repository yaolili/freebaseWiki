#########################################################################
# File Name: splitFreebaseWTWikiId.py
# Author: yaolili
# mail: yaolili@pku.edu.cn
# Created Time: Fri 13 Nov 2015 01:12:23 PM CST
#########################################################################
##!/usr/bin/python

import os
import sys
import re
import gzip

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "sys.argv[1]: freebaseMapWiki file"
        print "sys.argv[2]: original freebase file"
        print "sys.argv[3]: output file"
        exit()

    result = file(sys.argv[3], "w+")
    mapDict = {}
    
    with open(sys.argv[1], 'r') as mapFile:
        for line in mapFile:
            freebaseId, wikiId = line.strip().split("\t")
            try:
                mapDict[freebaseId] = re.match('"(\d+)"', wikiId).group(1)
            except e:
                print "regex wikiId error!"
                print "%s : %s" %(freebaseId, wikiId)
    print "mapDict done!"
    
    reStrSub = ".*ns/(.+\w)"
    
    num = 0
    with gzip.open(sys.argv[2], 'r') as originalFile:
        for line in originalFile:
            num += 1
            if num % 100000 == 0:
                print num

            trippleContent = line.strip().split()
            if len(trippleContent) < 3:
                print "Error! no tripple in a line!"
                exit()
            subject = re.match(reStrSub, trippleContent[0])
            predicate = trippleContent[1]
            obj = trippleContent[2]
            
            if subject.group(1) not in mapDict:
                continue
            wikiId = mapDict[subject.group(1)]
            print "write"
            string = wikiId + "\t" + predicate + "\t" + obj + "\n"
            result.write(string)
    result.close()
