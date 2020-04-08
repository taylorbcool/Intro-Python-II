# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, desc, items=None):
    self.name = name
    self.desc = desc

    if items is None:
      self.items = []
    else:
      self.items = items
