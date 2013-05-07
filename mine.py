#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setting
from boto.sqs import connect_to_region
from datetime import datetime

aws = connect_to_region(setting.AWSREGION, aws_access_key_id=setting.AWSID, aws_secret_access_key=setting.AWSPWD)
print aws.get_all_queues()

q = aws.get_queue('twilio_coscup')
print q.count()

m = q.new_message(str(datetime.now()))
print m
print q.write(m)

read_m = q.read()
if read_m:
    print read_m.get_body()
    #print q.delete_message(read_m)
else:
    print u'No msg.'
