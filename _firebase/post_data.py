#! /usr/bin/env python

import sys

from db import Db
from config import config

fb_url = config['firebase']
rootRef = '/sample/status/'

if len(sys.argv) > 1:
    data = sys.argv[1]
    # location, timestamp, temperature, pressure, altitude, humidity
    data = data.split(",")
    if len(data) == 6:
        status = {
            "timestamp": data[1],
            "temperature": data[2],
            "pressure": data[3],
            "altitude": data[4],
            "humidity": data[5]
        }

        db_ = Db(fb_url)
        rootRef += "/" + data[0]
        res = db_.post_data(rootRef, status)
        if res:
            # for debug
            print "Firebase: Data posted successfully"

    else:
        # debug
        print "Error: Data not in format: location, timestamp, temperature, pressure, altitude, humidity"
