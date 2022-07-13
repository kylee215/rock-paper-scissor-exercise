import random


print("Rock, Paper, Scissors, Shoot!")
# this is the "game.py" file

# Processing user inputs
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
print("You chose:", user_choice)


# Validating user inputs


# Simulating computer selection
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

# Determining the winner


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