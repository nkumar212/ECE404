#! /usr/bin/env python

from BitVector import *
import timeit

def euclid_gcd(n1, n2):

	if n1 < n2:
		n1,n2 = n2, n1

	while n2 != 0:
		n1,n2 = n2, n1%n2

	return n1


def stein_gcd(n1, n2):

	if n1 == n2:
		return n1

	if (n1 == 0) and (n2 == 0):
		return 0
	
	if n1 == 0:
		return n2

	if n2 == 0:
		return n1

	if ((n1%2) == 0) and ((n2%2) == 0):
		return (stein_gcd(n1/2, n2/2) * 2)

	if ((n1%2) == 0) and ((n2%2) == 1):
		return (stein_gcd(n1/2, n2))

	if ((n1%2) == 1) and ((n2%2) == 0):
		return (stein_gcd(n1, n2/2))

	if ((n1%2) == 1) and ((n2%2) == 1):
		if n1 >= n2:
			return stein_gcd((n1-n2)/2, n2)
		else:
			return stein_gcd((n2-n1)/2, n1)


