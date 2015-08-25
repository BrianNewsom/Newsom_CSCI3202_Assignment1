import Queue

class MyQueue:

	q = Queue.Queue()
	type_err = TypeError("Sorry, this queue only handles integers, please supply an integer")

	def put(self, item):
		if type(item) is int:
			self.q.put(item)
		else:
			raise type_err
		
	def get(self):
		return self.q.get()
