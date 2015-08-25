from Node import Node

class BinaryTree:
	root = None

	def add_recursive(self, head, value, parent_value):
		# Returns true if parent value is found and false if not
		if head is None:
			return False

		if head.key is parent_value:
			# We've found a match, handle
			if head.left is None and head.right is None:
				head.left = Node(head, value)
			elif head.left is not None and head.right is None:
				head.right = Node(head, value)
			elif head.left is not None and head.right is not None:
				print "Parent has two children, node not added"
			else: 
				print "Case not matched :/"
			return True 
		else:
			# If we didn't match on the head, recurse down both sides of the tree
			return self.add_recursive(head.left, value, parent_value) or self.add_recursive(head.right, value, parent_value)

	def add(self, value, parent_value):
		print "Attempting to add %s under %s" % (value, parent_value)
		if self.root is None:
			self.root = Node(None, value)
		else:
			if not self.add_recursive(self.root, value, parent_value):
				print "Parent not found"

