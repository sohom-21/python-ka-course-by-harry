
# these sort of function that have a parameter value by default.
# mean that if there is no value supplied for that argument use the default value.
# Otherwise, use the value that is given during the function call.

# This is known as default parameter value:

def goodDay(name, ending='Thank you'):
    print(f'good Day {name}')
    print(ending)
    return 'done'



goodDay('harry')
goodDay('sohom', 'please come again')