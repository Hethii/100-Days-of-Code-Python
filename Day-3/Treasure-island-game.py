print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
crossroad= input('''You\'re at a crossroad. 
Where do you want to go? Type "left" or "right" ''').lower()
if crossroad == "right":
  lake = input('''You\'ve come to a lake. 
  There is an island in the middle of the lake. 
  Type "wait" to wait for a boat. Type "swim" to swim across. ''').lower()
  if lake == "wait":
    colour = input("""You arrive at the island unharmed. 
    There is a house with 3 doors. One red, 
    one yellow and one blue. Which colour do you choose? """).lower()
    if colour == "red":
      print("You enter a room of beasts. Game Over.")
    elif colour == "blue":
      print("It\'s a room full of fire. Game Over.")
    elif colour == "yellow":
      print("You found the treasure! You Win!" )
    else:
      print("You chose a door that doesn\'t exist. Game Over.")
  else:
    print("You got attacked by an angry trout. Game Over.")
    
else:
  print("You fell into a hole. Game Over.")