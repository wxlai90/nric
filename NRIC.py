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
		self.nric = ''
		if not prefix:
			prefix = random.choice(['S', 'T']) 
		while len(self.nric) < 7:
			self.nric += str(random.randint(0,9))
		self.nric_digits = self.nric[0:7]
		self.checksum_digit = self.calculate_checksum(self.nric_digits)
		self.suffix = self.lookup_table(prefix, self.checksum_digit)
		self.full_valid_nric = prefix + self.nric_digits + self.suffix
		return self.full_valid_nric
	
	def calculate_checksum(self, nric_digits):
		self.sum = 0
		self.weights = [ 2, 7, 6, 5, 4, 3, 2 ]

		for i, k in zip(self.weights, nric_digits):
			self.sum += i * int(k)
		
		self.checksum_digit = self.sum % 11
		return self.checksum_digit
		
	def lookup_table(self, prefix, checksum_digit):
		if prefix in ['S', 's']:
			self.table = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z', 'J' ]
		elif prefix in ['T', 't']:
			self.table = [ 'H', 'I', 'Z', 'J', 'A', 'B', 'C', 'D', 'E', 'F', 'G' ]

		self.checksum_alphabet = self.table[10 - checksum_digit]
		return self.checksum_alphabet

