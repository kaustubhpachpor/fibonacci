#!/bin/py
'''
About This Script:
This script is a pretty short version of fibonacci sequence. Please be my guest and modify this script or reuse anywhere as per your requirements.

Author: Kaustubh Pachpor
'''
def fib(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b
		b = temp + b
	yield b - temp

for x in fib(20):
	print(x)
