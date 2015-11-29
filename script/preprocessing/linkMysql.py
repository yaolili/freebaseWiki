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
    result = {}

    if not wikiIdEntity:
        return result
    try:
        db = MySQLdb.connect(host="localhost", user="root", passwd="q1w2e3r4", db="wikiLink" )
        cursor = db.cursor()
        wikiIdSet = []
        for key in wikiIdEntity:
            wikiIdSet.append(key)
        for wikiId in wikiIdSet:
            getStrSql = "SELECT property FROM wikiPro WHERE wikiId = %d" % (wikiId)
            cursor.execute(getStrSql)
            #Notice! Here you can't use like this: result.append(cursor.fetchone())
            string = cursor.fetchone()
            idSql = "SELECT freebaseId FROM wikiFreebaseId WHERE wikiId = %d" % (wikiId)
            cursor.execute(idSql)
            freebaseId = cursor.fetchone()
            if string and freebaseId:
                sqlEntity = freebaseId[0] + ":" + wikiIdEntity[wikiId]
                result[sqlEntity] = string[0]
        return result
    except MySQLdb.Error, e:
        print e    
    db.close()

if __name__ == '__main__':
    #test usage! can not use now!
    aList = [2100075, 25964, 46313, 22212, 10779, 1564205, 5177, 435268, 5177, 30010, 30003, 52648, 195718, 25964, 11604823, 689, 5334607, 101623, 101623, 101623, 47917, 4721, 31717, 4721, 221773]
    print connectDB(aList)
