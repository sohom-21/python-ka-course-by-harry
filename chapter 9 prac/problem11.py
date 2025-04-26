"""Write a python program to rename a file to 'renamed_by_python.txt'."""
import shutil

old_file = input("Enter the name of the file you want to rename: ").strip()
new_file = "renamed_by_python.txt"

try:
    shutil.move(old_file, new_file)
    print(f"File renamed to {new_file}")
except FileNotFoundError:
    print("The file does not exist.")
