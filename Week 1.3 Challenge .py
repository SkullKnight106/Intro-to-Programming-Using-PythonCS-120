# Week 1.3 Challenge
# Utilize a decision structure that will allow the user to input the number of items in their cart. Loop through their cart until all item prices have been entered.  
# Suppose you are the cashier of the 10-item checkout lane. Take the previous step and improve it: 
# if the user enters a number of items greater than 10, inform them that they must go to a different line. 
# Once the user has inputted all of their items, confirm that they have provided you with all of the items from their cart. 
# Maybe they want to add a candy bar at the last minute? Accommodate this potential request by using a decision structure. 
# If the user confirms that they’re done entering prices, continue on. If the user would like to add another item (or items), repeat the process until they are satisfied.  

# Constants for initial values and sales tax rate
INITIAL_CART_TOTAL = 0.0
SALES_TAX_RATE = 0.06
MAX_ITEMS = 10

# Step 1: Ask the user for the number of items
num_items = int(input("Enter the number of items in your cart: "))

# Step 2: Check if the number of items is valid for the 10-item checkout lane
if num_items > MAX_ITEMS:
    print("You have more than 10 items. Please proceed to a different checkout lane.")
else:
    # Initialize cart total
    cart_total = INITIAL_CART_TOTAL
    
    # Step 3: Loop to input item prices
    for i in range(1, num_items + 1):
        item_price = float(input(f"Enter the price of item {i}: $"))
        cart_total += item_price

    # Step 4: Confirm if the user wants to add more items
    while True:
        add_more = input("Would you like to add another item? (yes/no): ").strip().lower()
        if add_more == 'yes':
            additional_item_price = float(input("Enter the price of the additional item: $"))
            cart_total += additional_item_price
        elif add_more == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")

    # Step 5: Calculate sales tax and final total
    sales_tax = cart_total * SALES_TAX_RATE
    final_total = cart_total + sales_tax

    # Step 6: Display the results
    print(f"\nYour total before tax: ${cart_total:.2f}")
    print(f"Sales tax (6%): ${sales_tax:.2f}")
    print(f"Your final total after tax: ${final_total:.2f}")


