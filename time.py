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
		os.system("am start --user 0 -n de.niklaskellner.floatingcounter/de.niklaskellner.floatingcounter.gui.activity.MainActivity ")
	if a == "c":
		a = "Create"
	c.append(a)
	d.append(taskEnd)
	
print(str(d[0]) + ": " + c[0])
print("in progress")
meow = int(datetime.datetime.now().minute)
while(int(d[0].minute) + 15 >= meow):
	meow = int(datetime.datetime.now().minute)
	time.sleep(1)
while(int(d[0].minute) + 15 < meow): 
	end = input("done?(y/h/n)")
	if end == "y":
		i=i+1
	elif end == "h":
		i=i+0.37
	if (end == "y" or end == "n" or end == "h"):
		break
localStorage.setItem('lvl', float(i))
os.system("clear ")
print("Level: ", localStorage.getItem('lvl'))