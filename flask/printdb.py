#usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json

class getmongo:
    con = MongoClient('127.0.0.1', 27017)
    db = con["sensordb"]
    # col = db.false_collection
    col = db.predict
    global dic
    dic = {}
    count = 0
    
    for data in col.find():
        del data['_id']
# Bson$B$r(BJson$B$KJQ49(B
        json_list = json.dumps(data)
# Json$B$r%G%#%/%7%g%J%j$KJQ49(B
        dic[count] = json.loads(json_list)
        print dic[count]
        count += 1
