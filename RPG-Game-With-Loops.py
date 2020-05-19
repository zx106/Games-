# RPG
# User random to create attributes for your character and the computer's character
# Strength: 1 - 20
# Intelligence: 1 - 10
# Magic: 1 - 30
# Have the user choose Fight, Steal, or Magic
# The stronger character wins a fight
# The smarter character can steal from the other
# The more magical character can defeat the other 
import os
import random

# User attributes
user_health = 100
user_strength = 0
user_intelligence = 0
user_magic = 0

# Computer attributes
computer_health = 100
computer_strength = 0
computer_intelligence = 0
computer_magic = 0

# Define your functions here
def print_header():
    print("""
  _         _             _     _   _    
 | |   __ _| |__ _  _ _ _(_)_ _| |_| |_  
 | |__/ _` | '_ \ || | '_| | ' \  _| ' \ 
 |____\__,_|_.__/\_, |_| |_|_||_\__|_||_|
                 |__/        
Welcome to the Labyrinth...prepare to die!             
    """)

# generate_stats():
# Careful with global and local variables
def generate_stats():
    global user_strength
    global user_intelligence
    global user_magic
    # Generate user stats
    user_strength = random.randint(1, 20)
    user_intelligence = random.randint(1, 10)
    user_magic = random.randint(1, 30)

    global computer_strength
    global computer_intelligence
    global computer_magic
    # Generate computer stats
    computer_strength = random.randint(1, 20)
    computer_intelligence = random.randint(1, 10)
    computer_magic = random.randint(1, 30)

# print_fight_type(type):
# Type should be F, S, or M
def print_fight_type(type):
    type = type.upper()
    if type == "F":
        print("""
    ___________ ____________  
    |           )._______.-'
    `----------'
    You decide to fight with your knife...
    """)
    
    elif type == "S":
        print("""
     {O-
    //\\===+-
     \\
      ))
     ||
     You decide to steal from this vagabond...
    """)
    
    elif type == "M":
        print("""
           *
         *   *
       *  \\\\* / *
       * --.:. *
      *   * :\\\\ -
        .*  | \\\\
               \\\\
                \\\\ 
    You decide to use your magic to fight...
    """)
  
# print_type_result(type):
# Type result should be F, S, or M
def print_fight_result(type):
    global computer_health 
    global user_health 
    type = type.upper()
    if user_choice == "F":
        if user_strength > computer_strength:
            print("You win the fight!")
            computer_health -= 20
        else:
            print("You fight well, but ultimately lose.")
            user_health -= 20

    elif user_choice == "S":
        if user_intelligence > computer_intelligence:
            print("You steal the Jewel of Power and weaken your enemy.")
            computer_health -= 10
        else:
            print("You fail...and are lightly injured.")
            user_health -= 10
    
    elif user_choice == "M":
        if user_magic > computer_magic:
            print("You cast a spell and injure your enemy!")
            computer_health -= 30
        else:
            print("Your enemy turns your spell against you...you feel undescribable pain!")
            user_health -= 30
            
    else:
        print("That was not one of the choices.")
# print_stats():
def print_stats():

    print("")
    print("User Stats")
    print("Strength: " + str(user_strength))
    print("Intelligence: " + str(user_intelligence))
    print("Magic: " + str(user_magic))
    print("Health: " + str(user_health))

    print("")
    print("Computer Stats")
    print("Strength: " + str(computer_strength))
    print("Intelligence: " + str(computer_intelligence))
    print("Magic: " + str(computer_magic))
    print("Health: " + str(computer_health))
    
# is_player_dead():
# Should return True if player_health <= 0
# Else return False
def is_player_dead(): 
    if user_health <= 0:
        print("Your enemy finally defeats you - you are dead!")
        return True 
    else: 
        return False 
    
# is_computer_dead():
# Should return True if computer_health <= 0
# Else return False
def is_computer_dead(): 
    if computer_health <= 0:
        print("You finally defeat your enemy - he dies cursing your name!")
        return True 
    else: 
        return False 

while True:
    os.system("clear")
    generate_stats()

    # Header
    print_header()
    
    # Choose which type of battle: (F)ight, (S)teal, (M)agic
    user_choice = input("What type of battle? (F)ight, (S)teal, (M)agic > ").upper()
    print_fight_type(user_choice)
    
    # Determine the winner
    print_fight_result(user_choice) 
    
    # Print stats
    print_stats()
    
    # Check for player death
    is_player_dead() 
    is_computer_dead() 
    
    # Ask for a replay    
    if computer_health < 0 or user_health < 0:
        choice = input("Please type (Y)es to replay, or (N)o to finish. > ")
        if replay == "Y":
            user_health = 100
            computer_health = 100
            continue
        else:
            break
            
    delay = input("Press enter to continue. ") 
            
     

    
