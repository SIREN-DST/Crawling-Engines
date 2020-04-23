# ElasticSearch Logstash Kibana FileBeat UserManual

##  Prerequisite

 - Some or good grip on the Linux administration commands.

 - Should have idea about installation of Operating Systems

 - Should have good idea about the VMware players (if installation is to be done on VM).

 #

 #### Basic Installation Steps: Installation of Operating System/Virtual Machine:
 
 - The above products of Apache would run good on Ubuntu 16.04 LTS and Ubuntu 18.04 LTS version of the operating systems including 2 cpu processes, 4GB RAM and open ports 9200,5601,5044

 - You can get the image files of the OS by clicking on the link:

	 - https://ubuntu.com/download/desktop (Ubuntu 18.04.3 LTS / Ubuntu 16.04.3 LTS)

 - If the system is running on Windows Operating System, then it would be better to make a dual-boot for the other operating system to be installed or we can use the VMware Workstation Player 15.xx version for the installation of the Ubuntu OS. 

	- Link for VMware: https://www.vmware.com/in/products/workstation-player/workstation-player-evaluation.html

 - Please install the VMWare Workstation Player.

 - After installation and running VMWare Workstation Player, you would get the window where there is a tab called Create a New Virtual Machine

 - After the click, please ensure the details are filled and the path to the installation of image file of the Linux is to be provided.

 -  Then we could customize the processor speed, RAM, others as per the system requirements.

 - After clicking finish, the virtual machine would start up and the installation of OS would be in process.

**Installation of Java Version:**

 - After the running of Linux OS, use the key Ctrl+Alt+T (To Open Terminal).

 - After the opening of the terminal, please follow the below steps:
 - Installation of Java with related commands:

		 - sudo su (Run the programs in administrator mode)

		 - sudo apt-get update (To check for the updates of OS)


		 - sudo apt-get install openjdk-8-jdk

		 - java -version

		 - export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

		 - export PATH=$PATH:$JAVA_HOME/bin


**Expected Output**


![Java Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/1.JPG)

#

**Installation of ElasticSearch Logstash Kibana Filebeat Services on Ubuntu 18.04:**
#

ELK is the combination of three open source projects: Elasticsearch, Logstash, Kibana and Filebeat. Elasticsearch is a search and analytics engine. Logstash is a server-side logs processing pipeline that transport logs from multiple sources simultaneously, transforms it, and then sends it to a “stash” like Elasticsearch. Kibana is to visualize logs with charts and graphs from Elasticsearch. You can visit the link https://www.fosstechnix.com/install-elk-stack-on-ubuntu/ for any queries or other information required.

WorkFlow = ElasticSearch —> Kibana —> Logstash —> Filebeat


**Installation and Configuration of ElasticSearch**

Here, We are adding ElasticSearch official apt package and this is signed with GPG keys

	$ sudo apt-get install vim 
	
	$ sudo wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add –

Next add the repository in /etc/apt/sources.list.d/elastic-6.x.list using below command.

	$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

To install elasticsearch enter below command

	$ sudo apt-get update 
	$ sudo apt-get install elasticsearch

**Expected Output**

![ElasticSearch Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/2.JPG)

Let’s make changes in below configuration file

	$ sudo vi /etc/elasticsearch/elasticsearch.yml 
	
uncomment network.host

	network.host: 0.0.0.0
	http.port : 9200 or 9300 (Your choice)
	
To start elasticsearch services

	$ sudo systemctl start elasticsearch
	
To enable elasticsearch at system startup

	$ sudo systemctl enable elasticsearch
	
To stop elasticsearch (Not recommended at the time of installation)

	$ sudo systemctl stop elasticsearch

**Expected Output**

![ElasticSearch Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/3.JPG)

 Enter below command to check elasticsearch is running or not
 
	 $ sudo apt-get install curl -y 
	 
	 $ curl -X GET "localhost:9200"

**Expected Output**

![ElasticSearch Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/4.JPG)
 
 #
 #### Installation and Configuration Kibana
 #
To install Kibana

	$ sudo apt-get install kibana

**Expected Output** 

![Kibana Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/5.JPG)

Now let’s make changes in below configuration file for to access kibana

	$ sudo vi /etc/kibana/kibana.yml
	
uncomment server.host at line 7 and make changes as mentioned below

	server.host: "0.0.0.0"
	
To start kibana service

	$ sudo systemctl start kibana
	
To enable kibana at system startup

	$ sudo systemctl enable kibana

**Expected Output**

![Kibana Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/6.JPG)

To check the status of kibana service

	$ sudo systemctl status kibana
	
To stop kibana service (Not recommended)

	$ sudo systemctl stop kibana

**Expected Output**

![Kibana Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/7.JPG)

#

**Installation and Configuration of Logstash**
#

To install logstash

	$ sudo apt-get install logstash -y

**Expected Output**

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/8.JPG)

To load logstash beat create the below config file and insert below lines.

	$ sudo vim /etc/logstash/conf.d/02-beats-input.conf input { beats { port => 5044 } }
	
save and close the file

Create the configuration file and insert below lines

	$ sudo nano /etc/logstash/conf.d/30-elasticsearch-output.conf

**Expected Output**

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/9.JPG)

To start Logstash Services

	$ sudo systemctl start logstash

To enable logstash at system startup

	$ sudo systemctl enable logstash

To stop logstash services (Not recommended)

	$ sudo systemctl stop logstash

To check status of logstash

	$ sudo systemctl status logstash

**Expected Output**

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/10.JPG)

#
## Installation and Configuration of Filebeat

	$ sudo apt-get install filebeat
	
Now let’s make changes in below configuration file

	$ sudo vi /etc/filebeat/filebeat.yml

In the configuration file go to Filebeat Section change false to true as shown below:

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/11.JPG)

In the configuration file go to Kibana Section as shown below:


![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/12.JPG)

In the configuration file got ElasticSearch Section as shown below:

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/13.JPG)

To start filebeat services:

	$ sudo systemctl start filebeat
	
To enable filebeat at system startup

	$ sudo systemctl enable filebeat

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/14.JPG)

To check status of filebeat services

	$ sudo systemctl status filebeat

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/15.JPG)

Now lets check that ElasticSearch is receiving datalog from filebeat using below command

	$ sudo curl -XGET 'http://localhost:9200/filebeat-*/_search?pretty'

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/16.JPG)

Finally lets login into kibana portal using http:/<ip of the server>:5601 (Ex: http://localhost:5601)

Create index pattern by using Discover → Create Index Pattern → filebeat-* → Index pattern → @timestamp

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/17.JPG)

**Expected Output**

![Logstash Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELKF/18.JPG)

**That’s all folks !!! Happy Visualization of ELK features running on your local machine.**


