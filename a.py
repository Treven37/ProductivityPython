import subprocess
import math
import os
from localStoragePy import localStoragePy
localStorage = localStoragePy('learn', 'text')
if (localStorage.getItem('lvl')):
	i = float(localStorage.getItem('lvl'))
else:
	i = 1

os.system("history -c ")
os.system("am start --user 0 -n com.beforesoft.launcher/com.beforesoftware.launcher.activities.LauncherActivity ")
os.system("clear ")
print("Level: ", localStorage.getItem('lvl'))
	