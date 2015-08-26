import unittest
from Graph import Graph


class TestGraph(unittest.TestCase):

	
	def setUp(self):
		print "=========== Running Graph Test ==========="
		self.g = Graph()

	def tearDown(self):
		print "==========================================="

	def test_add_vertices_and_edges(self):
		# Create graph with 10 vertices and 20 edges, then find 5 vertices and print their neighbors
		g = self.g
		for i in range(1,11):
			g.addVertex(i)
		for i in range(1,6):
			g.addEdge(i, 2*i)
			g.addEdge(i+1, 2*i - 1)
			g.addEdge(i+2, 2*i)
			g.addEdge(i, i+1)
		for i in range(1,6):
			g.findVertex(i)
		
	def test_add_vertex_adds_to_dict(self):
		# Add vertex then ensure it is added to the underlying dictionary
		g = self.g
		g.addVertex(1)
		self.assertEqual(g.d[1], [])

	def test_add_vertex_then_edge_creates_bidirectional_edges(self):
		# Add vertices and edge then make sure the edges are created in both vertices lists
		g = self.g
		g.addVertex(1)
		g.addVertex(2)
		g.addEdge(1,2)
		self.assertEqual(g.d[1], [2])
		self.assertEqual(g.d[2], [1])

if __name__ == "__main__":
	unittest.main()
