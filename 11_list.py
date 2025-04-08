
#list are containers to store a set of values of any data type
friends = ['Apple','Orange',5,346.5,False,"Aakash","Rohan"]
print(friends[0])

friends[0] = 'Grapes' #unlike strings lists are mutable and a List can be indexed just like a string
print(friends)

print(friends[3:6])
print(friends[0:7:2]) #just like the string we can also slice and skip value in lists