# Week 8.3
# Write a program that calculates the amount of money a person would earn over some time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. 
# The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. 
# The output should be displayed in a dollar amount, not the number of pennies. 
# Convert the dollar amount to three other currencies and output the new values with the currency type. 


def calculate_salary(days, conversion_rates):
    """
    Calculates and displays daily and total salary based on doubling pennies.
    Converts the total salary to other currencies.

    :param days: The number of days worked
    :param conversion_rates: Dictionary of conversion rates for other currencies
    """
    salary = 0.01  # Starting salary in dollars (1 penny)
    total_salary = 0.0  # Total salary accumulator

    print("Day\tSalary (in $)") # Display Header: Creates a formatted table header to display daily salaries.
    print("-" * 20)

    
    for day in range(1, days + 1):       # Iterates through each day using a for loop. 
        print(f"{day}\t${salary:.2f}")
        total_salary += salary          # Adds the daily salary to total_salary.
        salary *= 2                      # Double the salary each day

    # Display total salary in USD
    print("-" * 20)
    print(f"Total Pay: ${total_salary:.2f}\n") # The string begins with f, indicating that it is a formatted string literal. F-strings allow variables or expressions to be embedded directly within a string by enclosing them in curly braces {}.
                                                # :.2f  .2 ensures that the number is rounded to two decimal places. f which ensures that the value is displayed as a decimal number
    
    # Convert and display in other currencies
    print("Total Pay in Other Currencies:")
    for currency, rate in conversion_rates.items(): # Iterates through the conversion_rates dictionary.
        converted_salary = total_salary * rate      # Multiplies total_salary by each conversion rate.
        print(f"{currency}: {converted_salary:.2f}") # Prints the converted salary for each currency.

def main():
    try:
        # User input for number of days
        days = int(input("Enter the number of days worked: "))
        if days <= 0:
            raise ValueError("The number of days must be greater than zero.")

        # conversion_rates: A dictionary mapping currency names to their conversion rates relative to USD.
        conversion_rates = {
            "EUR (Euro)": 0.85,
            "GBP (British Pound)": 0.75,
            "JPY (Japanese Yen)": 110.5
        }

        # Calculate and display the salary
        calculate_salary(days, conversion_rates)

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the program
main()
