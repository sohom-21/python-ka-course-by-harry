"""Write a program to find out whether a file is identical & matches the content of another file."""

with open('this.txt') as f:
    content = f.read()
with open('this_Copy.txt') as f:
    content2 = f.read()

if content == content2:
    print('yes these files are indentical')
else:
    print('no these files are indentical')
