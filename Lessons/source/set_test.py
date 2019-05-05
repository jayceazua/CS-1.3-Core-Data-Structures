from set import HashSet 
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class HashSetTest(unittest.TestCase):
# initializer testing
    def test_init_with_elements(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet()
      assert s.size == 0
      s = HashSet(names)
      assert s.size == 7
      assert (names[0] in s) is True
      assert (names[2] in s) is True
      assert (names[5] in s) is True

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
