from hashtable import HashTable

class HashSet (object):
  # initializer 
  def __init__(self, elements=None):
    self.container = HashTable()
    self.size = self.container.size
    if elements is not None:
      print(elements)
      for item in elements:
        self.size += 1
        self.container.set(item, None)

  def __str__(self):
    """Return a formatted string representation of this hash table."""
    items = ["{!r}".format(key) for key, _ in self.container.items()]
    return "{" + ", ".join(items) + "}

  def __iter__(self):
    return self.container.__iter__()
# Part 1
  def add(self, element):
    if self.contains(element):
      raise ValueError("Element already exist")
    self.size += 1
    self.container.set(element, None)

  def remove(self, element):
    if self.contains(element):
      self.size -= 1
      self.container.delete(element)
    raise ValueError("Element does not exist")

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
  pass
