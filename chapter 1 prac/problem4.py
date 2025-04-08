import os #using the OS module in python

# specify the directory you want to list
directory_path = 'C:/'
# list all the files and directories in the specified path
directory = os.listdir(directory_path)
#print each file and directory name
print(directory)