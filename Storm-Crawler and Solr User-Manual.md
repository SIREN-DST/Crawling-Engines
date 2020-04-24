
# Crawling-Engines
### Storm-Crawler and Apache Solr User Manual 
##
**Prerequisite**

 - Some or good grip on the Linux administration commands.
 
 - Should have an idea about installation of Operating Systems.
 
 - Should have good idea about the VMware players(if installation is to be done on VM).
 
##
**Basic Installation Steps**

**Installation of Operating System/Virtual Machine:**

 - The above products of Apache would run good on Ubuntu 16.04 LTS and Ubuntu 18.04 LTS version of the operating systems including 3-4 CPU's cores, minimum of 8GB RAM, and disk space of 100GB or above.
 
 - You can get the image files of the OS by clicking on the link: [Ubuntu OS ](https://ubuntu.com/download/desktop) (Ubuntu 18.04.3 LTS/Ubuntu 16.04.3 LTS).
 
 - If the system is running on Windows Operating System, then it would be better to make a dual-boot for other operating system to be installed or we can use the VMware Player or Workstation 15.xx version for the installation of the Ubuntu OS.
 
	 - Link for VMware: [VMware Download Link](https://www.vmware.com/in/products/workstation-player/workstation-player-evaluation.html)
	 
 - Please install the VMWare Workstation Player.
 
 - After the installation and running VMWare Workstation Player, you could get a window where there is a tab called Create a New Virtual Machine.
 
 - After the click, please ensure the details are filled and the path to the installation of image file of the Linux OS is to be provided.
 
 - Then we could customize the processor cores, RAM, others as per the system requirements.
 
 - After clicking finish, the virtual machine would start up and the installation of OS would be in process.
 
##

**Installation of Java Version**
 - After the running of Linux OS, use the key Ctrl+Alt+T (To open Terminal).
 
 - After the opening of the Terminal, please follow the below steps:
 
	- Installation of Java with related commands:
	
		- sudo su (Run the programs in administrator mode)
		
		- sudo apt-get update (To check for the updates of OS).
	
		- sudo apt-get install openjdk-8-jdk
		
		- java -version
		
		- export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

		- export PATH=$ PATH: $ JAVA_HOME/bin (No spaces between the symbol and word).
		
**Expected Output**

![Java Version Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/1.png)
##

**Installating Requirements**

Before getting to the StormCrawler itself lets get into the basics of StormCrawler and the required dependencies that StormCrawler works based on these.

 - We need the Zookeeper 3.4.14 and Storm 1.2.2 source files (Very specific to the versions).
 
 - All the installation steps that are going to be used would work on Ubuntu 16.04.3 LTS and Ubuntu 18.04.3 LTS

 - Make sure all the dependencies and tools are up to date.

##

**What is StormCrawler?**

StormCrawler is an open source SDK for building distributed web crawlers based on Apache Storm. The project is under Apache license v2 and consists of a collection of reusable resources and components, written mostly in Java.

 - The aim of StormCrawler is to help build web crawlers that are:
	 - Scalable, resilient, low latency, easy to extend and polite yet efficient.
	 
##

**Installation and Configuration of Apache Solr:**

 - To start with we download the required Solr Version 8.2.0 from its official site or mirrors. Or by simply using the following commands to download Apache Solr 8.2.0.
 
 - Ensure that all the procedures are to be used in the super user mode (Administrative Mode).

	- $ sudo su 

	-  cd /opt 

	- wget https://archive.apache.org/dist/lucene/solr/8.2.0/solr-8.2.0.tgz

 - Next, we extract Apache Solr Service installer shell script from the downloaded Apache Solr archive file and run the installer using the following commands:

	 - tar xzf solr-8.2.0.tgz solr-8.2.0/bin/install_solr_service.sh --strip-components=2

	 - ./install_solr_service.sh solr-8.2.0.tgz

	 - sudo service solr start 

	 
**Output**

![Solr Running Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/1.PNG)
##

**Installation and Configuration of Zookeeper:**

To install ZooKeeper framework on our machine, visit the following link and download ZooKeeper. In this project we are using ZooKeeper 3.4.14 (ZooKeeper-3.4.14.tar.gz). Link : http://zookeeper.apache.org/releases.html

	Extract the tar file using the following commands:
	

 - $ cd /opt 

 -  sudo su 

 - wget http://mirror.23media.de/apache/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz 

 -  tar -zxf zookeeper-3.4.14.tar.gz # cd zookeeper-3.4.14
 
 -  mkdir data

Open configuration file named conf/zoo.cfg using the command nano/vim 
-> vi conf/zoo.cfg and setting all the following paramaters as starting point.


 - Note: VIM is not a package inbuilt, we need to install the tool to use it.

 - cd /opt 

 -  sudo apt-get install vim 

 - nano conf/zoo.cfg or vim conf/zoo.cfg

Inside the zoo.cfg file please mention the below:
	tickTime=2000 
	dataDir=/opt/zookeeper-3.4.14/data 
	clientPort=2181 
	initLimit=5 
	syncLimit=2

Once the configuration file has been saved successfully, you can start the Zookeeper server.Use the following command to start the ZooKeeper server.
	
 -  cd /opt /opt/zookeeper-3.4.14/bin
 
 - ./zkServer.sh start

After executing this command, we will get a response as follows:
ZooKeeper JMX enabled by default 
Using config: /opt/zookeeper-3.4.14/bin/../conf/zoo.cfg 
Starting zookeeper … STARTED
Use the following command to start the CLI.


-	bin/zkCli.sh  

After connecting the server and performing all the operations, you can stop the ZooKeeper server by using the following command (Not recommended)

 - bin/zkServer.sh stop

 ##
**Installation and Configuration of Apache Storm**

To install Storm framework on your machine, visit the following link and download Storm . In this project we are using Storm 1.2.2 (Storm-1.2.2.tar.gz). http://storm.apache.org/downloads.html

 - Extract the tar file using the following commands:

	 - $ sudo su  

	 - cd /opt 

	 -  wget http://archive.apache.org/dist/storm/apache-storm-1.2.2/apache-storm-1.2.2.tar.gz  

	 - tar -zxf apache-storm-1.2.2.tar.gz 

	 -  cd apache-storm-1.2.2 # mkdir data

 - The current release of Storm contains a file at conf/storm.yaml that configures Storm daemons. Add the following information to that file. # nano conf/storm.yaml or vi conf/storm.yaml

	 -  nano conf/storm.yaml or vi conf/storm.yaml 

	 - storm.zookeeper.servers: - "localhost" storm.local.dir: “/path/to/apache-storm-1.2.2/data” 

	 - nimbus.host: "localhost" 

	 - supervisor.slots.ports: 
	 -     6700 
	 -  	6701
	 -  	6702 
	 -  	 6703

 - Adding to PATH

	 - STORM_HOME=”/opt/apache-storm-1.2.2” 

	 - export PATH=$PATH:$STORM_HOME/bin

 ##
 
 **Creating a StormCrawler Project: **
 We are going to start a StormCrawler project on a single node. To do so, we have to clone the whole project from its repository on github in any directory you want:
 
 - To install git and clone a Storm Crawler directory.

	 - $ sudo apt-get install git -y 

	 - $ cd /opt 

	 - /opt $ mkdir stormcrawler 

	 - /opt/stormcrawler 

	 - $ git clone https://github.com/DigitalPebble/storm-crawler.git

	 
**NOTE:** These instructions assume that you have Apache Maven installed.


 - $ sudo apt-get install maven -y 

 - $ mvn -v

We can now generate a brand new StormCrawler-based project using:

 -     $ mvn archetype:generate - DarchetypeGroupId=com.digitalpebble.stormcrawler -DarchetypeArtifactId=storm-crawler-archetype -DarchetypeVersion=1.14

 After downloading all needed packages, it will ask you a groupId, you can name it whatever you want, but here we name it com.dipe. and for artifactId we name it solrDemo. For ‘ version’ 1.0-SNAPSHOT and ‘package’ com.dipe we just hit enter. 

After creating project, this is what is available inside of solrDemo directory
	 - crawler-conf.yaml crawler.flux pom.xml README.md src
##

**Configuring our Crawler**

At the first place we should configure Solr as our backend for storing data. 

To do so, add the following lines to pom.xml in <dependencies></dependencies> section:
 -     /opt/solrDemo 
 -     $ vi pom.xml <dependency> <groupId>com.digitalpebble.stormcrawler</groupId> <artifactId>storm-crawler-solr</artifactId> <version>${stormcrawler.version}</version> </dependency>
 
Then copy solr-conf.yaml from the directory you have cloned before to the project directory. 

This is a command you can use to achieve this:
 - $ cp stormcrawler/external/solr/solr-conf.yaml /opt/solrDemo/
 Now we start Solr using StormCrawler configurations:

 - sudo service solr stop 

 -  sudo /opt/solr-8.2.0/bin/solr start -force -s /opt/stormcrawler/external/solr/cores

If starting Solr with those configs was successful, you can see the following cores in Solr Web Admin Panel

-     docs,metrics and status

Then add the following lines to crawler.flux in includes section in solrDemo directory, mention the correct path to the given below path of files along with their valid directories:

![Solr Running Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/2.PNG)

And bolts section should like this:

![Solr Running Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/3.PNG)

 Also you can write the websites you want to crawl in this file by changing the urls given in the image below:
 
![Solr Running Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/4.PNG)

In crawler-conf.yaml set the following config:

-     http.content.limit = -1

If you want to crawl images and videos or other media urls, comment out or remove (#) the following lines in /solrDemo/src/main/resources/default-regex-filters.txt file,otherwise skip these steps


 -     (?i)\.(apk|deb|cab|iso|gif|jpg|png|svg|ico|css|sit|eps|wmf|rar|tar|jar|zip|gz|bz2|rpm|tgz|mov|exe|jpeg|jpe|bmp|js|mpg|mp3|mp4|m4a|ogv|kml|wmv|swf|flv|mkv|m4v|webm|ra|wma|wav|avi|xspf|m3u)(\?|&|$)

And then add the following lines to /solrDemo/src/main/resources/ parsefilters.json file:
 -     $ { "class": "com.digitalpebble.stormcrawler.parse.filter.LinkParseFilter", "name": "LinkParseFilter", "params": { "pattern": "//IMG/@src" } }
You can set the depth of your crawler in /solrDemo/src/main/resources/ urlfilters.json file, I set this value to 2 but you can change it to any value you want. Make sure this file looks like this:
 -     { "com.digitalpebble.stormcrawler.filtering.URLFilters": [ { "class": "com.digitalpebble.stormcrawler.filtering.basic.BasicURLFilter", "name": "BasicURLFilter", "params": { "maxPathRepetition": 8, "maxLength": 8192 } }, { "class": "com.digitalpebble.stormcrawler.filtering.depth.MaxDepthFilter", "name": "MaxDepthFilter", "params": { "maxDepth": 2 } }, { "class": "com.digitalpebble.stormcrawler.filtering.basic.BasicURLNormalizer", "name": "BasicURLNormalizer", "params": { "removeAnchorPart": true, "unmangleQueryString": true, "checkValidURI": true, "removeHashes": false } }, { "class": "com.digitalpebble.stormcrawler.filtering.host.HostURLFilter", "name": "HostURLFilter", "params": { "ignoreOutsideHost": false, "ignoreOutsideDomain": false } }, { "class": "com.digitalpebble.stormcrawler.filtering.regex.RegexURLNormalizer", "name": "RegexURLNormalizer", "params": { "regexNormalizerFile": "default-regex-normalizers.xml" } }, { "class": "com.digitalpebble.stormcrawler.filtering.regex.RegexURLFilter", "name": "RegexURLFilter", "params": { "regexFilterFile": "default-regex-filters.txt" } } ] }

Now everything is done and we can compile our project using the following command:


 - mvn clean package

 When compile operation is done, you can now run the crawler by the following command:

  -     /opt/apache-storm-1.2.2/bin # storm jar /opt/solrDemo/target/solrDemo-1.0-SNAPSHOT.jar org.apache.storm.flux.Flux --local /opt/solrDemo/crawler.flux --sleep 86400000

**Output**

![Solr Running Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/5.PNG)

Now you can see the status of crawling, in status core of Solr Web Admin Panel, like below: 

![Crawler Running Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/6.PNG)

As you can see, we have discovered all URLs in those websites. Now it’s time to fetch data. To do so, we have to change the crawler.flux like below: We remove this:

![Crawler.flux Config](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/7.PNG)

And write this:

![Crawler.flux Config](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/8.PNG)

Now we run the previous command again:
 -     /opt/apache-storm-1.2.2/bin # storm jar /opt/solrDemo/target/solrDemo-1.0-SNAPSHOT.jar org.apache.storm.flux.Flux --local /opt/solrDemo/crawler.flux --sleep 86400000

After crawling operation is finished successfully, we can see the content of each URL in docs core in Solr Web Admin Panel.

![Solr Data Collection](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/StormCrawler/9.PNG)

***That’s all folks !!! Enjoy crawling your own URL’s.***


 


