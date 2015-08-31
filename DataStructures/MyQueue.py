import Queue

class MyQueue:
	# Simply wraps python Queue data structure, enforcing int type

	q = Queue.Queue()
	type_err = TypeError("Sorry, this queue only handles integers, please supply an integer")

	def put(self, item):
		# Add to queue
		if type(item) is int:
			self.q.put(item)
		else:
			raise type_err
		
	def get(self):
		# Get next element in queue and remove it
		return self.q.get()
