#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
input= form.getvalue("lvm")
if(input=="fdisk"):
	cmd = "sudo fdisk -l "
	output = sp.getstatusoutput(cmd)
	print(output)
	if output[0] == 0:
		print(output[1])
elif(input=="mountpoints"):
	cmd = "sudo df -h"
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="cpv"):
	devicename= form.getvalue("devicename")
	cmd = "sudo pvcreate {}".format(devicename)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="dpv"):
	devicename= form.getvalue("devicename")
	cmd = "sudo pvdisplay {}".format(devicename)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="cvg"):
	vgname= form.getvalue("vgname")
	devicename= form.getvalue("devicename")
	cmd = "sudo vgcreate {} {} ".format(vgname,devicename)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="dvg"):
	vgname= form.getvalue("vgname")
	cmd = "sudo vgdisplay {}".format(vgname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="clv"):
	vgname= form.getvalue("vgname")
	lvname= form.getvalue("lvname")
	size= form.getvalue("size")
	cmd = "sudo lvcreate --size {}G --name {} {}".format(size,lvname,vgname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="dlv"):
	vgname= form.getvalue("vgname")
	lvname= form.getvalue("lvname")
	cmd = "sudo lvdisplay {}/{}".format(vgname,lvname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="flv"):
	vgname= form.getvalue("vgname")
	lvname= form.getvalue("lvname")
	cmd = "sudo mkfs.ext4 /dev/{}/{}".format(vgname,lvname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="elv"):
	vgname= form.getvalue("vgname")
	lvname= form.getvalue("lvname")
	size= form.getvalue("size")
	cmd = "sudo lvextend --size +{}G /dev/{}/{}".format(size,vgname,lvname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="rlv"):
	vgname= form.getvalue("vgname")
	lvname= form.getvalue("lvname")
	cmd = "sudo resize2fs /dev/{}/{}".format(vgname,lvname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
else:
	print("choose correct option")
	
	



	

