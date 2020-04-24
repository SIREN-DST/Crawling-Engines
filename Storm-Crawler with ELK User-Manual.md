
# Crawling-Engines

### Storm-Crawler with ELK User Manual 
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

![Java Version Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Stormcrawler/1.png)
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

![Solr Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Stormcrawler/2.PNG)
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

	 -     cd /opt 

	 -     sudo apt-get install vim 

	 -     nano conf/zoo.cfg or vim conf/zoo.cfg

Inside the zoo.cfg file please mention the below:

	tickTime=2000 
	dataDir=/opt/zookeeper-3.4.14/data 
	clientPort=2181 
	initLimit=5 
	syncLimit=2

Once the configuration file has been saved successfully, you can start the Zookeeper server.Use the following command to start the ZooKeeper server.
	
 -  	cd /opt /opt/zookeeper-3.4.14/bin
 
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

To install Storm framework on your machine, visit the following link and download Storm . In this project we are using Storm 1.2.3 (Storm-1.2.3.tar.gz). http://storm.apache.org/downloads.html

 - Extract the tar file using the following commands:

		 - $ sudo su  

		 - cd /opt 

	 -  	wget http://archive.apache.org/dist/storm/apache-storm-1.2.3/apache-storm-1.2.3.tar.gz  

			 - tar -zxf apache-storm-1.2.3.tar.gz 

	 -  	cd apache-storm-1.2.3 
	 -  	mkdir data

 - The current release of Storm contains a file at conf/storm.yaml that configures Storm daemons. Add the following information to that file. # nano conf/storm.yaml or vi conf/storm.yaml

	 -  	nano conf/storm.yaml or vi conf/storm.yaml 

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

		 - $ git clone https://github.com/cnf271/stormcrawlertest.git

	 
**NOTE:** These instructions assume that you have Apache Maven installed.


	 - $ sudo apt-get install maven -y 

	 - $ mvn -v

We can now generate a brand new StormCrawler-based project using:

 -     $ mvn archetype:generate - DarchetypeGroupId=com.digitalpebble.stormcrawler -DarchetypeArtifactId=storm-crawler-archetype -DarchetypeVersion=1.15

 After downloading all needed packages, it will ask you a groupId, you can name it whatever you want, but here we name it com.dipe. and for artifactId we name it solrDemo. For ‘ version’ 1.0-SNAPSHOT and ‘package’ com.dipe we just hit enter. 

After creating project, this is what is available inside of solrDemo directory
	 - crawler-conf.yaml crawler.flux pom.xml README.md src
##

**Configuring our Crawler**

At the first place we should configure Solr as our backend for storing data. 

To do so, add the following lines to pom.xml in <dependencies></dependencies> section:
 -     /opt/solrDemo 
 -     $ vi pom.xml 
		 - <dependency> <groupId>com.digitalpebble.stormcrawler</groupId> <artifactId>storm-crawler-solr</artifactId> <version>${stormcrawler.version}</version> </dependency>
			 - <dependency> <groupId>com.digitalpebble.stormcrawler</groupId> <artifactId>storm-crawler-elasticsearch</artifactId><version>1.15</version></dependency>

 
Then copy solr-conf.yaml from the directory you have cloned before to the project directory. 

This is a command you can use to achieve this:

	 - $ cp stormcrawler/external/solr/solr-conf.yaml /opt/solrDemo/


 Now we start Solr using StormCrawler configurations:

	 - sudo service solr stop 

 -  	sudo /opt/solr-8.2.0/bin/solr start -force -s /opt/stormcrawler/external/solr/cores

If starting Solr with those configs was successful, you can see the following cores in Solr Web Admin Panel

-     docs,metrics and status

Then add the following lines to crawler.flux in includes section in solrDemo directory, mention the correct path to the given below path of files along with their valid directories:

![Solr Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Stormcrawler/3.PNG)

And bolts section should like this:

![Solr Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Stormcrawler/4.PNG)

 Also you can write the websites you want to crawl in this file by changing the urls given in the image below:
 
![Solr Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Stormcrawler/5.PNG)

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
 
## First Things First,

In order to work with Elasticsearch, we may need to delete some existing files and replace them with Elasticsearch compatible StormCrawler files. (Please note that, above configurations are good enough to do a proper web crawling and we are deviating from the basic StormCrawling as our end goal is to feed-in the crawled data to Elasticsearch).

Go ahead and clone the StormCrawler GitHub  [repository](https://github.com/jordillachmrf/stormcrawler)  to a separate folder. All we need is few configuration files from repo’s  _/external/elasticsearch_ folder. Copy the following files from  _/external/elasticsearch_  to previously created  _stormcrawlertest_ folder.

-   	ES_IndexInit.sh

-  	 	es-conf.yaml

-   	es-crawler.flux

-   	es-injector.flux

-   	Kibana (Folder)

And delete the following file from  _stormcrawlertest_ folder.

-   	crawler.flux

Now create a text file called  _seeds_ inside the  _stormcrawlertest_ directory.

After the alterations,  _stormcrawlertest_ folder should look like the below image.

![Solr Running Output](https://github.com/abhaymehtre/Crawling-Engines/blob/master/images/ELK_Stormcrawler/6.png)

Briefly explaining each and every file’s sole purpose.

-   **ES_IndexInit** -  Bash script containing information about the indexes we are going to create in Elasticsearch.

-   **es-conf.yaml** -  Contains information about configurations for Elasticsearch resources. (For now, will stick with the default configurations)

-   **es-injector.flux** -  Contains how URLs are injected to Elasticsearch  _search_ index. Initially, there is one  _spout_ (FileSpout — Reads URLs from a text file) and one  _Bolt_ (StatusUpdaterBolt — updates the status index after each and every inject in injector flux file.

-   **es-crawler.flux** -  Does the actual crawling part. Contains one spout (AggregationSpout— checks and retrieve URLs from Elasticsearch server to crawl) and several  _bolts_ (Several bolts to extract URLs, Fetch Data and index the content etc.)

-   **seeds.txt** -  Text file containing URLs of the website we are about to crawl (In this tutorial we will be telling the StormCrawler to use the URLs given in the  _seeds.txt_) Go ahead and add a URL to the text file. To start with the URLs I have added  [http://www.mit.edu/](http://www.mit.edu/)  to seeds.txt file.

-   **crawler-conf.yaml**- contains default configurations for StormCrawler.

## Change the default configurations of  **ES_IndexInit bash script**

By default, ES_IndexInit bash script has disabled the content saving option, when storing data in Elasticsearch index. Further,  __source_ has been disabled as well by default. You may want to change the configurations as follows, to get the StormCrawler to store the content data and display them in the query result.

	echo "Creating content index with mapping"

	curl $ESCREDENTIALS -s -XPUT $ESHOST/content -H 'Content-	Type: application/json' -d '

	{

	"settings": {

	"index": {

	"number_of_shards": 5,

	"number_of_replicas": 1,

	"refresh_interval": "60s"

	}

	},

	"mappings": {

	"_source": {

	"enabled": true

	},

	"properties": {

	"content": {

	"type": "text",

	"index": "true",

	"store": true

	},

	"host": {

	"type": "keyword",

	"index": "true",

	"store": true

	},

	"title": {

	"type": "text",

	"index": "true",

	"store": true

	},

	"url": {

	"type": "keyword",

	"index": "false",

	"store": true

	}

	}

	}

	}'

## Creating Relevant Indexes in Elasticsearch

Before stepping into the creation of maven project, we may need to create several indexes in Elasticsearch. That can be done by executing the  _ES_IndexInit_ bash script. Executing the  _ES_IndexInit_  bash script help us creating and deleting existing indexes we have added in Elasticsearch.

**What is ES_IndexInit bash script and its purpose ?**

_ES_IndexInit_ bash script contains several curl commands which creates and deletes (initially) existing search indexes. You may change them accordingly.

Bash script will create following indexes in ES,

-   **Content** - contains the actual content crawled by the StormCrawler along with a their  _host_,  _title_ and  _url_ etc.

-   **Status** - creates an index in ES which gives a status of the website domain that has been injected/crawled to ES. For ex: DISCOVERED, FETCHED, REDIRECTION, FETCH_ERROR and ERROR. More on status index  [here](https://github.com/DigitalPebble/storm-crawler/wiki/statusStream).

-   **Metrics** - contains metrics provided by Apache Storm and StormCrawler itself, such as worker id which was used to crawl the url, worker host etc.

Execute the bash script by simply running the following command inside the project directory.

/opt/stormcrawlertest # ./ES_IndexInit.sh

Once the script has been executed, following browser URLs can be used to check the status of above indexes.

[http://localhost:9200/status/_search?pretty](http://localhost:9200/status/_search?pretty)
[http://localhost:9200/content/_search?pretty](http://localhost:9200/content/_search?pretty)
[http://localhost:9200/metrics/_search?pretty](http://localhost:9200/metrics/_search?pretty)

## Injecting URLs to Elasticsearch

**What is actually meant by injecting URLs to Elasticsearch ?**

By injecting the URLs to Elasticsearch, a spout will be used to retrieve URLs from a particular source and send them to ES server for discovery.

In our case, we will be using  [_FileSpout_](https://github.com/DigitalPebble/storm-crawler/blob/master/core/src/main/java/com/digitalpebble/stormcrawler/spout/FileSpout.java)_,_ which will read the URLs from a text file and send them to the ES server. Further, several other spouts can be used to perform the task depending on the requirement. For example,  [_MemorySpout_](https://github.com/DigitalPebble/storm-crawler/blob/master/core/src/main/java/com/digitalpebble/stormcrawler/spout/MemorySpout.java) can be used when URLs are stored in memory.

We will be using Apache Flux to inject our URLs to the Elasticsearch server. Apache Flux is a framework that can be used to deploy our application using Apache Storm.

Go ahead and execute the following command in the project directory,

	storm jar /opt/stormcrawlertest/target/stormcrawlertest-1.0-SNAPSHOT.jar  org.apache.storm.flux.Flux --local /opt/stormcrawler/es-injector.flux

As we are running the injector in local mode, Apache Flux uses a default  _Time To Live_  (_TTL_) of 60 seconds. Injector will try to inject maximum number of URLs from  _seeds.txt_  to ES server during this period. However, in our case 60 seconds is more than enough to inject two URLs to the ES server. In the initial inject process, Injector topology will only try to discover the root URLs we have added in the text file.

Once the injector has been successfully ran for 60 seconds, we can check the status index for discovery status of the URLs.

{  
  "took" : 0,  
  "timed_out" : false,  
  "_shards" : {  
    "total" : 10,  
    "successful" : 10,  
    "skipped" : 0,  
    "failed" : 0  
  },  
  "hits" : {  
    "total" : {  
      "value" : 1,  
      "relation" : "eq"  
    },  
    "max_score" : 1.0,  
    "hits" : [  
      {  
        "_index" : "status",  
        "_type" : "_doc",  
        "_id" : "6a5d8441f5fee2387f82ac87499ee8f48876c06b0f1696afb98b643cacd9678e",  
        "_score" : 1.0,  
        "_routing" : "www.mit.edu",  
        "_source" : {  
          "url" : "http://www.mit.edu/",  
          "status" : "DISCOVERED",  
          "metadata" : { },  
          "key" : "www.mit.edu",  
          "nextFetchDate" : "2019-10-29T11:14:16.000Z"  
        }  
      }  
    ]  
  }  
}

## Crawling the injected URLs

Once the URLs have been injected to the ES server, Crawler topology can be used to crawl the pages depending on the crawl  _status_ and  _nextfetchDate_. Aggregation spout in Crawler flux will retrieve the URLs from status index and will start crawling them. Same as the Injector, Crawler topology will only run for 60 seconds in the local mode. In order to scrape an entire website, you may need to run the crawler flux multiple times.

Following command will start the crawler in local mode. Please ensure the path to the files are correct or else the code would not work as expected.

	storm jar /opt/stormcrawler/target/stormcrawlertest-1.0-SNAPSHOT.jar  org.apache.storm.flux.Flux --local /opt/stormcrawler/es-crawler.flux

After a successful run, you can check the  _status_ and  _content_ indexes for actual results. You may notice that, statuses of the URLs that have been injected earlier has been changed to FETCHED status, which means content in the given URL haven been successfully crawled and indexed to ES server by StormCrawler.

Snippet of the  _content_ index is given below.

	{  
	  "took" : 0,  
	  "timed_out" : false,  
	  "_shards" : {  
    "total" : 5,  
    "successful" : 5,  
    "skipped" : 0,  
    "failed" : 0  
	  },  
	  "hits" : {  
    "total" : {  
      "value" : 7,  
      "relation" : "eq"  
    },  
    "max_score" : 1.0,  
    "hits" : [  
      {  
        "_index" : "content",  
        "_type" : "_doc",  
        "_id" : "6a5d8441f5fee2387f82ac87499ee8f48876c06b0f1696afb98b643cacd9678e",  
        "_score" : 1.0,  
        "_source" : {  
          "content" : "Spotlight: Oct 29, 2019 MIT chemists have devised a way to synthesize polymers that can break down more readily in the body and in the environment. The materials could be useful for delivering drugs or imaging agents in the body, or as an alternative to some industrial plastics. Full story Oct 29, 2019 Share: Twitter Facebook",  
          "url" : "http://www.mit.edu/",  
          "domain" : "mit.edu",  
          "title" : "MIT - Massachusetts Institute of Technology"  
        }  
      },  
      {  
        "_index" : "content",  
        "_type" : "_doc",  
        "_id" : "ac6f172a5b208139bb56bdc477b021e699a2281105e7ee33d53002875c62e31b",  
        "_score" : 1.0,  
        "_source" : {  
          "content" : "homenewseducationresearchoffices+servicescommunityeventsaboutmap search people directory name/email reverse lookup (7 digits) lastname sounds like about the online people directory how to update | emergency services search format example first name last name william barton rogers last name rogers username wbrogers username with wildcard wbrog*, wbr?gers, wbro[jg]ers seven-digit phone number 253-1000 This directory does not allow searching by first name only. massachusetts institute of technology 77 massachusetts avenue cambridge, ma 02139-4307 TEL 617.253.1000 TDD/TTY, please use TRS (711) about this site contact MIT Google People Offices More Options",  
          "url" : "http://web.mit.edu/people.html",  
          "domain" : "mit.edu",  
          "title" : "MIT - people directory"  
        }  
      }  
...

As you can see, during the initial crawling process, StormCrawler was able to crawl 7 contents from  [http://www.mit.edu/](http://www.mit.edu/)  website. If you run the crawler again, you may notice an increment in the total hits count.

In this article, The Usermanual have discussed how to setup a StormCrawler project with Elasticsearch configurations. Further, The document have explained how ES_IndexInit bash script helps us in creating relevant indexes in Elasticsearch and what are the changes that needs to be done to the script, in order to store the content. I have added the sample project in one of [GitHub](https://github.com/cnf271/stormcrawlertest) Repository for your reference.







***That’s all folks !!! Enjoy crawling your own URL’s.***


 


