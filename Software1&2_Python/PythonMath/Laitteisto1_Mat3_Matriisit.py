import numpy as np
print("-----------------------------------------------------")
print("1.Tehtävä:")
# 1. A
T1_A_1 = np.array([[-1, 2], [3, 1]])
T1_A_2 = np.array([[0, 1, 3], [2, -3, 5]])
A12 = np.dot(T1_A_1, T1_A_2)
print(f"1.A Matriisin vastaus:\n{A12}\n")
# 1. B
T1_B_1 = np.array([[1, 3, 5], [0, -2, 1],[2, -1, 4]])
T1_B_2 = np.array([[1], [-3], [-1]])
B12 = np.dot(T1_B_1, T1_B_2)
print(f"1.B Matriisin vastaus:\n{B12}\n")
# 1. C
T1_C_1 = np.array([[2, 0, 1], [1, -3, 4],[0, 1, 5]])
T1_C_2 = np.array([[3], [-5], [7]])
C12 = np.dot(T1_C_1, T1_C_2)
print(f"1.C Matriisin vastaus:\n{C12}\n")

# 1. D
T1_D_1 = np.array([[1, -4, 2], [3, 0, -2],[2, 1, 0]])
T1_D_2 = np.array([[5, 1, -1], [-2, 1, 3],[0, 3, 4]])
D12 = np.dot(T1_D_1, T1_D_2)
print(f"1.D Matriisin vastaus:\n{D12}\n")
print("-----------------------------------------------------")
# 3. TEHTÄVÄ
A = np.array([[1, 2, 3], [1, 0, -2]])
B = np.array([[1], [4], [2]])
C = np.array([[1,0,2]])

AB = np.dot(A,B)
#BA = np.dot(B,A)
#AC = np.dot(A,C)
#CA = np.dot(C,A)
BC = np.dot(B,C)
CB = np.dot(C,B)
print("3.Tehtävä:\nMahdolliset matriisien tulot ovat:")
print(f"\nAB:\n{AB}\n\nBC:\n{BC}\n\nCB:\n{CB}\n")
print("-----------------------------------------------------")
#5.TEHTÄVÄ

viis_a = np.array([[1, 1/2], [2, 1]])
viis_b = np.array([[-1, -2], [2, 4]])

viis_ab = np.dot(viis_a, viis_b)
viis_ba = np.dot(viis_b, viis_a)
print(f"5.Tehtävä:\nAB:\n{viis_ab}\nBA:\n{viis_ba}")
print("-----------------------------------------------------")