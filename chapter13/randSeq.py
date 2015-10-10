
from random import choice

class RandSeq(object):
	def __init__(self,data):
		self.data = data
	def __iter__(self):
		return self
	def next(self):
		return choice(self.data)

for item in RandSeq(("rock", "paper", "scissors")):
	print item
