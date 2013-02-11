#! /usr/bin/env python

from BitVector import *

def gen_pseudorand_stream(state):

	i = 0
	j = 0

	while 1:
		
		i = (i + 1) % 256
		j = (j + state[i]) % 256
	
		state[i], state[j] = state[j], state[i]
		rand_byte = (state[i] + state[j]) % 256

		yield rand_byte
		

filein = raw_input("Enter Input Filename: ")
fileout = raw_input("Enter Output Filename: ")
key = raw_input("Enter Key: ")

state = []

for i in range(255):
	state.append(i)

j = 0

for i in range(255):
	j = (j + state[i] + ord(key[i % len(key)]) ) % 256
	state[i], state[j] = state[j], state[i]


fhdout = open(fileout, 'r+b')

stream = BitVector( filename = fhdin )

cipher_byte = BitVector( size = 0 )
random_stream = gen_pseudorand_stream(state)

while (stream.more_to_read):

	byte = stream.read_bits_from_file(8)
	if byte.getsize() > 0:
		
		cipher_byte = byte ^ random_stream.next()
		cipher_byte.write_to_file( fhdout )		
