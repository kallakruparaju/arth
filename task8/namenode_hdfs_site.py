import os
namenode_folder = input("\t\t\tFolder name for namenode:")
os.system("rm -rf {}".format(namenode_folder))
os.system("mkdir {}".format(namenode_folder))
file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(namenode_folder)
	
file_hdfs.write(hdfs_data)
	
