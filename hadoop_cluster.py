#HADOOP CLUSTER Script written by RAHUL SIL.

import os
import time
import subprocess
import webbrowser

os.system("clear")


def remote():
	os.system("clear")
	print("\n\n")
	os.system("tput setaf 2")
	print("\t\t\t\t\tWELCOME TO HADOOP CLUSTER SETUP ")
	print("\t\t\t\t--------------------------------------------")
	print("""
		- Press 1 for HADOOP SERVICES.
		- Press 2 to quit  """)

	os.system("tput setaf 9")

	choice = int(input("\nENTER YOUR CHOICE : "))

	if choice == 1:
		def hadoop():
			os.system("tput setaf 3")
			print("\t\t\t\tWELCOME TO HADOOP WORLD")
			print("\t\t\t\t---------------------------------------")
			print("""
				- Press 1 to know about Hadoop.
				- Press 2 to configure Hadoop Cluster.
				- Press 3 to start services of Hadoop Cluster.
				- Press 4 to stop the services of Hadoop Cluster.
				- Press 5 to configure and launch Client.
				- Press 6 to see the HADOOP CLUSTER REPORT.
				- Press 7 to upload a file to cluster.
				- Press 8 to open webUI of Hadoop in your browser.
				- Press 9 for Hadoop Elasticity with LVM.
				- Press 10 To quit the menu """)

			ch = int(input("\nENTER YOUR CHOICE : "))

			if ch == 1:
				print("Will be available soon")

			elif ch == 2:
				print("""
					- Press 1 to configure NameNode.
					- Press 2 to configure DataNode. """)

				config_choice = int(input("\n ENTER YOUR CHOICE : "))

				if config_choice == 1:
					print("\n\t\t\t---------- CONFIGURATION OF NAMENODE WILL HAPPEN NOW --------------")

					os.system("yum install wget -y")
					rc = subprocess.getstatusoutput("rpm -q hadoop")[0]

					if rc == 1:
						print("\n\n\t\t\t--------- Hadoop software is installing --------- ")
						os.system(
							"wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
						os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
						print("\n\n\t\t\t--------- HADOOP SUCCESSFULLY INSTALLED !! -----------")
						time.sleep(2)

						print("\n\n\t\t\t--------- JDK software is installing --------- ")
						os.system(
							"wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm")
						os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
						print("\n\n\t\t\t--------- JDK SUCCESSFULLY INSTALLED !! -----------")
						print("\n\n")

					os.system("hadoop version")

					print("\n\n-------- CONFIGURING NAMENODE ---------")
					time.sleep(1)
					os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")

					print("\nIf you are configuring the NAMENODE in AWS, enter name_ip as 0.0.0.0")
					name_ip = input("\nENTER THE IP ADDRESS OF NAMENODE : ")
					port_number = int(input("\nENTER THE PORT NUMBER :"))
					datadir = input("\nENTER THE DIRECTORY NAME YOU WANT : ")
					os.system(
						f"rm -rf /{datadir};mkdir /{datadir};echo 3 >/proc/sys/vm/drop_caches")

					datafile = open("/etc/hadoop/hdfs-site.xml", 'w')
					datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name>
<value>/{datadir}</value>
</property>

</configuration>''')
					datafile.close()
					datafile1 = open("/etc/hadoop/core-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://{name_ip}:{port_number}</value>
</property>

</configuration>''')
					datafile1.close()
					os.system("tput setaf 2")
					print("\n WHEN PROMPTED TO ENTER YES OR NO , PRESS 'Y' IN CAPITALS' ")
					os.system("hadoop namenode -format")
					os.system("tput setaf 3")

				elif config_choice == 2:
					print("\n\t\t\t---------- CONFIGURATION OF DATANODE WILL HAPPEN NOW --------------")

					os.system("yum install wget -y")
					rc = subprocess.getstatusoutput("rpm -q hadoop")[0]

					if rc == 1:
						print("\n\n\t\t\t--------- Hadoop software is installing --------- ")
						os.system(
							"wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
						os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
						print("\n\n\t\t\t--------- HADOOP SUCCESSFULLY INSTALLED !! -----------")
						time.sleep(2)

						print("\n\n\t\t\t--------- JDK software is installing --------- ")
						os.system(
							"wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm")
						os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
						print("\n\n\t\t\t--------- JDK SUCCESSFULLY INSTALLED !! -----------")
						print("\n\n")

					os.system("hadoop version")

					print("\n\n-------- CONFIGURING DATANODE ---------")
					time.sleep(1)
					os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")

					name_ip = input("\nENTER THE IP ADDRESS OF NAMENODE : ")
					port_number = int(input("\nENTER THE PORT NUMBER :"))
					datadir = input("\nENTER THE DIRECTORY NAME YOU WANT : ")
					os.system(
						f"rm -rf /{datadir};mkdir /{datadir};echo 3 >/proc/sys/vm/drop_caches")
					datafile = open("/etc/hadoop/hdfs-site.xml", 'w')
					datafile.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name.dir</name>
<value>/{datadir}</value>
</property>

</configuration>''')
					datafile.close()
					datafile1 = open("/etc/hadoop/core-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://{name_ip}:{port_number}</value>
</property>

</configuration>''')
					datafile1.close()
			elif ch == 3:
				node = input(
					"\n\t\t YOU CONFFIGURED THIS SYSTEM AS [NAMENODE] OR [DATANODE] ? ").upper()
				if node == "NAMENODE":
					print("\n\t\t\t--------- NAMENODE SERVICES ARE STARTING !! ---------- ")
					os.system("hadoop-daemon.sh start namenode;jps")

				elif node == "DATANODE":
					print("\n\t\t\t--------- DATANODE SERVICES ARE STARTING !! ---------- ")
					os.system("hadoop-daemon.sh start datanode;jps")

				output = input(
					"\n\t\t DO YOU WANT TO MAKE THE SERVICES OF HADOOP PERMANENT ? [Y/N] ").upper()
				if output == "Y":
					file1 = open("/etc/rc.d/rc.local", "a")
					file1.write("\n hadoop-daemon.sh start namenode")
					file1.close()

			elif ch == 4:
				node = input(
					"\n\t\t YOU CONFFIGURED THIS SYSTEM AS [NAMENODE] OR [DATANODE] ? ").upper()
				if node == "NAMENODE":
					print("\n\t\t\t--------- NAMENODE SERVICES ARE STOPPING !! ---------- ")
					os.system("hadoop-daemon.sh stop namenode;jps")

				elif node == "DATANODE":
					print("\n\t\t\t--------- DATANODE SERVICES ARE STOPPING !! ---------- ")
					os.system("hadoop-daemon.sh stop datanode;jps")

			elif ch == 5:
				print("\n\n--------------CONFIGURING CLIENT-----------")
				os.system("yum install wget -y")
				rc = subprocess.getstatusoutput("rpm -q hadoop")[0]

				if rc == 1:
					print("\n\n\t\t\t--------- Hadoop software is installing --------- ")
					os.system(
						"wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/hadoop-1.2.1-1.x86_64.rpm")
					os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
					print("\n\n\t\t\t--------- HADOOP SUCCESSFULLY INSTALLED !! -----------")
					time.sleep(2)

					print("\n\n\t\t\t--------- JDK software is installing --------- ")
					os.system(
						"wget https://hadoop-arth.s3.ap-south-1.amazonaws.com/jdk-8u171-linux-x64.rpm")
					os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm")
					print("\n\n\t\t\t--------- JDK SUCCESSFULLY INSTALLED !! -----------")
					print("\n\n")

				os.system("hadoop version")

				t.sleep(1)
				os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
				name_ip = input("\nENTER THE IP ADDRESS OF NAMENODE : ")
				port_number = int(input("\nENTER THE PORT NO :"))
				datafile1 = open("/etc/hadoop/core-site.xml", 'w')
				datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{name_ip}:{port_number}</value>
</property>
</configuration>''')
				datafile1.close()
				os.system("systemctl stop firewalld;setenforce 0")
				print("\n\n\t\t-------------- CLIENT SERVICE STARTED ----------")

				client_choice = input(
					"\n\n\t\t DO YOU WANT TO CHANGE THE BLOCK SIZE [Y/N] : ").upper()
				if client_choice == "Y":
					block_size = input("\n\n\t\t ENTER THE BLOCK SIZE (in MB ) : ")
					block_size = block_size * 1024 * 1024

					datafile1 = open("/etc/hadoop/hdfs-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.block.size</name>
<value>{block_size}</value>
</property>
</configuration>''')
					datafile1.close()

				client_choice = input(
					"\n\n\t\t DO YOU WANT TO CHANGE THE REPLICATION FACTOR [Y/N] : ").upper()
				if client_choice == "Y":
					replication_factor = input("\n\n\t\t ENTER THE REPLICATION FACTOR : ")

					datafile1 = open("/etc/hadoop/hdfs-site.xml", 'w')
					datafile1.write(f'''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.replication</name>
<value>{replication_factor}</value>
</property>
</configuration>''')
					datafile1.close()

			elif ch == 6:
				os.system("hadoop dfsadmin -report")

			elif ch == 7:
				filepath = input("\n\n\t\t ENTER THE FILEPATH : ")
				os.system(f"hadoop fs -put /{filepath}  /")

			elif ch == 8:
				name_ip = input("\n\n\t\t ENTER THE NAMENODE IP : ")
				webbrowser.open(f"http://{name_ip}:50070")

			elif ch == 9:
				while True:
				    print("""
    					\n
    					- Press 1 : To check how many storage is attached to the OS
    					- Press 2 : To create Physical Volume
    					- Press 3 : To display Physical Volume
    					- Press 4 : To create Volume Group
    					- Press 5 : To display Volume Group
    					- Press 6 : To create Logical Volume
    					- Press 7 : To display Logical Volume
    					- Press 8 : To format the LV
					    - Press 9 : To mount the LV
    					- Press 10 : To exit """)

				    ch = int(input("Enter your Choice : "))

				    if ch == 1:
					    os.system("fdisk -l")
                    elif ch == 2:
                        pv1 = input("Enter the name of storage 1 : ")
						pv2 = input("Enter the name of storage 2 : ")
						os.system("pvcreate {}".format(pv1))
						os.system("pvcreate {}".format(pv2))
                    elif ch == 3:
						pv = input("Enter the name of storage : ")
						os.system("pvdisplay {}".format(pv))

					elif ch == 4:
						vgn = input("Give name to the VOLUME GROUP : ")
						pvn1 = input("Enter the name of storage 1 : ")
						pvn2 = input("Enter the name of Storage 2 : ")
						os.system("vgcreate {} {} {}".format(vgn, pvn1, pvn2))

					elif ch == 5:
						vgn1 = input("Enter the name of VOLUME GROUP : ")
						os.sytem("vgdisplay {}".format(vgn1))

					elif ch == 6:
						size = input("Enter size for your LOGICAL VOLUME : ")
						lvn = input("Give name to your LOGICAL VOLUME : ")
						vgn2 = input("Enter name of the VOLUME GROUP : ")
						os.system("lvcreate --size {}G --name {} {}".format(size, lvn, vgn2))

					elif ch == 7:
						os.system("lvdisplay")

					elif ch == 8:
						vgn = input("Enter the name of VOLUME GROUP : ")
						lvn = input("Enter the name of LOGICAL VOLUME : ")
						os.system("mkfs.ext4  /dev/{}/{}".format(vgn, lvn))

					elif ch == 9:
						user_dir = input(
							"\n\n\t\t ENTER THE DIRECTORY USED IN HADOOP CLUSTER : ")
						vgn = input("Enter the name of VOLUME GROUP : ")
						lvn = input("Enter the name of LOGICAL VOLUME : ")
						os.system(f"mount /dev/{vgn4}/{lvn2}  /{user_dir} ")

					elif ch == 10:
						break

					input("\t PRESS ENTER TO CONTINUE -------- ")

			elif ch == 10:
				remote()
		hadoop()

	elif choice == 2:
		return
	print("\n")
	ext = input("WANT TO RUN AGAIN THE HADOOP MENU[Y/N] : ").upper()
	if ext == "Y":
		remote()
	elif ext == "N":
		return


inp = input("\n\n\t\t FOR RUNNING THE HADOOP CLUSTER PRESS Y : ").upper()
if inp == "Y":
	remote()
