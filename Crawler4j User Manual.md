
# Crawling-Engines
### Crawler4j User Manual 
##
**Prerequisite**

 - Some or good grip on the Linux administration commands.
 
 - Should have an idea about installation of Operating Systems.
 
 - Should have good idea about the VMware players(if installation is to be done on VM).
 
 - Should have good idea of Integrated Development Environment based Consoles (Eclipse or Netbeans)

 
##
**Basic Installation Steps**

**Installation of Operating System/Virtual Machine:**

 - The above products of Crawler would run good on Windows and Linux Operating Systems.
 
 - You can get the image files of the OS by clicking on the link: [Ubuntu OS ](https://ubuntu.com/download/desktop) (Ubuntu 18.04.3 LTS/Ubuntu 16.04.3 LTS).
 
 - If the system is running on Windows Operating System, then it would be better to make a dual-boot for other operating system to be installed or we can use the VMware Player or Workstation 15.xx version for the installation of the Ubuntu OS.
 
	 - Link for VMware: [VMware Download Link](https://www.vmware.com/in/products/workstation-player/workstation-player-evaluation.html)
	 
 - Please install the VMWare Workstation Player.
 
 - After the installation and running VMWare Workstation Player, you could get a window where there is a tab called Create a New Virtual Machine.
 
 - After the click, please ensure the details are filled and the path to the installation of image file of the Linux OS is to be provided.
 
 - Then we could customize the processor cores, RAM, others as per the system requirements.
 
 - After clicking finish, the virtual machine would start up and the installation of OS would be in process.

 - In this documentation, the installation and setup is based on the Windows OS.
 
##

**Installation of Java Version (Linux Version for Implementation)**

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

**Installation Requirements**

Before getting to the Crawler4j itself let’s get into the basics of Crawler4j and the required dependencies that Crawler4j works based on these.

 - We need the Eclipse IDE with Juno or Kepler versions. Visit the https://www.eclipse.org/downloads/. We need the versions of Java 1.5 + higher along with JRE and JDK .
 
 - All the installation steps that are going to be used would work on Windows 7 or higher Versions.

 - Make sure all the dependencies and tools (Java installation) are up to date.

##

**What is Crawler4j?**

Crawler4j is a Java library which provides a simple interface for crawling the web. Using it, you can setup a multi-threaded web crawler in 5 minutes! It is also very efficient; it has been able to download and parse 200 pages per second on a Quad core PC with cable connection.
 
##

**Installation and Configuration of Crawler4j:**

• To start with we download the required Eclipse Juno or Kepler from its official site or mirrors.

• Once downloaded, install and the configure the java path into the environmental variables of the system and direct it to the eclipse.

• Once the eclipse installation is done, we need to go to File → New Project → Maven Project.

• Under the Maven project please select the archtype to quickstart with snapshot mode.

• Then we would arrive at the page where you could see the project directory where all the source files and the resources are present.

• Once the folder is generated in the eclipse lets get on to work.

• We should download the jar for the version of crawler4j we are using. We can get the crawler4j jar by visiting https://jar-download.com/artifact-search/crawler4j. Version used here is 4.4.0

• Firstly, we need to build the pom.xml with the dependency that crawler4j needs for running the crawl. You can import it after searching the web or just put the same dependency as given below.
 
**Output**

![Dependency Properties Configuration](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/Crawler4j/1.PNG)

 - Custom crawler class should be added by extending the WebCrawler class provided by Crawler4j framework. Two methods, “shouldVisit” and “visit” methods should be overridden to provide expected behavior for the crawler as given in below code snippet.

 -  Firstly we need to generate a class in the eclipse for writing the code for the crawler. 

 -  The first file would be TestCrawler.java and the link for this code is https://gist.githubusercontent.com/csgsajeewa/7715c5910a99d51ee3c29e4ff82c545f/raw/606a0895d3d92bbdac971d48b8ca55aed657b557/TestCrawler.java 

 -  After copying the code and pasting it into the IDE, please ensure to resolve all the errors present by appending to some jar file or the version of the java. 

 -  Then there is an other file named App.java where the URL is given and the conditions for the crawling is mentioned. 

 - Please ensure the depth of crawl, the crawl storage path and the url you wanted to crawl in the App.java file. You can use the path to reach the file https://gist.github.com/csgsajeewa/da4decff5ac0d00c77731a66b90552ef#file-app-java

**Output**


![Crawler4j Crawl Output ](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/Crawler4j/2.PNG)





***That’s all folks !!! Enjoy crawling your own URL’s.***

