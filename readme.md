# Crawling-Engines

#### Apache Nutch and Apache Solr, MongoDB User Manuals

**What is Apache Nutch?**

Apache Nutch is a highly extensible and scalable open source web crawler software project. Stemming from Apache Lucene, the project has diversified and now comprises two codebases, namely:

- Nutch 1.x: A well matured, production ready crawler. 1.x enables fine grained configuration, relying on Apache Hadoop data structures, which are great for batch processing.

- Nutch 2.x: An emerging alternative taking direct inspiration from 1.x, but which differs in one key area; storage is abstracted away from any specific underlying data store by using Apache Gora for handling object to persistent mappings. This means we can implement an extremely flexibile model/stack for storing everything (fetch time, status, content, parsed text, outlinks, inlinks, etc.) into a number of NoSQL storage solutions.

- Being pluggable and modular of course has it's benefits, Nutch provides extensible interfaces such as Parse, Index and ScoringFilter's for custom implementations e.g. Apache Tika for parsing. Additionally, pluggable indexing exists for Apache Solr, Elastic Search, etc.

Nutch can run on a single machine, but gains a lot of its strength from running in a Hadoop cluster

Nutch is a project of the Apache Software Foundation and is part of the larger Apache community of developers and users.

[Apache Nutch, Solr, MongoDB User Manuals Link](https://github.com/SIREN-DST/Crawling-Engines/blob/master/Apache%20Nutch%2C%20Solr%20MongoDB%20Readme.md)



#### Storm-Crawler and Apache Solr

**What is StormCrawler?**

StormCrawler is an open source SDK for building distributed web crawlers based on Apache Storm. The project is under Apache license v2 and consists of a collection of reusable resources and components, written mostly in Java.

- The aim of StormCrawler is to help build web crawlers that are:
  - Scalable, resilient, low latency, easy to extend and polite yet efficient.
  
  [StormCrawler and Solr User Manuals Link](https://github.com/SIREN-DST/Crawling-Engines/blob/master/Storm-Crawler%20and%20Solr%20User-Manual.md)
  
#### Crawler4j
  
**What is Crawler4j?**

Crawler4j is a Java library which provides a simple interface for crawling the web. Using it, you can setup a multi-threaded web crawler in 5 minutes! It is also very efficient; it has been able to download and parse 200 pages per second on a Quad core PC with cable connection.

[Crawler4j User Manual Link](https://github.com/SIREN-DST/Crawling-Engines/blob/master/Crawler4j%20User%20Manual.md) 

#### Heritrix

**What is Heritrix?**

Heritrix is a web crawler designed for web archiving. It was written by the Internet Archive. It is available under a free software license and written in Java. The main interface is accessible using a web browser, and there is a command-line tool that can optionally be used to initiate crawls. 

[Heritrix User Manual Link](https://github.com/SIREN-DST/Crawling-Engines/blob/master/Heritrix%20User%20Manual.md)

#
