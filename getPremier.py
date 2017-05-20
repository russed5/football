#!/usr/bin/python
# Copyright © 01 April 2017 Dell Inc. or its subsidiaries.  All Rights Reserved.
#
# Author: russed5
# Revision: 1.0
# Code Reviewed by: olearj10


import urllib.request
import json

url = "https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&format=jason"
response = urllib.request.urlopen(url)
data = response.read()
#encoding = data.info().get_content_charset('utf-8')
#ddd = json.loads(data)

print('thirdpass but second commit from local')
print('secondpass')
print(data)

