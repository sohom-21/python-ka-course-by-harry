
# ***** Since list are mutable whatever function or methods are used on it changes the list completely unlike strings that would return us a new string *****

l1 = [7,9,"orange",'grapes',80.9]
l2 = [54,7,9,3,16,5,20]
#print(l1.sort()) # cannot use sort method in list where both int and str is present
l2.sort() #updates the list to [3, 5, 7, 9, 16, 20, 54] or more appropriate word would be to arrange in ascending order
print(l2)

l2.reverse() #updates the list [54, 20, 16, 9, 7, 5, 3] or more appropriate word would be to arrange in reverse order
print(l2)

l2.append(230) #adds the element(230) to the end of list [54, 20, 16, 9, 7, 5, 3, 230]
print(l2)

l2.insert(0,75) #adds an element at a given index
# Here it adds element 20 in index 0 of the list

c = l2.pop() #removes an element from the list when no index is specified it will remove from the end of the list
print(f"{c} is the element that is removed and the updated list is {l2}")

d = l2.pop(0) #removes the element at the specified index and ****returns the Value***
print(f'{d} is the element at index 0 that was removed and the updated list is {l2}')

l2.remove(20) #removes a desired element from the list
print(f'20 is the element that was removed and the updated list is {l2}')

length = len(l1) #just like in strings we can also use len function to find out the length of a list
print(length)

minimum_value = min(l2) # returns the smallest value present in a list
print(minimum_value)

maximum_value = max(l2) #returns the largest value present in a list
print(maximum_value)

#Similar to min() and max(), sum() returns the sum of all elements in a list. This works when the elements are numeric.
total = sum(l2)
print(total)