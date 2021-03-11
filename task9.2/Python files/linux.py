#!/usr/bin/python3
import subprocess 
import cgi
print("content-type:text/plain")
print()

form=cgi.FieldStorage()
cmd=form.getvalue("input")
y="sudo {}".format(cmd)
z=subprocess.getoutput(y)
print(z)







			


