import unittest
from MyStack import MyStack


class TestMyStack(unittest.TestCase):

	def setUp(self):
		print "=========== Running Stack Test ==========="
		self.s = MyStack()
	
	def tearDown(self):
		print "==========================================="

	def test_push_appends(self):
		# Unit test of push command
		self.s.push(1)
		self.assertTrue(self.s.l.pop(), 1)

	def test_pop_removes(self):
		# Unit test of pop command
		self.s.push(1)
		self.s.l.append(1)
		self.assertTrue(self.s.pop(), 1)

	def test_10_elements(self):
		# Comprehensive test, add and remove 10 elements, ensure they are popped in the correct order for a stack
		in_elements = []
		out_elements = []

		for i in range(0,10):
			print "Pushing %d onto stack" % i
			self.s.push(i)
			in_elements.append(i)
		for i in range(0,10):
			popped = self.s.pop()
			out_elements.append(popped)
			print "Popping %d off stack" % popped

		# Reverse out_elements because we expect the opposite order returned off the stack
		out_elements.reverse()
		self.assertEqual(in_elements, out_elements)
		

if __name__ == "__main__":
	unittest.main()
