import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?
print(len(a[a < 0]))


# 2. How many positive numbers are there?
print(len(a[a > 0]))


# 3. How many even positive numbers are there?
print(len(a[(a % 2 == 0) & (a > 0)]))


# 4. If you were to add 3 to each data point, how many positive numbers would there be?
print(len(a[(a+3) > 0]))


# 5. If you squared each number, what would the new mean and standard deviation be?
print(f"The new mean would be {(a**2).mean()} and the new standard deviation would be {(a**2).std()}")