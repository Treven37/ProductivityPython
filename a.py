import subprocess
import math
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
if (int(i) > 1):
	localStorage.setItem('exp', i)
	a = input("Are you sure you want to open unproductive app? (Y/N)")
	if (a == "Y"):
		os.system("am start --user 0 -n com.beforesoft.launcher/com.beforesoftware.launcher.activities.LauncherActivity ")
		os.system("history -c ")
		os.system("clear ")
		print("Level: ", "%.2f"%math.cbrt(i*i2*i3))
else:
	localStorage.setItem('exp', i)
	a = input("\n\n\nAre you sure you want to open unproductive app? (Y/N)")
	if (a == "Y"):
		os.system("am start --user 0 -n com.beforesoft.launcher/com.beforesoftware.launcher.activities.LauncherActivity ")
		os.system("history -c ")
		os.system("clear ")
		print("Level: ", "%.2f"%math.cbrt(i*i2*i3))
	