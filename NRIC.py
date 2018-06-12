#!/usr/bin/python

class Nric(object):

	def __init__(self):
		pass

	def validate(self, nric):
		prefix  = nric[0]
		if prefix.isdigit():
			print "Prefix not provided, assuming it's [S]"
			prefix = 'S'
		nric_digits = ''.join(c for c in nric if c.isdigit())
		while len(nric_digits) < 7:
			print "NRIC not at least 7 digits"
			import random
			nric_digits += str(random.randint(0, 9))
		nric_digits = nric_digits[0:7] # make sure it's only 7 digits
		checksum_digit = self.calculate_checksum(nric_digits)
		suffix = self.lookup_table(prefix, checksum_digit)
		full_valid_nric = prefix + nric_digits + suffix
		if nric.upper() == full_valid_nric:
			return True, full_valid_nric
		else:
			return False, full_valid_nric

	def random(self, prefix = ''):
		import random
		nric = ''
		if not prefix:
			prefix = random.choice(['S', 'T']) 
		while len(nric) < 7:
			nric += str(random.randint(0,9))
		nric_digits = nric[0:7]
		checksum_digit = self.calculate_checksum(nric_digits)
		suffix = self.lookup_table(prefix, checksum_digit)
		full_valid_nric = prefix + nric_digits + suffix
		return full_valid_nric
	
	def calculate_checksum(self, nric_digits):
		sum = 0
		weights = [ 2, 7, 6, 5, 4, 3, 2 ]

		for i, k in zip(weights, nric_digits):
			sum += i * int(k)
		
		checksum_digit = sum % 11
		return checksum_digit
		
	def lookup_table(self, prefix, checksum_digit):
		if prefix in ['S', 's']:
			table = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z', 'J' ]
		elif prefix in ['T', 't']:
			table = [ 'H', 'I', 'Z', 'J', 'A', 'B', 'C', 'D', 'E', 'F', 'G' ]

		checksum_alphabet = table[10 - checksum_digit]
		return checksum_alphabet
