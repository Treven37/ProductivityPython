import subprocess
import math
import datetime
import os
from localStoragePy import localStoragePy
localStorage = localStoragePy('learn', 'text')
if (localStorage.getItem('a')):
	i = float(localStorage.getItem('a'))
else:
	i = 1
if (localStorage.getItem('b')):
	i2 = float(localStorage.getItem('b'))
else:
	i2 = 1
if (localStorage.getItem('c')):
	i3 = float(localStorage.getItem('c'))
else:
	i3 = 1

if (localStorage.getItem('date')):
	date = int(localStorage.getItem('date'))
else:
	date = 0
	
if (datetime.datetime.now().day != date):
	if (localStorage.getItem('record')):
		record = localStorage.getItem('record')
		r = record.split("\n")
		imp=math.cbrt(i*i2*i3)-float(r[-1])
		record+="\n"+str(imp)
		record+="\n"+str(math.cbrt(i*i2*i3))
	else:
		record = ""
		record += str(math.cbrt(i*i2*i3))
	localStorage.setItem('date', datetime.datetime.now().day)
	localStorage.setItem('record', record)
else:
	pass
print(localStorage.getItem('record'))