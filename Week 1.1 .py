# This program asks the user for a value for variable 'a',
# performs operations on 'a' and 'b', then displays 'a', 'b', and 'c' using a single print statement.

# Step 1: Prompt the user to enter a value for variable 'a'
a = float(input("Enter a value for variable a: "))  # Using float to handle decimal values if necessary

# Step 2: Add 2 to a and assign the result to b
b = a + 2

# Step 3: Multiply b with 4 and assign the result to a
a = b * 4

# Step 4: Divide a by 3.14 and assign the result to b
b = a / 3.14

# Step 5: Subtract 8 from b and assign the result to a
a = b - 8

# Displaying the final values of a, b, and c in a single print statement
# 'c' is the final value of 'b' after all operations
c = b

# Printing the results for a, b, and c
print(f"Final values - a: {a}, b: {b}, c: {c}")

