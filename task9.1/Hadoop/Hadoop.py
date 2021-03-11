import os
import speech_recognition as sr
import pyttsx3
def Hadoop():
	os.system("tput setaf 2")
	os.system("echo 'Hadoop' | figlet -f 3d_row -d ./fonts/ ")
	os.system("sleep 3")
	os.system("tput setaf 1")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("clear")
		os.system("tput setaf 1")
		print("The available Requriments in Hadoop")
		os.system("tput setaf 5") 
		print("\n\t\t\tConfigure Namenode\n\t\t\tConfigure Datanode\n\t\t\tConfigure Client\n\t\t\tTo go Main Menu")
		os.system("tput setaf 3")
		print("Start Saying your Requirement in Hadoop")
		pyttsx3.speak("Start Saying your Requirement in Hadoop")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	print("Processing your Requirement, plz wait....")
	pyttsx3.speak("Processing your Requirement, please wait")
	hadoop= r.recognize_google(audio)
	print(hadoop)
	if(("configure namenode" in hadoop) or ("configure masternode" in hadoop)):
		Namenode.Namenode()
	elif(("configure datanode" in hadoop) or ("configure slavenode" in hadoop)):
		Datanode.Datanode()
	elif("configure client" in hadoop):
		Client.Client()
	elif("main menu" in Hadoop):
		 main.main()
	else :
        	print("select Correct requirement...")
	
	
	

while(True):	
	Hadoop()
