"""# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'."""

f = open("poem.txt",mode='r')
data = f.read()
if "Twinkle" in data:
    print("Twinkle is present in the data in the file \n")
    print(data)
else:
    print("The word is not present in this file")
f.close()