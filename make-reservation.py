#!/usr/bin/python

import sys
import os
import unisport
import urllib

try:
    reservableId = sys.argv[1]
except IndexError as e:
    sys.exit("Parameter missing.")

unisport.init()
unisport.hy_login()

bookingUrl = 'https://unisport.fi/yol/web/fi/crud/create/reservation.json'

params = {'reservableId': reservableId}
data = urllib.urlencode(params)

result = unisport.br.open(bookingUrl, data)
print result.read()
