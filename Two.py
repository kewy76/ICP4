# Kate Williams
# 6/14/2018

import numpy as np

a = np.random.random((10, 10))  # Create random array

print("The maximum of each row is " + str(a.max(axis=1)))
print("The minimum of each row is " + str(a.min(axis=1)))