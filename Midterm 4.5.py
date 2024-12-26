# Midterm 4.5
# Question 5: Write a program that utilizes functions to conduct the following tasks:
#Take an order from a customer at your restaurant; the order should contain a food item and a price. 
#Implement a loop that will allow you to take the order for everyone at table (a value entered by the user).  
# Output the order to the user to ensure it was heard correctly.  
# Calculate the order total by adding all of the inputted prices together into a variable called order_total.  
# Return to the table with the order_total. Output the order total and user input/output to confirm that the user agrees with the total. If they agree, say goodbye to the user. 
# If they do not agree, reduce the total by 15%.  
# Write the order total to a file and name the file orders.txt. This will serve as documentation for the restaurant.  


def take_order():
    """Function to take orders for all customers at the table."""
    num_customers = int(input("Enter the number of people at the table: "))
    orders = []  # List to store orders (food item, price)
    order_total = 0.0  # Variable to store total cost
    
    # Loop to take orders for each customer
    for i in range(num_customers):
        food_item = input(f"Enter the food item for customer {i + 1}: ")
        price = float(input(f"Enter the price for {food_item}: $"))
        orders.append((food_item, price))
        order_total += price
    
    return orders, order_total

def confirm_order(orders):
    """Function to output the order to the user for confirmation."""
    print("\nHere is your order summary:")
    for i, (food, price) in enumerate(orders, start=1):
        print(f"Customer {i}: {food} - ${price:.2f}")

def adjust_total(order_total):
    """Function to adjust the order total if the user does not agree."""
    response = input(f"\nYour total is ${order_total:.2f}. Do you agree with this total? (yes/no): ").lower()
    if response == 'yes':
        print("Thank you for your confirmation! Enjoy your meal.")
    else:
        order_total *= 0.85  # Reduce the total by 15%
        print(f"The adjusted total after a 15% reduction is ${order_total:.2f}.")
    return order_total

def write_to_file(order_total):
    """Function to write the order total to a file."""
    with open("orders.txt", "w") as file:
        file.write(f"Order Total: ${order_total:.2f}\n")
    print("The order total has been saved to orders.txt.")

def main():
    orders, order_total = take_order()
    confirm_order(orders)
    final_total = adjust_total(order_total)
    write_to_file(final_total)

# Run the program
main()
