# Week 7.4
# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. The dictionary should have the following key-value pairs:
# The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. The dictionary should have the following key-value pairs:
# The program should let the user enter a course number, then it should display the course’s room number and the instructor. 

def main():
    # Create dictionaries for room numbers and instructors
    course_rooms = {
        'CS101': 3004,
        'CS102': 4501,
        'CS103': 6755,
        'NT110': 1244,
        'CM241': 1411
    }

    course_instructors = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    }

    # Prompt the user to enter a course number
    course_number = input("Enter a course number (e.g., CS101): ")

    # Retrieve and display course information
    if course_number in course_rooms and course_number in course_instructors:
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        print(f"Course: {course_number}") # The f in print(f"...") denotes a formatted string literal, commonly known as an f-string. F-strings allow you to embed expressions or variables directly within a string by placing them inside curly braces {}.
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
    else:
        print("Course number not found. Please check your input.")

# Execute the program
main()
