#!/usr/bin/env python
# coding: utf-8

# host = '192.168.33.10'
host = '127.0.0.1'
port = 9199
name = 'test2'

import sys
import json
import random
import jubatus
from jubatus.common import Datum
from getmongo import convertMongo 
from getpre import preMongo

getmongo = convertMongo()

class LuxClassifier():

    def train(self, client, mongo_ip, mongo_port, db_name, collection_name):
        train_sensors_dic = getmongo.getTrainSensorsDic(mongo_ip, mongo_port,
                                                        db_name,  collection_name)
        train_sensor_data = []
        value = 0

        for line in train_sensors_dic:
            value  = train_sensors_dic[line]['Value']
            result = train_sensors_dic[line]['Result']
            train_sensor_data.append((result, Datum({'Value': value})))

        # training data must be shuffled on online learning!
        random.shuffle(train_sensor_data)

        # run train
        client.train(train_sensor_data)
        print 'Train Complete!'

    def predict(self, client, mongo_ip, mongo_port, db_name):
        getpre  = preMongo()
        dic_pre = getpre.getDic()
        data = []
        predict_result = []

        for line in dic_pre:
            value = dic_pre[line]['Value']
            data.append(Datum({'Value':value}))
        
        for d in data:
            res = client.classify([d])
            # getmongo.postDB(max(res[0], key=lambda x: x.score).label, str(d.num_values[0][1]))

            sys.stdout.write(max(res[0], key=lambda x: x.score).label)
            sys.stdout.write(' ')
            sys.stdout.write(str(d.num_values[0][1]))
            sys.stdout.write('\n')

            hoge = str(d.num_values[0][1])
            predict_result.append({'Result': (max(res[0], key=lambda x: x.score).label), 
                                   'Value'  : hoge})

        return predict_result

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.Classifier(host, port, name)
    lux_classifier = LuxClassifier()
    lux_classifier.train(client, '127.0.0.1', 27017, 'sensordb', 'sensors')
    # lux_classifier.predict(client)
