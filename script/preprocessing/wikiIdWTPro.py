#########################################################################
# File Name: extractEntity.py
# Author: yaolili
# mail: yaolili@pku.edu.cn
# Created Time: Wed 11 Nov 2015 04:38:17 PM CST
#########################################################################
##!/usr/bin/python

import sys
import os
import re
import gzip 

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "sys.argv[1]: input file - freebasePart.txt"
        print "sys.argv[2]: output file"
        print "sys.argv[3]: log file"
        exit()
   
    result = open(sys.argv[2], 'w+')
    log = open(sys.argv[3], 'w+')
    reStrObj = ".*ns/(.+\w)"

    wikiPro = {}
    #Notice! here is the first wikiId in freebasePart.txt
    curId = "42210866"
    curPro = []
    with open(sys.argv[1],'r') as fin:
        for i, line in enumerate(fin):    
            trippleContent = line.strip().split("\t")
            if len(trippleContent) < 3:
                log.write("Line:" + str(i) + " error! No tripple in a line!")
                exit()
            wikiId = trippleContent[0]
            predicate = trippleContent[1]
            obj = re.match(reStrObj, trippleContent[2])
     
            if not obj:
                continue
            if wikiId == curId:
                curPro.append([predicate, obj.group(1)])
            else:
                string = curId + "\t" + "".join(str(x) for x in curPro) + "\n"
                log.write("Line:" + str(i) + ", write!")
                result.write(string)
                curId = wikiId
                curPro = [[predicate, obj.group(1)]]
    result.close()
    log.close()
