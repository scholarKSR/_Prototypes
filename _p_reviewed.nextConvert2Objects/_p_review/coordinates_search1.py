#! /usr/bin/env python3
#Foundations of python network programming
#https://github.com/brandon-rhodes/

from pygeocoder import Geocoder

if __name__ == '__main__':
	address = '207 N. Defiance St, Archbold, OH'
	print(Geocoder.geocode(address)[0].coordinates)

