# Week 2.2
# a program that asks the user to enter a number of seconds 

# Function to convert seconds into days, hours, minutes, and seconds
def convert_seconds(total_seconds):
    # Calculate the number of days
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400

    # Calculate the number of hours
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

    # Calculate the number of minutes
    minutes = remaining_seconds // 60

    # The remaining seconds
    seconds = remaining_seconds % 60

    # Display the result
    if total_seconds >= 86400:
        print(f"{total_seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
    elif total_seconds >= 3600:
        print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
    elif total_seconds >= 60:
        print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
    else:
        print(f"{total_seconds} seconds is less than a minute.")

# Ask the user to enter the number of seconds
user_seconds = int(input("Enter the number of seconds: "))

# Call the function to perform the conversion
convert_seconds(user_seconds)
