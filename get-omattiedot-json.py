#!/usr/bin/python

import unisport
import urllib

unisport.init()
unisport.hy_login()

# -----

jsonFile = unisport.br.open('https://unisport.fi/yol/web/fi/crud/read/user.json?id=authenticated')
print jsonFile.read()
