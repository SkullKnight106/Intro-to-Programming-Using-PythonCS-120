 # Week 3.4
#In mathematics, the notation n! represents the factorial of the nonnegative integer n. 
# The factorial of n is the product of all the nonnegative integers from 1 to n. For example, 
# 7! = 1×2×3×4×5×6×7=5,0407!=1×2×3×4×5×6×7=5,040 
# 4! = 1×2×3×4=24 
# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that number. 
# Apply input validation and then, display the factorial.

# Function to calculate the factorial
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Input validation loop
while True:
    try:
        number = int(input("Enter a nonnegative integer: "))
        if number < 0:
            print("Please enter a nonnegative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Calculate the factorial
result = calculate_factorial(number)

# Display the result
print(f"The factorial of {number} is {result}")



