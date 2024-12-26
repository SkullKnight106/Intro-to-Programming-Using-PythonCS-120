# Week 4.3
# Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. 
# Use the function in a program that prompts the user to enter a number then displays a message indicating whether the number is prime. 
# Write another program that displays all of the prime numbers from 1 to 100. The program should have a loop that calls the is_prime function. 

# Function to determine if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):  # Check divisibility up to the square root of the number
        if number % i == 0:
            return False
    return True

# Program to prompt the user for a number and check if it is prime
user_number = int(input("Enter a number to check if it is prime: "))
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

# Program to display all prime numbers from 1 to 100
print("\nPrime numbers from 1 to 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=' ')

