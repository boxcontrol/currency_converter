# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:22:05 2013

@author: BoxControL (http://boxcontrol.net)
"""


import requests



a = raw_input('Enter currency to convert from?')
a = a.upper()

b = raw_input('Enter currency to convert to?')
b = b.upper()

c = float(raw_input('Enter value to convert?'))

url = ('http://rate-exchange.appspot.com/currency?from=%s&to=%s') % (a, b)
print url

r = requests.get(url)
print r.json()['rate']

print c*r.json()['rate']

urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (a, b)

#split and strip
split1 = (' : 1 %s = ') % a
strip1 = (' %s</h2>') % b

ralt = requests.get(urlalt)
d = float(ralt.text.split(split1)[1].split(strip1)[0].strip()) 
print d

print c * d









