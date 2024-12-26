# Week 5.4 Challenge
# Write a program that asks the user for the following information:
# Their name
# A brief description of themself. 
# Then, create an HTML file; we are going to build a simple webpage. The HTML file should hold contain the information entered by the user.
# If you would like an added challenge, add some creativity to your webpage. 
# Build out a full resume webpage on your user. Include information such as: Hobbies/interests Education Work history  Skills 
# For information such as hobbies/interests and skills, use lists to store the information. 


# Function to collect user information and create an HTML webpage
def create_html_webpage():
    # Collect user information
    name = input("Enter your name: ")
    description = input("Enter a brief description of yourself: ")
    hobbies = input("Enter your hobbies/interests (comma-separated): ").split(',')
    education = input("Enter your education details: ")
    work_history = input("Enter your work history: ")
    skills = input("Enter your skills (comma-separated): ").split(',')

    # File name for the HTML webpage
    file_name = "resume.html"

    # Build the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{name}'s Webpage</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }}
            h1, h2 {{ text-align: center; color: #2c3e50; }}
            .container {{ max-width: 800px; margin: auto; padding: 20px; }}
            ul {{ list-style-type: square; }}
            hr {{ border: 0; height: 1px; background: #ccc; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{name}</h1>
            <p><strong>About Me:</strong> {description}</p>
            <hr />
            <h2>Hobbies & Interests</h2>
            <ul>
                {''.join(f'<li>{hobby.strip()}</li>' for hobby in hobbies)}
            </ul>
            <hr />
            <h2>Education</h2>
            <p>{education}</p>
            <hr />
            <h2>Work History</h2>
            <p>{work_history}</p>
            <hr />
            <h2>Skills</h2>
            <ul>
                {''.join(f'<li>{skill.strip()}</li>' for skill in skills)}
            </ul>
        </div>
    </body>
    </html>
    """

    # Write the HTML content to the file
    with open(file_name, "w") as file:
        file.write(html_content)

    print(f"\nHTML webpage '{file_name}' has been created successfully.")
    print("Open the file in your browser to view your resume webpage.")

# Main function to execute the program
if __name__ == "__main__":
    create_html_webpage()


