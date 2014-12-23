#!/bin/env python
# -*- coding: utf-8 -*-
# hello.py

#name = raw_input('Pls input your name:')
#print 'Hello', name

classmates = ['Bob','Tina','Yanyan']
print classmates
for name in classmates:
    print name

#age = raw_input('Pls input your age:')
age = 30
if age >= 18:
    print age,'Adult.'
else:
    print age,'Teenager'

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print sum

sum = 100
n = 100
while n > 0:
    n = n-2
    sum = sum + n
print sum

#birth = int(raw_input('Pls input ur birth year:'))
birth = 2008
if birth > 2000:
    print '蛋蛋后'
else:
    print '蛋蛋前'
# 蛋蛋后

family = {'anata':'xc','xfer':'hh'}
print family['anata']
print family.get('anata')
print family.iterkeys()

s1 = set([1,1,2,3,4,5,6,6,6,8,7])
s2 = set([3,5,20,100,88])
print s1
print s2
print s1 & s2
print s1 | s2