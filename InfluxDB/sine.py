#!/usr/bin/python

import json
import math
import sys

from time import sleep

import requests


DATABASE = 'perfmondb'
STATUS_MOD = 10

n = 0
while True:
    for d in range(0, 360):
        v = [{'name': 'sin', 'columns': ['val'], 'points': [[math.sin(math.radians(d))]]}]
        r = requests.post('http://192.168.208.45:8086/db/%s/series?u=root&p=root' % DATABASE, data=json.dumps(v))
        if r.status_code != 200:
            print 'Failed to add point to influxdb -- aborting.'
            sys.exit(1)
        n += 1
        sleep(1)
        if n % STATUS_MOD == 0:
            print '%d points inserted.' % n