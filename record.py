import subprocess
import math
import datetime
import os
from localStoragePy import localStoragePy
localStorage = localStoragePy('learn', 'text')
if (localStorage.getItem('lvl')):
	i = float(localStorage.getItem('lvl'))
else:
	i = 1

if (localStorage.getItem('date')):
	date = int(localStorage.getItem('date'))
else:
	date = 0
	
if (datetime.datetime.now().day != date):
	if (localStorage.getItem('recordlvl')):
		record = localStorage.getItem('recordlvl')
		r = record.split("\n")
		imp=math.cbrt(i*i2*i3)-float(r[-1])
		record+="\n"+str(imp)
		record+="\n"+str(math.cbrt(i*i2*i3))
	else:
		record = ""
		record += str(i)
	localStorage.setItem('date', datetime.datetime.now().day)
	localStorage.setItem('recordlvl', record)
else:
	pass
print(localStorage.getItem('recordlvl'))