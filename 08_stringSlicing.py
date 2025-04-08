Name = 'Sohom' #Strings are immutable meaning they cannot be changed after they have been defined,
# so in the string sohom i cannot replace the o with i sihim

Name_Short = Name[0:3]  #sl = name[start_index:End_index] The String Start Index is 0 and goes till End Index (length of String or desired length)
print(Name_Short)
Name_Short = Name[0:5] #sl = name[start_index:End_index] The String Start Index is 0 and goes till End Index (length of String)
print(Name_Short)

# length of a string can be found out by a function called len
length_of_String_Name = len(Name)
print(length_of_String_Name)
