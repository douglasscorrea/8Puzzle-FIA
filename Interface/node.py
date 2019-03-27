class Node():
	def __init__(self, upper, value):
		self.upper = upper
		self.value = value
		self.lowers = []

	def get_lowers(self):
		return self.lowers

	def append_lower(self, node):
		self.lowers.append(node)

	def get_upper(self):
		return self.upper

	def set_uppers(self, node):
		self.upper = node

	def set_value(self, value):
		self.value = value

	def get_value(self):
		return self.value