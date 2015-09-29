__author__ = 'ugunipati'

import urllib2
import re
import requests

website = urllib2.urlopen("http://timesofindia.indiatimes.com/")
html = website.read()
links = re.findall('"((http://).*?)"', html)
#print links

for link in links:
   print link[0]
   response = urllib2.urlopen(link[0])
   print response.getcode()
