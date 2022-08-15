
import numpy as np

array = np.arange(1, 101, 1)
sq_of_sum = array.sum()**2
sum_of_sq = np.power(array, 2).sum()
print(sq_of_sum - sum_of_sq)
