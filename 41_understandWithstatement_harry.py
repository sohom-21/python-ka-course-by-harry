f = open("37_myExp_file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("37_myExp_file.txt") as f:
         print(f.read())

# you don't have to explicitly close the file,
# The with statement which a best tool or syntactic sugar does it automatically.
"""
# Now going back to the file 41_withStatement_file_io.py
# lets understand how we can write or append at any desired line we wish in a file.
"""