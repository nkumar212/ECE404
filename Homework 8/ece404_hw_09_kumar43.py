#! /usr/bin/env python

import sys
from scapy import *
import socket


def port_check(addr, port):

	

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((addr,port))

		return 1

	except socket.error, (message, value): 

		return 0

	except socket.timeout:

		return 0



host = raw_input("Enter Host name: ")
start = raw_input("Enter starting port: ")
end = raw_input("Enter Ending port: ")

for i in range(int(start), int(end)):

	check = port_check(host, i)

	if check == 1:

		print str(i),

