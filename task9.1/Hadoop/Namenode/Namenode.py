import os
import speech_recognition as sr
from Hadoop import Hadoop
import pyttsx3
def Namenode():
	os.system("tput setaf 2")
	os.system("echo 'Namenode' | figlet -f 3d_row -d ./fonts/ ")
	os.system("sleep 3")
	os.system("tput setaf 1")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("clear")
		os.system("tput setaf 1")
		print("The available Requriments in Namenode")
		os.system("tput setaf 5") 
		print("\n\t\t\tConfigure Namenode\n\t\t\tformat namenode\n\t\t\tstart service of namenode\n\t\t\tstatus of namenode\n\t\t\t\n\t\t\thadoop report\n\t\t\tstop service of namenode\n\t\t\tGo to hadoop\n\t\t\tTo go Main Menu")
		os.system("tput setaf 3")
		print("Start Saying your Requirement in Namenode")
		pyttsx3.speak("Start Saying your Requirement in Namenode")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	print("Processing your Requirement, plz wait....")
	pyttsx3.speak("Processing your Requirement, please wait")
	namenode= r.recognize_google(audio)
	print(namenode)
	if(("configure namenode" in namenode) or ("configure masternode" in namenode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Namenode| figlet -f 3d_row -d ./fonts/ ")
		namenode_ip= input("Enter IP of Namenode at which you want to configure :")
		os.system("scp namenode.py root@{}:/root/".format(namenode_ip))
		os.system("ssh root@{} python3 namenode.py".format(namenode_ip))
	elif(("format namenode" in namenode) or ("format masternode" in namenode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Namenode Format| figlet -f 3d_row -d ./fonts/ ")
		namenode_ip= input("Enter IP of Namenode at which you want to configure :")
		os.system("ssh root@{} hadoop namenode -format".format(namenode_ip))
	elif(("start service of namenode" in namenode) or ("start service of masternode" in namenode) or ("start daemon of namenode" in namenode) or ("start daemon of masternode" in namenode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Namenode starting Daemon | figlet -f 3d_row -d ./fonts/ ")
		namenode_ip= input("Enter IP of Namenode at which you want to configure :")
		os.system("ssh root@{} hadoop-daemon.sh start namenode".format(namenode_ip))
	elif(("status of namenode" in namenode) or ("status of masternode" in namenode) or ("masternode status" in namenode) or ("masternode status" in namenode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Namenode status| figlet -f 3d_row -d ./fonts/ ")
		namenode_ip= input("Enter IP of Namenode at which you want to configure :")	
		os.system("ssh root@{} jps".format(namenode_ip))
	elif(("stop service of namenode" in namenode) or ("stop service of masternode" in namenode) or ("stop daemon of namenode" in namenode) or ("stop daemon of masternode" in namenode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo Namenode stopping Daemon | figlet -f 3d_row -d ./fonts/ ")
		namenode_ip= input("Enter IP of Namenode at which you want to configure :")
		os.system("ssh root@{} hadoop-daemon.sh stop namenode".format(namenode_ip))
	elif(("cluster report" in namenode) or ("hadoop report" in namenode) or ("hadoop cluster report" in namenode)):
		pyttsx3.speak("wait a second Processing your Requirement")
		os.system("tput setaf 6")
		os.system("echo hadoop report | figlet -f 3d_row -d ./fonts/ ")
		datanode_ip= input("Enter IP of datanode/namenode at which you want to configure :")
		os.system("ssh root@{} hadoop dfsadmin -report".format(namenode_ip))
	elif("main menu" in namenode):
		 main.main()
	elif("hadoop menu" in namenode):
		 Hadoop.Hadoop()
	else :
        	print("select Correct requirement...")
while(True):
	Namenode()
