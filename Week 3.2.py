 # Week 3.2
# Running on a particular treadmill you burn 4.2 calories per minute. 
# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

# Define the calorie burn rate per minute
calories_per_minute = 4.2

# Loop through the specified time intervals
for minutes in [10, 15, 20, 25, 30]:
    # Calculate the calories burned for the current interval
    calories_burned = minutes * calories_per_minute
    # Display the results
    print(f"Calories burned after {minutes} minutes: {calories_burned:.1f}")

