# Write a program to greet all the person names stored in a list 'l' and which starts with S.
l= ["Harry", "Soham", "Sachin", "Rahul"]

for item in l:
    if item.startswith("S") or item.startswith('s'):
        print(f"Hello have a great day {item}")
    else:
        print(item)