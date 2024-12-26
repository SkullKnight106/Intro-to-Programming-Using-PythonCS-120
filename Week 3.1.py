 # Week 3.1
# Write a program that keeps a running total of the number of bugs collected during the five days. 
# The loop should ask for the number of bugs collected for each day, and when the loop is finished, 
# the program should display the total number of bugs collected. 

# Initialize a variable to store the total count of bugs collected
total_bugs = 0

# Loop through each day to collect the number of bugs
for day in range(1, 6):
    # Ask the user for the number of bugs collected on that day
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    
    # Add the number of bugs collected that day to the total
    total_bugs += bugs_collected

# After the loop, display the total number of bugs collected
print(f"\nTotal bugs collected over 5 days: {total_bugs}")

