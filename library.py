#! /usr/bin/env python
def name_input(sentence):
	name = raw_input(sentence)
	if len(name) > 10:
		print "That name is too long. I will give you a nick name."
		return name[0:9]
	else:
		return name

def int_input(sentence):
	number = raw_input(sentence)
	try:
		number = int(number)
		return number	
	except:
		print "Not an int, try again."
		number = int_input(sentence)

def float_input(sentence):
	number = raw_input(sentence)
	try:
		number = float(number)
		return number
	except:
		print "Not a float, try again."
		number = float_input(sentence)