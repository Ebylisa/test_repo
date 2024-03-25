# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Create a continuous loop so the user can play multiple rounds
while True:
    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # Check if the user selected a valid choice
    if user_choice in options:
        # Generate the computer selection
        computer_choice = random.choice(options)

        # Create a variable called user_full_choice to hold the text of the 
        # full word for the user's choice by using a match case statement
#if user_choice=="r"

        # Run Conditionals
        # First check if there is a tie
        if user_choice == computer_choice:
            print(f"You both chose {user_full_choice}!")
            print("A smashing tie!")
        else:
            # Tell the user what they chose
            print(f"You chose {user_full_choice}")

            # Refactor the conditionals into a nested match statement.
#While user-choice     

            # Check the user_choice first, then inside each case, check the 
            # computer_choice
match if user_choice = 'r'

        # Ask the user if they would like to play again and save the answer as 
        # a variable
        print("Would you like to play again?")
        play_again = input("Type (y) to continue or anything else to exit. ")

        # If the user's answer is not "y" or "Y", break from the loop
        if play_again.lower() != "y":
            break
    else:
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")

print("Thank you for playing Rock Paper Scissors. See you next time!")