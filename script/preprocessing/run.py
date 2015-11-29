#########################################################################
# File Name: run.py
# Author: yaolili
# mail: yaolili@pku.edu.cn
# Created Time: Sun 15 Nov 2015 09:10:30 PM CST
#########################################################################
##!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
from getWikifierEntity import getWikiIdEntity
from linkMysql import connectDB

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "sys.argv[1]: input test.txt.wikification.tagged.full.xml file"
        print "sys.argv[2]: ouput file"
        exit()
    
    output = file(sys.argv[2], 'w+')
    wikiIdEntity = getWikiIdEntity(sys.argv[1])
    result = connectDB(wikiIdEntity)
    #print result
    #print type(result)
    for key in result:
        output.write(key + "\t" + result[key] + "\n")
    output.close()
