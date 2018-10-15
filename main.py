from room import Room
from character import Enemy, Character
from item import Item
import time


# ___________________________Rooms________________________________________
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

tower= Room("tower")
tower.set_description("stone stairs leading upwards")

tower1= Room("tower level 1")
tower1.set_description("stone stairs leading upwards and downwards")

tower2 =Room("tower level 2")
tower2.set_description("stone stairs leading upwards and downwards")


tower3 =Room("tower level 3")
tower3.set_description("stone stairs leading upwards and downwards")

tower4 =Room("tower level 4")
tower4.set_description("stone stairs leading upwards and downwards")


tower5 =Room("tower level 5")
tower5.set_description("Top of the tower , it is very windy up here, but the view is terrific.")



dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

driveway= Room("Driveway")
driveway.set_description("Gravel driveway")

hall=Room("entrance hall")
hall.set_description(" A large open hall with rooms off and a staircase in the far end")
hall2=Room("entrance hall")
hall2.set_description(" A large open hall with rooms off and a large sweeping staircase leading up")


library=Room("Library")
library.set_description("A large room with books covering all the walls, floor to ceiling")

staircase = Room("Staircase")
staircase.set_description("A staircase sweeping betwwen floors")

landing=Room("Landing")
landing.set_description("A long corridor with bedrooms off at each side")

cellar=Room("Cellar")
cellar.set_description("A dark, damp and smelly cellar. The sound of dripping water can be heard.")

games_room=Room("Games room")
games_room.set_description("A full size snooker table dominates the room")


corridor1=Room("corridor")
corridor1.set_description("A long corridor with rooms off all sides")


corridor2=Room("corridor 2")
corridor2.set_description("A long corridor with rooms off all sides")



corridor3=Room("corridor 3")
corridor3.set_description("A long corridor with rooms off all sides")

secret_passage=Room("secret passage")
secret_passage.set_description("A dark passage")

corridor4=Room("corridor 4")
corridor4.set_description("A long corridor with rooms off all sides")




master_bedroom=Room("Master Bedroom")
master_bedroom.set_description("A four poster bed sits in this bedroom")
# _________________________Room links_________________________________________
kitchen.link_room(hall, "south")
hall.link_room(kitchen, "north")
hall.link_room(driveway,"west")
hall.link_room(dining_hall,"south")
hall.link_room(hall2,"east")
hall2.link_room(hall,"west")
hall2.link_room(staircase,"east")
staircase.link_room(hall2,"west")
hall2.link_room(library,"south")
library.link_room(hall2,"north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
driveway.link_room(hall, "east")
dining_hall.link_room(hall, "north")
staircase.link_room(landing,"east")
landing.link_room(staircase,"west")
kitchen.link_room(cellar,"down")
cellar.link_room(kitchen,"up")
library.link_room(games_room,"south")
games_room.link_room(library,"north")
master_bedroom.link_room(tower,"up")
tower.link_room(master_bedroom,"down")
tower.link_room(tower1,"up")
tower1.link_room(tower,"down")
tower1.link_room(tower2,"up")
tower2.link_room(tower1,"down")
tower2.link_room(tower3,"up")
tower3.link_room(tower2,"down")
tower3.link_room(tower4,"up")
tower4.link_room(tower3,"down")
tower4.link_room(tower5,"up")
tower5.link_room(tower4,"down")
corridor4.link_room(master_bedroom,"south")
master_bedroom.link_room(corridor4,"north")
corridor1.link_room(landing,"west")
landing.link_room(corridor1,"east")
corridor1.link_room(corridor2,"east")
corridor2.link_room(corridor1,"west")
corridor3.link_room(corridor2,"west")
corridor2.link_room(corridor3,"east")
corridor4.link_room(corridor3,"west")
corridor3.link_room(corridor4,"east")
secret_passage.link_room(library,"west")
library.link_room(secret_passage,"east")




# ______________________________Characters__________________________________
ogre = Enemy("Igor", "A smelly Ogre")
ogre.set_conversation("What's up, dude! I'm hungry, maybe I will eat you.")
ogre.set_weakness("sword")
dining_hall.set_character(ogre)


spider = Enemy("A Spider","An enormous black hairy spider with countless eyes and furry legs.")
spider.set_conversation("Sssss....I'm so bored...")
spider.set_weakness("book")
cellar.set_character(spider)

dog = Enemy("Titan", "An enormous slobbering Rottwieler")
dog.set_conversation("Grrrr, Woof Woof.. Grrrrrr")
dog.set_weakness("bone")
landing.set_character(dog)



# ______________________________Items_____________________________________
sword= Item("sword")
sword.set_description("A small silver sword")
sword.set_description2("A small silver sword, that will only do damage to smaller opponents")
games_room.set_item(sword)

book = Item("book")
book.set_description("A heavy book")
book.set_description2("A heavy book, titled 'How to get rid of household pests' ")
library.set_item(book)


key = Item("key")
key.set_description("A brass key")
key.set_description2("A large brass key ")

plant_pot= Item("plant pot")
plant_pot.set_description(" A large plant pot that is too heavy to pick up")
plant_pot.set_description2("The pot is too heavy to lift , but you may be able to move it if you try")
driveway.set_item(plant_pot)


gold_key = Item("gold key")
gold_key.set_description("A gold key")
gold_key.set_description2("A small gold key")
cellar.set_item(gold_key)


bone = Item("bone")
bone.set_description("A big bone.")
bone.set_description2("A big bone, that might tempt an animal that is hungry")
ballroom.set_item(bone)


crossbow= Item("crossbow")
crossbow.set_description("A powerful weapon ")
crossbow.set_description2("A powerful weapon, that would do a lot of damage to an opponent")
tower5.set_item(crossbow)

book_case= Item("Book case")
book_case.set_description("A tall book case containing many books ")
book_case.set_description2("There is one book in the display that looks out of place")
library.set_item(book_case)


# ______________________________MAIN LOOP_____________________________________
#_______________________opening description____________________________
print("You walk up a long gravel drive and arrive outside a grand, imposing house. The house is large and appears to be uninhabited.")
#__________________________________________________________________________
current_room = driveway
backpack = []
commands = ["examine", "move", "get", "take","kill","fight","north","south","east","west","up","down", "inventory","inv", "talk", "open", "unlock"]
dead = False
unlocked = False
while dead == False:
  
  print("\n")
  current_room.get_details()
  
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  item = current_room.get_item()
  if item is not None:
    item.describe()
  
  command = input("> ")
  

  if command in ["north", "south", "east", "west","up", "down"]:
  	# check if door is locked
    if unlocked==False:
      print("The door is locked, you cannot proceed")
    # Move in the given direction
    else:
      current_room = current_room.move(command)
      
     
  elif command == "talk":
    # Talk to the inhabitant - check whether there is one!
    if inhabitant is not None:
      inhabitant.talk()
     
  elif command =="examine":
    item.describe2()
  elif command == "move" and current_room == driveway:
    print("You move the plant pot slightly to reveal a key that was concealed beneath it.")  
    current_room.set_item(key)
    time.sleep(2)
  elif command == "move" and current_room == library:
    print("The book case begins to move and slides accross to reveal a doorway and steps leading down.")  
    time.sleep(2)
  
  elif command == "unlock" or command=="open":
      
      print("What will you unlock it with?")
      open_with = input()    
      # Do I have this item?
      if open_with in backpack:
        unlocked = True
        print("The door is unlocked and open, you may proceed")
      else:
        print("You do not have the key")
  elif command == "commands":
    print("These are the commands you can use: ")
    print (commands[0:17])
 
  elif command =="inventory" or command =="inv":
    print ("you are carrying these items  ")
    print (backpack[0:7])

  elif command == "fight" or command=="kill":
    if inhabitant is not None:
      # Fight with the inhabitant, if there is one
      print("What will you fight with?")
      fight_with = input()
      
      # Do I have this item?
      if fight_with in backpack:
      
        if inhabitant.fight(fight_with) == True:
          # What happens if you win?
          print("Hooray, you won the fight!")
          current_room.character = None
          if inhabitant.get_defeated() == 3:
            print("Congratulations, you have vanquished the enemy horde!")
            dead = True
        else:
          # What happens if you lose?
          print("Oh dear, you lost the fight.")
          print("That's the end of the game")
          dead = True
      else:
        print("You don't have a " + fight_with)
    else:
      print("There is no one here to fight with")
  elif command == "get" or command=="take":
    if item is not None:
      print("You put the " + item.get_name() + " in your backpack")
      backpack.append(item.get_name())
      current_room.set_item(None)
    else:
      print("There's nothing here to get!")
  else:
    print("I don't know how to " + command)
#________________________________________________________________________
