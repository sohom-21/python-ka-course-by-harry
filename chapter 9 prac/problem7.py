"""Write a program to find out the line number where python is present from ques 6."""
lineno = 1

def line_number():
    global lineno
    try:
        with open('filekalog.log', mode='r') as file:
            line_occurrence = file.readlines()
            for lineMeLine in line_occurrence:
                if 'python' in lineMeLine:
                    print(f"python is present in line no: {lineno}")
                    break
                lineno += 1
            else:
                print('No python is not present in the file')
    except FileNotFoundError:
        print(f'Something went wrong {FileNotFoundError}')

line_number()