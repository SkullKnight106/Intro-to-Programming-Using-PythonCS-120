# Week 6.4
# A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. 
# A positive integer greater than 1 is composite if it is not prime. 
# Write a program that asks the user to enter an integer greater than 1, then displays all of the prime numbers that are less than or equal to the number entered. 
# The program should work as follows:
# Once the user has entered a number, the program should populate a list with all of the integers from 2 up through the value entered.
# The program should then use a loop to step through the list. The loop should pass each element to a function that displays the element whether it is a prime number


def is_prime(number):
    """
    Determines if a number is prime.
    :param number: Integer to check for primality
    :return: True if prime, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):  # Check divisors up to sqrt(number)
        if number % i == 0:
            return False
    return True

def display_primes_up_to(limit):
    """
    Displays all prime numbers up to the given limit.
    :param limit: The upper bound for checking primes
    """
    primes = []  # List to store primes
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    print(f"\nPrime numbers up to {limit}: {primes}")

def main():
    #  Get user input and validate
    while True:
        try:
            upper_limit = int(input("Enter an integer greater than 1: "))
            if upper_limit > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    #  Display all prime numbers up to the given limit
    display_primes_up_to(upper_limit)

# Execute the program
main()
