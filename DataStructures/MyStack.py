class MyStack:
	# List to store stack
	l = []

	def push(self, item):
		# Add an element to a list
		self.l.append(item)
	
	def pop(self):
		# Remove most recently added element to stack
		return self.l.pop()

	def checkSize(self):
		# Check size of current stack
		return len(self.l)