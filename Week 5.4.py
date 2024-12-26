# Week 5.4
# Write a program that asks the user for the following information:
# Their name
# A brief description of themself. 
# Then, create an HTML file; we are going to build a simple webpage. The HTML file should hold contain the information entered by the user.

import webbrowser

def create_html_file():
    # Get user input
    name = input("Enter your name: ")
    description = input("Enter a brief description of yourself: ")

    # Create HTML content
    html_content = f"""
    <html>
    <head>
    <title>Simple Webpage</title>
    </head>
    <body>
        <center>
            <h1>{name}</h1>
        </center>
        <hr />
        <p>{description}</p>
        <hr />
    </body>
    </html>
    """

    # Write the content to an HTML file
    filename = "user_info.html"
    with open(filename, 'w') as file:
        file.write(html_content)

    print(f"The HTML file '{filename}' has been created.")

     # Open the HTML file in the default web browser
    webbrowser.open(filename)

# Execute the function
create_html_file()

