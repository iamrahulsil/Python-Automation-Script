import os
os.system("tput setaf 1")
print("\t\t\t WEBSERVER")
os.system("tput setaf 7")
print("\t\t\t----------------")
print("""Configure Web Server and Install
	Press 0: installation"
	Press 1:	status of webserver")
	press 2: launch Webserver""")

print("Enter Your Choice")
ch=input()

if int(ch)  == 0:
	os.system("rpm -q httpd")
elif int(ch) == 1:
	os.system("systemctl status httpd")
elif int(ch) == 2:
	print("""Press 1: launch Webserver locally
	Press 2: launch Webserver remotely
	Press 3: launch Webserver on docker
	Press 4: launch Webserver on AWS""")
	ch=input("Enter Your Choice")
	x = "$PWD"
	if int(ch)  == 1:
		os.system("systemctl start httpd")
		os.system("systemctl status")
	elif int(ch) == 2:
		print("Enter Host IP, username and password")
		ip = input("IP :")
		userName = input("user :")
		#passwd = input("passwd :")
		os.system("ssh {0}@{1} systemctl start httpd".format(userName,ip))
	elif int(ch) == 3:
		os.system("docker pull httpd")
		os.system("docker run -dit --name my-apache-app -p 8080:80 -v {}:/usr/local/apache2/htdocs/ httpd".format(x))
	elif int(ch) = 4:
		
