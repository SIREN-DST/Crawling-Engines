'''
Imports
'''
from config import *
from newspaper import Article
import sys as sys
import pandas as pd 
import csv
from collections import defaultdict
import re
'''
URL Extract
'''
columns = defaultdict(list)
with open('SecurityIDRBT.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
url_list = []                                 # based on column name k
for element in range(len(columns['Body'])):
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', columns['Body'][element])
        for url in urls:
            url_list.append(url)
'''
Find Unique URLs and filter with semantic search results
'''
url_unique = []
for element in url_list:
    if element not in url_unique:
        if element not in common_urls_http: 
            if element not in common_urls_https:
                url_unique.append(element)
'''
Write it in a new CSV
'''    

with open('url.csv', 'w',newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in url_unique:
        wr.writerow([word])

        
        
 