#!/usr/bin/env python

import datetime

print datetime.datetime.now()

# adding more features
num = 0
for x in range(10):
    num += x
print x
print 'some more things happened'

for y in range(20):
    num += y * y

print y
print 'final version 2'
