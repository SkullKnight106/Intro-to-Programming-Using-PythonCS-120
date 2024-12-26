# Week 4.1
# Write a function that determines whether a number is even or odd. 
# Write another function that generates 100 random numbers and keeps a count of how many of those random numbers are even, and how many of them are odd. 
# Finally, write a function that displays the even values in a list from least to greatest. 

import random

# Function to determine if a number is even or odd
def is_even(number):
    return number % 2 == 0

# Function to generate 100 random numbers and count evens and odds
def generate_and_count_random_numbers():
    even_count = 0
    odd_count = 0
    even_numbers = []

    for _ in range(100):
        num = random.randint(1, 100)  # Generate a random number between 1 and 100
        if is_even(num):
            even_count += 1
            even_numbers.append(num)
        else:
            odd_count += 1

    return even_count, odd_count, even_numbers

# Function to display sorted even numbers
def display_sorted_evens(even_numbers):
    even_numbers.sort()  # Sort the list of even numbers
    print("Even numbers in sorted order:", even_numbers)

# Main execution
even_count, odd_count, even_numbers = generate_and_count_random_numbers()
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
display_sorted_evens(even_numbers)
