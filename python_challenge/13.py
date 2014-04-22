#!/usr/bin/env python

import xmlrpclib

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(server.phone('Bert'))
