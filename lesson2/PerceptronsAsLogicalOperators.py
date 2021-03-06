"""
Author: Simone Biffi
Data: 23/12/2018

"""

import pandas as pd


def and_perceptron():
    # TODO: Set weight1, weight2, and bias
    weight1 = 1.0
    weight2 = 1.0
    bias = -2.0

    # DON'T CHANGE ANYTHING BELOW
    # Inputs and outputs
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, False, False, True]
    outputs = []

    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    output_frame = pd.DataFrame(outputs, columns=['Input 1',
                                                  '  Input 2',
                                                  '  Linear Combination',
                                                  '  Activation Output',
                                                  '  Is Correct'])
    print(output_frame.to_string(index=False))


def or_perceptron():
    # TODO: Set weight1, weight2, and bias
    weight1 = 1.0
    weight2 = 1.0
    bias = -1.0

    # DON'T CHANGE ANYTHING BELOW
    # Inputs and outputs
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [False, True, True, True]
    outputs = []

    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    output_frame = pd.DataFrame(outputs, columns=['Input 1',
                                                  '  Input 2',
                                                  '  Linear Combination',
                                                  '  Activation Output',
                                                  '  Is Correct'])
    print(output_frame.to_string(index=False))


def not_perceptron():

    # TODO: Set weight1, weight2, and bias
    weight1 = 0.0
    weight2 = -1.0
    bias = 0.0

    # DON'T CHANGE ANYTHING BELOW
    # Inputs and outputs
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    correct_outputs = [True, False, True, False]
    outputs = []

    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    output_frame = pd.DataFrame(outputs, columns=['Input 1',
                                                  '  Input 2',
                                                  '  Linear Combination',
                                                  '  Activation Output',
                                                  '  Is Correct'])


if __name__ == '__main__':
    print('AND Perceptron: \n')
    and_perceptron()

    print('Or Perceptron: \n')
    or_perceptron()

    print('Not Perceptron: \n')
    not_perceptron()
