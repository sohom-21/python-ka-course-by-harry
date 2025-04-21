"""
# A file is a data Stored in a storage Device.
# A python program can talk to the file by reading contents from it and  Writing contents to it.
"""

f = open("35_file.txt", mode='r')
data = f.read()
print(data)
f.close()