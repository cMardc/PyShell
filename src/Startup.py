#!/bin/python3


startup_text = """

Welcome To PyShell!
This is a mini-shell made for beginners to learn how shells looks like.
Any built-in shell programs (examples: BASH, cmd, PowerShell), also works with our shell
Type __help__ to get more information.

"""
help_text = """

Special commands:
__help__ - Get help about commands.
__exit__ - Exits the shell.

Basic commands:
view: List visible files and folders in the current directory.
goto <directory>: Change the current directory.
display <file_path>: View the contents of a file.
current: Display the current working directory.
show_current: Show current directory on start.
hide_current: Hide current directory on start.
create_file <file_name>: Create a new file
create_folder <folder_name>: Create a new folder
view_all: List all files and folders in the current directory.
copy <source_file> <new_file>: Copy a file/folder
move <source_file> <new_file>: Move a file/folder
delete <source>: Delete a file/folder
delete_folder <source>: Delete a folder
__help__: Get help about PyShell.
__exit__: Exit PyShell.
version: Check version.
<shell_command>: Execute a shell command.

Any builtin commands {example: BASH, cmd, Powershell} will work.

"""
