#########################################################################
# File Name: getWikifierEntity.py
# Author: yaolili
# mail: yaolili@pku.edu.cn
# Created Time: Thu 12 Nov 2015 11:16:37 AM CST
#########################################################################
##!/usr/bin/python

import os
import re
import sys
from bs4 import BeautifulSoup as BS

def getWikiId(inputFile):
    try: 
        with open(inputFile, 'r') as content_file:
            content = BS(content_file.read())
            topDisam = [a.get_text() for a in content.find_all('topdisambiguation')]
            #print len(topDisam)
            wikiIdSet = []
            for entity in topDisam:
                eachProperty =  entity.strip().split("\n") 
                if len(eachProperty) < 3:
                    print "Less than  three property of an entity!"
                    exit()
                if len(eachProperty) == 4:
                    attributes = eachProperty[3]
                else:
                    attributes = " "
                wikiTitle = eachProperty[0]
                wikiId = eachProperty[1]
                #print wikiId
                #print type(wikiId)
                score = eachProperty[2]
                wikiIdSet.append(int(wikiId))
        #print wikiIdSet
        return wikiIdSet
    except IOError, e:
        print 'Could not open file:', e

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "sys.argv[1]: input file!"
        exit()
    print getWikiId(sys.argv[1])
