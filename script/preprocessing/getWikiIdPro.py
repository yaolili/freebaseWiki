#########################################################################
# File Name: getWikiIdPro.py
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
        print "sys.argv[1]: wikiIdFromFreebase file"
        print "sys.argv[2]: original freebase file"
        print "sys.argv[3]: output file"
        exit()

    result = file(sys.argv[3], "w+")
    mapDict = {}
    entityDict = {}
    
    with open(sys.argv[1], 'r') as mapFile:
        for line in mapFile:
            freebaseId, wikiId = line.strip().split("\t")
            mapDict[freebaseId] = wikiId
    print "mapDict done!"
    
    reStrSub = ".*ns/(.+\w)"
    reStrObj = ".*ns/(.+\w)"
    reStrPre = ".*\.com/(.+\w)|.*\.org/(.+\w)"
    reStrKey = '"(\d+)"'
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
            predicate = re.match(reStrPre, trippleContent[1])
            obj = trippleContent[2]
            
            if not predicate:
                print "Predicate error!"
                print trippleContent[1]
                exit()
            if subject.group(1) not in mapDict:
                continue
            #subject in mapDict
            wikiId = re.match(reStrKey, mapDict[subject.group(1)])
            if not wikiId:
                print 'In %s, wikiId is wrong! %s : %s' % (sys.argv[1], subject.group(1), mapDict[subject.group(1)])
                exit()
            key = int(wikiId.group(1))
            if key not in entityDict:
                entityDict[key] = [[predicate.group(1), obj]]
            else:
                aList = entityDict[key]
                aList.append([predicate.group(1), obj])
                entityDict[key] = aList
    print "Begin write"
    for key in entityDict:
        string = "".join(str(x) for x in entityDict[key])
        result.write(key + "\t" + string + "\n")
    
    result.close()
