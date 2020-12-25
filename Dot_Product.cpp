



import numpy as np

a = [ 1, 2, 3, 4 ]
b = [ 1, 2, 3, 4 ]
print("This is a list ")
print(a)
print(b)
print("----------")
print("This is a NP array ")
a = np.array([a])
b = np.array([b]).T
print(a)
print(b)

output = np.dot( a, b )
print(output)

