# Contest between runners
# Runners have 2 attributes
# Speed (1 - 20)
# Stamina (1 - 30)
# Attributes are determined randomly
# The user chooses (S)hort Distance, or (L)ong Distance
# The user with the best speed wins a short distance race
# The user with more stamina wins a long distance race
# Whoever gets 3 wins first is the overall winner
# The stats will change each time
import os
import random
import time 

while True: 
    os.system("clear")

    print("Welcome to the Track and Field game!")
    user_choice = input("Please choose (S)hort Distance or (L)ong Distance. If you get to win first 3 round, teh computer lose. > ").upper()
# Generate User Stats
    user_speed = random.randint(1,20)
    user_stamina = random.randint(1, 30)

# Generate Computer Stats
    computer_speed = random.randint(1,20)
    computer_stamina = random.randint(1,30)

    
# User decides the type of challenge
    user_wins = 0 
    computer_wins = 0 
    
    
    # Determine the winner
    
    if user_choice == "S":
        if user_speed > computer_speed:	
            print("You win the game.")
            user_wins += 1
             
        else:
            computer_wins += 1 
            print("The computer wins the game.")
            
    elif user_choice == "L":
	    if user_stamina > computer_stamina:
	        print("You win the game.")
	        user_wins += 1
	    else:
		    computer_wins += 1
		    print("The computer wins the game.")

    else:
        print("That was not an option.")

    
    if user_wins == 3 or computer_wins == 3: 
    
        extra = input("Would you like to play it again. (Y)es or (N)o? > ") 
        if extra == "Y":
            computer_wins == 0 
            user_wins == 0
            continue  
        else:  
            print("Goodbye!")
            exit()
            
   
       

# Print stats
    print("")
    print("""User stats
User speed: {}
User stamina: {}""".format(user_speed, user_stamina))

    print("")
    print("""Computer stats
Computer speed: {}
Computer stamina: {}""".format(computer_speed, computer_stamina))

    delay = input("Press ENTER to exit. ")		