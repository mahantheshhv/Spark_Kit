# How to install python modules on cluster

we should have pip so we should install pip first
	
	wget https://bootstrap.pypa.io/get-pip.py
	
	python27 get-pip.py 

we should install python development tools
	
	yum install python27-devel 

now to install any python package use pip

	pip2.7 install numpy 

as the module is now installed on driver/master this package has to be pushed across the cluster ,to copy the files across the cluster(script is already available on the driver )

	~/spark-ec2/copy-dir /usr/local/lib/python2.7/site-packages/numpy


