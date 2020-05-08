#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from datetime import datetime, date, timedelta, time

y = (datetime.today() + timedelta(minutes = -5)).strftime("%Y-%m-%dT%H:%M:%SZ")
a = (datetime.today() + timedelta(minutes = -5)).strftime("%Y-%m-%dT%H:%M:%SZ")
print(a)


