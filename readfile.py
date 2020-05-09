# -*- coding: UTF-8 -*-

fileecs = open("ecsinstanceid")
instanceid = fileecs.readlines()
ino = len(instanceid)
i = 0
#print(instanceid)
for i in range(0,ino):
    newinstanceid = [x.strip() for x in instanceid if x.strip() != '']
    print(newinstanceid[i])
    i += 1