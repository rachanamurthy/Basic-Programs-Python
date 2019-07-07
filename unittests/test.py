'''
Outcomes Possible :
  There are three types of possible test outcomes :
    OK – This means that all the tests are passed.
    FAIL – This means that the test did not pass and an AssertionError exception is raised.
    ERROR – This means that the test raises an exception other than AssertionError.
'''
import unittest

from test_exception import test_exception
from test_product import product

class TestStringMethods(unittest.TestCase): 
  def test_product(self): 
    self.assertEqual(product(2,3),6)
  
  def test_isupper(self):         
    self.assertTrue('FOO'.isupper()) 
    self.assertFalse('Foo'.isupper())

  def test_exception_TypeError(self):
  	with self.assertRaises(TypeError):
  		sum('a',1)

  def test_exception_NameError(self):
  	with self.assertRaises(NameError):
  		test_exception()

# This test case would raise 'Error' as the function test_exception() does not have any Syntax Errors
  # def test_exception_SyntaxError(self):
  # 	with self.assertRaises(SyntaxError):
  # 		test_exception()
  
if __name__ == '__main__': 
  unittest.main() 