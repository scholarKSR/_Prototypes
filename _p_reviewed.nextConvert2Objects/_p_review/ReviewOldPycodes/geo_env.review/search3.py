#! /usr/bin/env python3
#Foundations of python network programming
#https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/search3.py

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
	path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
	connection = http.client.HTTPConnection('maps.google.com')
	connection.request('GET',path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
	address = input('address for coordinates: ')
	geocode(address)
