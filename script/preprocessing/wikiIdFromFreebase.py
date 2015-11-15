#########################################################################
# File Name: wikiIdFromFreebase.py
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
        print "sys.argv[1]: input file"
        print "sys.argv[2]: output file"
        print "sys.argv[3]: log file"
        exit()
   
    result = open(sys.argv[2], 'w+')
    log = open(sys.argv[3], 'w+')
    reStrSub = ".*ns/(.+\w)"
    reStrPre = ".*key/(wikipedia\.en_id)"
    
    with gzip.open(sys.argv[1],'r') as fin:
        for i,line in enumerate(fin):
            if i < 3000000000:
                continue
            trippleContent = line.strip().split("\t")
            if len(trippleContent) < 3:
                log.write("Line:" + str(i) + "Error! no tripple in a line!" + "\n")
                exit()
            freebaseId = re.match(reStrSub, trippleContent[0])
            predicate = re.match(reStrPre, trippleContent[1])
            wikiId = trippleContent[2]
           
            if not predicate:
                continue
            log.write("Num:" + str(i) + ", write!" + "\n")
            string = freebaseId.group(1) + "\t" + wikiId + "\n"
            result.write(string)
    log.close()
    result.close()
