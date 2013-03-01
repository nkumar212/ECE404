#!/usr/bin/env python
## sha1_from_command_line.py
## by Avi Kak (kak@purdue.edu)
## Feb 19, 2013
## Call syntax:
##
## sha1_from_command_line.py string_to_be_hashed
## This script takes its message on the standard input from
## the command line and sends the hash to its standard
## output. NOTE: IT ADDS A NESWLINE AT THE END OF THE OUTPUT
## TO SHOW THE HASHCODE IN A LINE BY ITSELF.
import sys
import BitVector
from BitVector import *

def sig0( x ):

	x_copy = x.deep_copy()
		
	val = (x_copy >> 1) ^ (x_copy >> 8) ^ (x_copy.shift_right(7))
	
	return val

def sig1( x ):

	x_copy = x.deep_copy()

	val = (x_copy >> 19) ^ (x_copy >> 61) ^ (x_copy.shift_right(6))

	return val


k = ['428a2f98d728ae22', '7137449123ef65cd', 'b5c0fbcfec4d3b2f', 'e9b5dba58189dbbc','3956c25bf348b538', '59f111f1b605d019', '923f82a4af194f9b', 'ab1c5ed5da6d8118', 'd807aa98a3030242', '12835b0145706fbe', '243185be4ee4b28c', '550c7dc3d5ffb4e2','72be5d74f27b896f', '80deb1fe3b1696b1', '9bdc06a725c71235', 'c19bf174cf692694', 'e49b69c19ef14ad2', 'efbe4786384f25e3', '0fc19dc68b8cd5b5', '240ca1cc77ac9c65','2de92c6f592b0275', '4a7484aa6ea6e483', '5cb0a9dcbd41fbd4', '76f988da831153b5', '983e5152ee66dfab', 'a831c66d2db43210', 'b00327c898fb213f', 'bf597fc7beef0ee4','c6e00bf33da88fc2', 'd5a79147930aa725', '06ca6351e003826f', '142929670a0e6e70', '27b70a8546d22ffc', '2e1b21385c26c926', '4d2c6dfc5ac42aed', '53380d139d95b3df','650a73548baf63de', '766a0abb3c77b2a8', '81c2c92e47edaee6', '92722c851482353b', 'a2bfe8a14cf10364', 'a81a664bbc423001', 'c24b8b70d0f89791', 'c76c51a30654be30','d192e819d6ef5218', 'd69906245565a910', 'f40e35855771202a', '106aa07032bbd1b8', '19a4c116b8d2d0c8', '1e376c085141ab53', '2748774cdf8eeb99', '34b0bcb5e19b48a8','391c0cb3c5c95a63', '4ed8aa4ae3418acb', '5b9cca4f7763e373', '682e6ff3d6b2b8a3', '748f82ee5defb2fc', '78a5636f43172f60', '84c87814a1f0ab72', '8cc702081a6439ec','90befffa23631e28', 'a4506cebde82bde9', 'bef9a3f7b2c67915', 'c67178f2e372532b', 'ca273eceea26619c', 'd186b8c721c0c207', 'eada7dd6cde0eb1e', 'f57d4f7fee6ed178','06f067aa72176fba', '0a637dc5a2c898a6', '113f9804bef90dae', '1b710b35131c471b', '28db77f523047d84', '32caab7b40c72493', '3c9ebe0a15c9bebc', '431d67c49c100d4c','4cc5d4becb3e42b6', '597f299cfc657e2a', '5fcb6fab3ad6faec', '6c44198c4a475817']


# Initialize hashcode for the first block. Subsequetnly, the
# output for each 512-bit block of the input message becomes
# the hashcode for the next block of the message.

h0 = BitVector(hexstring= '6a09e667f3bcc908')
h1 = BitVector(hexstring= 'bb67ae8584caa73b')
h2 = BitVector(hexstring= '3c6ef372fe94f82b')
h3 = BitVector(hexstring= 'a54ff53a5f1d36f1')
h4 = BitVector(hexstring= '510e527fade682d1')
h5 = BitVector(hexstring= '9b05688c2b3e6c1f')
h6 = BitVector(hexstring= '1f83d9abfb41bd6b')
h7 = BitVector(hexstring= '5be0cd19137e2179')


filein = raw_input('Enter Input Filename: ')
fileout = raw_input('Enter Output Filename: ')

inbv = BitVector(filename = filein)
bv = BitVector( size = 0 )

counter = 0

while(inbv.more_to_read):

	messagebv = inbv.read_bits_from_file(1024)
	bv += messagebv



length = bv.length()
bv1 = bv + BitVector(bitstring="1")
length1 = bv1.length()
howmanyzeros = (896 - length1) % 1024
zerolist = [0] * howmanyzeros

bv2 = bv1 + BitVector(bitlist = zerolist)
bv3 = BitVector(intVal = length, size = 128)
bv4 = bv2 + bv3

words = [None] * 80

for n in range(0,bv4.length(),1024):
	block = bv4[n:n+1024]
	words[0:16] = [block[i:i+64] for i in range(0,1024,64)]
	for i in range(16, 80):
		words[i] = BitVector( intVal = ((int(words[i-16]) + int(sig0(words[i-15])) + int(words[i-7]) + int(sig1(words[i-1]))) % 64), size = 64)	
		a,b,c,d,e,f,g,h = h0,h1,h2,h3,h4,h5,h6,h7
	for i in range(80):

		a_copy = a.deep_copy()
		e_copy = e.deep_copy()
		
		chefg = (e & f) ^ (~e & g)
		majabc = (a & b) ^ (a & c) ^ (b & c)

		sigA = (a_copy >> 28) ^ (a_copy >> 34) ^ (a_copy >> 39)
		sigE = (e_copy >> 14) ^ (e_copy >> 18) ^ (e_copy >> 41)

		T1 = BitVector( intVal = ((int(h) + int(chefg) + int(sigE) + int(words[i]) + int(BitVector(hexstring = k[i]))) % 64) , size = 64)
		T2 = BitVector( intVal = ((int(sigA) + int(majabc)) % 64), size = 64)

		h = g
		g = f
		f = e
		e = BitVector( intVal = ((int(d) + int(T1)) % 64), size = 64)
		d = c
		c = b
		b = a
		a = BitVector( intVal = ((int(T1) + int(T2)) % 64), size = 64)	

	h0 = BitVector( intVal = (int(h0) + int(a)) % (64), size = 64 )
	h1 = BitVector( intVal = (int(h1) + int(b)) % (64), size = 64 )
	h2 = BitVector( intVal = (int(h2) + int(c)) % (64), size = 64 )
	h3 = BitVector( intVal = (int(h3) + int(d)) % (64), size = 64 )
	h4 = BitVector( intVal = (int(h4) + int(e)) % (64), size = 64 )
	h5 = BitVector( intVal = (int(h5) + int(f)) % (64), size = 64 )
	h6 = BitVector( intVal = (int(h6) + int(g)) % (64), size = 64 )
	h7 = BitVector( intVal = (int(h7) + int(h)) % (64), size = 64 ) 

message_hash = h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7

fhd = open( fileout, 'wb' )

hash_hex_string = message_hash.getHexStringFromBitVector()
fhd.write(hash_hex_string)

fhd.close()
