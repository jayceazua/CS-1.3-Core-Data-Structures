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
      print(s.container)
      assert s.size == 7

    def test_init_without_elements(self):
      s = HashSet()
      assert s.size == 0
      assert len(s.container) == 0
# Part 1
    def test_add(self):
      s = HashSet()
      assert s.size == 0
      assert len(s.container) == 0
      s.add("something")
      assert s.size == 1
      self.assertCountEqual(s.container.keys(), ["something"])
      s.add("another")
      assert s.size == 2
      self.assertCountEqual(s.container.keys(), ["something", "another"])

    def test_remove(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet(names)
      assert s.size == 7
      s.remove("Winnie")
      assert s.size == 6
      assert ("Winnie" in s) is False

    def test_contains(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      s = HashSet()
      assert s.size == 0
      s = HashSet(names)
      assert s.size == 7
      assert (names[0] in s) is True
      assert (names[2] in s) is True
      assert (names[5] in s) is True
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
