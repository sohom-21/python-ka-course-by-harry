
s = {1,2,3,3,5,5,8}
print(s, type(s))

#length property
# returns the length  of the set
print(len(s))

#functions
# 1. add(elem)
# Ek element add karta hai set me.

s.add(int(input('Enter a number of your choice')))
print(f'Sets is {s}')
# This is the output
# Enter a number of your choice6
# Sets is {1, 2, 3, 5, 6, 8}

# 2. remove(elem)
# Element hataata hai, agar element nahi mila toh error deta hai.
s.remove(5)
print(s) #{1, 2, 3, 6, 8}

# 3.discard(elem)
#Same as remove(), lekin error nahi deta agar element na mile.
s.discard(20)
print(s)

# 4.pop()
# Set se random element hataata hai, aur usko return bhi karta hai.
value = s.pop()
print(f'the Value that was popped out form the set {s} is {value}')

# # 5.clear()
# # poora set empty kar deta hai
# s.clear()
# print(s) # set() returned empty set

#6.union(set2) or |
# Do sets ka combination deta hai (duplicates hata ke).
b = {1,2,3,6,10,40,70,80,120,100}
print(s.union(b)) #{1, 2, 3, 100, 6, 70, 40, 10, 80, 120}
print( s | b)

# 7.intersecion(sets) or &
#Common elements return karta hai.
print(s.intersection(b))
print(s & b)

# 8.difference(set2) or -
#set a me jo hai but set b me nahi, wo deta hai.
print(s.difference(b))
print( s - b)
print(b - s)

#symmetric_difference(set2) or ^
# Aise elements jo sirf ek set me hain, dono me nahi.

set1 = set([1, 2, 3])
set2 = set([3, 4, 5])

print(set1 & set2)  # Intersection
print(set1 | set2)  # Union
print(set1 - set2)  # Difference
print(set1 ^ set2)  # Symmetric Difference

print(s.issubset(b))
print(s.issuperset(b))
