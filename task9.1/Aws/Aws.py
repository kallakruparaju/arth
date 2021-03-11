import os
import speech_recognition as sr
import pyttsx3
def Aws():
	os.system("tput setaf 2")
	os.system("echo 'Aws' | figlet -f 3d_row -d ./fonts/ ")
	os.system("sleep 3")
	os.system("tput setaf 1")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("clear")
		os.system("tput setaf 1")
		print("The available Requriments in AWS")
		os.system("tput setaf 5") 
		print("\n\t\t\taws configure\n\t\t\tKey-pair\n\t\t\tcreate security group\n\t\t\tcreate security rule \n\t\t\tlaunch aws instance\n\t\t\tlaunch redhat instance\n\t\t\tstart instance\n\t\t\tstop instance\n\t\t\tdescribe instance\n\t\t\tcreate volume\n\t\t\tattach volume\n\t\t\tdetach volume\n\t\t\tTo go main menu") 
		os.system("tput setaf 3")
		print("Start Saying your Requirement in AWS")
		pyttsx3.speak("Start Saying your Requirement in AWS")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	print("Processing your Requirement, plz wait....")
	pyttsx3.speak("Processing your Requirement, please wait")
	aws= r.recognize_google(audio)
	print(aws)
	
	if(("configure aws" in aws) or ("aws configuration" in aws) ):	
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo aws configure| figlet -f 3d_row -d ./fonts/ ")
		os.system("aws configure")
	elif(("create key pair" in aws) or ("key pair" in aws)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Key-pair | figlet -f 3d_row -d ./fonts/ ")
		keyname=input("enter key name : ")
		keyfile=input("enter filename for key : ")
		os.system("aws ec2 create-key-pair --key-name {}  --output text > {}.pem".format(keyname,keyfile))
	elif(("create security group" in aws) or ("security group" in aws)):	
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo security group| figlet -f 3d_row -d ./fonts/ ")
		groupname =input("enter group name : ")
		description=input("enter description : ")
		os.system("aws ec2 create-security-group --group-name {}  --description {}".format(groupname,description))
	elif(("create security rule" in aws) or ("security ingress rule" in aws)):	
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo security rule | figlet -f 3d_row -d ./fonts/ ")
		groupname =input("enter group name : ")
		protocol=input("enter protocol name : ")
		port=input("enter protocol name : ")
		os.system("aws ec2 authorize-security-group-ingress  --group-name  {} --protocol {} --port {}  --cidr 0.0.0.0/0".format(groupname,protocol,port))
	elif(("launch aws instance" in aws) or ("launch aws instances" in aws)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo launch instance | figlet -f 3d_row -d ./fonts/ ")
		keyname=input("enter key name : ")
		securitygroupid=input("enter security group id : ")
		os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(keyname,securitygroupid))
	elif(("launch redhat instance" in aws) or ("launch redhat instances" in aws)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo launch instance | figlet -f 3d_row -d ./fonts/ ")
		keyname=input("enter key name : ")
		securitygroupid=input("enter security group id : ")
		os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(keyname,securitygroupid))
	elif(("start instance" in aws) or ("start instances" in aws)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo start instance| figlet -f 3d_row -d ./fonts/ ")
		instanceid=input("enter instance id: ")
		os.system(" aws ec2 start-instances --instance-id {}".format(instanceid))
	elif(("stop instance" in aws) or ("stop instances" in aws)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo stop instance| figlet -f 3d_row -d ./fonts/ ")
		instanceid=input("enter instance id: ")
		os.system(" aws ec2 stop-instances --instance-id {}".format(instanceid))
	elif(("describe instance" in aws) or ("describe instances" in aws)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo describe instance| figlet -f 3d_row -d ./fonts/ ")
		os.system("aws ec2 describe-instances")
	elif("create volume" in aws):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo create volume | figlet -f 3d_row -d ./fonts/ ")
		availabilityzone=imput("enter availability zone: ")
		size=input("enter size of volume: ")
		volumetype=input("volume type: ")
		os.system("aws ec2 create-volume --volume-type {}--size {}  --availability-zone {}".format(volumetype,size,availabilityzone))
	elif("attach volume" in aws):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo attach volume | figlet -f 3d_row -d ./fonts/ ")
		volumeid=input("enter volume id: ")
		instanceid=input("enter instance id: ")
		os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volumeid,instanceid))
	elif("detach volume" in aws):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo detach volume | figlet -f 3d_row -d ./fonts/ ")
		volumeid=input("enter volume id: ")
		instanceid=input("enter instance id: ")
		os.system("aws ec2 detach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volumeid,instanceid))
	elif("main menu" in aws):
		 main.main()
	else :
        	print("select Correct requirement...")

while(True):	
	Aws()
