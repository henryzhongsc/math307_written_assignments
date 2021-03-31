import numpy as np

input = [2, 4, -11, 4, -9, 4, -1, 6, 2, -1, 1, 5, 6, -7, -8, -20, 20, 2, -2, 0]

A = np.asarray(input)
A = np.reshape(A, (4, 5))

# print(A)
for i in [1, 2, np.inf]:
    result = np.linalg.norm(A, i)
    print(f'{i} norm = {result}')


power_2_sum = 0
for i in input:
    power_2_sum += abs(i)**2

print(power_2_sum)