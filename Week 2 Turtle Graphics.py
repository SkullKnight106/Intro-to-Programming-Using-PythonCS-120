# Week 2 - Assignment Turtle Graphics 
# Write an if statement that uses the turtle graphics library to determine whether the turtle is inside of a rectangle. 
# The rectangle’s upper-left corner is at (100, 100) and its lower-right corner is at (200, 200). If the turtle is inside the rectangle, hide the turtle.  

import turtle

# Function to check if turtle is inside the rectangle
def check_turtle_position():
    # Get turtle's current position
    x = turtle.xcor()  # Current x-coordinate of the turtle
    y = turtle.ycor()  # Current y-coordinate of the turtle

    # Rectangle boundaries
    left_bound = 100  # Left (x) boundary of the rectangle
    right_bound = 200  # Right (x) boundary of the rectangle
    upper_bound = 100  # Upper (y) boundary of the rectangle
    lower_bound = 200  # Lower (y) boundary of the rectangle

    # Check if turtle's position is inside the rectangle
    if left_bound <= x <= right_bound and upper_bound <= y <= lower_bound:
        turtle.hideturtle()  # Hide the turtle if inside the rectangle

# Move the turtle to a position 
turtle.penup()  # Prevent drawing when moving
turtle.goto(150, 150)  # Move turtle to a location inside the rectangle
turtle.pendown()

# Call the function to check the turtle's position
check_turtle_position()

# Keep the turtle window open
turtle.done()
