# The break Statement
# break is used to come out of the loop when encountered.
# It instructs the program to '''exit the loop now'''

for i in range(5):
    if i == 3:
        break #exit the loop right now
    else:
        print(i)
print('End of break example \n')

#continue is used to stop the current iteration of the loop and continues with the next one.
#It instructs the program to "skip this iteration"
for i in range(5):
    if i == 3:
        continue #skip this iteration right now
    else:
        print(i)
print('End of continue example \n')

# pass is a null statement in python.
# It instructs to do nothing
L = [1,2,5,8,9]
for i in L:
    pass # with pass the program will throw an error
print('End of pass example \n')