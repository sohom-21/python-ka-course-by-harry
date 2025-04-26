''' Write a program to make a copy of a text file "this. txt" '''

with open('this.txt') as f:
    content = f.read()
with open('this_Copy.txt',mode='w') as f:
    f.write(content)