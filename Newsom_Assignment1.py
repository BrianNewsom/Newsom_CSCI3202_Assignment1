# Main file running all tests/drivers for CSCI 3202 Assignment 1

import unittest
# Import as to enforce ordering in printing
from DataStructures.TestMyQueue import TestMyQueue as Test01
from DataStructures.TestMyStack import TestMyStack as Test02
from DataStructures.TestBinaryTree import TestBinaryTree as Test03
from DataStructures.TestGraph import TestGraph as Test04 

if __name__ == "__main__":
	unittest.main()