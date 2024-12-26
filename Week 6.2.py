# Week 6.2
# Design a program that asks the user to enter a series of 20 numbers. 
# The program should store the numbers in a list then display the following:
# The lowest number in the list
# The highest number in the list
# The total of all numbers in the list
# The average of the numbers in the list 

def analyze_numbers():
    # Initialize an empty list to store numbers
    numbers = []

    # Collect 20 numbers from the user
    for i in range(1, 21):
        while True:  # Input validation loop
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Perform calculations
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    # Display results
    print("\nAnalysis of the numbers:")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of all numbers: {total}")
    print(f"Average of the numbers: {average:.2f}")

# Call the function
analyze_numbers()



