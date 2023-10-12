import unittest
import numpy as np
from matrix_calc import *

class MatrixCalculatorTest(unittest.TestCase):
    def test_matrix_addition(self):
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6], [7, 8]])
        expected_result = np.array([[6, 8], [10, 12]])

        result = matrix_addition(matrix1, matrix2)

        self.assertTrue(np.array_equal(result, expected_result))

if __name__ == '__main__':
    unittest.main()