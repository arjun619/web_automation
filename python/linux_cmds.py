#!/usr/bin/python3

import subprocess
import cgi
import os

print("content-type: text/html")
print()
a=cgi.FieldStorage()
cmd=a['option'].value
print(cmd)
cmd=int(cmd)
if cmd==1:
	print(subprocess.getoutput("date"))
elif cmd==2:
	print(subprocess.getoutput("free -m"))
elif cmd==3:
	print(subprocess.getoutput("cal"))

else:
	print("enter valid command")

