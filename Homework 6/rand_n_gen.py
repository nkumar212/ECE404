#! /usr/bin/env python

from BitVector import *

pcheck = 0
qcheck = 0

ev = BitVector( intVal = 65537 )
pv = BitVector( intVal = 0 )
qv = BitVector( intVal = 0 )

n_found = 0

while( n_found == 0 ):

	if pcheck == 0:
		pv = pv.gen_rand_bits_for_prime(128)
		pcheck = pv.test_for_primality()

	if qcheck == 0:
		qv = qv.gen_rand_bits_for_prime(128)
		qcheck = qv.test_for_primality()

	if (pcheck != 0) and (qcheck != 0):

		n = pv.gf_multiply(qv)
		p = int(pv)
		q = int(qv)
		ptemp = BitVector( intVal = (p-1), size = 128)
		qtemp = BitVector( intVal = (q-1), size = 128)

		if int(ptemp.gcd(ev)) != 1 and int(qtemp.gcd(ev)) != 1:
			
			pcheck = 0
			qcheck = 0
			n_found = 0

		else:

			n_found = 1
			
			print "P: " + str(int(pv))
			print "Q: " + str(int(qv))
			print "N: " + str(int(n))
