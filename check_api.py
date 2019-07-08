import urllib
import urllib2
import json
from pprint import pprint
import sys

url = "http://127.0.0.1:9250/jpdrmm/search"
data = {
    "question"  : 'Is smoking related to cataract ?',
    "id"        : '123',
}

req = urllib2.Request(url, data=json.dumps(data))
req.add_header('Content-type', 'application/json')
response = urllib2.urlopen(req)
ret_data = json.loads(response.read())
pprint(ret_data)
