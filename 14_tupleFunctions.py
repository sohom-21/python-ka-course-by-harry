#tuple is an immutable data type in python

a = (1, 2, 3, 5, 7, 7, False, "Rohan", "Shiva")
b = (1, 6, 4, 7, 8, 20, 50, 25, 16, 17)
c = (3,)  #to form a tuple consisting of a single element we must specify with ',' after element
print(type(a))  #<class 'tuple'>

no = a.count(7)  #since tuple is an immutable datatype in python; the count returns how many times a particular element occurs in the tuple
print(no)

tuple_Index = a.index(7)  # returns the first index of the first occurrence of a specified value in the tuple. Raises a 'Value Error' if not found
print(tuple_Index)

try:
    tuple_Index = a.index(8)  #since this will give value error to avoid the program from crashing directly
    # it is written like this in a try block
    print(f"Index of 8: {tuple_Index}")
except ValueError:
    print("Value 8 not found in the tuple.")

# Tuple Concatenation
concat = a + b
print(concat)

# length function in tuples
length = len(concat)  # just like in strings and list we can also use the len function in tuples
print(length)

#These functions return the smallest and largest element of a tuple, respectively.
# They work only for tuples containing comparable elements.

minimum_value = min(b)  # returns the smallest value present in a tuple
print(minimum_value)

maximum_value = max(b)  #returns the largest value present in a tuple
print(maximum_value)

#Similar to min() and max(), sum() returns the sum of all elements in a tuple. This works when the elements are numeric.
a = (1, 2, 3, 4, 5)
total = sum(a)
print(total)  # Output: 15

#tuple slicing
a = (10, 20, 30, 40, 50)
sliced_tuple = a[1:4]  # Slicing from index 1 to 3
print(sliced_tuple)  # Output: (20, 30, 40)

#tuples formation through repetition
a = (1, 2)
repeated = a * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)

#in operator
a = (1, 2, 3, 4, 5)
is_present = 3 in a
print(is_present)  # Output: True

# tuple unpacking
my_tuple = (1, 2, 3)
j, k, l = my_tuple #assigns 1 in j,2 in k,3 in l
print(j, k, l)

# reverse tuples
print(reversed(b)) #output <reversed object at 0x000002A1771A6350>

# reverse tuple list
print()