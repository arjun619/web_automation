#!/usr/bin/python3

import subprocess
import cgi
import os

print("content-type: text/plain")
print()

w=subprocess.getoutput("sshpass -p '47695' scp /var/www/cgi-bin/thisfile.txt root@192.168.54.23:/root")
print(w)
print(subprocess.getoutput("whoami"))
#l=subprocess.getoutput("ansible all -m copy -a 'src=/root/ip.txt dest=/root'")
#print(l)
print("Files Updated go back to the previous page ")
