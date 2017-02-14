#!/usr/bin/env python

# A simple python script that create a DOI based on system timestamp.

import json,cgi,time
import httplib2, sys, base64, codecs

res=[]
retCode=0
errCode=''
doi='11623'
res =  "%s/sci-gaia:%s" % (doi,time.time())
print "Content-type: application/json\n\n"
print json.dumps(res)
