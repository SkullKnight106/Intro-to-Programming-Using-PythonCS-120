 # Week 3.3
# At one college, the tuition for a full-time student is $10,000 per semester. 
# It has been announced that the tuition will increase by 2 percent each year for the next 5 years. 
# Write a program with a loop that displays the projected semester tuition amount for the next 5 years. 

# Initial tuition cost
tuition = 10000

# Define the percentage increase
increase_rate = 0.02

# Loop through the next 5 years
for year in range(1, 6):
    # Calculate the tuition increase for the current year
    tuition += tuition * increase_rate
    # Display the projected tuition for the year, rounded to 2 decimal places
    print(f"Year {year}: ${tuition:.2f}")

