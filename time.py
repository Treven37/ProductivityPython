import datetime
import time
import os
import math
import random
from localStoragePy import localStoragePy
localStorage = localStoragePy('learn', 'text')
if (localStorage.getItem('lvl')):
	i = float(localStorage.getItem('lvl'))
else:
	i = 1
c = []
d = []
j = 0
start = input("do you have 15mins? (y/n)")
if start == "y":
	print("task: \na. Improve Blood Flow\nb. Learn STEM or Connected Learnings\nc. Create")
	a = random.choice("abc");
	if (c == []):
		last = datetime.datetime.now()
	else:
		last = d[-1]
	taskEnd = last + datetime.timedelta(minutes=0)
	if a == "a":
		a = "Improve Blood Flow"
	if a == "b":
		a = "Learn STEM/Other | Connected Learnings"
	if a == "c":
		a = "Create"
	c.append(a)
	d.append(taskEnd)
	j=j+1
print(str(d[0]) + ": " + c[0])
print("in progress")
time.sleep(10*60)
end = input("done?(y/h/n)")
if end == "y":
	i=i+1
elif end == "h":
	i=i+0.37
localStorage.setItem('lvl', float(i))
os.system("clear ")
print("Level: ", localStorage.getItem('lvl'))

