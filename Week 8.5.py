# Week 8.5
# Design a program that lets the user enter the total rainfall for each of 12 months into a list. 
# The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the highest and lowest amounts. 

def calculate_rainfall():
    """
    Collects rainfall data for 12 months, calculates total and average rainfall,
    and determines the months with the highest and lowest rainfall.
    """
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    rainfall = []

    # Collect rainfall data
    print("Enter the total rainfall for each month:")
    for month in months:
        while True:
            try:
                amount = float(input(f"{month}: "))
                if amount < 0:
                    print("Rainfall cannot be negative. Please try again.")
                else:
                    rainfall.append(amount)
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    # Calculate total and average rainfall
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(rainfall)

    # Determine the months with the highest and lowest rainfall
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    # Display results
    print("\nRainfall Statistics:")
    print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Highest rainfall: {max_rainfall:.2f} inches in {max_month}")
    print(f"Lowest rainfall: {min_rainfall:.2f} inches in {min_month}")


# Execute the program
calculate_rainfall()


