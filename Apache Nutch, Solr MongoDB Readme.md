# Crawling-Engines
### Apache Nutch, Apache Solr, MongoDB Installation Procedure and User Manual 
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
![Java Version Output](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/1.png)
##
**Installation of Apache Nutch/Mongodb/Apache Solr:**

Your flavor of Linux may vary, if you have the correct versions of the main components like MongoDB, Nutch, and Solr, you should be good. I did not try setting this up on the Mac though. We will stick to Ubuntu 18.04 LTS for the rest of this installation procedure.
##
**Apache Nutch**

Nutch 2.x is only available as a source bundle, so it will need to be built using ant after configuring.
![Apache Nutch Download Details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/2.png)  

Next, we configure Nutch by editing $NUTCH_HOME/conf/nutch-site.xml. (Nutch home : the path of the directory) This is where we define the crawldb database driver, enable plugins, and the crawl behavior, to restrict it to only the domain defined.
![Nutch-Site Details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/3.png)
Figure 1.1: The configuration lines that are addressed in nutch-site.xml file. 
The path of the xml file: https://gist.github.com/lobster1234/ef8e9f6fbea6154da720d2534d490706#file-nutch-site-xml

![Gora Properties Details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/4.png)

Figure 1.2: These configuration lines that are addressed above need to copy into $ NUTCH_HOME/conf/gora.properties file. Nutch 2.x uses Apache Gora to manage persistence.

![Gora Properties Details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/5.PNG)
Figure 1.3: The configuration lines that are addressed in $ NUTCH_HOME/conf/gora.properties file. The path to the XML file: https://gist.github.com/lobster1234/60a4422b398c029dca0e3ee452c5dd2a#file-gora-properties

We also change $ NUTCH_HOME/conf/ivy/ivy.xml to enable MongoDB driver which will be used by Apache Gora. This is done by uncommenting the MongoDB line in the file.

![MongoDB details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/6.PNG)

Figure 1.4: The configuration lines that needs to be uncommented via the $NUTCH_HOME/conf/ivy/ivy.xml file. The path to the xml file : https://gist.github.com/lobster1234/7edffdff1410102013b3d271f6e22c35

**Note** 
 - Please change the url path in the $NUTCH_HOME/conf/ivy/ivysettings.xml file.
 - Change the http to https in the first four lines of the code as show in the figure below:
 
![IVY details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/7.PNG)

Figure 1.5: We need to change the http to https in file $NUTCH_HOME/ivy/ivysettings.xml. 
Now we build Nutch. Install ant if it is not installed already.
 - $ sudo apt-get install ant
 And we build Nutch from $NUTCH_HOME folder.
 - $ pwd
 /home/ubuntu/apache-nutch-2.3.1
 - $ ant runtime
 This would take about 20-30 mins to get the build ready.
 ##
 **MongoDB**
The installation procedure for mongodb in Ubuntu.
 - $ wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-3.4.7.tgz 
 - $ mkdir data 
 - $ mkdir logs 
 - $ tar xvfz mongodb-linux-x86_64-ubuntu1604-3.4.7.tgz $ cd mongodb-linux-x86_64-ubuntu1604-3.4.7/bin 
 - $ ./mongod --dbpath ~/data/ --logpath ~/logs/mongodb.log –-fork (Make sure that the data and logs mentioned here is the path of the directory in which the extracted data is available. EX: /home/abhay/Desktop/Nutch/mongodb-linux-86_x64-ununtu1604-3.4.7/data/ or /logs)
##
**Solr**
Let us get Solr 6.5.1 set up.
We will download and install Solr, and create a core named nutch to index the crawled pages. Then, we will copy the schema.xml from Nutch configuration to this newly created core.
 - $ wget http://archive.apache.org/dist/lucene/solr/6.5.1/solr-6.5.1.tgz 
 - $ tar xvfz solr-6.5.1.tgz 
 - $ cd solr-6.5.1/bin 
 - $ ./solr start 
 - $ ./solr create_core -c nutch -d basic_configs 
 - $ ./solr stop 
 - $ cd ../server/solr/nutch/conf $ cp ~/apache-nutch-2.3.1/conf/schema.xml .
Here comes the skullduggery. We will need to “fix” schema.xml and solrconfig.xml in this folder. We will also remove the managed-schema file, as we’re providing the schema configuration externally.
 - $ rm managed-schema 
 - $ vi schema.xml 
 Please find the changed file in the given link and change accordingly: https://gist.github.com/lobster1234/35078e4fc1df30e249b986e19fd67202
It is important to remove all instances of enablePositionIncrements="true" from every <filter class="solr.StopFilterFactory" declaration. If not removed, the core will fail to initialize.
Next, we have to fix the solrconfig.xml
 - $ vi solrconfig.xml
Locate the section for **AddSchemaFieldsUpdateProcessorFactory** and comment out the <lst> elements, like so-

![Solr Config details](https://github.com/SIREN-DST/Crawling-Engines/blob/master/images/ApacheNutch/8.PNG)
##
**Crawl and Index**

Now that we have everything set up, we are ready to put Nutch in action. First, tell nutch what URL(s) to crawl. We do this by creating a simple text file and pointing Nutch to it.
 - $ cd ~/apache-nutch-2.3.1/ 
 
 - $ mkdir urls 
 
 - $ vi urls/seeds.text
 
Enter the URL(s) in this file, for example. https://www.wikipedia.org. One URL per line. Once the seed file is set up, run the following -
$ runtime/local/bin/nutch inject urls/
 
InjectorJob: starting at 2020-02-13 07:43:22 

InjectorJob: Injecting urlDir: urls

InjectorJob: Using class org. apache. gora.mongodb.store.MongoStore as the Gora storage class. 

InjectorJob: total number of urls rejected by filters: 0 

InjectorJob: total number of urls injected after normalization and filtering: 1 Injector: finished at 2020-02-13 07:43:25, elapsed: 00:00:03

This has initialized the crawl database - we can use the MongoDB CLI to check out the resulting database and collection. 

Path : $NUTCH_HOME/ mongodb-linux-x86_64-ubuntu1604-3.4.7/bin/./mongo

-> show dbs

local 0.000GB nutchdb 0.005GB

-> use nutchdb 

switched to db nutchdb 

-> show collections 

webpage

Next, we generate the top 50 URLs. Do not worry if you see a different number like 20 below.

$ runtime/local/bin/nutch generate -topN 50 

$ runtime/local/bin/crawl urls <namedb> <solrurl> <number of rounds> GeneratorJob: starting at 2020-02-13 08:56:36 
	
GeneratorJob: Selecting best-scoring urls due for fetch. 

GeneratorJob: starting 

GeneratorJob: filtering: true 

GeneratorJob: normalizing: true 

GeneratorJob: topN: 50

GeneratorJob: finished at 2020-02-13 08:56:38, time elapsed: 00:00:02 GeneratorJob: generated batch id: 1502528196-1091715892 containing 20 URLs

Now that Nutch has selected N URLs, we go ahead fetch them.

 - $ runtime/local/bin/nutch fetch -all
 
 Next, we update the DB with the current status.
 
  - $ runtime/local/bin/nutch updatedb -all
  
  Finally, we index these pages in Solr
  
  $ runtime/local/bin/nutch solrindex http://localhost:8983/solr/nutch -all
  
   IndexingJob: starting
   
	 Active IndexWriters : 
	 
	 SOLRIndexWriter
	 
	 solr.server.url : URL of the SOLR instance (mandatory)
	 
	 solr.commit.size : buffer size when sending to SOLR (default 1000)
	 
	 solr.mapping.file : name of the mapping file for fields (default solrindex-mapping.xml) 
	 
	 solr.auth : use authentication (default false) solr.auth.username : username for authentication
	 
solr.auth.password : password for authentication 

- If you have access to the Solr console (http://localhost:8983), fire it up in a browser. 
- Here, we’re querying Solr for any content that matches test (hence q=content:test) and only return the url, meta_description, and anchor (hence fl=url,%20meta_description,%20anchor,%20title). We will get a list of at most 10 results in a JSON format. 
- You may want to play with different values for different fields either via the Solr Console or curl.
##
**Cheat Codes for Smooth Running of the Apache Nutch Crawling services.**

Running everything again 

cd ~/Desktop/Nutch/nutch/runtime/local/ bin/nutch inject urls bin/nutch generate -topN 10

bin/nutch fetch -all 

bin/nutch parse -all 

bin/nutch updatedb -all 

bin/nutch solrindex http://localhost:8983/solr/nutch -all

Crawling of an urls using commands

Cd ~/Desktop/Nutch/runtime/local/

Syntax : bin/crawl <seedDir> <crawlID> [<solrurl>] <number of rounds>
	
Syntax Example : bin/crawl urls nutchdb http://localhost:8983/solr/nutch 1 or 2 based on the crawl depth.

Note: crawlID is uniquely generated the nutchdb here is used an crawlID that stores the data.

One liner Syntax bin/nutch inject urls && bin/nutch generate -topN 10 && bin/nutch fetch -all && bin/nutch parse -all && bin/nutch updatedb -all bin/nutch solrindex http://localhost:8983/solr/nutch -all

Clearing the solr database rm -rf ~/Desktop/Nutch/solr/server/solr/nutch cd ~/Desktop/Nutch/solr && bin/solr restart bin/solr create_core -c nutch -d basic_configs

Clearing the mongo database 

The hbase db store the url's for nutch, you may want to clear this also ~/Desktop/Nutch/ mongodb-linux-x86_64-ubuntu1604-3.4.7/bin/ ./mongo

➢ show dbs admin 0.00GB

Local 0.00GB

Nutchdb 0.00GB

➢ use nutchdb

switched to db nutchdb

➢ show collections

Webpage

nutchdb_webpage

➢ exit

To drop any table from the db we use db.<name of the table>.drop()
	
Syntax example : db.nutchdb_webpage.drop()

***There we have it - a fully functional, end to end crawler and indexer setup!***
