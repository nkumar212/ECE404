#! usr/bin/env python


s0 = ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"]
s1 = ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"]
s2 = ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"]
s3 = ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"]
s4 = ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"]
s5 = ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6s", "cb", "be", "39", "4a", "4c", "58", "cf"]
s6 = ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"]
s7 = ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"]
s8 = ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"]
s9 = ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"]
sa = ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"]
sb = ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"]
sc = ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"]
sd = ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"]
se = ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "cd", "55", "28", "df"]
sf = ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]

sbox = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, sa, sb, sc, sd, se, sf]


def SubBytes(byteArr):

	
	outArr = [][]

	for i in 0 to 3: 
		
		for j in 0 to 3:

			[RBV, CBV] = byteArr[i][j].divide_into_two()

			row = int(RBV)
			col = int(CBV)

			outArr[i][j] = BitVector( hextstring = sbox[row][col] )

	return outArr


def ShiftRows(byteArr)

	out0 = [byteArr[0][0], byteArr[0][1], byteArr[0][2], byteArr[0][3]]
	out1 = [byteArr[1][1], byteArr[1][2], byteArr[1][3], byteArr[1][0]]
	out2 = [byteArr[2][2], byteArr[2][3], byteArr[2][0], byteArr[2][2]]
	out3 = [byteArr[3][3], byteArr[3][0], byteArr[3][1], byteArr[3][2]]

	outArr = [out0, out1, out2, out3]

	return outArr


def MixColumns(byteArr)

	sprime = [][]
	
	temp01 = BitVector( intVal = 01 )
	temp02 = BitVector( intVal = 02 )
	temp03 = BitVector( intVal = 03 )


	for i in 0 to 3:

		sprime[0][i] = (temp02.gf_multiply(byteArr[0][i])) ^ (temp03.gf_multiply(byteArr[1][i])) ^ byteArr[2][i] ^ byteArr[3][i]

		sprime[1][i] = byteArr[0][i] ^ (temp02.gf_multiply(byteArr[1][i])) ^ (temp03.gf_multiply(byteArr[2][i])) ^ byteArr[3][i]

		sprime[2][i] = byteArr[0][i] ^ byteArr[1][i] ^ (temp02.gf_multiply(bitArr[2][i])) ^ (temp03.gf_multiply(bitArr[3][i]))

		sprime[3][i] = (temp03.gf_multiply(bitArr[0][i])) ^ bitArr[1][i] ^ bitArr[2][i] ^ (temp02.gf_multiply(bitArr[3][i]))

	return sprime


def KeyExpansion( key, Nk)

	w = []

	i = 0

	while (i < Nk):
		w[i] = key[4 * i] + key[4*i+1] + key[4*i+2] + key[4*i+3]
		i +=1

	i = Nk

	while (i < Nb * (Nr + 1) ):

		temp = w[i-1]
		if (i % Nk == 0):
			temp = SubWord(RotWord(temp)) ^ Rcon[i/Nk]
		else if (Nk > 6 and i % Nk == 4):
			temp = SubWord(temp)
		w[i] = w[i-Nk] ^ temp
		i += 1


