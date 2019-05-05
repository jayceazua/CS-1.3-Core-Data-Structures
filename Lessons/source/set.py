from hashtable import HashTable

class HashSet (object):
  # initializer 
  def __init__(self, elements=None):
    self.container = HashTable()
    self.size = self.container.size
    if elements is not None:
      for item in elements:
        self.add(item)

  def __str__(self):
    """Return a formatted string representation of this hash table."""
    items = ["{!r}".format(key) for key, _ in self.container.items()]
    return "{" + ", ".join(items) + "}"

# Part 1
  def add(self, element):
    if self.contains(element):
      raise ValueError("Element already exist")
    self.size += 1
    self.container.set(element, None)

  def remove(self, element):
    if self.size == 0:
      raise ValueError("Nothing to remove, set is empty")
    self.size -= 1
    self.container.delete(element)

  def contains(self, element):
    return self.container.contains(element)
# Part 2
  def union(self, other_set):
    pass
  def intersection(self, other_set):
    pass
  def difference(self, other_set):
    pass
  def is_subset(self, other_set):
    pass


if __name__ == "__main__":
  names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
  s = HashSet(names)
  
