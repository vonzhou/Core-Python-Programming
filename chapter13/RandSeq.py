
from random import choice

class RandSeq(object):
	def __init__(self,data):
		self.data = data
	def __iter__(self):
		return self
	def next(self):
		return choice(self.data)


for i in range(10):
	print RandSeq(("rock", "paper", "scissors")).next()
