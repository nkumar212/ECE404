#! /usr/bin/env python

import sys

fd = open(sys.argv[1], "r")

v = fd.read()

aux = {}
for i in v:

	if i.isalpha():

		if i in aux:
			aux[i] += 1
		else:
			aux[i] = 1

	
for j in aux.keys():

	print j + ":" + str(aux[j])


