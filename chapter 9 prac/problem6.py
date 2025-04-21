"""Write a program to mine a log file and find out whether it contains 'python'."""

def file_create(file_name):
         with open(file_name, mode='w') as file:
                  file.write(input('Enter the paragraph that you want to have for your log file: '))
         choice = input('Do you wish to check the file now ??(y/n): ')
         if(choice == 'y'):
                  file_check(file_name)

def file_check(file_name,searchWord='python'):
         try:
                  with open(file_name, mode='r+')as file:
                           data = file.read().lower()
                  if(data == ''):
                           file_create(file_name)
                  elif(searchWord in data):
                           print(f"This file {file_name} contains the word python in it")
                  else:
                           print(f"This file {file_name} does not contain the word python in it")
         except FileNotFoundError:
                  file_create(file_name)

if __name__ == "__main__":
         file_name = input('Enter your file name: ').strip()
         file_check(file_name)