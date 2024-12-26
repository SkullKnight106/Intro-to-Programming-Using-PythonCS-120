# Week 3.5 Challenge
# Write a program that utilizes a constant to store the total amount of the user’s grocery store cart. 
# Allow the user to purchase five items; the price will be inputted by the user for each item. Process this data by adding it to your cart total constant. 
# Once the user has inputted all five items, output their total including a sales tax of 6%. 
# Rewrite your code to integrate the use of sentinels. 
# Try to maximize the efficiency of your code by removing any unnecessary lines that could be improved through the integration of sentinels. 
# Challenge
# Utilize functions to improve your program. Create the following functions: 
# A function that prints a formatted list of all the items in the user’s grocery cart.  
# A function that calculates the subtotal and then outputs a formatted receipt.  


# Constants
SALES_TAX_RATE = 0.06
SENTINEL = -1

# Functions
def add_item_to_cart(cart, max_items=5):
    """
    Allows the user to add items to the cart with an option to exit early using a sentinel value.
    Returns a list of item prices.
    """
    print(f"Enter prices for up to {max_items} items. Enter {SENTINEL} to finish early.")
    for item in range(1, max_items + 1):
        try:
            price = float(input(f"Enter the price for item {item}: "))
            if price == SENTINEL:
                print("Exiting early.")
                break
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            cart.append(price)
        except ValueError:
            print("Invalid input. Please enter a valid price.")
    return cart

def print_cart_items(cart):
    """
    Prints a formatted list of all items in the user's cart.
    """
    print("\nYour cart contains:")
    for i, price in enumerate(cart, 1):
        print(f"Item {i}: ${price:.2f}")

def calculate_total(cart):
    """
    Calculates the subtotal, sales tax, and final total.
    Returns the formatted receipt as a string.
    """
    subtotal = sum(cart)
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    return subtotal, sales_tax, total

def print_receipt(cart, subtotal, sales_tax, total):
    """
    Prints the formatted receipt.
    """
    print("\nReceipt:")
    print_cart_items(cart)
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales Tax (6%): ${sales_tax:.2f}")
    print(f"Total Amount: ${total:.2f}")

# Main Program
def main():
    cart = []
    # Step 1: Add items to cart
    add_item_to_cart(cart)

    if not cart:
        print("No items were added to the cart.")
        return

    # Step 2: Calculate totals
    subtotal, sales_tax, total = calculate_total(cart)

    # Step 3: Print receipt
    print_receipt(cart, subtotal, sales_tax, total)

# Execute the program
if __name__ == "__main__":
    main()

