#!/bin/python3

import os
import subprocess
import Startup
from colorama import Fore, Style
from pathlib import Path
import tempfile
from subprocess import call
import json


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
    json_file_path = "../config/color.json"
    json_file_path2 = "../config/config.json"

    color_dict = {}
    config_dict = {}

    try:
        with open(json_file_path, "r") as json_file:
            color_dict = json.load(json_file)
    except FileNotFoundError:
        print(f"JSON file not found at {json_file_path}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")

    try:
        with open(json_file_path2, "r") as json_file:
            config_dict = json.load(json_file)
    except FileNotFoundError:
        print(f"JSON file not found at {json_file_path2}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")

    show_dir = False

    if config_dict:
        if config_dict["show_dir"]:
            show_dir = config_dict["show_dir"]

    if not color_dict:
        print(Fore.MAGENTA + Startup.startup_text)
        print(Fore.RESET)
    else:
        if color_dict["STARTUP"]:
            current_color = color_dict["STARTUP"]
            if current_color == "RED":
                print(Fore.RED + Startup.startup_text)
                print(Fore.RESET)
            elif current_color == "BLUE":
                print(Fore.BLUE + Startup.startup_text)
                print(Fore.RESET)
            elif current_color == "GREEN":
                print(Fore.GREEN + Startup.startup_text)
                print(Fore.RESET)
            elif current_color == "WHITE":
                print(Fore.WHITE + Startup.startup_text)
                print(Fore.RESET)
            elif current_color == "MAGENTA":
                print(Fore.MAGENTA + Startup.startup_text)
                print(Fore.RESET)

    current_dir = os.getcwd()
    # Continue until exit
    while True:
        # Print a starting point without '\n'
        if show_dir:
            if not color_dict:
                print(Fore.GREEN + current_dir, end="")
            else:
                if color_dict["DIR"]:
                    current_color = color_dict["DIR"]
                    if current_color == "MAGENTA":
                        print(Fore.MAGENTA + current_dir, end="")
                    elif current_color == "RED":
                        print(Fore.RED + current_dir, end="")
                    elif current_color == "BLUE":
                        print(Fore.BLUE + current_dir, end="")
                    elif current_color == "GREEN":
                        print(Fore.GREEN + current_dir, end="")
                    elif current_color == "WHITE":
                        print(Fore.WHITE + current_dir, end="")

        if not color_dict:
            print(Fore.BLUE + "$ ", end="")
        else:
            if color_dict["SIGN"]:
                current_color = color_dict["SIGN"]
                if current_color == "BLUE":
                    print(Fore.BLUE + "$ ", end="")
                elif current_color == "RED":
                    print(Fore.RED + "$ ", end="")
                elif current_color == "GREEN":
                    print(Fore.GREEN + "$ ", end="")
                elif current_color == "MAGENTA":
                    print(Fore.MAGENTA + "$ ", end="")
                elif current_color == "WHITE":
                    print(Fore.WHITE + "$ ", end="")

        print(Style.RESET_ALL, end="")

        if color_dict:
            if color_dict["INPUT"]:
                current_color = color_dict["INPUT"]
                if current_color == "BLUE":
                    print(Fore.BLUE, end="")
                elif current_color == "RED":
                    print(Fore.RED, end="")
                elif current_color == "GREEN":
                    print(Fore.GREEN, end="")
                elif current_color == "MAGENTA":
                    print(Fore.MAGENTA, end="")
                elif current_color == "WHITE":
                    print(Fore.WHITE, end="")

        input_cmd = input()
        if input_cmd == "__exit__":  # exit case
            break
        elif input_cmd == "__help__":
            print(Style.RESET_ALL, end="")

            if color_dict:
                if color_dict["HELP"]:
                    current_color = color_dict["HELP"]
                    if current_color == "BLUE":
                        print(Fore.BLUE, end="")
                    elif current_color == "RED":
                        print(Fore.RED, end="")
                    elif current_color == "GREEN":
                        print(Fore.GREEN, end="")
                    elif current_color == "MAGENTA":
                        print(Fore.MAGENTA, end="")
                    elif current_color == "WHITE":
                        print(Fore.WHITE, end="")

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
            config_dict["show_dir"] = True
            try:
                with open(json_file_path2, "w") as json_file:
                    json.dump(config_dict, json_file, indent=4)
            except FileNotFoundError:
                print(f"JSON file not found at {json_file_path2}")
            except Exception as e:
                print(f"Error writing to JSON file: {e}")
        elif input_cmd == "hide_current":
            show_dir = False
            config_dict["show_dir"] = False
            try:
                with open(json_file_path2, "w") as json_file:
                    json.dump(config_dict, json_file, indent=4)
            except FileNotFoundError:
                print(f"JSON file not found at {json_file_path2}")
            except Exception as e:
                print(f"Error writing to JSON file: {e}")
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
