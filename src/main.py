#!/bin/python3

import os
import subprocess
from colorama import Fore, Style  # @brief Import necessary modules
from pathlib import Path
import tempfile
from subprocess import call
import json
import datetime
import platform
import psutil
import shutil
import editor
import curses
import sys


def mv(source, destination):
    """
    @brief Move a file or directory from source to destination.

    @param source: The source path.
    @type source: str
    @param destination: The destination path.
    @type destination: str
    """
    try:
        shutil.move(source, destination)
    except FileNotFoundError:
        print(Fore.RED + f"Error: '{source}' not found." + Fore.RESET)
    except PermissionError:
        print(
            Fore.RED
            + f"Error: Permission denied for '{source}' or '{destination}'"
            + Fore.RESET
        )


def cp(source, destination):
    """
    @brief Copy a file from source to destination.

    @param source: The source path.
    @type source: str
    @param destination: The destination path.
    @type destination: str
    """
    try:
        if os.path.exists(source):
            if os.path.isfile(source):
                shutil.copy(source, destination)
            else:
                raise IsADirectoryError(
                    Fore.RED + "Source is not a valid file." + Fore.RESET
                )
        else:
            raise FileNotFoundError(Fore.RED + "Source file not found" + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + f"Error: '{source}' not found." + Fore.RESET)
    except PermissionError:
        print(
            Fore.RED
            + f"Error: Permission denied for '{source}' or '{destination}'"
            + Fore.RESET
        )


def rm(file_or_directory):
    """
    @brief Remove a file or directory.

    @param file_or_directory: The path to the file or directory to remove.
    @type file_or_directory: str
    """
    try:
        if os.path.isfile(file_or_directory):
            os.remove(file_or_directory)
        elif os.path.isdir(file_or_directory):
            shutil.rmtree(file_or_directory)
        else:
            print(
                Fore.RED
                + f"Error: '{file_or_directory}' is not a file or directory."
                + Fore.RESET
            )
    except FileNotFoundError:
        print(Fore.RED + f"Error: '{file_or_directory}' not found." + Fore.RESET)
    except PermissionError:
        print(
            Fore.RED
            + f"Error: Permission denied for '{file_or_directory}'"
            + Fore.RESET
        )


def rmdir(directory):
    """
    @brief Remove an empty directory.

    @param directory: The directory to remove.
    @type directory: str
    """
    try:
        if os.path.isdir(directory):
            os.rmdir(directory)
        else:
            raise NameError(Fore.RED + "Source is not a directory" + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + f"Error: '{directory}' not found." + Fore.RESET)
    except PermissionError:
        print(Fore.RED + f"Error: Permission denied for '{directory}'" + Fore.RESET)


def get_system_info():
    """
    @brief Get system information.

    @return: A dictionary containing system information.
    @rtype: dict
    """
    info = {}

    # Get OS information
    info["OS"] = platform.system()
    info["OS Version"] = platform.version()

    # Get machine information
    info["Machine"] = platform.machine()

    # Get memory information
    virtual_memory = psutil.virtual_memory()
    info["Total Memory (RAM)"] = virtual_memory.total
    info["Available Memory (RAM)"] = virtual_memory.available

    # Get disk space information
    disk_partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in disk_partitions:
        partition_info = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            "Total Space": partition_info.total,
            "Used Space": partition_info.used,
            "Free Space": partition_info.free,
            "File System Type": partition.fstype,
        }
    info["Disk Space"] = disk_info

    # Get CPU information
    cpu_info = {}
    cpu_info["CPU Cores"] = os.cpu_count()
    cpu_info["CPU Usage"] = psutil.cpu_percent(interval=1, percpu=True)
    info["CPU"] = cpu_info

    # Get current user
    info["Current User"] = os.getenv("USER") or os.getenv("LOGNAME")

    return info


def view(directory):
    """
    @brief List the contents of a directory.

    @param directory: The directory to list.
    @type directory: str

    @return: A list of files and folders in the directory.
    @rtype: list
    """
    normal_contents = []
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if not os.path.basename(item_path).startswith("."):
                normal_contents.append(item)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    return normal_contents


def view_all(directory):
    """
    @brief List all contents of a directory.

    @param directory: The directory to list.
    @type directory: str

    @return: A list of all files and folders in the directory.
    @rtype: list
    """
    return os.listdir(directory)


def create_file(name):
    """
    @brief Create an empty file.

    @param name: The name of the file to create.
    @type name: str
    """
    if "/" in str(name):
        raise NameError("Can't include '/' in names")
        print(Fore.RED + f"Can't include '/' in file names")
        print(Fore.RESET, end="")
        return

    try:
        with open(str(name), "w"):
            pass  # This creates an empty file
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")
        print(Fore.RESET, end="")


def create_folder(folder_name):
    """
    @brief Create a folder (directory).

    @param folder_name: The name of the folder to create.
    @type folder_name: str
    """
    folder_name = str(folder_name)
    try:
        Path(folder_name).mkdir()
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")
        print(Fore.RESET, end="")


def display(file_path):
    """
    @brief Display the contents of a file.

    @param file_path: The path to the file to display.
    @type file_path: str
    """
    try:
        with open(file_path, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(Fore.RED + "File not found: " + file_path)
        print(Fore.RESET, end="")


def remove_space(text):
    """
    @brief Remove spaces from a text string.

    @param text: The text string to process.
    @type text: str

    @return: The text string with spaces removed.
    @rtype: str
    """
    return text.replace(" ", "")


def main():
    """
    @brief Main function of the script.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.dirname(script_dir)

    json_file_path = os.path.join(script_dir, "config", "color.json")
    json_file_path2 = os.path.join(script_dir, "config", "config.json")
    json_file_path3 = os.path.join(script_dir, "config", "texts.json")
    log_file_path = os.path.join(script_dir, "log", "history.log")

    help_text = ""
    startup_text = ""

    color_dict = {}
    config_dict = {}
    text_dict = {}

    try:
        with open(json_file_path3, "r") as json_file:
            texts_dict = json.load(json_file)
    except FileNotFoundError:
        print(Fore.RED + f"JSON file not found at {json_file_path3}" + Fore.RESET)
    except json.JSONDecodeError as e:
        print(Fore.RED + f"Error parsing JSON file: {e}" + Fore.RESET)

    if texts_dict:
        if texts_dict["startup_text"] and texts_dict["help_text"]:
            startup_text = texts_dict["startup_text"]
            help_text = texts_dict["help_text"]

    # Load color configuration from a JSON file
    try:
        with open(json_file_path, "r") as json_file:
            color_dict = json.load(json_file)
    except FileNotFoundError:
        print(Fore.RED + f"JSON file not found at {json_file_path}" + Fore.RESET)
    except json.JSONDecodeError as e:
        print(Fore.RED + f"Error parsing JSON file: {e}" + Fore.RESET)

    # Load additional configuration from another JSON file
    try:
        with open(json_file_path2, "r") as json_file:
            config_dict = json.load(json_file)
    except FileNotFoundError:
        print(Fore.RED + f"JSON file not found at {json_file_path2}" + Fore.RESET)
    except json.JSONDecodeError as e:
        print(Fore.RED + f"Error parsing JSON file: {e}" + Fore.RESET)

    show_dir = False

    if config_dict:
        if config_dict["show_dir"]:
            show_dir = config_dict["show_dir"]

    if not color_dict:
        print(Fore.MAGENTA + startup_text)
        print(Fore.RESET)
    else:
        if color_dict["STARTUP"]:
            current_color = color_dict["STARTUP"]
            if current_color == "RED":
                print(Fore.RED + startup_text)
                print(Fore.RESET)
            elif current_color == "BLUE":
                print(Fore.BLUE + startup_text)
                print(Fore.RESET)
            elif current_color == "GREEN":
                print(Fore.GREEN + startup_text)
                print(Fore.RESET)
            elif current_color == "WHITE":
                print(Fore.WHITE + startup_text)
                print(Fore.RESET)
            elif current_color == "MAGENTA":
                print(Fore.MAGENTA + startup_text)
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
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{timestamp} : {input_cmd}\n")
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

            print(help_text)
        elif input_cmd == "view":
            files = view(current_dir)
            for file in files:
                print(f"'{file}'", end=" ")
            print("")
        elif input_cmd == "view_all":
            files = view_all(current_dir)
            for file in files:
                print(f"'{file}'", end=" ")
            print("")
        elif input_cmd.startswith("goto "):
            target_dir = input_cmd[5:]  # Extract the directory after "goto "
            try:
                os.chdir(target_dir)  # Change to the target directory
                current_dir = os.getcwd()  # Update the current directory
            except FileNotFoundError:
                print(Fore.RED + "Directory not found: " + target_dir + Fore.RESET)
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
                print(
                    Fore.RED + f"JSON file not found at {json_file_path2}" + Fore.RESET
                )
            except Exception as e:
                print(Fore.RED + f"Error writing to JSON file: {e}" + Fore.RESET)
        elif input_cmd == "hide_current":
            show_dir = False
            config_dict["show_dir"] = False
            try:
                with open(json_file_path2, "w") as json_file:
                    json.dump(config_dict, json_file, indent=4)
            except FileNotFoundError:
                print(
                    Fore.RED + f"JSON file not found at {json_file_path2}" + Fore.RESET
                )
            except Exception as e:
                print(Fore.RED + f"Error writing to JSON file: {e}" + Fore.RESET)
        elif input_cmd.startswith("create_file "):
            file_name = input_cmd[12:]
            try:
                create_file(file_name)
            except NameError as e:
                print(Fore.RED + str(e) + Fore.RESET)
        elif input_cmd.startswith("create_folder "):
            folder_name = input_cmd[14:]
            create_folder(folder_name)
        elif input_cmd == "version":
            if config_dict:
                if config_dict["version"] and config_dict["name"]:
                    print(
                        config_dict["name"]
                        + " - version "
                        + str(config_dict["version"])
                    )
                else:
                    print(Fore.RED + "Error while loading version" + Fore.RESET)
            else:
                print(Fore.RED + "Error while loading config.json" + Fore.RESET)
        elif input_cmd == "history":
            with open(log_file_path, "r") as log_file:
                print(log_file.read())
        elif input_cmd == "info":
            system_info = get_system_info()

            # Print the collected information
            for category, data in system_info.items():
                print(f"{category}:")
                if isinstance(data, dict):
                    for key, value in data.items():
                        print(f"  {key}: {value}")
                else:
                    print(f"  {data}")
                print()
        elif input_cmd.startswith("move "):
            _, source, destination = input_cmd.split()
            mv(source, destination)
        elif input_cmd.startswith("copy "):
            _, source, destination = input_cmd.split()
            try:
                cp(source, destination)
            except FileNotFoundError as e:
                print(str(e))
            except NameError as e:
                print(str(e))
            except Exception as e:
                print("Unknown error: " + str(e))
        elif input_cmd.startswith("delete "):
            _, file_or_directory = input_cmd.split()
            rm(file_or_directory)
        elif input_cmd.startswith("delete_folder "):
            _, directory = input_cmd.split()
            rmdir(directory)
        elif input_cmd.startswith("edit "):
            _, file_name = input_cmd.split()
            curses.wrapper(editor.main, file_name)
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
