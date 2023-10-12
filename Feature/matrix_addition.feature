Feature: use matrix_addition method to add up matrices
    Scenario: Adding two matrices
        Given I have two matrices: [[1, 2], [3, 4]] and [[5, 6], [7, 8]]
        When I perform matrix addition
        Then the result should be [[6, 8], [10, 12]]