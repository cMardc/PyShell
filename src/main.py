#!/bin/python3

import os
import subprocess
import Startup
from colorama import Fore, Style
from pathlib import Path
import tempfile
from subprocess import call


def view(directory):
    return os.listdir(directory)


def create_file(name):
    try:
        with open(name, "w"):
            pass  # This creates an empty file
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")
        print(Fore.RESET, end="")


def create_folder(folder_name):
    try:
        Path(folder_name).mkdir()
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")
        print(Fore.RESET, end="")


def display(file_path):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(Fore.RED + "File not found: " + file_path)
        print(Fore.RESET, end="")


def remove_space(text):
    return text.replace(" ", "")


def main():
    show_dir = False
    print(Fore.MAGENTA + Startup.startup_text)
    print(Fore.RESET)
    current_dir = os.getcwd()
    # Continue until exit
    while True:
        # Print a starting point without '\n'
        if show_dir:
            print(Fore.GREEN + current_dir, end="")
        print(Fore.BLUE + "$ ", end="")
        print(Style.RESET_ALL, end="")
        input_cmd = input()
        if input_cmd == "__exit__":  # exit case
            break
        elif input_cmd == "__help__":
            print(Startup.help_text)
        elif input_cmd == "view":
            files = view(current_dir)
            for file in files:
                print(file, end=" ")
            print("")
        elif input_cmd.startswith("goto "):
            target_dir = input_cmd[5:]  # Extract the directory after "goto "
            try:
                os.chdir(target_dir)  # Change to the target directory
                current_dir = os.getcwd()  # Update the current directory
            except FileNotFoundError:
                print("Directory not found: " + target_dir)
        elif input_cmd.startswith("display "):
            file_path = input_cmd[8:]
            display(file_path)
        elif input_cmd == "current":
            print(current_dir)
        elif input_cmd == "show_current":
            show_dir = True
        elif input_cmd == "hide_current":
            show_dir = False
        elif input_cmd.startswith("create_file "):
            file_name = input_cmd[12:]
            create_file(file_name)
        elif input_cmd.startswith("create_folder "):
            folder_name = input_cmd[14:]
            create_folder(folder_name)
        elif remove_space(input_cmd) != "":
            if input_cmd.strip() != "":
                try:
                    if " " not in input_cmd:
                        # Execute the command without spaces as-is

                        if (
                            input_cmd.startswith("vim")
                            or input_cmd.startswith("nvim")
                            or input_cmd.startswith("nano")
                        ):
                            EDITOR = os.environ.get("EDITOR", input_cmd)  # that easy!

                            initial_message = (
                                ""  # if you want to set up the file somehow
                            )

                            with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
                                tf.flush()
                                call([EDITOR, tf.name])

                                # do the parsing with `tf` using regular File operations.
                                # for instance:
                                tf.seek(0)
                                edited_message = tf.read()
                        else:
                            subprocess.Popen(
                                input_cmd, shell=True
                            )  # works great, but lags when nano,vim is opened
                    else:
                        # Split the command into arguments and execute it
                        cmd_parts = input_cmd.split()
                        subprocess.Popen(cmd_parts, text=True)
                except FileNotFoundError:
                    print(Fore.RED + "Invalid command: " + input_cmd + Fore.RESET)


if __name__ == "__main__":
    main()
