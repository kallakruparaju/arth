import os
import speech_recognition as sr
import pyttsx3
from Docker import Docker
from Aws import Aws
from Hadoop import Hadoop
os.system("tput setaf 2")
os.system("echo 'Welcome to Python Automation Menu' | figlet -f 3d_row -d ./fonts/ ")
os.system("sleep 3")
os.system("tput setaf 1")
def main():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		os.system("tput setaf 6")
		os.system("clear")
		os.system("tput setaf 1")
		print("The available Technologies")
		os.system("tput setaf 5")
		print("\nDocker\nHadoop\nAWS")
		os.system("tput setaf 2")
		print("Start Saying your Requirement Technology")
		pyttsx3.speak("Start Saying your Requirement Technology")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	print("Processing your Requirement, plz wait....")
	pyttsx3.speak("Processing your Requirement, please wait")
	technology= r.recognize_google(audio)
	print(technology)
	if("docker" in technology):
		Docker.Docker()
	if("hadoop" in technology):
		Hadoop.Hadoop()
	if("aws" in technology):
		Aws.Aws()
	else :
        	print("select Correct Technology...")

if __name__ == "__main__":
    main()
