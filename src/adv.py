from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
  'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

  'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

  'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

  'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

  'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('What is your name?\n'), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

''' 
when there is no input, command will be an empty string inside a list
command will have 1 arg for movement and 2 args for interacting with items so it's necessary to make command a list
'''
command = ['']


while command[0] != 'q':
  print(f'\n*** {player.current_room.name} ***')
  print(f'{player.current_room.desc}')

  if len(player.current_room.items) > 0:
    print(f'\nThis room contains {player.current_room.items}')

  command = input('\nCommands:\nMove: [n]orth, [s]outh, [e]ast, [w]est\nPick up item: [take item_name]\nDrop item: [drop item_name]\nOpen inventory: [i] or [inventory]\nQuit game: [q]\n').split() 
  # ^^^^^ splitting this input(hopefully) puts the commands into list form for when items are added

  if len(command) < 2:
    if command[0] == 'n':
      try:
        player.current_room = player.current_room.n_to
      except AttributeError:
        print("\nYou can't go north")

    elif command[0] == 's':
      try:
        player.current_room = player.current_room.s_to
      except AttributeError:
        print("\nYou can't go south")

    elif command[0] == 'e':
      try:
        player.current_room = player.current_room.e_to
      except AttributeError:
        print("\nYou can't go east")

    elif command[0] == 'w':
      try:
        player.current_room = player.current_room.w_to
      except AttributeError:
        print("\nYou can't go west")

    elif command[0] == 'i' or 'inventory':
      if len(player.items) > 0:
        print(f"{player.name}'s items':\n{str(player.items)}")
      # elif len(player.items) == 0:
      #   print("You're not carrying anything!")

    elif command[0] != 'q':
      print('\ninvalid command')

  elif len(command) == 2:
    if command[0] == 'take':
      if command[1] in player.current_room.items == True:
        try:
          player.items.append(command[1])
          player.current_room.items.remove(command[1])
          command[1].on_take()
        except:
          print("\nYou can't pick that up.")
      else:
        print("\nNo item here by that name.")
    
    elif command[0] == 'drop':
      if command[1] in  player.items == True:
        try:
          player.items.remove(command[1])
          player.current_room.items.append(command[1])
          command[1].on_drop()
        except:
          print("\nYou can't drop that.")
      else:
        print("\nYou don't have that item to drop!")

    elif command[0] != 'q':
      print('\ninvalid command')