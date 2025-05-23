smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
         if smallest is None or itervar < smallest:
                  smallest = itervar
                  break
         print("Loop:", itervar, smallest)
print("Smallest:", smallest)


S=[1,2,4,1,2]
# result = list(dict.fromkeys(S))
result = [x for i, x in enumerate(S) if S.index(x) == i]
print(result) 
