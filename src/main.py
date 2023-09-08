#!/bin/python3

import os
import subprocess
import Startup






def view(directory):
    return os.listdir(directory)

def display(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print('File not found: ' + file_path)



def remove_space(text):
    return text.replace(' ', '')

def main():
    print(Startup.startup_text)
    current_dir = os.getcwd()
    # Continue until exit
    while True:
        # Print a starting point without '\n'
        print('$', end='')
        input_cmd = input()
        if input_cmd == '__exit__': #exit case
            break
        elif input_cmd == '__help__':
            print(Startup.help_text)
        elif input_cmd == 'view':
            files = view(current_dir)
            for file in files:
                print(file, end=' ')
            print('')
        elif input_cmd.startswith('goto '):
            target_dir = input_cmd[5:]  # Extract the directory after "goto "
            try:
                os.chdir(target_dir)  # Change to the target directory
                current_dir = os.getcwd()  # Update the current directory
            except FileNotFoundError:
                print('Directory not found: ' + target_dir)
        elif input_cmd.startswith('display '):
            file_path = input_cmd[8:]
            display(file_path)
        elif input_cmd == 'current':
            print(current_dir)
        elif remove_space(input_cmd) != '':
            if input_cmd.strip() != '':
                try:
                    if ' ' not in input_cmd:
                        # Execute the command without spaces as-is
                        subprocess.Popen(input_cmd, shell=True, text=True)
                    else:
                        # Split the command into arguments and execute it
                        cmd_parts = input_cmd.split()
                        subprocess.Popen(cmd_parts, text=True)
                except FileNotFoundError:
                    print('Invalid command: ' + input_cmd)

if __name__ == "__main__":
    main()
