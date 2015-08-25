class MyStack:
	l = []

	def push(self, item):
		self.l.append(item)
	
	def pop(self):
		return self.l.pop()

	def checkSize(self):
		return len(self.l)