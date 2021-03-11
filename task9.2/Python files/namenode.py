#!/usr/bin/python3
print("content-type: text/html")
print()

import subprocess as sp
import cgi
form = cgi.FieldStorage()
namenodeip = form.getvalue("x")
cmd="scp namenode_hdfs_site.py root@{0}:/root/".format(namenodeip)
output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status==0:
    print("output :{} ".format (out))
else:
    print("Some Error occured : {}".format (out) )
