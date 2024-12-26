# Midterm 4.2
# Question 2: A book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:  
# Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.
 

# Ask the user for the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

# Determine the points awarded based on the number of books purchased
if books_purchased == 0:
    points_awarded = 0
elif books_purchased == 2:
    points_awarded = 5
elif books_purchased == 4:
    points_awarded = 15
elif books_purchased == 6:
    points_awarded = 30
elif books_purchased >= 8:
    points_awarded = 60
else:
    points_awarded = 0  # Default case if none of the conditions match

# Display the points awarded
print(f"You have earned {points_awarded} points.")

