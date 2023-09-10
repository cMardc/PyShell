#!/bin/python3

from main import create_file
import os


def create_id_card():
    print("Welcome to the ID Card Generator!")

    # Get user input
    name = input("Enter your name: ")
    id_number = input("Enter your ID number: ")
    department = input("Enter your department: ")

    # Prompt the user to specify the directory
    directory = input(
        "Enter the directory path to save the ID card (leave blank for the current directory): "
    )

    if not directory:
        # Use the current directory if no directory is specified
        directory = ""

    # Generate the content for the ID card
    id_card_content = f"Name: {name}\nID Number: {id_number}\nDepartment: {department}"

    # Create a file name for the ID card
    file_name = f"{name.replace(' ', '_')}_ID_Card.txt"

    # Create the ID card file in the specified directory
    id_card_path = os.path.join(directory, file_name)
    create_file(id_card_path)

    # Write the ID card content to the file
    with open(id_card_path, "w") as id_card_file:
        id_card_file.write(id_card_content)

    print(f"ID Card created and saved as '{file_name}' in '{directory}'")


if __name__ == "__main__":
    create_id_card()
