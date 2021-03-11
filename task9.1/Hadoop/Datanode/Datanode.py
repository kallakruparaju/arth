import os
import speech_recognition as sr
from Hadoop import Hadoop
import pyttsx3
def Datanode():
	os.system("tput setaf 2")
	os.system("echo 'Datanode' | figlet -f 3d_row -d ./fonts/ ")
	os.system("sleep 3")
	os.system("tput setaf 1")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("clear")
		os.system("tput setaf 1")
		print("The available Requriments in Datanode")
		os.system("tput setaf 5") 
		print("\n\t\t\tConfigure datanode\n\t\t\tstart service of datanode\n\t\t\tstatus of datanode\n\t\t\t\n\t\t\thadoop report\n\t\t\tstop service of datanode\n\t\t\tGo to hadoop\n\t\t\tTo go Main Menu")
		os.system("tput setaf 3")
		print("Start Saying your Requirement in Datanode")
		pyttsx3.speak("Start Saying your Requirement in Datanode")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	print("Processing your Requirement, plz wait....")
	pyttsx3.speak("Processing your Requirement, please wait")
	datanode= r.recognize_google(audio)
	print(namenode)
	if(("configure datanode" in datanode) or ("configure slavenode" in datanode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo datanode| figlet -f smmono12 -d ./figletfonts40/")
		datanode_ip= input("Enter IP of datanode at which you want to configure :")
		os.system("scp datanode.py root@{}:/root/".format(datanode_ip))
		os.system("ssh root@{} python3 datanode.py".format(datanode_ip))
	elif(("start service of datanode" in datanode) or ("start service of slavenode" in datanode) or ("start daemon of datanode" in datanode) or ("start daemon of slavenode" in datanode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo datanode starting Daemon | figlet -f smmono12 -d ./figletfonts40/")
		datanode_ip= input("Enter IP of datanode at which you want to configure :")
		os.system("ssh root@{} hadoop-daemon.sh start datanode".format(datanode_ip))
	elif(("status of datanode" in datanode) or ("status of slavenode" in datanode) or ("slavenode status" in datanode) or ("slavenode status" in datanode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo datanode status| figlet -f smmono12 -d ./figletfonts40/")
		datanode_ip= input("Enter IP of datanode at which you want to configure :")	
		os.system("ssh root@{} jps".format(datanode_ip))
	elif(("stop service of datanode" in datanode) or ("stop service of slavenode" in datanode) or ("stop daemon of datanode" in datanode) or ("stop daemon of slavenode" in datanode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo datanode stopping Daemon | figlet -f smmono12 -d ./figletfonts40/")
		datanode_ip= input("Enter IP of datanode at which you want to configure :")
		os.system("ssh root@{} hadoop-daemon.sh stop datanode".format(datanode_ip))
	elif(("cluster report" in datanode) or ("hadoop report" in datanode) or ("hadoop cluster report" in datanode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo hadoop report | figlet -f smmono12 -d ./figletfonts40/")
		datanode_ip= input("Enter IP of datanode at which you want to configure :")
		os.system("ssh root@{} hadoop dfsadmin -report".format(datanode_ip))
	elif("main menu" in datanode):
		 main.main()
	elif("hadoop menu" in datanode):
		 Hadoop.Hadoop()
	else :
        	print("select Correct requirement...")
while(True):
	Datanode()
