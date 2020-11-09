import os
import aws

print("\n")

def mainaws():
	
	os.system("tput setaf 10")
	print("\t\t\t Welcome to our Menu App")

	os.system("tput setaf 7")
	print("\t\t\t ----------------------\n")

	os.system("tput setaf 3")
	print("Press 2: for AWS")
	os.system("tput setaf 13")
	print("Press 5: for exit")

	os.system("tput setaf 7")

	print("\n")
	ach = input("Enter your choice: ")
	if(int(ach) == 2):	
		aws()
	elif(int(ach) == 5):
		os.system("tput setaf 10")
		print("\n\t\t\t Thank You for Visiting !!!")		
		os.system("tput setaf 7")
		print("\t\t\t ----------------------\n")		
		exit()
	else:
		print("Invalid Input...")

def awsec2():

	while(True):
		ach3 = input("Enter your choice: ")
		print("\n")
		os.system("tput setaf 7")
	
		if(int(ach3) == 1):
			os.system("tput setaf 3")
			print("""Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment. """)
			print("\n")
		os.system("tput setaf 7")
				
		if(int(ach3) == 2):
			aimgid = input("Enter your AMI Id: ")
			ainstancetype = input("Enter your Instance type (e.g. t2.micro): ")
			acount = input("Enter no. of instances you want to launch: ")
			asubnet = input("Enter your region subnet: ")
			asecurity = input("Enter the security group ID: ")
			akey = input("Enter your AWS key: ")
			#	os.system(""" aws ec2 run-instances --image-id  {aimgid} --instance-type {ainstancetype} --count {acount} --subnet-id {asubnet} --security-group-ids {asecurity} --key-name {akey} """)
			os.system("tput setaf 3")
			os.system(" aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {} ".format(aimgid, ainstancetype, acount, asubnet, asecurity, akey))
			print("\n")
		os.system("tput setaf 7")
				
		if(int(ach3) == 3):
			os.system(" aws ec2 describe-instances ")
			print("\n")
		os.system("tput setaf 7")
					
		if(int(ach3) == 4):
			ainstidstart = input("Enter your Instance ID: ")
			os.system(" aws ec2 start-instances --instance-ids {} ".format(ainstidstart))
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach3) == 5):
			ainstidstop = input("Enter your Instance ID: ")
			os.system(" aws ec2 stop-instances --instance-ids {} ".format(ainstidstop))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach3) == 6):
			ainstidterm = input("Enter your Instance ID: ")
			os.system(" aws ec2 terminate-instances --instance-ids {} ".format(ainstidterm))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach3) == 7):
			return aws()	

def awsebs():
	while(True):
		ach4 = input("Enter your choice: ")
		print("\n")
		os.system("tput setaf 7")
		if(int(ach4) == 1):
			os.system("tput setaf 3")
			print("""Amazon Elastic Block Store (EBS) is an easy to use, high performance block storage service designed for use with Amazon Elastic Compute Cloud (EC2) for both throughput and transaction intensive workloads at any scale. A broad range of workloads, such as relational and non-relational databases, enterprise applications, containerized applications, big data analytics engines, file systems, and media workflows are widely deployed on Amazon EBS.""")
			print("\n")
		os.system("tput setaf 7")
		
		if(int(ach4) == 2):
			azone = input("Enter your availability zone: ")
			asize = input("Enter the size of your EBS in GiB: ")
			avolume = input("Enter your EBS volume type: ")
			os.system("tput setaf 3")
			os.system(" aws ec2 create-volume --availability-zone {} --size {} --volume-type  {}".format(azone, asize, avolume))
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach4) == 3):
			adevice = input("Enter your device(e.g. sdb): ")
			ainstanceid = input("Enter your Instance ID: ")
			avolumeid = input("Enter your EBS volume ID: ")
			os.system("tput setaf 3")
			os.system("  aws ec2 attach-volume --device {} --instance-id {} --volume-id {} ".format(adevice, ainstanceid, avolumeid))
			print("\n")
		os.system("tput setaf 7")
		
		if(int(ach4) == 4):
			return aws()

def awss3():
	while(True):
		ach5 = input("Enter your choice: ")
		print("\n")
		os.system("tput setaf 7")
		if(int(ach5) == 1):
			os.system("tput setaf 3")
			print("""S3 bucket is one of the many services provided by AWS. It is nothing but public cloud storage where you can store your files, kind of a folder in your pc but unlike pc, you can access it anywhere you want. S3 is an abbreviation of Simple Storage Service. AWS provides many ways to upload a file on the s3 bucket, which are given below:
1. Upload file using Drag and Drop
2. Upload file using click
3. Upload file using aws CLI in the terminal.""")
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach5) == 2):
			abname = input("Enter your bucket name: ")
			aregion = input("Enter region where you want S3 bucket: ")
			os.system("tput setaf 3")
			os.system(" aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(abname, aregion, aregion))
			os.system("tput setaf 3")
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach5) == 3):
			apath = input("Enter path of your file located in your local device: ")
			abucketname = input("Enter your S3 bucket name: ")
			abucketfolder = input("Enter your S3 bucket folder name: ")
			os.system(" aws s3 cp {} s3://{}/{} --acl public-read ".format(apath, abucketname, abucketfolder))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach5) == 4):
			return aws()	
	

def aws():

	#if(int(ach) == 2):
	os.system("tput setaf 3")
	print("""
Press 1: to know about AWS
Press 2: to install AWS CLI
Press 3: to configure AWS
Press 4: to create a key pair
Press 5: for EC2 instance
Press 6: for EBS volume
Press 7: to create IAM user
Press 8: for S3 storage
Press 9: to create Cloudfront distribution
Press 10: to go back to main menu""")
	os.system("tput setaf 7")
	print("\n")
	while(True):
		ach2 = input("Enter your choice: ")
		print("\n")

		if(int(ach2) == 1):
			os.system("tput setaf 3")
			print("""Amazon Web Services (AWS) is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis. As of 2020, AWS comprises more than 175 products and services including computing, storage, networking, database, analytics, application services, deployment, management, mobile, developer tools, and tools for the Internet of Things. The AWS Command Line Interface is a unified tool to manage your AWS services.""")	
			print("\n")
		os.system("tput setaf 7")
			
		if(int(ach2) == 2):
			#os.system("tput setaf 3")
			# os.system("pip3 install --upgrade --user awscli")
			os.system(""" curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" """)
			os.system("""unzip awscliv2.zip""")
			os.system("""sudo ./aws/install""")
			os.system("tput setaf 3")			
			print("\nAWS successfully installed\n\nAWS Version: ")	
			os.system("aws --version")
			print("\n")	
		os.system("tput setaf 7")
		
		if(int(ach2) == 3):
			os.system(" aws configure ")
			print("\n")				
		os.system("tput setaf 7")
	
		if(int(ach2) == 4):
			akey = input("Enter key name: ")
			os.system(" aws ec2 create-key-pair --key-name {} ".format(akey))
			print("\n")
		os.system("tput setaf 7")
	
		if(int(ach2) == 5):
			os.system("tput setaf 3")
			print("""Press 1: to know about EC2 instances
Press 2: to launch an EC2 instance
Press 3: to describe EC2 instances
Press 4: to start an EC2 instance
Press 5: to stop an EC2 instance
Press 6: to terminate an EC2 instance
Press 7: to go back to main menu""")
			os.system("tput setaf 7")
			print("\n")
			awsec2()

		if(int(ach2) == 6):
			os.system("tput setaf 3")
			print("""Press 1: to know about EBS 
Press 2: to create EBS volume
Press 3; to attach EBS to EC2 instance
Press 4: to go back to main menu""")
			os.system("tput setaf 7")
			print("\n")
			awsebs()
				
		if(int(ach2) == 7):
			auser = input("Enter your user name: ")
			os.system("tput setaf 3")
			os.system(" aws iam create-user --user-name {} ".format(auser))
			print("\n")
		os.system("tput setaf 7")

		if(int(ach2) == 8):
			os.system("tput setaf 3")
			print("""Press 1: to know about S3 storage
Press 2: to configure S3
Press 3: to upload a file from your local computer to S3 storage
Press 4: to go back to main menu""")
			os.system("tput setaf 7")
			print("\n")
			awss3()

		if(int(ach2) == 9):
			adomain = input("Enter your domain url: ")
			aobject = input("Enter name of your object: ")
			os.system("tput setaf 3")
			os.system(" aws cloudfront create-distribution  --origin-domain-name  {} --default-root-object {} ".format(adomain, aobject))
			print("\n")
		os.system("tput setaf 7")
			
		if(int(ach2) == 10):
			return mainaws()
											

mainaws()
