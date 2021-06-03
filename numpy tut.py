import numpy as np

a = np.array([0,1,2,3,4])

print(np.arange(10))

L = range(1000)
timeit [i**2 for i in L]
