name = '''Sohom ghosh'''
var = 123
white_spaced_text = '''  Python3.12.6   '''

print(str(var)) # '123' <-----output
#coverts an object to a string

print(len(name)) #11 <-----output
# prints the length of  a string

print(name.endswith('sh')) #True <-----output
# prints whether the string ends with  a particular string character; returns true or false
# remember both the functions are extremely case-sensitive

print(name.startswith('s')) #False <-----output
# prints whether the string starts with  a particular string or character; returns true or false
# remember both the functions are extremely case-sensitive

print(name.capitalize()) #Sohom ghosh <---output
# capitalize() function returns the capitalized first alphabet of the string

print(name.title()) #Sohom Ghosh <---output
# title() function returns the capitalized first alphabet of each word in the string

print(name.upper()) #SOHOM GHOSH <---output
#upper() returns the string in Upper case

print(name.lower()) #sohom ghosh <---output
#lower() returns the string in lower case

print(name.count('o')) #3 <-----output
# prints the number of time a particular character occurs within a string

print(name.replace("ghosh", "paul")) #Sohom paul <-----output
# This function replaces the old word with new word in the entire string

print(white_spaced_text.strip())
#removes leading and trailing WhiteSpace from a String

print(white_spaced_text.lstrip())
#removes leading WhiteSpace from a String

print(white_spaced_text.rstrip())
#removes trailing WhiteSpace from a String

print(name.split()) #['Sohom', 'ghosh'] <-----output
# splits the string at the specified seperator and returns a list

print(name.split('o')) #['S', 'h', 'm gh', 'sh'] <-----output
# splits the string at the specified seperator and returns a list
