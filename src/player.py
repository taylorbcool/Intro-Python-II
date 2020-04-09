# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, items=None):
    self.name = name
    self.current_room = current_room

    if items is None:
      self.items = []
    else:
      self.items = items