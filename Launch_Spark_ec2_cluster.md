# Launching Spark 1.4 on EC2

To make the job of installing and managing the spark cluster Spark 1.4 comes with a extended provision of setting up Spark on Amazon EC2.

# Requirements

1) AWS account 

2) Linux machine

3) Spark 1.4 (can be downloaded from here http://spark.apache.org/downloads.html)

# Before starting

1)Download and extract spark 1.4.1 from ( http://spark.apache.org/downloads.html) into your linux machine

2)Create an AWS account and login (https://aws.amazon.com/)

3)Create a key pair (for authentication to aws ) and get Access Key Id and Secret Access Key by clicking Account > Security Credentials > Access Credentials and download the credentials  (Keep these credentials safely)

4)Now open terminal on your local access machine and add follwing lines to .bashrc(set the environment variables)
       4.1)open .bashrc (using vi or nano or other editor)
       4.2)add the following lines to your .bashrc file
       		export AWS_SECRET_ACCESS_KEY=xxxxxxx 
       		export AWS_ACCESS_KEY_ID=xxxxxxxxxxx
       		NOTE:add the original id and key you got it from aws   


# Launching a cluster