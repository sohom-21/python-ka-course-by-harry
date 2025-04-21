"""
#3. Write a program to generate multiplication tables from 2 to 20 and write it to the
 different files. Place these files in a folder for a 13 - year old.
"""

def generate_tables(n, times=10):
    table = ''
    for i in range(1, times+1):
        table += f"{n} x {i} is {n*i}\n"

    with open(f'tables/{n}multiples.txt', mode='w') as file:
        file.write(table)

times  = int(input('Enter the number, till the times you want to see the multiplications: '))
for i in range(2, 21):
    generate_tables(i, times)