#coding: utf-8

import requests
import sys
import re

url = 'http://hashtoolkit.com/reverse-hash/?hash='
try:
	hasH = sys.argv[1]
except:
	print ("\nComando: hash.py HASH")
	sys.exit()

http = requests.get(url+hasH)
content = http.content
descrypt = re.findall("<span title=\"decrypted (md5|sha1|sha256|sha384|sha512) hash\">(.*)</span>", content)
print ("\nHash Identificada: "+descrypt[0][0])
print ("Senha Descryptada: "+descrypt[0][1])