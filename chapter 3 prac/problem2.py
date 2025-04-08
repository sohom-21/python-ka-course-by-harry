letter = '''
        Dear <|Name|>,
        you are selected!
        <|Date|>
         '''
# write a program to fill in a letter template given below with name and date
Name = input('Enter your name')
Date = input('Enter today\'s date')
print((letter.replace("<|Name|>",Name)).replace('<|Date|>',Date))