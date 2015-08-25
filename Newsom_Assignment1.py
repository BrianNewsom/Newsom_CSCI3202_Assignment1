print "hello world"

from DataStructures.MyQueue import MyQueue
from DataStructures.BinaryTree import BinaryTree

if __name__ == "__main__":
	bt = BinaryTree()
	bt.add(2,None)
	bt.add(3,2)
	bt.add(4,2)
	bt.add(5,2)
	bt.add(6,4)
	bt.print_tree()

	bt.delete(6)
	bt.print_tree()
	
	bt.delete(3)
	bt.print_tree()
	bt.delete(4)
	bt.print_tree()
	
	bt.delete(2)
	bt.print_tree()
