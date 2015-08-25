import unittest
from MyQueue import MyQueue


class TestMyQueue(unittest.TestCase):

	
	def setUp(self):
		print "=========== Running Queue Test ==========="
		self.q = MyQueue()
	
	def tearDown(self):
		print "==========================================="

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
			popped = self.q.get()
			out_elements.append(popped)
			print "Popping %d from queue" % popped

		self.assertEqual(in_elements, out_elements)
	
if __name__ == "__main__":
	unittest.main()
