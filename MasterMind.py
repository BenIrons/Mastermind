import random
from tkinter import *

def start():

    slots = [0,0,0,0]#Defines that slots is an array
    slots = random.sample(range(1,6),4)#Gets 4 random nubers between 1 and 6
    global redPeg #sets redPeg as a global variable 
    for y in range(0,11):#this for function will end the game if the user exceeds the amount of rounds
        if y == 10:
            print("You're out of rounds!")
            print("Hidden Code - ",slots)
            limbo()
            
              
        TotalGuess = [0,0,0,0]#defines totalGuess as an array
        TotalGuess[0] = int(input("Number between 1-6...")) 
        #User input will be put into TotalGuess position 0
        TotalGuess[1] = int(input("Number between 1-6..."))
        TotalGuess[2] = int(input("Number between 1-6..."))
        TotalGuess[3] = int(input("Number between 1-6..."))
        
        def feedback():#This function gives feedback on the userinput
            global redPeg
            redPeg = 0
            whitePeg = 0
            x = 0
            b = 0
                                            
            for x in range(0,4):#Changes the value of x from 0 to 4
                if TotalGuess[x] == slots[x]:#if user guess = hidden code 
                    redPeg = redPeg + 1#Add one to redPeg
                    continue
                if TotalGuess[x] in slots:#If the value in slot x of TotalGuess is in slots
                    whitePeg = whitePeg + 1#WhitePeg + 1
                    continue

            
            if redPeg == 4: #Win function
                win() 
                   
                                            
                

            print("Red Pegs - ",redPeg)#prints the value redPeg holds
            print("White Pegs - ",whitePeg)#prints the value whitePeg holds  
            print("Guess - ",TotalGuess)#prints the value totalguess holds
        feedback()
        


def Home():#Like a lobbby allows the user to start the game
    print("Welcome to MasterMind")
    usrinput = input("To start press enter...")
    if usrinput == "":
        start()
    else:
        usrinput

def limbo():#After a game allows the user to either restart or quit
    input1 = input("Would you like to replay, y or n?...")
    if input1 == "y":
        Home()
    else:
        quits()

def win():#checks to see if the user has won and if so prints you win and goes to limbo
    if redPeg == 4:
        print("You win!")
        limbo()

def quits():
    print("Goodbye :)")
    quit()
        



        
Home()
    
    




    



