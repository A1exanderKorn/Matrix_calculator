from behave import *
from matrix_calc import *
import ast

@given('I have two matrices: {matrix1} and {matrix2}')
def step_imp1(context):
    list_variable_1 = ast.literal_eval(matrix1)
    list_variable_2 = ast.literal_eval(matrix2)
    context.matrix_1 = list_variable_1
    context.matrix_2 = list_variable_2


@when('I perform matrix addition')
def step_imp1(context):
    context.result = matrix_addition(context.matrix1, context.matrix2)
    


@then('Then the result should be {exp_res}')
def step_imp1(context):
    list_variable_res = ast.literal_eval(exp_res)
    context.expected_result = np.array(list_variable_res)
    assert np.array_equal(context.result, context.expected_result)