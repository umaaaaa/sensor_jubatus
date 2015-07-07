#!/usr/bin/env python
# coding: utf-8
import jubatus
from lux_classifier import LuxClassifier

# host = '192.168.33.10'
host = '127.0.0.1'
port = 9199
name = 'test2'

client = jubatus.Classifier(host, port, name)
lux_classifier = LuxClassifier()
lux_classifier.train(client)
