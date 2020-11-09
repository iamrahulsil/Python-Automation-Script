#THIS IS A DOCKER SCRIPT WRITTEN IN PYTHON BY YASH GUPTA
#ARTH GROUP NO: 4.9

#Importing python libraries
import os 
import subprocess
import getpass

#Main Function()
def docker_main():
	def docker():
	#Cleaning the terminal window
		os.system("clear")

		os.system("tput setaf 6")
		print("\t\t\tWELCOME TO DOCKER-CE CONTAINER ENGINE ")
		os.system("tput setaf 6")
		print("\t\t\t************************************* ")


		#Input:passwd
		passwd = getpass.getpass("Please enter your Password:- ")


		#Authorizing the User 
		if passwd != "docker":              
			 print("INVALID PASSWORD!!!")
			 exit()

			 
		os.system("clear")

		# Main Menu 	
		os.system("tput setaf 6")
		print("\t\t\tWELCOME TO DOCKER-CE CONTAINER ENGINE ")
		os.system("tput setaf 6")
		print("\t\t\t************************************* ")

		user_choice = int(input("Please enter your choice:-  "))
		os.system("tput setaf 6")
		print("""\t\t\t\ DOCKER-CE MAIN MENU
					\n
					[1]. View Docker-Info
					[2]. Install Docker-CE
					[3]. View Docker-CE Services
					[4]. Configure Docker-CE
					[5]. Docker-CE Images	
					[6]. Launch any env inside Docker-CE	
					[7]. Quit from Docker-Services
					[8]. Go to Main Menu
					""") 
		os.system("tput setaf 6")
		print("\t\t\t************************************* ")
			 
		#docker_info()
		def docker_info():
			os.system("clear")
			print("""
			>> Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages 				called containers.
			>> Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate 				with each other through well-defined channels.
			>> All containers are run by a single operating system kernel and therefore use fewer resources than virtual machines.The service 				has both free and premium tiers. The software that hosts the containers is called Docker Engine.
			>> Docker Inc. was founded by Solomon Hykes and Sebastien Pahl during the Y Combinator Summer 2010 startup incubator group and 				launched in 2011.
			>> Hykes started the Docker project in France as an internal project within dotCloud, a platform-as-a-service company.It was first 				started in 2013 and is developed by Docker, Inc. """)
			exit()

		
		#docker_install()
		def docker_install():
			os.system("clear")
			rc = subprocess.getstatusoutput("rpm -q docker-ce")[0]
			if ( rc == 1 ):
				os.system("mkdir /etc/yum.repos.d/docker.repo ") 
				docker_repo = open("/etc/yum.repos.d/docker.repo" , 'w')
				docker_repo.write(f''' 
				[docker]
				name=Docker-CE
				baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
				gpgcheck=0 
				''')
				docker_repo.close()		
				os.system("sudo yum install docker-ce --nobest -y")

			else:
				print("Docker-CE is Already installed in your system")


			
		#docker_services()	
		def docker_services():
			os.system("clear")
			while True:		
				os.system("wait(10)")
				os.system("clear")		
				print("""
					\n
					[0]. Status of Docker-CE
					[1]. Start Docker-CE
					[2]. Stop Docker-CE
					[3]. Enable Docker-CE
					[4]. Disable Docker-CE	
					[5]. Restart Docker-CE	
					[6]. Quit from Docker-Services
					[7]. Go to Main Menu
				""") 

				user_service_choice = input("What you want to do? ")	

				if int(user_service_choice) == 0:
					os.system("systemctl status docker.service")
				elif int(user_service_choice) == 1:	
					os.system("systemctl start docker.service")
				elif int(user_service_choice) == 2:
					os.system("systemctl stop docker.service")
				elif int(user_service_choice) == 3:
					os.system("systemctl enable docker.service")
				elif int(user_service_choice) == 4:
					os.system("systemctl disable docker.service")
				elif int(user_service_choice) == 5:
					os.system("systemctl restart docker.service")
				elif int(user_service_choice) == 6:
					return docker()
				elif int(user_service_choice == 7):
					return docker_main()
				else:
					print(" NOT SUPPORTED VALUE ") 
		#docker_configure()
		def docker_configure():	
				def docker_terminate():
					os.system("clear")
					while True:
						os.system("tput setaf 6")						
						print("""
						\n
						\t\t\t  CONTAINER TERMINATION MENU
						\t\t\t ****************************
						[0]. Particular Docker Container
						[1]. Back to Configure Menu
						""")
						
						container_delete = int(input("What you want to do?"))
						if int(container_delete == 0):
							container_name = input("Please enter your container name:-  ")
							os.system("sudo docker container rm {}".format(container_name))
						elif int(container_delete == 1):
							return docker_configure()
						else:
							print(" \t\t\t VALUE NOT SUPPORTED ")



				os.system("clear")
				while True:
					os.system("tput setaf 6")
					print("""\n
						\t\t\t    DOCKER-CE MAIN MENU
						\t\t\t*******************************				

								[0]. Download Docker-CE Image
								[1]. Launch Docker-CE Container
								[2]. Stop Docker-CE Container
								[3]. Terminate Docker-CE Container
								[4]. List Docker Containers
								[5]. Quit from Docker-Services
								[6]. Go to Main Menu
								""") 
					user_container_choice = int(input("\t\t What you want to do?  "))
					 			
					if int(user_container_choice == 0):
						image_name = str(input("Please provide image name:-  "))
						os.system("sudo docker pull {}".format(image_name))
					elif int(user_container_choice == 1):
						container_name = str(input("Enter Container name:- "))
						imge_name = str(input("Enter Image name:-  "))
						imge_version = input("Enter Image version:-  ")		
						os.system("sudo docker run -it --name {} {}:{}".format(container_name,imge_name,imge_version))
					elif int(user_container_choice == 2):
						container_name = str(input("Enter Container name:- "))
						os.system("sudo docker stop {}".format(container_name))
					elif int(user_container_choice == 3):	
						docker_terminate()
					elif int(user_container_choice == 4):
						os.system("sudo docker container ps -a")
					elif int(user_container_choice == 5):
						return docker()
					elif int(user_container_choice == 6):	
						return docker_main()
					else:
						print(" \t\t\t VALUE NOT SUPPORTED  ")	

	#docker_images()
	def docker_images():
		def docker_delete_images():
			os.system("clear")
			while True:
					os.system("tput setaf 6")						
					print("""
					\n
					\t\t\t    CONTAINER IMAGE DELETION
					\t\t\t ******************************
					[0]. Particular Docker Image
					[1]. Back to Image Menu
					""")
					
					image_delete = int(input("What you want to do?"))

					if int(image_delete == 0):
						image_name = str(input("Enter Image name:-  "))
						image_version = input("Enter Image version:-  ")
						os.system("sudo docker rmi {}:{}".format(image_name,image_version))
					elif int(image_delete == 1):
						return docker_images()
					else:
						print("\t\t\t VALUE NOT SUPPORTED  ")



			os.system("clear")
			while True:		
				os.system("wait(10)")
				os.system("clear")
				os.system("tput setaf 6")	
				print("""
				\n 
				\t\t\t  DOCKER IMAGE SUB-MENU
				\t\t\t ***********************
				[0]. List Container Images
				[1]. Delete Container Images
				[2]. Quit from Docker-CE
				[3]. Go to Main Menu
				""")

				user_image_choice = int(input("What you want to do?"))
				 			
				if int(user_image_choice == 0):
					os.system("sudo docker images -a")
				elif int(user_image_choice == 1):
					docker_delete_images()
				elif int(user_image_choice == 2):
					return docker()
				elif int(user_image_choice == 3):	
					return docker_main()
				else:
					print("\t\t\t VALUE NOT SUPPORTED  ")

		#docker_Launch_any_env()
		def docker_launch_any_env():
			os.system("clear")
			con_name = str(input("Enter Container name:- "))
			img_name = str(input("Enter Image name:-  "))
			img_version = input("Enter Image version:-  ")
			what_to_install = input("What you want to install?  ")
			what_to_execute = input("What you want to execute?  ")	
			os.system("sudo docker run -dit --network host --name {} {}:{}".format(con_name,img_name,img_version))
			os.system("sudo docker exec -it {} yum install {} -y".format(con_name,what_to_install))
			os.system("sudo docker exec -it {} {}".format(con_name,what_to_execute))
		
		#docker_quit()
		def docker_quit():
			return docker()
		
		#docker_main_menu_quit()
		def docker_main_menu_quit():
			return docker_main()

		#Docker-CE Sub-Menu functions
			if int(user_choice) == 1:
				docker_info()
			
			if int(user_choice) == 2:
				docker_install()	

			if int(user_choice) == 3:
				docker_services()

			if int(user_choice) == 4:
				docker_configure()

			if int(user_choice) == 5:
				docker_images()

			if int(user_choice) == 6:
				docker_launch_any_env()
			
			if int(user_choice) == 7:
				docker_quit()
			
			if int(user_choice) == 8:
				docker_main_menu_quit()

