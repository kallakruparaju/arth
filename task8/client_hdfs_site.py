import os
print("""
\n\t\tpress 1 :To configure both replica size and block size 
\t\tpress 2 :To configure only replica size
\t\tpress 3 :To configure only block size
\t\tpress 4 :To configure replica size and block size as default

""")
choice= int(input("\t\t\tEnter your choice:"))
if(choice==1):
	replica_size=int(input("Enter replica size:"))
	block_size=int(input("Enter block size in bytes:"))
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>

<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>\n'''.format(replica_size,block_size)
	file_hdfs.write(hdfs_data)

elif(choice==2):
	replica_size=int(input("Enter replica size:"))
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>
</configuration>\n'''.format(replica_size)
	file_hdfs.write(hdfs_data)
elif(choice==3):
	block_size=int(input("Enter block size in bytes:"))
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>\n'''.format(block_size)
	file_hdfs.write(hdfs_data)
elif(choice==4):
	file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
</configuration>\n'''
	file_hdfs.write(hdfs_data)
else:
	print("please enter correct input")

