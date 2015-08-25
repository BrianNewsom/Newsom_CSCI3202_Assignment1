from Node import Node
# So we can call out BinaryTree print function 'print'
# from __future__ import print_function

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

	def delete(self, value):
		print "Attempting to delete %s" % value
		if not self.delete_recursive(self.root, value):
			print "Node not found"

	def delete_recursive(self, head, value):
		if head is None:
			return False
		
		if head.key is value:
			if head.left is not None or head.right is not None:
				print "Node not deleted, has children"
			else:
				parent = head.parent
				if not parent:
					# if no parent, we don't need to sever any links, only change root
					self.root = None
				else:
					# Otherwise we'll need to delete the ref to the node
					if parent.left and parent.left.key is value:
						parent.left = None
					elif parent.right and parent.right.key is value:
						parent.right = None
				
			return True
		else:
			return self.delete_recursive(head.left, value) or self.delete_recursive(head.right, value)

	def print_tree(self):
		# Can't override python print function, must rename to print_tree
		print "Printing Binary Tree:"
		if self.root:
			self.print_rec(self.root)

	def print_rec(self, head):
		# Perform in order traversal
		print head.key
		if head.left:
			self.print_rec(head.left)
		if head.right:
			self.print_rec(head.right)
		
