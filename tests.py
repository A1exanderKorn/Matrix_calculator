import unittest
import numpy as np
from Feature.steps.matrix_calc import *

class MatrixCalculatorTest(unittest.TestCase):
    # def test_matrix_addition(self):
    #     matrix1 = [[1, 2], [3, 4]]
    #     matrix2 = [[5, 6], [7, 8]]
    #     expected_result = np.array([[6, 8], [10, 12]])
    #     result = matrix_addition(matrix1, matrix2)
    #     self.assertTrue(np.array_equal(result, expected_result))
    # def test_matrix_addition_wrongtype(self):
    #     matrix1 = "[1, 2], [3, 4]]"
    #     matrix2 = "[[5, 6], [7, 8]]"
    #     with self.assertRaises(TypeError):
    #         matrix_addition(matrix1, matrix2)
    #     self.assertRaises(TypeError)

    # def test_matrix_subtraction(self):
    #     matrix1 = [[1, 2], [3, 4]]
    #     matrix2 = [[5, 6], [7, 8]]
    #     expected_result = np.array([[-4, -4], [-4, -4]])
    #     result = matrix_subtraction(matrix1, matrix2)
    #     self.assertTrue(np.array_equal(result, expected_result))
    # def test_matrix_subtraction_wrongtype(self):
    #     matrix1 = "[1, 2], [3, 4]]"
    #     matrix2 = "[[5, 6], [7, 8]]"
    #     with self.assertRaises(TypeError):
    #         matrix_subtraction(matrix1, matrix2)
    #     self.assertRaises(TypeError)

    # def test_matrix_multiplication(self):
    #     matrix1 = [[1, 2], [3, 4]]
    #     matrix2 = [[5, 6], [7, 8]]
    #     expected_result = np.array([[19, 22], [43, 50]])
    #     result = matrix_multiplication(matrix1, matrix2)
    #     self.assertTrue(np.array_equal(result, expected_result))
    # def test_matrix_multiplication_wrongtype(self):
    #     matrix1 = "[1, 2], [3, 4]]"
    #     matrix2 = "[[5, 6], [7, 8]]"
    #     with self.assertRaises(TypeError):
    #         matrix_multiplication(matrix1, matrix2)
    #     self.assertRaises(TypeError)

    # def test_matrix_transpose(self):
    #     matrix1 = [[1, 2], [3, 4]]
    #     expected_result = np.array([[1, 3], [2, 4]])
    #     result = matrix_transpose(matrix1)
    #     self.assertTrue(np.array_equal(result, expected_result))
    # def test_matrix_transpose_wrongtype(self):
    #     matrix1 = "[1, 2], [3, 4]]"
    #     with self.assertRaises(TypeError):
    #         matrix_transpose(matrix1)
    #     self.assertRaises(TypeError)

    def test_matrix_inverse(self):
        matrix1 = [[3, -5], [1, -2]]
        expected_result = "[[ 3  1]\n [-5 -2]]"
        result = str(matrix_transpose(matrix1))
        self.assertTrue(np.array_equal(result, expected_result))
    def test_matrix_inverse_TypeError(self):
        matrix1 = "[1, 2], [3, 4]]"
        with self.assertRaises(TypeError):
            matrix_inverse(matrix1)
        self.assertRaises(TypeError)

    def test_matrix_squared(self):
        matrix1 = [[1, 2], [3, 4]]
        expected_result = "[[ 7 10]\n [15 22]]"
        result = str(matrix_squared(matrix1))
        self.assertTrue(np.array_equal(result, expected_result))
    def test_matrix_squared_TypeError(self):
        matrix1 = "[1, 2], [3, 4]]"
        with self.assertRaises(TypeError):
            matrix_squared(matrix1)
        self.assertRaises(TypeError)

    def test_matrix_pow(self):
        matrix1 = [[1, 2], [3, 4]]
        expected_result = "[[ 37  54]\n [ 81 118]]"
        result = str(matrix_pow(matrix1, 3))
        self.assertTrue(np.array_equal(result, expected_result))
    def test_matrix_pow_TypeError(self):
        matrix1 = "[1, 2], [3, 4]]"
        with self.assertRaises(TypeError):
            matrix_pow(matrix1, 3)
        self.assertRaises(TypeError)

    def test_sparse_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        expected_result = np.array([[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4]])
        result = create_sparse_matrix(matrix1)
        self.assertTrue(np.array_equal(result, expected_result))
    def test_sparse_matrix_TypeError(self):
        matrix1 = "[1, 2], [3, 4]]"
        with self.assertRaises(TypeError):
            create_sparse_matrix(matrix1)
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()