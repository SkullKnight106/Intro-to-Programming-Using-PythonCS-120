# This program calculates the profit based on the projected total sales,
# where the company makes 23% profit from its total sales.

# Step 1: Prompt the user to enter the projected amount of total sales
total_sales = float(input("Enter the projected total sales amount: "))  # Input is converted to a float to handle decimal values

# Step 2: Calculate the profit
profit_percentage = 0.23  # Profit is 23% of total sales. Pecentage can easily be changed here for different rates.
profit = total_sales * profit_percentage  # Calculate profit

# Step 3: Display the profit
print(f"The projected profit from total sales of ${total_sales:.2f} is ${profit:.2f}")

# Explanation:
# The profit is calculated as 23% of total sales and then displayed with proper formatting.
# The `.2f` ensures the output is formatted to 2 decimal places for better readability.
