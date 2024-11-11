import numpy as np
[]

def is_floats(x) -> bool:
    """Helper function to check float values for comparison"""
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False

def assertion(out, exp, atol):
    """Custom assertion function that handles float comparisons"""
    # Special handling for booleans
    if isinstance(out, bool) or isinstance(exp, bool):
        assert out == exp, f"out: {out}, exp: {exp}"
        return
        
    # Float comparison setup
    if atol == 0 and is_floats(exp):
        atol = 1e-6
    
    # Handle set conversion for sequences
    if isinstance(out, (list, tuple)) and isinstance(exp, (list, tuple)):
        out = set(out)
        exp = set(exp)
    
    # Do the actual comparison
    if out != exp and atol != 0:
        assert np.allclose(out, exp, rtol=1e-07, atol=atol)
    else:
        assert out == exp, f"out: {out}, exp: {exp}"

# Test data
inputs = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 4, 6, 8]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 7]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7]], [[], []], [[], [1, 2, 3]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9, 11]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15]], [[1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10], [2, 5, 8]], [[1, 'apple', [1, 2], [3, 4], {'name': 'John'}, 5.5], [2, 'apple', [3, 4], {'name': 'John'}, 5.5]], [[], [1, 2, 3, 4, 5]], [[], [1, 'a', [2, 3], {'name': 'John'}]], [[2, 4, 6, 8, 'abc'], ['abc', 4.5, 'xyz']], [['apple', 'banana', ['orange', 'grape'], 10], [['orange', 'grape'], 'pineapple', 10, 20]], [[[1, 2], [3, 4], [5, 6]], [[3, 4], [7, 8], [9, 10]]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 7, 5]], [[94.69906992408676], [1, 2, 3, 4, 5]], [[1, 3, 5, 7], [1, 3, 5, 7]], [[], [1, 2, 3, 4, 5, 2]], [[], [0, 3]], [[1, 3, 5, 7, 1], [1, 3, 5, 7, 1]], [['iip', 'grape', 'grape'], [1, 2, 3, 4, 5, 2]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [8, 5, 7]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [7, 5]], [[1, 3, 5, 7, 10, 11], [1, 3, 5, 7, 10, 11]], [[[4, 10, 4], [3, 4], [7, 8], [4, 10, 4]], [[4, 10, 4], [3, 4], [7, 8], [4, 10, 4]]], [[2, 4, 6, 8, 8], [2, 4, 6, 8, 8]], [[1, 'apple', [1, 2], [3, 4], {'name': 'John'}, 5.5], [2, 'apple', [3, 4], {'name': 'John'}, 5.5, 5.5]], [[1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10], [2, 5, 8, 8]], [[1, 0, 3, 5, 7], [1, 0, 3, 5, 7]], [[[1, 2], [3, 4], [5, 6]], [[3, 4, 4], [3, 4, 4], [7, 8], [9, 10]]], [[2, 4, 6, 8, 'abc'], ['grapeabc', 'abc', 4.5, 'xyz']], [['John'], [1, 2, 3, 4, 5, 2]], [[1, 3, 5, 7, 1, 7], [1, 3, 5, 7, 1, 7]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[94.69906992408676, 5, 5, False, [4.5, [31, -44, 5, 56, 0, 12, 75], True, None], True, 12, 7], []], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 7, 9, 11, 11]], [[1, 'apple', [1, 2], [3, 4], {'name': 'John'}, 5.5], ['apple', 94.69906992408676, 4.5, [3, 4], {'name': 'John'}, 5.5, 5.5, {'name': 'John'}]], [[1, 3, 7], [1, 3, 7]], [[1, 3, 3, 3], [1, 3, 3, 3]], [[2, 4, 6, 8, 'abc', 8], [2, 4, 6, 8, 'abc', 8]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 2, 7]], [[3, 5, 7], [3, 5, 7]], [[10, 9, 8, 7, 6, 1, 5, 4, 3, 2, 1], [5, 7]], [[[3, 4], [7, 8], [4, 10, 4], [4, 10, 4]], [[3, 4], [7, 8], [4, 10, 4], [4, 10, 4]]], [[10, 9, 8, 7, 6, 5, 3, 2, 1], [10, 9, 8, 7, 6, 5, 3, 2, 1]], [[1, 2, 2, 1], [1, 2, 2, 1]], [[2, 3, 5, 6, 7, 8, 9, 10], [2, 3, 5, 6, 7, 8, 9, 10]], [['applegrape', 'iip', 'applegrae', 'grape', 'grape', 'grape'], [1, 2, 3, 4, 5, 2]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 5], [7, 5]], [[1, 2, 3, 4, 5], []], [[[3], [7, 8], [9, 10], [9, 10]], [[3], [7, 8], [9, 10], [9, 10]]], [[2, 4, 6, 8, 'abc', 6], ['abc', 4.5, 'xyz']], [[[1, 2], [3, 4], [5, 6]], [[3, 4, 4, 4], [3, 4, 4, 4], [7, 8], [9, 10], [3, 4, 4, 4]]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1], [8, 5, 7]], [[5, 7], [5, 7]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]], [[3, 5, 7, 7], [3, 5, 7, 7]], [[10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1], [10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1]], [[[1, 2], [3, 4], [5, 6]], [[3, 4], [7, 8], [9, 12, 10]]], [['iip', 'grape', 'graapplegrapepe', 'grape'], [1, 2, 3, 4, 5, 2]], [[94.69906992408676], [1, 2, 3, 4, 5, 1]], [[2, 3, 5, 6, 7, 8, 9, 10, 2], [2, 3, 5, 6, 7, 8, 9, 10, 2]], [['apple', 'banana', ['orange', 'grape'], 10, ['orange', 'grape']], [['orange', 'grape'], 'pineapple', 10, 20]], [['applegrape', 'iip', 'applegrae', 'grape', 'gragpe', 'grape'], [2, 1, 2, 3, 4, 5, 2]], [[10, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1], [7, 5]], [[10, 9, 8, 6, 5, 5, 4, 3, 2, 1], [10, 9, 8, 6, 5, 5, 4, 3, 2, 1]], [[76, -83, 79, 76, 15, 31, 45], []], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 4, 1], [8, 5, 7]], [[-25.992038507469545, 79.87091961628252, 79.87091961628252], [-25.992038507469545, 79.87091961628252, 79.87091961628252]], [[[1, 2], [3, 4]], [[3, 4, 4, 4], [3, 4, 4, 4], [7, 8], [9, 10], [3, 4, 4, 4]]], [[3], [3]], [[[3, 4, 4], [3, 4, 4], [7, 8]], [[3, 4, 4], [3, 4, 4], [7, 8]]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [8, 5, 7, 5]], [['applegrape', 'iip', 'applegrae', 'grape', 'grape', 'grape'], [1, 2, 3, 4, 5, 1]], [[3, 5, 7, 7, 7], [3, 5, 7, 7, 7]], [[2, 4, 6, 8, 'abc'], ['abc', 'xyz']], [[1, 3, 5, 7, 11], [1, 3, 5, 7, 11]], [[1, 3, 5, 7, 1, 7, 1], [1, 3, 5, 7, 1, 7, 1]], [['iip', 'grape', 'graapplegrapepe', 'banana', 'graapplegrapepe'], [1, 2, 3, 4, 5, 2]], [[1, 3, 5, 7, 11, 3], [1, 3, 5, 7, 11, 3]], [[7, 5, 7], [7, 5, 7]], [['applegrape', 'iip', 'grape', 'iip'], [2, 1, 2, 3, 4, 5, 2]], [[[4, 10, 4, 4], [3, 4], [4, 10, 4, 4], [4, 10, 4, 4]], [[4, 10, 4, 4], [3, 4], [4, 10, 4, 4], [4, 10, 4, 4]]], [[[1, 2], [3, 4], [5, 6, 5]], [[3, 4], [7, 8], [9, 12, 10]]], [[10, 9, 8, 7, 6, 5, 4, 3, 1, 5], [10, 9, 8, 7, 6, 5, 4, 3, 1, 5]], [[1, 'apple', [1, 2], [3, 4], {'name': 'John'}, 5.5], [1, 'apple', [1, 2], [3, 4], {'name': 'John'}, 5.5]], [[1, 3, 5, 7, 1, 1], [1, 3, 5, 7, 1, 1]], [[1, 2, 3, 4, 5, 6, 7, 8, 10, 2], [1, 2, 3, 4, 5, 6, 7, 8, 10, 2]], [[10, 8, 6, 5, 5, 4, 3, 2, 1], [10, 8, 6, 5, 5, 4, 3, 2, 1]], [[2, 3, 5, 6, 7, 8, 9, 10, 2, 2], [2, 3, 5, 6, 7, 8, 9, 10, 2, 2]], [[2, 4, 6, 8, 'abc'], ['abc', 'xyz', 'xyz']], [[10, 9, 8, 6, 5, 4, 3, 13, 2, 1], [10, 9, 8, 6, 5, 4, 3, 13, 2, 1]], [[[10, 6, 5], [1, 2], [10, 6, 5]], [[10, 6, 5], [1, 2], [10, 6, 5]]], [[1, 2, 1], [1, 2, 1]], [['iip', 'grape', 'grape'], ['iip', 'grape', 'grape']], [['applegrape', 'iip', 'grape', 'iip'], ['applegrape', 'iip', 'grape', 'iip']], [[94.69906992408676, 94.69906992408676], [1, 14, 3, 4, 5, 1]], [[10, 9, 5, 8, 6, 5, 5, 4, 3, 2, 1], [10, 9, 5, 8, 6, 5, 5, 4, 3, 2, 1]], [[1, 3, 7, 10, 11], [1, 3, 7, 10, 11]], [['apple', 'banana', ['orange', 'grape'], 10], [['orange', 'grape'], 'pineapple', 10, 20, 'pineapple']], [[8, 5], [8, 5]], [[10, 9, 8, 5, 7, 6, 5, 4, 3, 3, 2, 1], [10, 9, 8, 5, 7, 6, 5, 4, 3, 3, 2, 1]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [8, 5, 7, -44, 5]], [[2, 4, 6, 8, 'abc'], [4.5, 'xyz']], [[10, 9, 8, 6, 5, 3, 3, 13, 2, 1, 8], [10, 9, 8, 6, 5, 3, 3, 13, 2, 1, 8]], [[[11], [9, 10], [11], [9, 10]], [[11], [9, 10], [11], [9, 10]]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5]], [[2, 4, 6, 8, 'abc', 6], ['abc', 'axyz', 4.5, 'applegrape']], [[4.5], [4.5]], [['ape', 'apple', 'banana', ['orange', 'grape'], 10], [['orange', 'grape'], 'pineapple', 10, 20]], [[4, 2, -83], [4, 2, -83]], [[1, 3, 5, 7, 1, 7, 1, -44], [1, 3, 5, 7, 1, 7, 1, -44]], [[1, 15, 3, 3, 3, 3], [1, 15, 3, 3, 3, 3]], [[2, 4, 6, 8, 20], [2, 4, 6, 8, 20]]]
results = [[1, 3, 5, 7, 9, 10], [2, 4, 6, 8, 9, 10], [1, 2, 3, 4, 6, 8, 9, 10], [10, 9, 7, 5, 3, 1], [10, 9, 8, 6, 4, 3, 2, 1], [10, 9, 8, 6, 4, 2], [], [], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 4, 6, 7, 9, 10], [1, [1, 2]], [], [], [2, 4, 6, 8], ['apple', 'banana'], [[1, 2], [5, 6]], [10, 9, 8, 6, 4, 3, 2, 1], [94.69906992408676], [], [], [], [], ['iip', 'grape', 'grape'], [10, 9, 6, 4, 3, 2, 1], [10, 9, 8, 6, 4, 3, 2, 1], [], [], [], [1, [1, 2]], [1, 3, 4, 6, 7, 9, 10], [], [[1, 2], [3, 4], [5, 6]], [2, 4, 6, 8], ['John'], [], [], [94.69906992408676, 5, 5, False, [4.5, [31, -44, 5, 56, 0, 12, 75], True, None], True, 12, 7], [2, 4, 5, 6, 8, 10], [1, [1, 2]], [], [], [], [10, 9, 8, 6, 4, 3, 1], [], [10, 9, 8, 6, 1, 4, 3, 2, 1], [], [], [], [], ['applegrape', 'iip', 'applegrae', 'grape', 'grape', 'grape'], [10, 9, 8, 6, 4, 3, 2, 1], [1, 2, 3, 4, 5], [], [2, 4, 6, 8, 6], [[1, 2], [3, 4], [5, 6]], [10, 9, 6, 4, 3, 2, 1, 1], [], [], [], [], [[1, 2], [5, 6]], ['iip', 'grape', 'graapplegrapepe', 'grape'], [94.69906992408676], [], ['apple', 'banana'], ['applegrape', 'iip', 'applegrae', 'grape', 'gragpe', 'grape'], [10, 9, 8, 6, 4, 3, 3, 2, 1], [], [76, -83, 79, 76, 15, 31, 45], [10, 9, 6, 4, 3, 2, 4, 1], [], [[1, 2], [3, 4]], [], [], [10, 9, 6, 4, 3, 2, 1], ['applegrape', 'iip', 'applegrae', 'grape', 'grape', 'grape'], [], [2, 4, 6, 8], [], [], ['iip', 'grape', 'graapplegrapepe', 'banana', 'graapplegrapepe'], [], [], ['applegrape', 'iip', 'grape', 'iip'], [], [[1, 2], [5, 6, 5]], [], [], [], [], [], [], [2, 4, 6, 8], [], [], [], [], [], [94.69906992408676, 94.69906992408676], [], [], ['apple', 'banana'], [], [], [10, 9, 6, 4, 3, 2, 1], [2, 4, 6, 8, 'abc'], [], [], [10, 9, 8, 7, 6, 4, 3, 2, 1], [2, 4, 6, 8, 6], [], ['ape', 'apple', 'banana'], [], [], [], []]

def ll_run_tests(response_data):
    """
    Main test function for code evaluation.
    Args:
        response_data: Dict containing response code
    Returns:
        bool: True if all test cases pass
    """
    try:
        # Initialize test environment
        global_namespace = {
            'np': np,
            'assertion': assertion,
            'is_floats': is_floats,
            'inputs': inputs,
            'results': results
        }
        
        # Execute solution code
        response_code = response_data.get('parsed_result', response_data.get('result', ''))
        exec(response_code, global_namespace)
        
        # Verify function exists
        func_name = "remove_elements"
        if func_name not in global_namespace:
            print(f"Function '{func_name}' not found in response")
            return False
        
        # Execute tests
        solution_func = global_namespace[func_name]
        
        # Run input/output tests
        for i, (test_input, expected) in enumerate(zip(inputs, results)):
            try:
                result = solution_func(*test_input)
                assertion(result, expected, 0)
            except AssertionError as e:
                print(f"Test case {i} failed: {str(e)}")
                print(f"Input: {test_input}")
                print(f"Expected: {expected}")
                print(f"Got: {result}")
                return False
        
        # Run assertion-based tests if any
        for test_case in ['assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]', 'assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7]) == [2, 4, 6, 8, 9, 10]', 'assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7]) == [1, 2, 3, 4, 6, 8, 9, 10]']:
            try:
                exec(test_case, global_namespace)
            except AssertionError as e:
                print(f"Assertion test failed: {str(e)}")
                print(f"Test case: {test_case}")
                return False
            
        return True
            
    except Exception as e:
        print(f"Error during test execution: {str(e)}")
        return False
