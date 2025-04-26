"""Write a program to wipe out the content of a file using python."""

def wipe_file(file_name):
         with open(file_name, mode='w') as file:
                  file.seek(0)
                  file.truncate()
                  # or 
                  # file.write('')

wipe_file('this.txt')