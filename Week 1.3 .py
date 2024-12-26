# Week 1.3
# This program calculates the total amount for five items purchased at a grocery store
# and applies a 6% sales tax to the total.

# Step 1: Define the constant for the initial total in the grocery cart (assuming it's $0 initially)
INITIAL_CART_TOTAL = 0.0

# Step 2: Define the sales tax rate as a constant (6%)
SALES_TAX_RATE = 0.06

# Step 3: Initialize a variable to keep track of the total cost of the items
cart_total = INITIAL_CART_TOTAL

# Step 4: Allow the user to input the price of five items
for i in range(1, 6):
    item_price = float(input(f"Enter the price of item {i}: "))  # Get the price of each item from the user
    cart_total += item_price  # Add the item price to the cart total

# Step 5: Calculate the sales tax
sales_tax = cart_total * SALES_TAX_RATE

# Step 6: Calculate the final total including sales tax
final_total = cart_total + sales_tax

# Step 7: Output the final total to the user, formatted to 2 decimal places
print(f"\nYour total before tax: ${cart_total:.2f}")
print(f"Sales tax (6%): ${sales_tax:.2f}")
print(f"Your final total after tax: ${final_total:.2f}")

# Explanation:
# We first define the initial cart total as a constant (starting at 0).
# The user is asked to input the price of 5 items, and each price is added to the running cart total.
# After all items are entered, we calculate the sales tax as 6% of the cart total.
# The final total is then calculated by adding the sales tax to the cart total.
# The result is printed with proper formatting (2 decimal places) for readability.
