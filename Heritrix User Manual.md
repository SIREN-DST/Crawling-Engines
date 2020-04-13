
# Crawling-Engines
### Heritrix User Manual 
##
**Prerequisite**

 - Some or good grip on the Linux administration commands.
 
 - Should have an idea about installation of Operating Systems.
 
 - Should have good idea about the VMware players(if installation is to be done on VM).
 
##
**Basic Installation Steps**

**Installation of Operating System/Virtual Machine:**

 - The above products of Apache would run good on Ubuntu 16.04 LTS and Ubuntu 18.04 LTS version of the operating systems.
 
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

![Java Version Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ApacheNutch/1.png)
##

**Installation Requirements**

Before getting to the StormCrawler itself lets get into the basics of StormCrawler and the required dependencies that StormCrawler works based on these.

 - We need the Zookeeper 3.4.14 and Storm 1.2.2 source files (Very specific to the versions).
 
 - All the installation steps that are going to be used would work on Ubuntu 16.04.3 LTS and Ubuntu 18.04.3 LTS

 - Make sure all the dependencies and tools are up to date.

##

**What is Heritrix?**

Heritrix is a web crawler designed for web archiving. It was written by the Internet Archive. It is available under a free software license and written in Java. The main interface is accessible using a web browser, and there is a command-line tool that can optionally be used to initiate crawls.
 
##

**Installation and Configuration Heritrix:**

 - To start with we download the required Heritrix 1.14.4.tar.gz file from the sourceforge website (https://sourceforge.net/projects/archive-crawler/)
 
 - Ensure that all the procedures are to be used in the super user mode (Administrative Mode).

 - Next, we extract Heritrix Service installer shell script from the downloaded Heritrix archive file and run the installer using the following commands:

	- $ sudo su 

	-  tar -xvf heritrix-1.14.4.tar.gz
	
 -  Now we export the HERITRIX_HOME property to the path where heritrix is extracted.
 
	- export HERITRIX_HOME=/home/heritrix-1.14.4

	- echo $HERITRIX_HOME/

 -  Once you get the proper path to your heritrix source files, we need to append the full permissions to the bin directory and as well as all the files present in the folder.

	 - chmod u+x $HERITRIX_HOME/bin/heritrix

 - To the help mode and to start the UI of the Heritirix, we need to ensure the “heritrix.properties” file is available in the folder. If its not available (especially in the higher versions of heritrix) we need to import the “heritrix.properties” file. Once if the file does exists then run the following command:

	 - HERITRIX_HOME/bin/heritrix -a admin:admin
 
**Output**

![Heritrix Start Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Heritrix/1.PNG)
##

**Installation and Configuration of Heritrix UI:**

Once after the UI is running properly on the your localhost “http://127.0.0.1:8080” then we start the procedure for crawling of the webpages.

**Output**
![Heritrix Start Page ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Heritrix/2.PNG)

Figure 1: The Heritrix UI running on the localhost machine.

 - The above output contains the Console, Jobs, Profiles and Logs, Reports and Setup and Help. 

 -  All of these are important and to begin with we go to the Jobs Section, In the job section you find a Create New Job section, where we need to click on Based on Profile or even we can click on the defaults. 

 -  With defaults the just type the Profile Name as per the crawl data and provide the urls that are needed to be crawled. 

 - In the below section we find the settings which would redirect the page to settings and configurations where the https-headers section would appear. 

 - Please provide the details of the user-agent and the from section in the configuration part. 

 - Once the details are filled, then submit the job and move to console page.

 -  In the console page, you find Crawler Status : Start, once started the Job Status would shift to Running and you get the alerts and to find the URLs getting crawled we can see it in the logs section of the User Interface.

**Output**


![Heritrix Start Page ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Heritrix/3.PNG)


Figure 2: To Configure and run a job in the Heritrix UI.



![Heritrix Start Page ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Heritrix/4.PNG)


Figure 2.1: To ensure that http-headers details are filled as shown above and then the job is submitted.

![Heritrix Start Page ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/Heritrix/5.PNG)


Figure 3: After the successful configuration, your Heritrix UI based crawling tool starts operating.



***That’s all folks !!! Enjoy crawling your own URL’s.***

