class Operations:
	number_a = 0
	number_b = 0

	def __init__(self, a, b):
		self.number_a = a
		self.number_b = b

	def sum(self):
		return self.number_a+self.number_b

	def sub(self):
		return self.number_a-self.number_b

	def mul(self):
		return self.number_a*self.number_b

	def div(self):
		return self.number_a/self.number_b
