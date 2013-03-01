#! /usr/bin/env python

def chinese_rem(p, q, c, d, n):

	pv = BitVector(intVal = p)
	qv = BitVector(intVal = q)
	vp = pow(c,d,p)
	vq = pow(c,d,q)

	xp = int(qv) * int(qv.multiplicative_inverse(pv))
	xq = int(pv) * int(pv.multiplicative_inverse(qv))

	rem = ( (vp*xp) + (vq*xq) ) % 128 

	return rem

from BitVector import *

filein = raw_input("Enter input file: ")
fileout = raw_input("Enter output file: ")
mode = raw_input("Encrypt (1) or Decrypt (2): ")

p_temp = raw_input("Enter P: ")
q_temp = raw_input("Enter Q: ")
n_temp = int(p_temp) * int(q_temp)

pv = BitVector( intVal = int(p_temp), size = 128)
qv = BitVector( intVal = int(q_temp), size = 128)
n = BitVector( intVal = int(n_temp), size = 256)

mode = int(mode)

if mode not in [1,2]:
	
	print "Error incorrect mode selected"
	quit()


ev = BitVector( intVal = 65537 )

d = BitVector( size = 0 )
ttotient = (int(pv) - 1) * (int(qv) - 1)
totient = BitVector( intVal = ttotient )
d = ev.multiplicative_inverse(totient)


in_bv = BitVector(filename = filein)
zero_bv = BitVector( intVal = 0, size = 128 )
mbv = BitVector(size = 0)
fhdout = open(fileout, 'wb')
mbv_final = BitVector( size = 0 )


print chinese_rem(61,53,2790,2753,3233)

if mode == 1:
	
	while(in_bv.more_to_read):
	
		temp = in_bv.read_bits_from_file( 128 )
		if len(temp) > 0:
		
			if len(temp) < 128:
			
				missingZ = 128 - len(temp)

				filler = BitVector( intVal = 0, size = missingZ )

				mbv = zero_bv + filler + temp
					
			else:
			
				mbv = zero_bv + temp

			print(mbv)
	
			c = pow(int(mbv), int(ev), int(n))
			cbv = BitVector( intVal = c, size = 256)

			cbv.write_to_file( fhdout )
else:

	while(in_bv.more_to_read):
		
		temp = in_bv.read_bits_from_file( 128 )
		if len(temp) > 0:	
			
			mbv = chinese_rem(int(pv), int(qv), int(temp), int(d), int(n))

		
			mbv_temp = BitVector( intVal = mbv )

			print(mbv_temp)
			print " "

			mbv_final = mbv_temp
			mbv_final.write_to_file( fhdout )





	
