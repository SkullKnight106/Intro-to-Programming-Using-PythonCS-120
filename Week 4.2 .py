# Week 4.2
# Write a program that asks the user to enter five test scores. The program should display a letter grade for each score and the average test score. 
# Write the following functions in the program:
# calc_average - This function should accept five test scores as arguments and return the average of the scores.
# determine_grade - This function should accept a test score as an argument and return a letter grade for the score 

# Function to calculate the average of five test scores
def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5

# Function to determine the letter grade for a given score
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program
scores = []  # List to store the test scores

# Prompt the user to enter five test scores
for i in range(1, 6):
    score = float(input(f"Enter score {i}: "))
    scores.append(score)
    # Display the letter grade for each score
    grade = determine_grade(score)
    print(f"Score {i}: {score} - Grade: {grade}")

# Calculate and display the average of the scores
average = calc_average(*scores)  # Unpacking the list to pass as arguments
print(f"\nAverage score: {average:.2f}")
print(f"Average grade: {determine_grade(average)}")


