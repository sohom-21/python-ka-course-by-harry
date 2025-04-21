# Open '35_file.txt' in read mode ('r')
f = open("35_file.txt", mode='r')
# Read the entire content of the file into a string
data = f.read()
# Print the file content and its type (should be <class 'str'>)
print(data, type(data))
# Always close the file after finishing reading/writing
f.close()

# Open another file '39_Readfile.txt' in read mode
anotherF = open('39_Readfile.txt', mode='r')

"""
# Read all lines from the file into a list, where each element is a line
lines  = anotherF.readlines()
print(lines, type(lines))  # Print the list of lines and its type

# Read one line at a time using readline()
line1 = anotherF.readline()
print(line1, type(line1))  # Print the first line and its type

line2 = anotherF.readline()
print(line2, type(line2))  # Print the second line and its type

line3 = anotherF.readline()
print(line3, type(line3))  # Print the third line and its type

line4 = anotherF.readline()
print(line4, type(line4))  # Print the fourth line and its type

line5 = anotherF.readline()
print(line5, type(line5))  # Print the fifth line and its type

line6 = anotherF.readline()
# Check if the line is empty (end of file reached)
print(line6 == "", type(line6))
"""

# Read and print each line one by one until the end of the file is reached
line1 = anotherF.readline()
while line1 != "":
    print(line1)  # Print the current line
    line1 = anotherF.readline()  # Read the next line

# Close the file after reading
anotherF.close()