import unittest
from MyQueue import MyQueue


class TestMyQueue(unittest.TestCase):

	q = MyQueue()
	
	print "=========== Running Queue Tests ==========="

	def test_non_integer_raises_exception(self):
		with self.assertRaises(Exception) as context:
			self.q.put("a")
		self.assertTrue(context.exception)

	def test_single_put_and_get(self):
		self.q.put(1)
		self.assertEqual(self.q.get(),1)

	def test_10_elements(self):
		in_elements = []
		out_elements = []
		
		for i in range(0,10):
			print "Putting %d in queue" % i
			self.q.put(i)
			in_elements.append(i)
		for i in range(0,10):
			print "Popping %d from queue" % self.q.get()
			out_elements.append(i)
		self.assertEqual(in_elements, out_elements)
	
class TestMyStack(unittest.TestCase):

	def test(self):
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()
