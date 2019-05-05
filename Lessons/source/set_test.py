from set import HashSet 
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class HashSetTest(unittest.TestCase):
# initializer testing
    def test_init_with_elements(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet(names)
      assert s.size == 7
      assert s.contains("Kojin") == True

    def test_init_without_elements(self):
      s = HashSet()
      assert s.size == 0
      assert len(s.container) == 0
# Part 1
    def test_add(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet(names)
      assert s.size == 7
      s.add("Katherine")
      assert s.size == 8
      assert s.contains("Katherine") == True
      

    def test_remove(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet(names)
      assert s.size == 7
      assert s.contains("Nabil") == True
      s.remove("Nabil")
      assert s.size == 6
      assert s.contains("Nabil") == False

    def test_contains(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet()
      assert s.size == 0
      s = HashSet(names)
      assert s.size == 7
      assert s.contains("Alex") == True
      assert s.contains("Jose") ==  False

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
