#!/usr/bin/python3
print("content-type: text/html")
print()

import cgi
import subprocess
import webbrowser
cmd=cgi.FieldStorage()
cmd=cmd['service'].value
print(cmd)

if cmd=="linux":
    t= subprocess.getoutput("webbrowser.open_new_tab(192.168.54.248/linux_menu.html")
    print(t)
if cmd=="aws":
    t=subprocess.getoutput("webbrowser.open_new_tab(192.168.54.248/aws_menu.html)")
    print(t)
    





