import random

print("Welcome, Player One.")
print("Rock, Paper, Scissors, Shoot!")
# this is the "game.py" file

# Processing user inputs
user_choice = input("Please make a selection ('rock', 'paper', 'scissors'):")
print("You chose:", user_choice)


# Validating user inputs
valid_options = ["rock", "paper", "scissors"]
user_choice = user_choice.lower()
if user_choice not in valid_options:  
    print("Invalid choice. Please start over with a valid selection.")
    exit() #quit running program

# Simulating computer selection

computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

# Determining the winner
if user_choice == computer_choice:
    print("Result: Tie")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Result: You win")
    else:
        print("Result: You lose")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Result: You win")
    else:
        print("Result: You lose")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Result: You win")
    else:
        print("Result: You lose")


# Displaying results

print("Thank you for playing.")