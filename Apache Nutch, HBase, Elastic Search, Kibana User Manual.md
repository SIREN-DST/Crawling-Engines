### Apache Nutch 2.3, Hbase 0.94.14 & Elastic Search 6.8 , Kibana User Manual 
#
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

![Java Version Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/1.JPG)

##

**Installation of Apache Nutch/HBase/Apache Solr:**

A guide on how to install Apache Nutch v2.3 with Hbase as data storage and search indexing via Solr 5.2.1.

Apache Nutch is an open source extensible web crawler. It allows us to crawl a page, extract all the out-links on that page, then on further crawls crawl them pages. It also handles the frequency of the calls and many other aspects which could be cumbersome to setup.

Let’s have a look at setting up Apache Nutch with Hbase.



##

**Getting all the tools**

OK first we need to get all the tools, on your machine create a working directory. If you fetch them from other mirrors, ensure you get the correct versions:


	Create our working dir
	mkdir ~/Desktop/Nutch  
    cd ~/Desktop/Nutch
    # Grab all our files (correct versions!)  
    curl -O [http://archive.apache.org/dist/nutch/2.3/apache-nutch-2.3-src.tar.gz]
    curl -O [http://archive.apache.org/dist/hbase/hbase-0.94.14/hbase-0.94.14.tar.gz]
    
    
    # Unzip and rename them (for convenience!)  
    tar -xzf apache-nutch-2.3-src.tar.gz && mv apache-nutch-2.3 nutch  
    tar -xzf hbase-0.94.14.tar.gz && mv hbase-0.94.14 hbase  
        
    # Delete command if you wanna start again!  
    rm -rf nutch hbase 
    
    # Move our source files to another directory to keep things clean!  
    mkdir gzips && mv apache-nutch-2.3-src.tar.gz hbase-0.94.14.tar.gz gzips
    Your working directory should now look like this:  
        
    ├ gzips  
    ├ hbase  
    ├ nutch  
   
#
**Make sure JAVA_HOME and NUTCH_JAVA_HOME environment variable is set**

In your ~/.bash_profile or ~/.bashrc ensure your JAVA_HOME is set correctly. We also need to set NUTCH_JAVA_HOME to point to our Java home directory.

**Setup Hbase**

open ~/Desktop/Nutch/hbase/conf/hbase-site.xml and add the following 2 **property** nodes


    open ~/Desktop/Nutch/hbase/conf/hbase-site.xml
    
    Edit `/conf/hbase-site.xml` and add
    
    <configuration>
    <property>
    <name>hbase.rootdir</name>
    <value>file:///path/where/the/data/should/be/stored</value>
    </property>
    <property>
    <name>hbase.cluster.distributed</name>
    <value>false</value>
    </property>
    </configuration>
Next, we need to tell gora to use Hbase for it’s default data store.

    open ~/Desktop/Nutch/nutch/conf/gora.properties
    open ~/Desktop/Nutch/nutch/runtime/local/conf/gora.properties
    
    Add this line under `HBaseStore properties` (to keep things organised)  
    gora.datastore.default=org.apache.gora.hbase.store.HBaseStore

We need to add/uncomment the gora-hbase dependency to our ivy.xml

    open ~/Desktop/Nutch/nutch/ivy/ivy.xml
    # Find and Uncomment this line (aprrox 118)  
    <dependency org="org.apache.gora" name="gora-hbase" rev="0.5" conf="*->default" />

 **Testing it all works! (and some common useful commands)**
      
    open ~/Desktop/Nutch/hbase/bin/start-hbase.sh
    Stop it (Outputs: stopping hbase......) - Can take a while, be patient  (This step is not necessary)
	~/Desktop/Nutch/hbase/bin/stop-hbase.sh (Not recommended)
	 Access the shell  
	 ~/Desktop/Nutch/hbase/bin/hbase shell#
		 list = list all tables
		disable 'webpage'  = disable the table (before dropping)  
	    drop 'webpage'     = drop the table (webpage is created & used by nutch)  
		exit               = exit from hbase# For the next part, we need to start hbase  
	~/Desktop/Nutch/hbase/bin/start-hbase.sh

#

 ## Configure nutch
 
 By default we must provide a user agent name to identify your crawler. In this case we also need to configure the data store to use HBaseStore. We’ll also add our plugin list here noting we have indexer-solr in the regular expression.
     
     open ~/Desktop/Nutch/nutch/conf/nutch-site.xml
     In `conf/nutch-site.xml` you need to name your spider and configure both HBase as a store and Elasticsearch as an indexer
     <?xml version="1.0"?>
    <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
    <!-- Put site-specific property overrides in this file. -->
	    <configuration>
	    <property>
	    <name>http.agent.name</name>
	    <value>Qbox Spider</value>
	    </property>
	    <property>
	    <name>storage.data.store.class</name>
	    <value>org.apache.gora.hbase.store.HBaseStore</value>
	    <description>Default class for storing data</description>
	    </property>
	    <property>
	    <name>plugin.includes</name>     
	    <value>protocol-httpclient|urlfilter-regex|parse-(text|tika|js)|index-(basic|anchor)|query-(basic|site|url)|response-(json|xml)|summary-basic|scoring-opic|urlnormalizer-(pass|regex|basic)|indexer-elastic</value>
	    </property>
	    <property>
	    <name>db.ignore.external.links</name>
	    <value>true</value>
	    </property>
	    <property>
	    <name>elastic.host</name>
	    <value>localhost</value>
	    </property>
	    <property>
		<name>elastic.port</name>
	    <value>9200</value>
	    </property>
	    <property>
	    <name>elastic.cluster</name>
	    <value>elasticsearch</value>
	    </property>
	    <property>
	    <name>elastic.index</name>
	    <value>nutchindex</value>
	    </property>
	    <property>
	    <name>parser.character.encoding.default</name>
	    <value>utf-8</value>
	    </property>
	    <property>
	    <name>http.content.limit</name>
	    <value>65536000</value>
	    </property>
	    <property>
	    <name>elastic.max.bulk.docs</name>
		  <value>250</value>
		  <description>Maximum size of the bulk in number of documents.</description>
		</property>
		<property>
		  <name>elastic.max.bulk.size</name>
		  <value>2500500</value>
		  <description>Maximum size of the bulk in bytes.</description>
		</property>
		</configuration>
		
**Note** 

 - Please change the url path in the
	
		 $NUTCH_HOME/conf/ivy/ivysettings.xml file.
		 
 - Change the http to https in the first four lines of the code as show in the figure below:
 
![IVY details](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/2.JPG)

#

## Compiling nutch

We need to compile Apache Nutch using ant. This is straight-forward but can take a while (10 minutes on my Macbook Pro 2012) if it’s the first time. Make sure you have hbase and solr running.
  
    # Start hbase and solr  
    ~/Desktop/Nutch/hbase/bin/start-hbase.sh  
	~/Desktop/Nutch/solr/bin/solr start# Build Nutch  
	cd ~/Desktop/Nutch/nutch  
	ant runtime
	
Once complete you’ll see BUILD SUCCESSFUL.

#

##  **Installation of ElasticSearch Kibana Services on Ubuntu 18.04:**

ELK is the combination of three open source projects: Elasticsearch, Logstash, Kibana and Filebeat. Elasticsearch is a search and analytics engine. Logstash is a server-side logs processing pipeline that transport logs from multiple sources simultaneously, transforms it, and then sends it to a “stash” like Elasticsearch. 

Kibana is to visualize logs with charts and graphs from Elasticsearch. You can visit the link https://www.fosstechnix.com/install-elk-stack-on-ubuntu/ for any queries or other information required. 

WorkFlow = Apache Nutch --> ElasticSearch --> Kibana

#


 **Installation and Configuration of ElasticSearch**
 
	 Here, We are adding ElasticSearch official apt package and this is signed with GPG keys
	 
		 $ sudo apt-get install vim 
		 $ sudo wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add –

Next add the repository in /etc/apt/sources.list.d/elastic-6.x.list using below command.

	$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

To install elasticsearch enter below command

	$ sudo apt-get update 
	$ sudo apt-get install elasticsearch
	
**Output**

![Elastic Search Output ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/3.JPG)

Let’s make changes in below configuration file

	$ sudo vi /etc/elasticsearch/elasticsearch.yml 

uncomment network.host and make changes as

	network.host: 0.0.0.0
	host.port : 9200/9300 (or else based on your choice)

To start elasticsearch services 

	$ sudo systemctl start elasticsearch 
	
 To enable elasticsearch at system startup 
 
	 $ sudo systemctl enable elasticsearch 
	 
 To stop elasticsearch (Not recommended at the time of installation)

	 $ sudo systemctl stop elasticsearch

**Output**

![Elastic Search Output ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/4.JPG)

Enter below command to check elasticsearch is running or not

	$ sudo apt-get install curl -y 

	$ curl -X GET "localhost:9200 or localhost:9300"

**Output**

![Elastic Search Output ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/5.JPG)

	
#	


 **Installation and Configuration Kibana**
#

To install Kibana

	$ sudo apt-get install kibana
	
![Kibana Installation ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/6.JPG)


Now let’s make changes in below configuration file for to access kibana 

	$ sudo vi /etc/kibana/kibana.yml 
	
 uncomment server.host at line 7 and make changes as mentioned below 

	server.host: "0.0.0.0" 
  To start kibana service
   
	  $ sudo systemctl start kibana  
  To enable kibana at system startup
   
	  $ sudo systemctl enable kibana

**Output**

![Kibana Installation ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/7.JPG)

To check the status of kibana service 

	$ sudo systemctl status kibana  
	
To stop kibana service (Not recommended) 

	$ sudo systemctl stop kibana

**Output**


![Kibana Installation ](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Nutch/8.JPG)


## Fire it all up!

Finally we can play!

Make sure you have hbase and solr running, let’s also setup our regular expressions and initial seed list here.

Ensure hbase and elastic search are started!  

    ~/Desktop/Nutch/hbase/bin/start-hbase.sh
    
	$ sudo systemctl start elasticsearch  

	We'll edit the regex filter to only crawl the apache nutch domain  
	open ~/Desktop/Nutch/nutch/runtime/local/conf/regex-urlfilter.txt
	 Add the following line before the `accept anything else +.`  
	+^http://nutch.apache.org

	Insert the url into our `seed` list  
	mkdir -p ~/Desktop/Nutch/nutch/runtime/local/urls/  
	echo "http://nutch.apache.org" > ~/Desktop/Nutch/nutch/runtime/local/urls/seed.txt

Finally, lets start our first crawl!

 Change our working dir  
 
cd ~/Desktop/Nutch/nutch/runtime/local/

 Inject the url's from our seed list (in the directory named `urls`)  

This injects into our Hbase database (as that's what we have specified)
  

    bin/nutch inject urls

 Generate a segment which tells Nutch which and how to fetch the urls.  

Creates folder <#timestamp#> under the <segments_dir> 
 
Inside that dir creates the folder "crawl_generate" where Nutch puts list of URLs to be fetched.  

	 topN = How many pages to crawl this depth  
 
 This will only contain 1 URL the first round we execute
   
	  bin/nutch generate -topN 10

Fetch the URLs we generated in the previous step. 
 
 Nutch places the data into the "content" and "crawl_fetch" folders inside the <segments_dir>/#timestamp# directory.  
 

	  bin/nutch fetch -all

Instruct Nutch to parse the fetched data which is placed into three folders  

 "crawl_parse", "parse_data" and "parse_text" inside the <segments_dir>/#timestamp# directory.  
 
 We can write a custom ParserFilter extension to parse content how we like  

	   bin/nutch parse -all

 Update the Database with the new urls  

	  bin/nutch updatedb -all

 Finally let's push everything to elastic search (and to our demo core)  
 

	bin/nutch bin/nutch index elasticsearch -all
	
	No IndexWriters activated - check your configuration
	
	You can query your data with Elasticsearch
	
	curl -X GET "http://localhost:9200/_search?query=myterm"





***There we have it - a fully functional, end to end crawler and indexer setup!***
