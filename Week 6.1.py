# Week 6.1
# Design a program that generates a seven-digit lottery number using a list. 
# The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a list element. 
# Then write another loop that displays the lottery number. Refer to random numbers covered in chapter 5.

import random

def generate_lottery_number():
    # Generate seven random numbers and store them in a list
    lottery_numbers = [random.randint(0, 9) for _ in range(7)]
    
    # Display the lottery number as a single sequence
    print("Your lottery number is:", end=" ")
    for number in lottery_numbers:
        print(number, end="")
    print()  # Move to the next line after displaying the number

# Call the function
generate_lottery_number()
