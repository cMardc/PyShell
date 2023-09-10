
![Logo](docs/assets/logos/png/logo-no-background.png)

# PyShell - A Beginner-Friendly Shell for Python Programming

![Static Badge](https://img.shields.io/badge/Language-Python-blue)
![GitHub](https://img.shields.io/github/license/cMardc/PyShell)
![GitHub all releases](https://img.shields.io/github/downloads/cMardc/PyShell/total)
![GitHub repo size](https://img.shields.io/github/repo-size/cMardc/PyShell)



PyShell is a simple, beginner-friendly shell for both shell and Python programming. This README file provides an overview of the PyShell code and how to use it effectively. It is designed to help beginners get started with shell and Python scripting in a user-friendly environment.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Usage](#usage)
4. [Commands](#commands)
5. [Getting Help](#getting-help)
6. [Exiting PyShell](#exiting-pyshell)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

PyShell is a Python script that provides a command-line interface for executing shell commands and Python scripts. It allows you to navigate directories, view files, and run shell commands or Python scripts in a simple and interactive manner. It is designed with beginners in mind, making it an excellent tool for learning shell and Python programming.

## Features

- **Simple and Interactive**: PyShell provides a user-friendly interface for running shell commands and Python scripts, making it accessible to beginners.
- **Directory Navigation**: You can navigate directories using the `goto` command.
- **View Files**: Use the `view` command to list files in the current directory.
- **Display File Contents**: You can view the contents of a file using the `display` command.
- **Execute Shell Commands**: Run shell commands directly from PyShell by entering the command.
- **Execute Python Scripts**: You can also run Python scripts from PyShell.
- **Help**: Get help with PyShell commands by using the `__help__` command.

## Usage

To use PyShell, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Save the PyShell code to a Python file, e.g., `pyshell.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `pyshell.py`.
5. Run PyShell by executing `python pyshell.py`.

You should see the PyShell prompt, which looks like this:

<pre>
$
</pre>


You can now start using PyShell to run commands and scripts.

## Commands

PyShell supports the following commands:

- `view`: List visible files and folders in the current directory.
- `goto <directory>`: Change the current directory.
- `display <file_path>`: View the contents of a file.
- `current`: Display the current working directory.
- `show_current`: Show current directory on start.
- `hide_current`: Hide current directory on start.
- `create_file <file_name>`: Create a new file
- `create_folder <folder_name>`: Create a new folder
- `edit <filename>`: Edit a file using basic text editor.
- `view_all`: List all files and folders in the current directory.
- `copy <source_file> <new_file>`: Copy a file/folder
- `move <source_file> <new_file>`: Move a file/folder
- `delete <source>`: Delete a file/folder
- `delete_folder <source>`: Delete a folder
- `__help__`: Get help about PyShell.
- `__exit__`: Exit PyShell.
- `version`: Check version.
- `<shell_command>`: Execute a shell command.


## Getting Help

If you need help with PyShell commands, you can use the `__help__` command to display the help text.

Example:
<pre>
$ __help__
</pre>


## Exiting PyShell

To exit PyShell, use the `__exit__` command:

<pre>
$ __exit__
</pre>

## Examples

Here's an example of commands in PyShell:

<pre>
$ goto /
$ current
/
$ show_current
/$ hide_current
$ view
'snap' 'srv' 'var' 'lib64' 'lib' 'tmp' 'bin' 'libx32' 'root' 'cdrom' 'run' 'sys' 'sbin' 'dev' 'opt' 'boot' 'lost+found' 'media' 'swapfile' 'lib32' 'etc' 'home' 'mnt' 'proc' 'usr' 
$ goto home
$ view
'root' 'cmard' 
$ goto cmard
$ create_folder test
$ goto test
$ view

$ create_file test.sh
$ edit test.sh
$ # wrote -> echo 'Hello, World!'   
Invalid command: # wrote -> echo 'Hello, World!'
$ bash test.sh
$ Hello, World!

$ __exit__
</pre>

You can also use PyShell as a module and create your own python script with it:

<pre>
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

</pre>

## Contributing

If you'd like to contribute to PyShell or report issues, please feel free to [create an issue](https://github.com/cMardc/PyShell/issues) or submit a pull request. Your contributions are welcome and appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
