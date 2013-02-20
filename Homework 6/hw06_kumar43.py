#! /usr/bin/env python

from BitVector import *

filein = raw_input("Enter input file: ")
fileout = raw_input("Enter output file: ")
mode = raw_input("Encrypt (1) or Decrypt (2): ")

p_temp = raw_input("Enter P: ")
q_temp = raw_input("Enter Q: ")
n_temp = raw_input("Enter N: ")

pv = BitVector( intVal = int(p_temp), size = 128)
qv = BitVector( intVal = int(q_temp), size = 128)
n = BitVector( intVal = int(n_temp), size = 256)

mode = int(mode)

if mode not in [1,2]:
	
	print "Error incorrect mode selected"
	quit()


ev = BitVector( intVal = 65537 )

d = BitVector( size = 0 )

d = ev.multiplicative_inverse(n)


in_bv = BitVector(filename = filein)
zero_bv = BitVector( intVal = 0, size = 128 )
mbv = BitVector(size = 0)
fhdout = open(fileout, 'wb')
mbv_final = BitVector( size = 0 )




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
		
		temp = in_bv.read_bits_from_file( 256 )
	
		
		m = pow(int(temp),int(d), int(n))
		mbv = BitVector( intVal = m, size = 256 )
		mbv_final = mbv[127:255]

		mbv_final.write_to_file( fhdout )





	
