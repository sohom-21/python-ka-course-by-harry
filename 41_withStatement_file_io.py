# Ask the user for the string to add
st = input('Enter the string that you want to add to the text file: ')

# Ask the user for the line number where they want to insert the text (1-based index)
line_no = int(input('Enter the line number where you want to insert the text: '))

# Open the file in read mode to get all lines
with open('39_Readfile.txt', mode='r') as f:
         lines = f.readlines()  # Read all lines into a list

# Insert the new string at the desired position (adjust for 0-based index)
# Add a newline character to ensure proper formatting
lines.insert(line_no - 1, st + '\n')

# Open the file in write mode to overwrite with the updated lines
with open('39_Readfile.txt', mode='w') as f:
         f.writelines(lines)  # Write all lines back to the file

# This approach allows you to insert text at any line you want, not just append at the end.