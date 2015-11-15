#########################################################################
# File Name: run.py
# Author: yaolili
# mail: yaolili@pku.edu.cn
# Created Time: Sun 15 Nov 2015 09:10:30 PM CST
#########################################################################
##!/usr/bin/python

import sys
import os
from getWikifierEntity import getWikiId
from linkMysql import connectDB

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "sys.argv[1]: input test.txt.wikification.tagged.full.xml file"
        print "sys.argv[2]: output file!"
        exit()

    wikiIdSet = getWikiId(sys.argv[1])
    print wikiIdSet
    result = connectDB(wikiIdSet)
    print result
