#!/usr/bin/python3
print("content-type: text/plain")
print()

import subprocess as sp
import cgi

form = cgi.FieldStorage()
input= form.getvalue("docker")
if(input=="images"):
	cmd = "sudo docker images"
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="containers"):
	cmd = "sudo docker ps -a"
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="container"):
	cmd = "sudo docker ps"
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print(output[1])
elif(input=="start"):
	osname= form.getvalue("osname")
	cmd = "sudo docker start {}".format(osname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("The container started")
elif(input=="attach"):
	osname= form.getvalue("osname")
	cmd = "sudo docker attach {}".format(osname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("The container attached")
elif(input=="stop"):
	osname= form.getvalue("osname")
	cmd = "sudo docker stop {}".format(osname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("The container stopped")
elif(input=="launch"):
	osname= form.getvalue("osname")
	image=form.getvalue("image")
	cmd = "sudo docker run -dit --name {} {}".format(osname,image)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("the os is launched with {}".format(image))		
		
	
elif(input=="containerremove"):
	osname= form.getvalue("osname")
	cmd = "sudo docker rm -f {}".format(osname)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("The container removed")
elif(input=="imageremove"):
	image= form.getvalue("image")
	cmd = "sudo docker rmi -f {}".format(image)
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("The image removed")
elif(input=="remove"):
	cmd = "sudo docker rm -f $(docker ps -qa)"
	output = sp.getstatusoutput(cmd)
	if output[0] == 0:
		print("all containers removed")
else:
	print("choose correct option")
	

