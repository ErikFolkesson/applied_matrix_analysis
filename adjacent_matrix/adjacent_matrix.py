import numpy as np

n = 4

A = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]
]

I = np.identity(n)

result = np.linalg.matrix_power(I + A, n-1)

print(result)

#Result:
#[[12. 10. 10.  6.]
# [10.  9.  9.  4.]
# [10.  9.  9.  4.]
# [ 6.  4.  4.  4.]]