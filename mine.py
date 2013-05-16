#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setting
from boto.sqs import connect_to_region
from datetime import datetime
from time import sleep
import json

aws = connect_to_region(setting.AWSREGION, aws_access_key_id=setting.AWSID, aws_secret_access_key=setting.AWSPWD)
print aws.get_all_queues()

q = aws.get_queue(setting.QUEUE_NAME)
print q.count()

'''
for i in xrange(5):
    m = q.new_message(json.dumps({'date': str(datetime.now())}))
    print m
    print q.write(m)
'''

def doing(something):
    try:
        r = json.loads(something)
        print r['date']
        return True
    except Exception as e:
        print e
        return False

def run_sqs(do):
    sleep_times = 0
    while 1:
        rest = q.count()
        print rest
        if rest:
            for i in xrange(setting.FEEDS):
                read_m = q.read()
                if read_m:
                    #print json.loads(read_m.get_body())
                    print do(read_m.get_body())
                    sleep_times = 0
                    #print q.delete_message(read_m)
                else:
                    print u'No msg.'
                    break
        else:
            if sleep_times >= setting.SLEEP_TIMES:
                break
            else:
                print 'ADD sleep_times'
                sleep_times += 1
                sleep(setting.SLEEP_SECONDS)

if __name__ == '__main__':
    run_sqs(doing)
