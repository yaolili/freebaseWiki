#!/usr/bin/python
#author: yaolili
#date: 2015/11/11

import sys
import os
import re

#read file
#input file path
#read input per line
#split 
#get content
#write a file

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'sys.argv[1]: original mapping file'
        print 'sys.argv[2]: output file'
        exit()
    
    result = file(sys.argv[2], "a+")
    reStrFre = '.*ns/(m\.\w+)'
    reStrWiki = '.*entity/(Q\d+)'
    for line in open(sys.argv[1]):
        freebase, middle, wiki = line.strip().split("\t")
        freebaseId = re.match(reStrFre, freebase)
        wikiId = re.match(reStrWiki, wiki)
        if middle != "<http://www.w3.org/2002/07/owl#sameAs>":
            print middle
            exit()
        if freebaseId and wikiId:
            #print freebaseId.group(1)
            #print wikiId(1)
            line = freebaseId.group(1) + "\t" + wikiId.group(1) + "\n"
            result.write(line)
        else:
            print "Error! freebaseId or wikiId is empty!"
