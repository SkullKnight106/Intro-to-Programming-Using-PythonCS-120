# Week 8.4
# There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. 
# Write a program that asks how many tickets for each class of seats were sold as well as the purchaser's name. 
# Save this information in an appropriate data structure (you make this decision), then output the contents of the data structure once all purchases have been made. 
# Finally, output the total amount of income generated from ticket sales.  


def calculate_ticket_sales():
    """
    Collects ticket sales information, stores it in a data structure, and calculates total income.
    """
    # Prices for each seat category
    seat_prices = {'A': 20, 'B': 15, 'C': 10}

    # Data structure to store ticket sales
    sales_data = []

    print("Welcome to Stadium Ticket Sales Program")
    while True:
        try:
            # Input purchaser's name
            name = input("Enter the purchaser's name (or type 'done' to finish): ").strip()
            if name.lower() == 'done':
                break

            # Input number of tickets sold for each category
            tickets_a = int(input("Enter the number of Class A tickets sold: "))
            tickets_b = int(input("Enter the number of Class B tickets sold: "))
            tickets_c = int(input("Enter the number of Class C tickets sold: "))

            # Calculate total for this purchase
            total = (tickets_a * seat_prices['A']) + (tickets_b * seat_prices['B']) + (tickets_c * seat_prices['C'])

            # Save the data
            sales_data.append({
                'Name': name,
                'Class A Tickets': tickets_a,
                'Class B Tickets': tickets_b,
                'Class C Tickets': tickets_c,
                'Total Sale': total
            })

        except ValueError:
            print("Invalid input. Please enter numeric values for ticket quantities.")

    # Display all sales data
    print("\nSales Data:")
    total_income = 0
    for sale in sales_data:
        print(f"Name: {sale['Name']}, "
              f"Class A: {sale['Class A Tickets']}, "
              f"Class B: {sale['Class B Tickets']}, "
              f"Class C: {sale['Class C Tickets']}, "
              f"Total: ${sale['Total Sale']:.2f}")
        total_income += sale['Total Sale']

    # Display total income
    print(f"\nTotal Income from Ticket Sales: ${total_income:.2f}")


# Execute the program
calculate_ticket_sales()
