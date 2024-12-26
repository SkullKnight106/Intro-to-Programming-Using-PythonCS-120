# Week 6.3
# Design a program that contains a function that accepts two arguments: a list, and a number n. This list should only contain numbers. 
# The function should display all of the numbers in the list that are greater than the number n. Let the user input the value n. 


def display_greater_numbers(numbers, n):
    """
    Displays all numbers in the list that are greater than n.
    :param numbers: List of numbers
    :param n: The number to compare against
    """
    print(f"\nNumbers greater than {n}:")
    for number in numbers:
        if number > n:
            print(number, end=" ")
    print()  # For a clean line after the output

def main():
    # Input the list of numbers from the user
    numbers = []
    count = int(input("Enter how many numbers you want to add to the list: "))
    for i in range(1, count + 1):
        while True:  # Input validation loop
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Input the value of n
    while True:
        try:
            n = float(input("Enter the number n to compare against: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Call the function to display numbers greater than n
    display_greater_numbers(numbers, n)

# Execute the program
main()
