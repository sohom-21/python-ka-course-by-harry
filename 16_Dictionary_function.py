marks = {
    'harry':100,
    'Shubham':56,
    'Rohan':23,
    0:'harry'
}

print(marks, type(marks)) #to check what the dictionary data type is and also print the whole dictionary
print(marks[0]) #printing specific key value pair
print(marks.items()) #items function returns entire list of items in the dictionary in form of tuples
print(marks.keys()) #prints only the key present in the dictionary as list
print(marks.values()) #prints only the values present in the dictionary as list
marks.update({"harry" : 99, 'Renuka':120}) #update a key value pair in the dictionary as it is mutable and also adds the pairs that not present in the library
print(marks)
print(marks.get('Renuka')) #returns the value of the specified keys

# chatgpt ka solution creating a dictionary using for loop
# information = {}
# n = int(input('kitne jaano ka data lena hai?'))
#
# for i in range(n):
#     name = input(f'tera naam kya hai{i+1}')
#     eknumber = input(f'number bol be {name}')
#     information[name] = eknumber
#
# print("\nFinal dictionary:")
# print(information)

marks = {}  # Step 1: Empty dictionary create kiya jisme data store hoga

n = int(input("Kitne students ka data lena hai? "))  # Step 2: User se poocha kitni entries chahiye

for i in range(n):  # Step 3: n times loop chalega
    entry = input(f"Entry {i + 1} (format: name,marks): ")  # Step 4: User se input lo, e.g., "Ramesh,88"

    name, score = entry.split(",")  # Step 5: Split kar diya comma ke basis pe → ['Ramesh', '88']

    marks[name.strip()] = int(
        score.strip())  # Step 6: strip() extra spaces hata deta hai, and score ko int mein convert kiya

print("\nFinal dictionary:")  # Step 7: Sab print karwa diya
print(marks)