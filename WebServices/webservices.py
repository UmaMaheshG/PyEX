from urllib2 import Request,urlopen,URLError

request = Request("http://ap1.salesforce.com")

try:
    response = urlopen(request)
    kittens = response.read()
except URLError,e:
    print "Not kittenz got error code", e
