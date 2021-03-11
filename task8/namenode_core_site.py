namenode_ip = input("\t\t\tEnter the IP of the namenode:")
namenode_port = input("\t\t\tEnter Port Number at which you want to run namenode service:")
file_core = open("/etc/hadoop/core-site.xml", "w")
core_data = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_ip,namenode_port)
file_core.write(core_data)   
