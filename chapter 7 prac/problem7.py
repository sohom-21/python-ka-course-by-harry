# Write a program to print the following star pattern.
# __*
# _***
# ***** for n = 3 | ( _ )'s are the space that need to be calculated

star_height_number = int(input('Decide the height of the stars in number: '))

for i in range(star_height_number):
    for k in range(star_height_number-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print('')

# but this is not the optimal code for this sort of star printing

for i in range(1, star_height_number+1):
    print(' '* (star_height_number-i), end='')
    print('*' * (2*i-1), end='')
    print('')