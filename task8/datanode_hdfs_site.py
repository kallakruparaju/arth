import os
datanode_folder = input("\t\t\tFolder name for datanode:")
os.system("rm -rf {}".format(datanode_folder))
os.system("mkdir {}".format(datanode_folder))
file_hdfs = open("/etc/hadoop/hdfs-site.xml","w")
hdfs_data =  '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
 
<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>{}</value>
</property>
</configuration>\n'''.format(datanode_folder)
file_hdfs.write(hdfs_data)
