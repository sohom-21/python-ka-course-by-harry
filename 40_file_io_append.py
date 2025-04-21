# Ask the user for the string to add
st = input('Enter the string that you want to add to the text file: ')
f = open('39_Readfile.txt', mode='a')
f.write(st)
f.close()
