"""A file contains a word "Donkey" multiple times. You need to write a program which
replace this word with ##### by updating the same file."""

def word_replace():
    try:
        with open('replace_word.txt', mode='r+') as file:
            data = file.read()
            data = data.lower()
            if data != "":
                file.seek(0)
                file.write(data.replace('donkey','######').capitalize())
            else:
                filecreate()
    except FileNotFoundError:
        filecreate()
    return

def filecreate():
    with open('replace_word.txt', mode='w') as file:
        file.seek(0)
        print("Generating or creating some random lines about donkeys..... ")
        file.write('Donkey is a nice donkey \n' * 6)
        file.write('donkey works hard\n' * 4)
        file.write('donkey loves carrots\n' * 4)

def file_revert_2original():
    try:
        with open('replace_word.txt', mode='r+') as file:
            data2revert = (file.read()).lower()
            if data2revert != '':
                file.seek(0)
                file.write((data2revert.replace('######','donkey')).capitalize())
            else:
                filecreate()
    except FileNotFoundError:
        filecreate()
    return
# toh basically ye bs phele wala ko hi capitalize karega as wo pure string as whole pe kaam karta hai
# for individual lines humko loops ya recursion ka isste mal karna parega but for now this is enough
"""if __name__ == "__main__":
    print("Enter 1 to see the file change donkey to ######\n")
    print("Enter 2 to see the change get reverted back to original\n")
    print("Enter 3 to exit the program\n")
    choice = input("Enter you choice")
    if choice == "1":
        word_replace()
    elif choice == "2":
        file_revert_2original()
    elif choice == "3":
        print("Thanks for trying out this program Good Bye!!!!!")
        exit()"""

"""Harry ka solution iske niche hai """

word  = "Donkey"
with open('file.txt', mode='r') as file:
    content = file.read()

contentnew = content.replace(word, "######")

with open('file.txt', mode='w') as file:
    file.write(contentnew)
