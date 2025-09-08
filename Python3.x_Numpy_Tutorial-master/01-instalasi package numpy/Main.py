import numpy as np

a = np.array([1,2,3,4,5])
b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array([(1,4,2,12), (2,3,4,10)])

print(a)
print(b, b[0][0])
print(c, c[0][0])

a = a + 1
b = b + [1]

print(a)
print(b)