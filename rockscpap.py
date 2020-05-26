print("Welcome to Rock, Paper, Scissors Game")
print("Here are the Rules:")
print("Rock crushes Scissors")
print()
print("Paper covers Rock")
print()
print("Scissors cuts Paper")
print()

import random

list1 = ["Rock", "Paper", "Scissors"]



scores_computer = 0

scores_human = 0

num_of_rounds = 1

while num_of_rounds <= 6:
    game = random.choice(list1)

    pick = input("Enter your pick! Rock, Paper, Scissors: ")
    
    

    if pick == game:
        print("you both chose", game, "it is a tie!")
        
    elif pick == "Rock" and game == "Scissors":
        print("Rock crushes Scissors, you win")
        num_of_rounds += 1
        scores_human += 1
        
    elif pick == "Rock" and game == "Paper":
        print("Paper covers Rock, computer wins")
        num_of_rounds += 1
        scores_computer += 1
    
    elif pick == "Scissors" and game == "Rock":
        print("Rock crushes Scissors, computer wins")
        num_of_rounds += 1
        scores_computer += 1

    elif pick == "Scissors" and game == "Paper":
        print("Scissors cuts Paper, you win")
        num_of_rounds += 1
        scores_human += 1
        
    elif pick == "Paper" and game == "Rock":
        print("Paper covers Rock, you win")
        num_of_rounds += 1
        scores_human += 1
        
    elif pick == "Paper" and game == "Scissors":
        print("Scissors cuts Paper, computer wins")
        num_of_rounds += 1
        scores_computer += 1
        
    else:
        print("invalid pick")
        
if scores_human > scores_computer:
    print("after", num_of_rounds-1, "rounds, you won", scores_human, "-", scores_computer)
elif scores_human < scores_computer:
    print("after", num_of_rounds-1, "rounds, computer won", scores_computer, "-", scores_human)
else:
    print("after", num_of_rounds-1, "rounds, it was a tie", scores_computer, "-", scores_human)

