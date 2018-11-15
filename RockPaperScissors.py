#Samantha Marah
#A Simple Rock/Paper/Scissors Game Developed In The Python Programming Language

#Imports The Random Library
import random

#Welcome Function - Just Welcomes The Player To The Game
def Welcome():
    print("Welcome To A Game Of Rock-Paper-Scissors!")

#Game Function
def TheGame():
    #Random Generator To Choose The Choice For The Computer
    RandomNumberGenerator = random.randint(1,3)

    #If The Random Generator Chooses A 1 Then The Computer Chooses Rock
    if RandomNumberGenerator == 1:
        ComputerChoice = "Rock"

    #If The Random Generator Chooses A 2 Then The Computer Chooses Paper
    elif RandomNumberGenerator == 2:
        ComputerChoice = "Paper"

    #Otherwise The Computer Chooses Scissors
    else:
        ComputerChoice = "Scissors"

    #Takes In The Players Input For Either Rock Paper Or Scissors
    KeyboardInput = input("Please Type In Either 'Rock', 'Paper' Or 'Scissors': ")

    #If The Player Choice & Computer Choice Are The Same
    #Then It Is A Tie
    if KeyboardInput == ComputerChoice:
        print("You Have Both Picked",KeyboardInput,"Please Try Again!")
        TryAgain() #Calls The TryAgain Function

    #If The Player Chosses Rock And The Computer Chooses Paper - Computer Wins
    if KeyboardInput == "Rock":
        if ComputerChoice == "Paper":
            print("Paper Beats Rock! Computer Wins")
            TryAgain() #Calls The TryAgain Function
            
        #Else If The Computer Chooses Scissors - Player Wins
        elif ComputerChoice == "Scissors":
            print("Rock Beats Paper! You Win!")
            TryAgain() #Calls The TryAgain Function

    #If The Player Chosses Paper And The Computer Chooses Rock - Player Wins
    if KeyboardInput == "Paper":
        if ComputerChoice == "Rock":
            print("Paper Beats Rock! You Win")
            TryAgain() #Calls The TryAgain Function

        #Else If The Computer Chooses Scissors - Computer Wins
        elif ComputerChoice == "Scissors":
            print("Scissors Beats Paper! Computer Wins")
            TryAgain() #Calls The TryAgain Function
             
    #If The Player Chosses Scissors And The Computer Chooses Rock - Computer Wins
    if KeyboardInput == "Scissors":
        if ComputerChoice == "Rock":
            print("Rock Beats Scissors! Computer Wins")
            TryAgain() #Calls The TryAgain Function

        #Else If The Computer Chooses Paper - Player Wins
        elif ComputerChoice == "Paper":
            print("Scissors Beats Paper! You Win")
            TryAgain() #Calls The TryAgain Function

    #Error Handling - If The Player Types In An Inccorect Input
    else:
        print("Error - Incorrect Input - Please Type In 'Rock', 'Paper' Or 'Scissors' - Please Try Again")
        TheGame() #Calls The TheGame Function

#TryAgain Function
def TryAgain():
    print("Would You Like To Play Again?")

    #Takes In The Players Input
    PlayAgain = input("Enter 'Yes' Or 'No': ")

    #If Player Says Yes - Loop The Game
    if PlayAgain == "Yes":
        TheGame() #Calls The TheGame Function

    #If The Player Says No - End The Game
    elif PlayAgain == "No":
        print ("Goodbye")

    #Otherwise Reloop The TryAgain Function
    else:
        TryAgain() #Calls The TryAgain Function

Welcome()
TheGame()