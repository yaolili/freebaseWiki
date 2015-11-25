#########################################################################
# File Name: linkMysql.py
# Author: yaolili
# mail: yaolili@pku.edu.cn
# Created Time: Sun 15 Nov 2015 10:03:07 PM CST
#########################################################################
##!/usr/bin/python

import os
import sys
import MySQLdb

def connectDB(wikiIdEntity):
    try:
        db = MySQLdb.connect(host="localhost", user="root", passwd="q1w2e3r4", db="wikiLink" )
    except e:
        print e
    cursor = db.cursor()
    result = {}
    wikiIdSet = []
    for key in wikiIdEntity:
        wikiIdSet.append(key)
    for wikiId in wikiIdSet:
        sql = "SELECT * FROM wikiPro WHERE wikiId = %d" % (wikiId)
        cursor.execute(sql)
        #Notice! Here you can't use like this: result.append(cursor.fetchone())
        string = cursor.fetchone()
        #print string
        #print type(string)
        
        if(string):
            sqlEntity = str(string[0]) + ":" + wikiIdEntity[int(string[0])]
            result[sqlEntity] = string[1]
    return result
    db.close()

if __name__ == '__main__':
    #test usage!
    aList = [2100075, 25964, 46313, 22212, 10779, 1564205, 5177, 435268, 5177, 30010, 30003, 52648, 195718, 25964, 11604823, 689, 5334607, 101623, 101623, 101623, 47917, 4721, 31717, 4721, 221773]
    print connectDB(aList)
