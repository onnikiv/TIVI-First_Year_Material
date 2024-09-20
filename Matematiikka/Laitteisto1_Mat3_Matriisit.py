import numpy as np


# 1.tehtävä a)
T1_A_1 = np.array([[-1, 2], [3, 1]])
T1_A_2 = np.array([[0, 1, 3], [2, -3, 5]])
A12 = np.dot(T1_A_1, T1_A_2)

print(f"1. a) Matriisin vastaus:\n{A12}\n")

#-----------------------

# 1.tehtävä b)
T1_B_1 = np.array([[1, 3, 5], [0, -2, 1],[2, -1, 4]])
T1_B_2 = np.array([[1], [-3], [-1]])
B12 = np.dot(T1_B_1, T1_B_2)

print(f"1. b) Matriisin vastaus:\n{B12}\n")

#-----------------------

# 1.tehtävä c)
T1_C_1 = np.array([[2, 0, 1], [1, -3, 4],[0, 1, 5]])
T1_C_2 = np.array([[3], [-5], [7]])
C12 = np.dot(T1_C_1, T1_C_2)

print(f"1. c) Matriisin vastaus:\n{C12}\n")

#-----------------------

# 1.tehtävä d)
T1_D_1 = np.array([[1, -4, 2], [3, 0, -2],[2, 1, 0]])
T1_D_2 = np.array([[5, 1, -1], [-2, 1, 3],[0, 3, 4]])
D12 = np.dot(T1_D_1, T1_D_2)

print(f"1. d) Matriisin vastaus:\n{D12}\n")

