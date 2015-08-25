class Graph():

	# Dictionary of vertices
	d = {} 

	def addVertex(self, value):
		# Add a vertex with no edges to the graph
		print "Attempting to add vertex with value %d" % value
		if value in self.d:
			print "Vertex already exists"
		else:
			self.d[value] = []

	def addEdge(self, value1, value2):
		# Add an edge between two values in the graph
		print "Attempting to add edge between %d and %d" % (value1, value2)
		if value1 not in self.d or value2 not in self.d:
			print "One or more vertices not found"
		else:
			self.d[value1].append(value2)
			self.d[value2].append(value1)
		
	def findVertex(self, value):
		print "Attempting to find vertex %d" % value
		v = self.d[value]
		if v:
			# For each adjacent vertex, print key
			for a in v:
				print a
		else:
			print "Vertex not found"

if __name__ == "__main__":
	g = Graph()
	g.addVertex(10)
	g.addVertex(20)
	g.addEdge(10,20)
	g.findVertex(20)
	g.findVertex(10)
	g.addVertex(100)
	g.addEdge(20,100)
	g.addEdge(10, 100)
	g.findVertex(100)
