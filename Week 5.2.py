# Week 5.2
# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold. 
# Next, write a program that reads the random numbers from the file, displays the numbers, 
# then displays the total of the numbers and the number of random numbers read from the file.

import random

def write_random_numbers(filename, count):
    """Writes a specified number of random numbers (1-500) to a file."""
    with open(filename, 'w') as file:
        for _ in range(count):
            number = random.randint(1, 500)
            file.write(f"{number}\n")
    print(f"{count} random numbers have been written to {filename}.")

# Get user input for the number of random numbers to generate
num_numbers = int(input("Enter the number of random numbers to generate: "))
filename = "random_numbers.txt"
write_random_numbers(filename, num_numbers)

def read_and_process_numbers(filename):
    """Reads numbers from a file, displays them, and calculates their total and count."""
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            total = sum(numbers)
            count = len(numbers)

            print("\nNumbers read from the file:")
            print(numbers)
            print(f"\nTotal of the numbers: {total}")
            print(f"Number of numbers read: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to read and process the numbers
read_and_process_numbers(filename)