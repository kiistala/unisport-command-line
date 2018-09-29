#!/usr/bin/python

import sys
import os
import unisport
import urllib

try:
    resId = sys.argv[1]
except IndexError as e:
    sys.exit("Parameter missing.")

unisport.init()
unisport.hy_login()

cancelUrl = 'https://unisport.fi/yol/web/fi/crud/update/reservation.json'

params = {'id': resId, 'update': 'cancel'}
data = urllib.urlencode(params)

# print data

result = unisport.br.open(cancelUrl, data)
print result.read()
