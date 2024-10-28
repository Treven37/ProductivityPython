import datetime
import os
import math
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
c = []
d = []
j = 0
while j < 1:
	print("task: \na. Improve Blood Flow\nb. Learn STEM or Connected Learnings\nc. Create")
	a = input();
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
if a == "Improve Blood Flow":
	print(str(d[0]) + ": " + c[0])
	j = int(input("How many minutes?"))
	i = i+(j/7)
if a == "Learn STEM/Other | Connected Learnings":
	j = int(input("How many Connected Learnings?"))*11
	i2 = i2+j
if a == "Create":
	i3 = int(input("SCC estimation of Cost to Develop the dir ∼/0\n"))/1073
localStorage.setItem('a', float(i))
localStorage.setItem('b', float(i2))
localStorage.setItem('c', float(i3))
os.system("clear ")
print("Level: ", "%.2f"%math.cbrt(i*i2*i3))

