#set is a collection of well-defined objects
# - and is a collection of non-repetitive elements
sets = {1,2,3,4,5}
print(type(sets))

# to make an empty set we must write in the following manner as just using {} will make it a empty dict not sets
marks = set() #this should make it an empty set
print(marks, type(marks))

# so why use sets in python because unlike dictionary and lists sets don't allow value or element repetition
mark = {1, 2, 4, 4, 9, 8}
print(mark) #{1, 2, 4, 8, 9} see how 4 is printed only once despite having 4 two times in the set

# sets are unordered
# sets are unindexed
# there is no way to change items in sets
# sets cannot contain duplicate values