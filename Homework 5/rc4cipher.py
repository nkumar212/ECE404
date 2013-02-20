#! /usr/bin/env python

from BitVector import *
import wave

#create gen function that returns next iteration of loop evertime .next() is called
#every iteration of loop is the pseudo random byte generated from the state vector

def gen_pseudorand_stream(state):

	i = 0
	j = 0

	while 1:
		
		i = (i + 1) % 256
		j = (j + state[i]) % 256
	
		state[i], state[j] = state[j], state[i]
		rand_byte = (state[i] + state[j]) % 256

		yield rand_byte
		
#get key , and in/out filenames from the user
filein = raw_input("Enter Input Filename: ")
fileout = raw_input("Enter Output Filename: ")
key = raw_input("Enter Key: ")

#create state vector
state = []

#initially fill state vector with corresponding hash value
for i in range(256):
	state.append(i)

j = 0

#permute the state vector with the key input by the user.
for i in range(256):
	j = (j + state[i] + ord(key[i % len(key)]) ) % 256
	state[i], state[j] = state[j], state[i]


#create output variables and open files for reading/writing
fhdout = wave.open(fileout, 'w')
output = "" 
outframe = []
wfile = wave.open(filein,'r')

#set parameters for outputfile
fhdout.setparams(wfile.getparams())

# "seed" gen function with they permuted state array
random_stream = gen_pseudorand_stream(state)

#read wave file frame by frame
for i in range(wfile.getnframes()):
	
	wframe = wfile.readframes(1)
	
	#take each byte from each frame, xor it with pseudo random byte and append to output string
	for j in range(len(wframe)):

		wbyte = ord(wframe[j])
		output += chr(wbyte ^ random_stream.next())	
		


#write output string to wave file.
fhdout.writeframes( output )

fhdout.close()
wfile.close()
