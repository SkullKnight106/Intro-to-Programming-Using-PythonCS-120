# Week 3.5
# Write a program that utilizes a constant to store the total amount of the user’s grocery store cart. 
# Allow the user to purchase five items; the price will be inputted by the user for each item. Process this data by adding it to your cart total constant. 
# Once the user has inputted all five items, output their total including a sales tax of 6%. 
# Rewrite your code to integrate the use of sentinels. 
# Try to maximize the efficiency of your code by removing any unnecessary lines that could be improved through the integration of sentinels. 

# Define constants for sales tax rate and sentinel value
SALES_TAX_RATE = 0.06
SENTINEL = -1

# Initialize the cart total
cart_total = 0.0

# Allow the user to enter up to five items or stop with a sentinel
for item in range(1, 6):
    price = float(input(f"Enter the price for item {item} (or enter {SENTINEL} to finish): "))
    
    # Check for sentinel value to exit early if needed
    if price == SENTINEL:
        print("Exiting early.")
        break
    
    # Add the item price to the cart total
    cart_total += price

# Calculate the final total including sales tax
final_total = cart_total * (1 + SALES_TAX_RATE)

# Display the total
print(f"Total amount including sales tax: ${final_total:.2f}")



