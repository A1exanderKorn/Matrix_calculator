import numpy as np

def matrix_addition(matrix1, matrix2):
    if type(matrix1) is not list or type(matrix1) is not list:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix1)
    matrix_2 = np.array(matrix2)
    return np.add(matrix_1, matrix_2)

def matrix_subtraction(matrix1, matrix2):
    if type(matrix1) is not list or type(matrix1) is not list:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix1)
    matrix_2 = np.array(matrix2)
    return np.subtract(matrix_1, matrix_2)

def matrix_multiplication(matrix1, matrix2):
    if type(matrix1) is not list or type(matrix1) is not list:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix1)
    matrix_2 = np.array(matrix2)
    return np.matmul(matrix_1, matrix_2)

def matrix_transpose(matrix):
    if type(matrix) is not list:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix)
    return np.array(np.transpose(matrix_1))

def matrix_inverse(matrix):
    if type(matrix) is not list:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix)
    return np.linalg.inv(matrix_1).astype(int)

def matrix_squared(matrix):
    if type(matrix) is not list:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix)

    return np.matmul(matrix_1, matrix_1)

def matrix_pow(matrix1, pow):
    if type(matrix1) is not list or type(pow) is not int:
        raise TypeError("wrong type")
    matrix_1 = np.array(matrix1)
    result = matrix_1
    for i in range(1, pow):
        result = np.matmul(result, matrix_1)
    return result

def create_sparse_matrix(matrix):
    sparse_matrix = []
    if type(matrix) is not list:
        raise TypeError("wrong type")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                sparse_matrix.append([i, j, matrix[i][j]])
    
    return np.array(sparse_matrix)

# print(create_sparse_matrix([[1, 2], [3, 4]]))
# if __name__ == '__main__':
#     matrix1 = []
#     matrix2 = []
#     while(True):
#         if matrix1 == []:
#             matrix1 = input("print matrix_1 ")
#         matrix2 = input("print matrix_2 ")
#         s = input("0 - exit; 1 - matrix_addition; 2 - matrix_subtraction; 3 - matrix_multiplication; 4 - matrix_transpose; 5 - matrix_inverse ")
#         if s == "0":
#             quit()
#         elif s == "1":
#             print("Matrix Addition:")
#             matrix1 = matrix_addition(matrix1, matrix2)
#             print(matrix1)
#         elif s == "2":
#             print("Matrix Addition:")
#             matrix1 = matrix_subtraction(matrix1, matrix2)
#             print(matrix1)
#         elif s == '3':
#             print("Matrix Addition:")
#             matrix1 = matrix_multiplication(matrix1, matrix2)
#             print(matrix1)
#         elif s == '4':
#             print("Matrix Addition:")
#             matrix1 = matrix_transpose(matrix1)
#             print(matrix1)
#         elif s == '5':
#             print("Matrix Addition:")
#             matrix1 = matrix_inverse(matrix1)
#             print(matrix1)

# matrix1 = np.array([[1, 2], [3, 4]])
# matrix2 = np.array([[5, 6], [7, 8]])

# print("Matrix Addition:")
# print(matrix_addition(matrix1, matrix2))

# print("Matrix Subtraction:")
# print(matrix_subtraction(matrix1, matrix2))

# print("Matrix Multiplication:")
# print(matrix_multiplication(matrix1, matrix2))

# print("Matrix Transpose:")
# print(matrix_transpose(matrix1))

# print("Matrix Inverse:")
# print(matrix_inverse(matrix1))