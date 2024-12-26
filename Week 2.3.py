# Week 2.3
# A classic programming problem exists called the “change-making problem”. In this problem, the program must complete the following: 
# The program should prompt the user to enter the number of coins for each value of coin: penny, nickel, dime, and quarter (we will not use a half-dollar). 
# Ideally, these coins will add up to equal exactly one dollar.  
# If the total value equals a dollar, the program should congratulate the user. 
# If the total value does not equal a dollar, the program should inform the user whether they were over a dollar or under a dollar in total value. 

# Constants for the value of each coin in dollars
PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25

# Get user input for the number of each type of coin
pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

# Calculate the total value of all the coins
total_value = (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)

# Check if the total equals one dollar
if total_value == 1.00:
    print("Congratulations! The total value is exactly one dollar.")
elif total_value > 1.00:
    print(f"The total value is over a dollar by ${total_value - 1.00:.2f}.")
else:
    print(f"The total value is under a dollar by ${1.00 - total_value:.2f}.")
