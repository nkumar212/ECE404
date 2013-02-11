#! /usr/bin/env python

import sys
from BitVector import *

            

s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,8,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

s7 = [[4,11,2,12,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

s_box = [s1, s2, s3, s4, s5, s6, s7, s8]


expansion_permutation = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0]
P_choice1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
P_choice2 = [13,16,10,23,0,4,2,27,14,5,20,9,22,18,11,3,25,7,15,6,26,19,12,1,40,51,30,36,46,54,29,39,50,44,32,47,43,48,38,55,33,52,45,41,49,35,28,31]
P_box = [15,6,19,20,28,11,27,16,0,14,22,25,4,17,30,9,1,7,23,11,31,26,2,8,18,12,29,5,21,10,3,24]

def get_encryption_key():

	#get key from user
	key = raw_input("Enter Key Filename: ")
	
	#convert key to bitvector
	keybv = BitVector(filename = key)
	keybv1 = keybv.read_bits_from_file( 64 )
	
	return keybv1


def extract_round_key( key ):

	#do initial permutation to convert 64 bits to 56
	r_keybv = key.permute( P_choice1 )
	
	#split 56 bit key into 2 halves and circular rotate each side left
	[LRK, RRK] = r_keybv.divide_into_two()

	LRK.circular_rot_left()
	RRK.circular_rot_left()

	#join two halves
	new_rkeybv = LRK + RRK

	#perform final permutation to get 48 bit round key
	final_rkeybv = new_rkeybv.permute ( P_choice2 )

	
	return final_rkeybv
	

def encrypt():

    #get key from user and then extract the round key.
    key = get_encryption_key()
    round_key = extract_round_key( key )

    #get the filename of the plaintext
    filein1 = raw_input("Enter name of Plaintext File: ")
 
    #convert file to bitvector
    bv = BitVector(filename = filein1)

    encrypted_text = ""	

    #loop through file 64 bits at a time
    while (bv.more_to_read):
        
	bitvec = bv.read_bits_from_file( 64 )
        
	if bitvec.length() == 64:
       
		#loop through 16 rounds for every 64 bit set
		for round_no in range(0,16):
			
			#perform single shift left during rounds 2,9,16
			if round_no in [2,9,16]:

				[temp_l, temp_r] = round_key.divide_into_two()

				temp_l.circular_rot_left()
				temp_r.circular_rot_left()
				
				round_key = temp_l + temp_r

			#perform double shift left during appropriate rounds
			elif round_no in [3,4,5,6,7,8,10,11,12,13,14,15]:

				[temp_l, temp_r] = round_key.divide_into_two()

				temp_l.circular_rot_left()
				temp_r.circular_rot_left()
				temp_l.circular_rot_left()
				temp_r.circular_rot_left()

				round_key = temp_l + temp_r
			
			
			#split 64 bits into right and left halves
			[LE, RE] = bitvec.divide_into_two()

			#expand 32 bits into 48 bits
		        newRE = RE.permute( expansion_permutation )

			#xor right side with round key
	        	out_xor = ( newRE ^ round_key )

			counter = 0
			RE_temp = BitVector(size = 0) 

			#loop through each 48 bit set by groups of 6
			for box in range(0,8):

				#begin s substitution

				#set row equal to the first and last bit of every 6 bit set concatenated
				row = out_xor[counter] + out_xor[counter + 5]
	
				#set column equal to the middle four bits concatenated
				column = out_xor[counter + 1] + out_xor[counter + 2] + out_xor[counter + 3] + out_xor[counter + 4]
	
				#append to empty string till done with 48 bits
				RE_temp += ( BitVector(intVal = (s_box[box][int(row)][int(column)]) , size = 4 ))

				counter += 6

			
			if RE_temp.length() == 32:		
			#convert RE temp back to 32 bits with PBOX permutation
				RE_modified = RE_temp.permute( P_box )
		
			#concatenate the unmodified Right side with the new right side xored with the left side
			bitvec = RE + (RE_modified ^ ( LE ))

			
		encrypted_text = encrypted_text + (str(bitvec))
		
    print encrypted_text

def decrypt():

    #get key from user and then extract the round key.
    key = get_encryption_key()
    round_key = extract_round_key( key )

    #get the filename of the cipherText
    filein = raw_input("Enter name of CipherText File: ")
 
    #convert file to bitvector
    bv = BitVector(filename = filein)

    encrypted_text = ""	

    #loop through file 64 bits at a time
    while (bv.more_to_read):
        
	bitvec = bv.read_bits_from_file( 64 )
        
	if bitvec.length() > 0:
       
		#loop through 16 rounds for every 64 bit set in reverse round from encryption
		for round_no in range(0,16):
			
			
			#split 64 bits into right and left halves
			[LE, RE] = bitvec.divide_into_two()

			#expand 32 bits into 48 bits
		        newRE = RE.permute( expansion_permutation )

			#xor right side with round key
	        	out_xor = ( newRE ^ round_key )

			counter = 0
			#loop through each 48 bit set by groups of 6
			for box in range(0,8):

				#begin s substitution

				#set row equal to the first and last bit of every 6 bit set concatenated
				row = out_xor[counter] + out_xor[counter + 5]
	
				#set column equal to the middle four bits concatenated
				column = out_xor[counter + 1] + out_xor[counter + 2] + out_xor[counter + 3] + out_xor[counter + 4]
	
				#append to empty string till done with 48 bits
				RE_temp.append( BitVector( intVal = (s_box[box][int(row)][int(column)]) , size = 4 ) )

				counter += 6

		
			#convert RE temp back to 32 bits with PBOX permutation
			RE_modified = RE_temp.permute( P_box )
		
			#concatenate the unmodified Right side with the new right side xored with the left side
			bitvec = RE + (RE_modified.bv_xor( LE ))

			#perform single shift left during rounds 2,9,16
			if round_no in [1,2,9,16]:

				[temp_l, temp_r] = round_key.divide_into_two()

				temp_l.circular_rot_right()
				temp_r.circular_rot_right()
				
				round_key = temp_l + temp_r

			#perform double shift left during appropriate rounds
			elif round_no in [3,4,5,6,7,8,10,11,12,13,14,15]:

				[temp_l, temp_r] = round_key.divide_into_two()

				temp_l.circular_rot_right()
				temp_r.circular_rot_right()
				temp_l.circular_rot_right()
				temp_r.circular_rot_right()

				round_key = temp_l + temp_r
		
		encrypted_text = encrypted_text + (str(bitvec))	
    print encrypted_text

#ask user for encryption or decryption
decision = raw_input("selec 1 for Encryption 2 for Decryption :")


if decision == "1":

	encrypt()

elif decision == "2":

	decrypt()

else:
	
	print "Sorry you entered a nonpossible option"





