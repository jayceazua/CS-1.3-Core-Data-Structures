from hashtable import HashTable

class HashSet (object):
  # initializer 
  def __init__(self, elements=None):
    self.elements = HashTable()
    self.size = 0
    if elements == None:
      for key, value in elements:
        self.size += self.elements.add(key, value)

  def __iter__(self):
    pass
  def get_elements(self):
    pass
  def length(self):
    pass
  def contains(self, element):
    pass
  def add(self, element):
    pass
  def remove(self, element):
    pass
  def union(self, other_set):
    pass
  def intersection(self, other_set):
    pass
  def difference(self, other_set):
    pass
  def is_subset(self, other_set):
    pass


if __name__ == "__main__":
  pass
