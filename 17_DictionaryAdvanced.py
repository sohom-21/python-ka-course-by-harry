# Clear method in dictionary clear()
# -removes all the elements from the dictionary.
marks = {
    'Harry':100,
    'Rajesh':80,
    'Sumir':70
}
old_marks = marks.copy()

marks.clear()
print(marks)
print(old_marks)
old_marks.popitem() #popitem to remove a key value pair
print(old_marks)
old_marks.pop('Rajesh') #pop to remove a specific key value pair
print(old_marks)
