# Week 4.3 Challenge
# Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. 
# Use the function in a program that prompts the user to enter a number then displays a message indicating whether the number is prime. 
# Write another program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime function. 
# Input the data into is_prime via file input (the file should have a singular number on it). 
# Then, write a function that outputs all of the prime numbers from 1 to 100 in the same file in place of the existing data. 
# Save your file and attach it with your homework submission.  


# Function to determine if a number is prime
def is_prime(number):
    """
    Determines if a number is a prime number.
    Args:
        number (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):  # Check divisibility up to the square root of the number
        if number % i == 0:
            return False
    return True

# Function to check if a number is prime using file input
def check_prime_from_file(filename):
    """
    Reads a number from a file and checks if it is prime.
    Args:
        filename (str): The path to the file containing the number.
    """
    try:
        with open(filename, 'r') as file:
            number = int(file.read().strip())
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print(f"Error: The file '{filename}' does not contain a valid integer.")

# Function to write all prime numbers from 1 to 100 to the same file
def write_primes_to_file(filename):
    """
    Writes all prime numbers from 1 to 100 to a file.
    Args:
        filename (str): The path to the file where the prime numbers will be written.
    """
    try:
        with open(filename, 'w') as file:
            primes = [str(num) for num in range(1, 101) if is_prime(num)]
            file.write(" ".join(primes))
        print(f"All prime numbers from 1 to 100 have been written to '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main Program
def main():
    """
    Main program to execute the prime-checking tasks.
    """
    # Input a number from the user to check if it is prime
    user_number = int(input("Enter a number to check if it is prime: "))
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        print(f"{user_number} is not a prime number.")

    # Display all prime numbers from 1 to 100
    print("\nPrime numbers from 1 to 100:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=' ')
    print("\n")

    # File operations
    filename = "prime_data.txt"
    print(f"\nChecking if a number in '{filename}' is prime...")
    check_prime_from_file(filename)

    print(f"\nWriting all prime numbers from 1 to 100 to '{filename}'...")
    write_primes_to_file(filename)

# Execute the program
if __name__ == "__main__":
    main()
