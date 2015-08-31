# Newsom_CSCI3202_Assignment1
## Brian Newsom
Homework assignment one for CSCI 3202 at CU Boulder

### To Run Tests (Using Python UnitTest Framework):
```
python Newsom_Assignment1.py
```

The Newsom_Assignment1 file simply imports all datastructures test files and runs them using the 
python unittest built-in library. These should run and pass without any additional installation, etc.
All tests proposed in the pdf are included, and should be clear from the printing, though in the code
these are commented as the comprehensive (or integration-like) tests.  Additional tests are added to further
test the features of the data structures.

For further information on the unit tests, see the documentation for built in Python UnitTest Framework at [https://docs.python.org/2/library/unittest.html](https://docs.python.org/2/library/unittest.html).

In order to use the data structures in a non-test environment, simply import all non test files inside of the DataStructures
directory. e.g.
```
from DataStructures.MyStack import MyStack
```

MyStack can now be used as expected, initialized as s = MyStack()

