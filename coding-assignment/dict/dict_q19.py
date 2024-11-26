# Create a dictionary where the keys are numbers from 1 to n and the values are their factorials

import math
n = 5
factorials = {i: math.factorial(i) for i in range(1, n + 1)}
print(factorials)