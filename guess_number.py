import os 
import random 
os.system("clear") 

while True:

    print("""
You can choose from 3 levels.
(E)asy: You guess on 3 digits. You could try 5 times.
(M)iddle: You guess on 4 digits. You could try 8 times.
(H)ard: You guess on 5 digits. You could try 12 times.
""")

    level = input("Please chose from E, M or H. > ").upper()

    if level == "E":
	    digit = 3
	    times = 5 
	    minimum = 100
	    maximum= 999
		
    elif level == "M":
	    digit = 4
	    times = 8
	    minimum = 1000
	    maximum= 9999
	
    elif level == "H":
	    digit = 5
	    times = 12
	    minimum = 10000
	    maximum= 99999
	
    else:
	    print("Please choose from E, M or H.")

    number = random.randint(minimum,maximum) 
    number = str(number) 
    
    while True: 
        message = ""		
        count = 0 
        guess = input("Please enter a {} digit number. > ".format(digit)) 

        for index in range (0, digit): 
            if number[index] == guess[index]: 
                message += "*" 
                count += 1
            elif number[index] <= guess[index]: 
                message += "<"        
            elif number[index] >= guess[index]: 
                message += ">"
        print(message) 
        print("You correctly guessed {} numbers!".format(count))

        times -= 1
        if message == "***" or message == "****" or message == "*****":
            print("Congratulations! You win the game!") 
            extra = input("Would you like to try this game again? (Y)es or (N)o.)").upper()
            if extra == "Y": 
                break
            else:
            	exit()
            
        if times >= 2:
            print("You can try {} more times.".format(times))
        elif times == 1:
            print("You can try 1 more times.")
        elif times == 0:
            print("You lose the game.")
            extra = input("Would you like to try this game again? (Y)es or (N)o.)").upper()
            if extra == "Y": 
                break
            else:
            	exit()
            

			
		
delay = input("Press ENTER to exit. ")		
		
		
		
		
		
		
		



    

