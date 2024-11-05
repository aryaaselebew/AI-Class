#Arya Nanda Putra | Nim: F55123087 | Kelas: C
import numpy as np

A = np.array([[3, 0], [-1, 2], [1, 1]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

print("Versi Menggunakan Library")

AC = np.dot(A, C)
D_plus_E = D + E
D_minus_E = D - E

print("Perkalian A dan C:\n", AC)
print("\nPenjumlahan D + E:\n", D_plus_E)
print("\nPengurangan D - E:\n", D_minus_E)

try:
    AD = np.dot(A, D)
except ValueError as e:
    print("\nPerkalian A dan D menghasilkan error:", e)

print("\nVersi Tanpa Library")

def matrix_multiplication(mat1, mat2):
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])
    
    if cols_mat1 != rows_mat2:
        raise ValueError("Dimensi matriks tidak cocok untuk perkalian.")
    
    result = [[0] * cols_mat2 for _ in range(rows_mat1)]
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

def matrix_addition(mat1, mat2, subtract=False):
    rows = len(mat1)
    cols = len(mat1[0])
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if subtract:
                result[i][j] = mat1[i][j] - mat2[i][j]
            else:
                result[i][j] = mat1[i][j] + mat2[i][j]
    return result

A_list = [[3, 0], [-1, 2], [1, 1]]
C_list = [[1, 4, 2], [3, 1, 5]]
D_list = [[1, 5, 2], [-1, 0, 1], [3, 2, 4]]
E_list = [[6, 1, 3], [-1, 1, 2], [4, 1, 3]]

AC_list = matrix_multiplication(A_list, C_list)

D_plus_E_list = matrix_addition(D_list, E_list)
D_minus_E_list = matrix_addition(D_list, E_list, subtract=True)

print("Perkalian A dan C:\n", AC_list)
print("\nPenjumlahan D + E:\n", D_plus_E_list)
print("\nPengurangan D - E:\n", D_minus_E_list)

try:
    AD_list = matrix_multiplication(A_list, D_list)
except ValueError as e:
    print("\nPerkalian A dan D menghasilkan error:", e)
