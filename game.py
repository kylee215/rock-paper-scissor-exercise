import random


print("Rock, Paper, Scissors, Shoot!")
# this is the "game.py" file

# Processing user inputs
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
print("You chose:", user_choice)


# Validating user inputs
valid_options = ["rock", "paper", "scissors"]
user_choice = user_choice.lower()
if user_choice not in valid_options:  
    print("invalid choice")
    exit() #quit running program

# Simulating computer selection

computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

# Determining the winner
if user_choice == computer_choice:
    print("Tie")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win")
    else:
        print("You lose")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win")
    else:
        print("You lose")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win")
    else:
        print("You lose")


# Displaying results

#-------------------
#Welcome 'Player One' to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!