import numpy as np
arr = np.array([10,20,30,40])
# toh humlog arrays ko ese declare karte hai
print(f'The type of {type(arr)}')
# yaha array ka class ye aaraha hai <class 'numpy.ndarray'>
# nd ka matlab n-dimentional array hota hai
print(f'The array that is formed is {arr}')

# So humlog log ek n-dimentional array kese bana enge wo dekhte hai

n_array = np.array([[10,20,30,40],[50,60,70,80]])
print(n_array)
# remember agr n_dimentional array me saare ke saare columns same nahi hai toh error aajata hai
"""
n_array1 = np.array([[10,20,30,40],[50,60,80],[20,40,50,70]])
print(n_array1)

            YE HAI ISKA OUTPUT ERROR DEKH NA .......
n_array1 = np.array([[10,20,30,40],[50,60,80],[20,40,50,70]])
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (3,) + inhomogeneous part.
"""
