"""write a program to replace some certain words in a file for a list of such words to be censored."""
def word_replace(file_name, words_list):
    try:
        with open(file_name, mode='r+') as file:
            data = file.read() # Reads the entire file content
            file.seek(0) # Move cursor to start for reading lines
            lines = file.readlines() # But after .read(), file pointer is at end, so this returns []
            # Problem: After file.read(), file.readlines() returns empty list.
            # Solution: Only use one of them, or re-open file for reading lines.
            if not(lines == ""):
                file.seek(0)
                file.truncate()  # clear previous content
                for line in lines:
                    updated_line = line.lower()
                    for word in words_list:
                        updated_line = updated_line.replace(word.lower(), '#'*len(word) )
                    file.write(updated_line.capitalize())
            with open(f"copy of {file_name}", mode='w') as f:
                f.write(data)        
    except FileNotFoundError:
        file_create(FileNotFoundError, file_name)

def file_revert_2original(file_name):
    with open(f'copy of {file_name}', mode='r') as f:
        data = f.read()
    with open(file_name, mode='w') as file:
        file.seek(0)
        file.truncate()
        file.write(data)

def file_create(arg, filename):
    if(arg == FileNotFoundError):
        file_name = filename
        with open(file_name, mode='w') as file:
            file.seek(0)
            file.write(input("Enter a paragraph or a series of multiple lines: "))
    return file_name

if __name__ == "__main__":
    File_name = input("Enter the name of your file: ")
    print("Enter 1 to see the file change donkey to ######\n")
    print("Enter 2 to see the change get reverted back to original\n")
    print("Enter 3 to exit the program\n")
    choice = input("Enter you choice")
    if choice == "1":
        words_list = list(input('Enter a list of words separated by comma to be censored: ').strip().split(','))
        word_replace(File_name, words_list)
    elif choice == "2":
        file_revert_2original(File_name)
    elif choice == "3":
        print("Thanks for trying out this program Good Bye!!!!!")
        exit()