#! /usr/bin/env python

from BitVector import *
import wave

w = wave.open('test1.wav','r')
for i in range(w.getnframes()):
	frame = w.readframes(1)
	
	for i in range(len(frame)):

		print ord(frame[i])
