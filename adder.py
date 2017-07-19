# 8-bit-binary adder
# Author: Rabin Gaire

import sys
import os

def userInput():
	upper_bit_int = int(input("Enter Upper Bit from column: "))
	lower_bit_int= int(input("Enter Lower Bit from column: "))
	upper_bit = [int(x) for x in list('{:08b}'.format(upper_bit_int))]
	lower_bit = [int(x) for x in list('{:08b}'.format(lower_bit_int))]
	return (upper_bit, lower_bit)

def andGate(bitOne, bitTwo):
	return bitOne & bitTwo

def orGate(bitOne, bitTwo):
	return bitOne | bitTwo

def compliment(bitValue):
	return ~bitValue

def xorGate(bitOne, bitTwo):
	return orGate(andGate(bitOne, compliment(bitTwo)), andGate(compliment(bitOne), bitTwo))

def calculateCarry(a, b, c, d):
	return orGate(andGate(a,b), andGate(c,d))

def calculateResult(upper_bit, lower_bit):
	result = []
	carry = 0
	for index in range(len(upper_bit)):
		after_xor_cal = xorGate(upper_bit[index], lower_bit[index])
		result.append(xorGate(after_xor_cal, carry))
		carry = calculateCarry(upper_bit[index], lower_bit[index], after_xor_cal, carry)

	result.append(carry)
	return list(reversed(result))

def main():
	while True:
		upper_bit, lower_bit = userInput()
		result = calculateResult(list(reversed(upper_bit)), list(reversed(lower_bit)))
		print(''.join(str(e) for e in result))

		quit = input("Write q if you want to quit the program: ")
		
		if quit == 'q':
			break


main()
