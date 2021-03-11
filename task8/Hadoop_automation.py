import os
os.system("tput setaf 1")
os.system("figlet -c My Menu")
os.system("tput setaf 2")
print("""
\n
\t\tpress 1 :To configure the Namenode
\t\tpress 2 :To configure the Datanode
\t\tpress 3 :To configure the Client
\t\tpress 4 :To EXIT
""")
os.system("tput setaf 6")
choice=int(input("Enter your choice  : "))
os.system("tput setaf 7")
while(True==1):
	os.system("tput setaf 1")
	os.system("figlet -c Hadoop Cluster")
	os.system("tput setaf 5")
	if choice==1:
		os.system("tput setaf 3")
		os.system("figlet -c Namenode")
		os.system("tput setaf 1")
		print("""
		\n
		\t\tpress 1 :To configure the Hdfs-site file
		\t\tpress 2 :To configure the Core-site file
		\t\tpress 3 :To Format the namenode
		\t\tpress 4 :To start the service of namenode
		\t\tpress 5 :To see the status of namenode
		\t\tpress 6 :To see the report of the hadoop cluster
		""")
		os.system("tput setaf 2")
		choice1=int(input("Enter your choice  : "))
		os.system("tput setaf 3")
		namenode_ip= input("Enter IP of Namenode at which you want to configure :")
		if choice1==1:
			
			os.system("scp namenode_hdfs_site.py root@{}:/root/".format(namenode_ip))
			os.system("ssh root@{} python3 namenode_hdfs_site.py".format(namenode_ip))
		elif choice1==2:
		
			os.system("scp namenode_core_site.py root@{}:/root/".format(namenode_ip))
			os.system("ssh root@{} python3 namenode_core_site.py".format(namenode_ip))
		elif choice1==3:
			
			os.system("ssh root@{} hadoop namenode -format".format(namenode_ip))
		elif choice1==4:
			
			os.system("ssh root@{} hadoop-daemon.sh start namenode".format(namenode_ip))
		elif choice1==5:
			
			os.system("ssh root@{} jps".format(namenode_ip))
		elif choice1==6:
			
			os.system("ssh root@{} hadoop dfsadmin -report".format(namenode_ip))
		
	elif choice==2:
		os.system("tput setaf 4")
		os.system("figlet -c Datanode")
		os.system("tput setaf 5")
		print("""
		\n
		\t\tpress 1 :To configure the Hdfs-site file
		\t\tpress 2 :To configure the Core-site file
		\t\tpress 3 :To start the service of datanode
		\t\tpress 4 :To see the status of datanode
		\t\tpress 5 :To see the report of the hadoop cluster	
		""")
		os.system("tput setaf 6")
		choice2=int(input("Enter your choice  : "))
		os.system("tput setaf 7")
		datanode_ip= input("Enter IP of Datanode at which you want to configure :")
		if choice2==1:
			
			os.system("scp datanode_hdfs_site.py root@{}:/root/".format(datanode_ip))
			os.system("ssh root@{} python3 datanode_hdfs_site.py".format(datanode_ip))
		elif choice2==2:
			
			os.system("scp datanode_core_site.py root@{}:/root/".format(datanode_ip))
			os.system("ssh root@{} python3 datanode_core_site.py".format(datanode_ip))
		elif choice2==3:
			
			os.system("ssh root@{} hadoop-daemon.sh start datanode".format(datanode_ip))
		elif choice2==4:
			
			os.system("ssh root@{} jps".format(datanode_ip))
		elif choice2==5:
			
			os.system("ssh root@{} hadoop dfsadmin -report".format(datanode_ip))
		else:
			print("please enter correct input")
	elif choice==3:
		os.system("tput setaf 1")
		os.system("figlet -c Client")
		os.system("tput setaf 2")
		print("""
		\n
		\t\tpress 1 :To configure the Hdfs-site file
		\t\tpress 2 :To configure the Core-site file
		""")
		os.system("tput setaf 4")
		choice3=int(input("Enter your choice  : "))
		os.system("tput setaf 5")
		if choice3==1:
			client_ip= input("Enter IP of Client  which you want to configure :")
			os.system("scp client_hdfs_site.py root@{}:/root/".format(client_ip))
			os.system("ssh root@{} python3 client_hdfs_site.py".format(client_ip))
		elif choice3==2:
			namenode_ip= input("Enter IP of client at which you want to configure :")
			os.system("scp client_core_site.py root@{}:/root/".format(client_ip))
			os.system("ssh root@{} python3 client_core_site.py".format(client_ip))
		else:
			print("please enter correct input")
	else:
		print("please enter correct input")
	print("""
	\n 
	\t\tpress 1 :To configure the Namenode
	\t\tpress 2 :To configure the Datanode
	\t\tpress 3 :To configure the Client
	\t\tpress 4 :To EXIT
	""")
	os.system("tput setaf 6")
	choice=int(input("Enter your choice  : "))
	os.system("tput setaf 7")
