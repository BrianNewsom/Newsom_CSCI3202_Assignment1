# Node class for use in binary tree

class Node:
	def __init__(self, parent, key):
		# Integer key 
		if type(key) is int:
			self.key = key
		else:
			raise TypeError('Please provide an integer key')
		
		# All node links
		self.parent = parent
		self.left = None
		self.right = None

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right

	def setKey(self, key):
		self.key = key

	def setParent(self, parent):
		self.parent = parent