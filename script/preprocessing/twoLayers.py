#-*- coding:utf-8 -*-
# AUTHOR:   yaolili
# FILE:     twoLayers.py
# ROLE:     get properties of specific freebaseId 
# CREATED:  2015-11-28 14:45:23
# MODIFIED: 2015-11-28 20:20:52

import sys
import os
import re
import MySQLdb

def connectDB(freebaseIdList):
    result = {}
    if not freebaseIdList:
        return result
    try:
        db = MySQLdb.connect(host="localhost", user="root", passwd="q1w2e3r4", db="wikiLink")
        cursor = db.cursor()
        for freebaseId in freebaseIdList:
            sql = "SELECT wikiId FROM wikiFreebaseId WHERE freebaseId = \"%s\"" % (freebaseId)
            cursor.execute(sql)
            wikiId = cursor.fetchone()
            if wikiId:
                wikiId = int(wikiId[0])
                getStringSql = "SELECT property FROM wikiPro WHERE wikiId = %d" % (wikiId)
                cursor.execute(getStringSql)
                string = cursor.fetchone()
                if string:
                    #print "string match!"
                    result[freebaseId] = string
        return result
    except MySQLdb.Error, e:
        print e
    db.close()

def isFreebaseEntity(obj):
    reStr = "^m\..+"
    result = re.match(reStr, obj)
    if result:
        return True
    else:
        return False

def twoLayers(inputFile, outputFile):
    result = open(outputFile, "w+")
    try:
        with open(inputFile, "r") as fin:
            for lineNum, line in enumerate(fin):
                freebase, string = line.strip().split("\t")
                pattern = r"(\[.*?\])";
                reResult = re.findall(pattern, string, re.M)
                if(reResult):
                    freebaseIdList = []
                    for i in range(0, len(reResult)):
                        reResult[i] = reResult[i].replace('[','').replace(']','')
                        predicate, obj = reResult[i].strip().split(", ")
                        obj = obj.strip().split("'")
                        if(isFreebaseEntity(obj[1])):
                            freebaseIdList.append(obj[1])
                    secondInfo = connectDB(freebaseIdList)
                    if secondInfo:
                        for key in secondInfo:
                            result.write(str(lineNum) + ":" + key + "\t" + str(secondInfo[key]) + "\n")
        print "file done!"
        result.close()
    except IOError, e:
        print 'Could not open file:', e
        exit()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "sys.argv[1]: input entity.txt file"
        print "sys.argv[2]: output file"
        exit()

    twoLayers(sys.argv[1], sys.argv[2])
