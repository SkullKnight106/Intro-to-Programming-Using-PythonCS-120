# Week 2.3 Challenge
# A classic programming problem exists called the “change-making problem”. In this problem, the program must complete the following: 
# The program should prompt the user to enter the number of coins for each value of coin: penny, nickel, dime, and quarter (we will not use a half-dollar). 
# Ideally, these coins will add up to equal exactly one dollar.  
# If the total value equals a dollar, the program should congratulate the user. 
# If the total value does not equal a dollar, the program should inform the user whether they were over a dollar or under a dollar in total value. 
# If the total value does not equal a dollar, inform the user of how far off they were.  
# Limit the user input to integers only. If the user inputs a string, return an error statement using the print() function. 
# Use a while loop to complete the following: create a running total that outputs every time the user adds more coins. 
# For instance, if the user enters two quarters, inform them that their total is now $0.50. 
# If they add three dimes, inform them that the total is now $0.80. 
# If, during this process, the total exceeds one dollar before the user has finished entering coins, inform them that they have exceeded a dollar and that they have lost the game.  
# Try to solve the problem for the user. Allow them to enter quarters and dimes. 
# If the total is under one dollar, inform them of how many nickels they can add in before they exceed one dollar. 
# If this value does not equal exactly one dollar, inform them of how many pennies need to be added.  


# Constants for the value of each coin in dollars
PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25

def get_integer_input(prompt):
    """Prompt the user for input and ensure it's a valid integer."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_and_display_solution(total_value):
    """Provide a solution to reach exactly $1 if total_value is less than $1."""
    remaining = 1.00 - total_value
    nickels_needed = int(remaining // NICKEL_VALUE)
    remaining -= nickels_needed * NICKEL_VALUE
    pennies_needed = int(round(remaining / PENNY_VALUE))
    print(f"You need {nickels_needed} more nickels and {pennies_needed} more pennies to make exactly $1.")

def main():
    print("Welcome to the Change-Making Game!")
    print("Try to add coins to make exactly $1.")

    total_value = 0.0  # Initialize the running total

    while total_value < 1.00:
        print(f"Current total: ${total_value:.2f}")
        
        # Prompt the user to enter the number of each coin
        print("\nAdd more coins:")
        quarters = get_integer_input("Enter the number of quarters: ")
        total_value += quarters * QUARTER_VALUE
        if total_value > 1.00:
            print(f"Your total is ${total_value:.2f}. You exceeded $1. You lose!")
            return

        dimes = get_integer_input("Enter the number of dimes: ")
        total_value += dimes * DIME_VALUE
        if total_value > 1.00:
            print(f"Your total is ${total_value:.2f}. You exceeded $1. You lose!")
            return

        nickels = get_integer_input("Enter the number of nickels: ")
        total_value += nickels * NICKEL_VALUE
        if total_value > 1.00:
            print(f"Your total is ${total_value:.2f}. You exceeded $1. You lose!")
            return

        pennies = get_integer_input("Enter the number of pennies: ")
        total_value += pennies * PENNY_VALUE
        if total_value > 1.00:
            print(f"Your total is ${total_value:.2f}. You exceeded $1. You lose!")
            return

    # Check if the total equals $1
    if total_value == 1.00:
        print("Congratulations! The total value is exactly $1.")
    else:
        print(f"Your total is under $1. You are short by ${1.00 - total_value:.2f}.")
        calculate_and_display_solution(total_value)

# Run the game
main()

