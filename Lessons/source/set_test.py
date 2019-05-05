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
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = HashSet(names)
        s2 = HashSet(names2)
        assert s1.size == 7
        assert s2.size == 6
        union = s1.union(s2)
        assert union.size == 11

    def test_intersection(self):
      names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
      names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
      s1 = HashSet(names)
      s2 = HashSet(names2)
      assert s1.size == 7
      assert s2.size == 6
      s1_s2_inter = s1.intersection(s2)
      assert s1_s2_inter.size == 2

    def test_difference(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = HashSet(names)
        s2 = HashSet(names2)
        diff1 = s1.difference(s2)
        diff2 = s2.difference(s1)
        assert diff1.size == 5
        assert diff2.size == 4
        

    def test_is_subset(self):
        names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
        names2 = ["Jack", "Jeremy", "Jake", "Jayce", "Julia", "Alex"]
        s1 = HashSet(names)
        s2 = HashSet(names2)
        assert s1.size == 7
        assert s2.size == 6
        union = s1.union(s2)
        assert union.size == 11
        assert s1.is_subset(union) is True
        assert s2.is_subset(union) is True
        names3 = ["this", "that", "thing"]
        s3 = HashSet(names3)
        assert s3.is_subset(union) is False


if __name__ == '__main__':
    unittest.main()
