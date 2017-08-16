__author__ = 'Yo'

'''


 QUITO
==============
'''
import couchdb
import sys
import urllib2
import re
import json
import sys
from pprint import pprint
#encoding:utf-8

def eliminarURL(text):
 link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
 links = re.findall(link_regex, text)
 for link in links:
  text = text.replace(link[0], ', ')
 return text
def eliminarCarita(text):
 link_regex = re.compile(
 '(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)')
 links = re.findall(link_regex, text)
 for link in links:
  text = text.replace(link[0], ', ')
 return text
def eliminarHashtag(text):
 outputSentence = ""
 changes = 0;
 returnMsg = ""
 word = str(text)
 for letter in word:
  if letter == "#":
   changes += 1;
  else:
   outputSentence += letter
   returnMsg = str(changes)
 return outputSentence

from couchdb import view

URL = 'localhost'
db_name = 'tweets_uio'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/') 
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()


url = 'http://127.0.0.1:5984/tweets_uio/_design/quito/_view/quito'
req = urllib2.Request(url)
f = urllib2.urlopen(req)

view = "codigo/ecuador"
LIMIT_OF_DOCUMENTS = 20000


for data in db.view(view, limit=LIMIT_OF_DOCUMENTS):
    json_data = db.get(data['id'])

    # eliminarURL(t)
    res1 = eliminarURL(json_data['text'])
    # eliminarCarita(res1)
    res2 = eliminarCarita(res1).encode('utf-8').strip()
    # eliminarHashtag(res2)
    res3 = eliminarHashtag(res2)

    f2 = open('/home/mpiuser/PycharmProjects/test/tweetsProcesados2.txt', 'a')
    f2.write("('"+res3+"', '"+json_data['label']['polarity'].encode('utf-8').strip()+"'),"'\n')
    f2.close()

    #print "('"+res2+"', '"+json_data['label']['polarity']+"'),"


