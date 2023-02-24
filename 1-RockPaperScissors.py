#Rock Paper Scissors

#importing the needed modules
import random  #this is what the computer will use to select it option

#creating and initialising of variables
# These must be  global variables
ComputerPoints = 0
PlayerPoints = 0
Options = ('rock', 'paper', 'scissors') 

#definging function to enable user select options

def user():
    global Options
    user_option = input('Select either rock, paper or scissors:\n ').lower()

    #next we will constrain user input to match Options
    if user_option not in Options:
        print ("You didn't enter a correct option. Try again!\n")
        return user()
    else:
        return user_option

#defining a function to enable computer select options
def computer():
    #computer would make selection randomly
    return random.choice(Options)


#defining a function for the game now
def game():
    #global variables where scores are kept 
    global ComputerPoints, PlayerPoints
    #setting the selected computer and player options to their global variables
    ComputerChoice = computer()
    PlayerChoice = user()

    #Computing who wins
    #First lets declare draws
    if PlayerChoice == ComputerChoice:
        print("It's a tie! No one earns a point.")

    #Seconding instances where player wins
    elif (PlayerChoice == "rock" and ComputerChoice == "scissors") or (PlayerChoice == "scissors" and ComputerChoice == "paper") or (PlayerChoice =="paper" and ComputerChoice == "rock"):
        PlayerPoints +=1
        print("Hurray You won!!!")
    #Next, all other instances are wins for the computer
    else:
        ComputerPoints +=1
        print("Sorry, I won")
    print ()

#Creating a loop for the number of turns per round
print("Welcome to the Rock, Paper and Scissors game! I hope you enoy it!!!")
while True:
    for i in range(5):
        game()
        
    #displaying results for the game so far
    print ("At the end of the round,\nYour score is: ", PlayerPoints, "\nMy score is: ", ComputerPoints)
    print()
    #dclaring the round winner
    if PlayerPoints > ComputerPoints:
        print("Hurray, You Won the Round!, Next time, I will get you!\n")
    else:
        print("I won, try harder! Bring it on!!!\n")
        #decision to continue or to stop
    continuation = input("Press 'c' to continue\nPress 'r' to restart\nor any other key to quit:\n")

    if continuation == 'c':
         #continue game
         continue
    elif continuation == 'r':
        #restart the whole game
        PlayerPoints = 0
        ComputerPoints = 0
    else:
        #stoping and closing the game
        break
print("Thanks for playing!")