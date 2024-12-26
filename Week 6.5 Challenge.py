# Week 6.5 Challenge
# A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. 
# A positive integer greater than 1 is composite if it is not prime. Once the user enters the integer, verify that is greater than 1. 
# If it is, display all prime numbers that are less than or equal to the approved input. The program should work as follows: 
# Once the user has inputted their integer, the program should fill a list with all integers from 2 and up until the inputted value is reached. 
# After the above step is complete, the program should use a loop to iterate through the list. 
# The loop should pass each element to a function that outputs the element and whether or not it is a prime number.
# If you would like an added challenge, complete the following: 
# Create a list of all prime numbers between 1 and 100. 
# Ask the user to enter a number between 1 and 100. 
# Search the list for the number. If it exists, inform the user of the location in the list. 
# If it does not, tell the user the closest prime number to the value that they inputted.


# Function to determine if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to the square root of the number
        if num % i == 0:
            return False
    return True

# Function to find the closest prime number to a given value
def closest_prime(number, prime_list):
    closest = min(prime_list, key=lambda x: abs(x - number))
    return closest

# Main program
def main():
    # Prompt user for a number greater than 1
    while True:
        try:
            user_number = int(input("Enter an integer greater than 1: "))
            if user_number > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Generate a list of integers from 2 to the user-entered number
    numbers = list(range(2, user_number + 1))
    
    # Filter the list to include only prime numbers
    primes = [n for n in numbers if is_prime(n)]
    
    # Display all primes up to the user-entered number
    print(f"\nPrime numbers up to {user_number}: {primes}")
    
    # Added Challenge
    # Generate a list of prime numbers between 1 and 100
    primes_1_to_100 = [n for n in range(2, 101) if is_prime(n)]
    print("\nList of prime numbers between 1 and 100:")
    print(primes_1_to_100)

    # Ask the user to enter a number between 1 and 100
    while True:
        try:
            query_number = int(input("\nEnter a number between 1 and 100: "))
            if 1 <= query_number <= 100:
                break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Check if the number is in the list of primes
    if query_number in primes_1_to_100:
        index = primes_1_to_100.index(query_number)
        print(f"{query_number} is a prime number and is located at index {index} in the list.")
    else:
        # Find the closest prime number
        closest = closest_prime(query_number, primes_1_to_100)
        print(f"{query_number} is not a prime number. The closest prime number is {closest}.")

# Run the program
if __name__ == "__main__":
    main()

