from set import HashSet 
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class HashSetTest(unittest.TestCase):
# initializer testing
    def test_init_with_elements(self):
      pass

    def test_init_without_elements(self):
      pass
# Part 1
    def test_add(self):
      pass

    def test_remove(self):
      pass

    def test_contains(self):
      pass
# Part 2
    def test_union(self):
      pass

    def test_intersection(self):
      pass

    def test_difference(self):
      pass

    def test_is_subset(self):
      pass


if __name__ == '__main__':
    unittest.main()
