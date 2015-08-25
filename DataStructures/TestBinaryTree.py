import unittest
from BinaryTree import BinaryTree


class TestBinaryTree(unittest.TestCase):

	b = BinaryTree()
	
	print "=========== Running BinaryTree Tests ==========="

	def test_add_integers_and_print(self):
		self.b.add(1, None)
		self.b.add(2, 1)
		self.b.add(3, 1)
		self.b.add(4, 2)
		self.b.add(5, 2)
		self.b.add(6, 3)
		self.b.add(7, 3)
		self.b.add(8, 4)
		self.b.add(9, 4)
		self.b.add(10, 5)

		self.b.print_tree()
		
	def test_delete_and_print(self):
		self.b.delete(10)
		self.b.delete(8)

		self.b.print_tree()

if __name__ == "__main__":
	unittest.main()
