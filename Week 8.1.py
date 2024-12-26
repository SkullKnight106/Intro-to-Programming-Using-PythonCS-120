# Week 8.1
# When a bank account pays compound interest, it pays interest not only on the principal amount that was deposited into the account but also on the interest that has accumulated over time. 
# Suppose you want to deposit some money into a savings account and let the account earn compound interest for a certain number of years. 
# The formula for calculating the balance of the account after a specified number of years is: A=P(1+rn)nt 
# Write a program that calculates for you. The program should ask the user to input the following: 
# The amount of principal originally deposited into the account 
# The annual interest rate paid by the account 
# The number of times per year that the interest is compounded (For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.) 
# The number of years the account will be left to earn interest 
# Once the input data has been entered, the program should calculate and display the amount of money that will be in the account after the specified number of years. 

# Compound Interest Calculator with Logging

def calculate_compound_interest(principal, annual_rate, times_compounded, years):
    """Calculate compound interest."""
    amount = principal * (1 + (annual_rate / times_compounded))**(times_compounded * years)
    return amount

def log_calculation_to_file(log_file, principal, annual_rate, times_compounded, years, amount):
    """Log calculation details to a file."""
    with open(log_file, 'a') as file:
        file.write(f"Principal: ${principal:.2f}, Annual Rate: {annual_rate*100:.2f}%, "
                   f"Times Compounded per Year: {times_compounded}, "
                   f"Years: {years}, Final Amount: ${amount:.2f}\n")

def main():
    log_file = "compound_interest_log.txt"
    
    # Input values
    try:
        principal = float(input("Enter the principal amount (P): "))
        annual_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
        times_compounded = int(input("Enter the number of times interest is compounded per year (n): "))
        years = float(input("Enter the number of years the account will earn interest (t): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Calculate compound interest
    final_amount = calculate_compound_interest(principal, annual_rate, times_compounded, years)
    
    # Display results
    print(f"The amount of money in the account after {years} years will be: ${final_amount:.2f}")
    
    # Log calculation
    log_calculation_to_file(log_file, principal, annual_rate, times_compounded, years, final_amount)
    print(f"Calculation logged to {log_file}.")

if __name__ == "__main__":
    main()




