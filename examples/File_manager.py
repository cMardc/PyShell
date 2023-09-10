#!/bin/python3

from main import mv, cp, rm, rmdir, view, create_file, create_folder
import os


def main():
    print("Welcome to the File Manager!")

    while True:
        print("\nMenu:")
        print("1. Move a file/directory")
        print("2. Copy a file")
        print("3. Remove a file/directory")
        print("4. List contents of a directory")
        print("5. Create an empty file")
        print("6. Create a folder")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            source = input("Enter the source path: ")
            destination = input("Enter the destination path: ")
            mv(source, destination)
        elif choice == "2":
            source = input("Enter the source file path: ")
            destination = input("Enter the destination path: ")
            cp(source, destination)
        elif choice == "3":
            file_or_directory = input("Enter the path to remove: ")
            if os.path.isfile(file_or_directory):
                rm(file_or_directory)
            elif os.path.isdir(file_or_directory):
                rmdir(file_or_directory)
        elif choice == "4":
            directory = input("Enter the directory path: ")
            contents = view(directory)
            print("\nContents of the directory:")
            for item in contents:
                print(item)
        elif choice == "5":
            file_name = input("Enter the name of the file to create: ")
            create_file(file_name)
        elif choice == "6":
            folder_name = input("Enter the name of the folder to create: ")
            create_folder(folder_name)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
