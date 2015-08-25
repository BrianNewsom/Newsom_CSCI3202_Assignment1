import unittest
from MyStack import MyStack


class TestMyStack(unittest.TestCase):

	s = MyStack()
	
	print "=========== Running Stack Tests ==========="

	def test_push_appends(self):
		self.s.push(1)
		self.assertTrue(self.s.l.pop(), 1)

	def test_pop_removes(self):
		self.s.l.append(1)
		self.assertTrue(self.s.pop(), 1)

	def test_10_elements(self):
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
