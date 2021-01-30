import os
import os.path as p
import sys
import platform


'''
files = os.listdir()
for i in files:
	print (i,"->",p.isfile(i))
'''

'''
stats = os.stat("Test.py")
print(stats.st_size)
'''

'''
for path in sys.path:
	print(path)
'''

for f in dir(platform):
	print(f)
	
print(platform.architecture())
print(platform.release())
print(platform.os)
print(platform.version())