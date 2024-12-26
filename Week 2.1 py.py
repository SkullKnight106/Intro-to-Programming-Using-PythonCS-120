# Week 2.1
# This program asks the user for the length and width of two rectangles
# The program should tell the user which rectangle has the greater area, or if the areas are the same

# Get the dimensions for the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Get the dimensions for the second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Calculate the area for both rectangles
area1 = length1 * width1
area2 = length2 * width2

# Compare the areas and display the result
if area1 > area2:
    print("The first rectangle has a greater area.")
elif area2 > area1:
    print("The second rectangle has a greater area.")
else:
    print("Both rectangles have the same area.")