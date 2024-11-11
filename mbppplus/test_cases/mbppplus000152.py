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
inputs = [[['Python', 3, 2, 4, 5, 'version']], [['Python', 15, 20, 25]], [['Python', 30, 20, 40, 50, 'version']], [[1, '2', True, 3.14, ['a', 'b'], [5, 6, 7], {'8': 'eight', '9': 'nine'}, 'Python', 10, 11, 12]], [['Python', 3.14, 5, 'version', 10, 7.5, 2, '3.14']], [[1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]], [[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]], [[25, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}]], [[1, 2, 3, ['Python', 4, 5, [6, 7, [8, 9, [10]]]], 'version', 11, 12, 13]], [[7, 9]], [[3, 1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]], [[1, 3, 30, 3]], [[3, 1, 2, 10, [3, 4, [5, 6, [7, 8, [9, 10]]]]]], [[3, 1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]], 3, 2]], [[1, 3, 30]], [[3, 1, [3, 4], 2, [3, 4], 5, 3, 2]], [[1, [3, 4, [5, 6, [7, 8, [9, 10]]]], 1]], [[1, 13, [3, 4, [5, 6, [7, 8, [9, 10]]]], 1]], [[1, 3]], [[1, 3, 2, 30, 3]], [[1, 2, 11, 1]], [[1]], [[25, {'y': [26, 27], 'yy': [26, 27]}, {'y': [26, 27], 'yy': [26, 27]}]], [[9, 7, 8, 9]], [[13, 7, 8, 9]], [[25, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}, 25, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}]], [[0]], [[26, 9]], [[4, 5, 6, 6]], [[1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]], 2]], [[1, 2, 3, ['Python', 4, 5, [6, 7, [8, 9, [10]]]], 'version', 11, 12, 'version']], [[4, 7, 8, 9]], [[25, {'y': [26], 'yy': [26]}, {'y': [26], 'yy': [26]}]], [[4, 7, 8, 8, 8]], [[1, 13, [3, 4, [5, 6, [7, 8, [9, 10]]]], 12, 1]], [[1, 12, [3, 4, [5, 6, [7, 8, [9, 10]]]], 12, 1]], [[1, 1, [3, 4, [5, 6, [7, 8, [9, 10]]]], 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]], [[25, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}, 25]], [[25, {'y': [26, 27], 'yy': [26, 27]}, {'y': [26, 27], 'yy': [26, 27]}, {'y': [26, 27], 'yy': [26, 27]}, 25]], [[1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]], 2, 2, 2]], [[9, 7, 8, 9, 8]], [[0, 0]], [[1, 2]], [[9]], [[1, [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]], [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]], 1]], [[0, 1, 13, [3, 4, [5, 6, [7, 8, [9, 10]]]], 1]], [[29]], [[13, 3, 30]], [[13]], [[4, 4, 7, 8, 9, 8]], [[0, 1]], [[1, 3, 30, 3, 1]], [[[3, 4, [5, 6, [7, 8, [9, 10]]]], 1]], [[3, 1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]], 3, 2, 3]], [[13, 3, 30, 30]], [[1, 2, 3, ['Python', 4, 5, [6, 7, [8, 9, [10]]]], 'version', 'z', 11, '', 12, 'y']], [[1, '2', 2, 3, ['Python', 5, [6, 7, [8, 9, [10]]]], 'version', 'z', 11, '', 12, 'y']], [[1, 1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]], [[0, 1, 0]], [[8, 13, 7, 8, 9]], [[26, 9, 26]], [[1, 1]], [[1, 3, 2, 30]], [[3, 1, 2, 10, [3, 4, [5, 6, [7, 8, [9, 10]]]], 1]], [[26, 28, 26]], [[13, 3, 3, 30]], [[1, [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]], [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]], 1, [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]]]], [[3, 30, 31, 30]], [[1, [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]], 1, [3, 4, [5, 6, [7, 8, [9, 10]]], [5, 6, [7, 8, [9, 10]]]]]], [[12, [3, 4, [5, 6, [7, 8, [9, 10]]]], 12, 1]], [[25, {'y': [27], 'yy': [27], 'Pythonyy': [27]}, {'y': [27], 'yy': [27], 'Pythonyy': [27]}]], [[3, 26, 2, 12, 2]], [[3, 1, 2, [27, 4, [5, 6, [7, 8, [9, 10]]]], 3]], [[25, 24, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}, 25, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}]], [[25, {'y': [26]}, {'y': [26]}]], [[2]], [[29, 9, 9, 9]], [[6, 7, 8, 9, 8]], [['Python', 3.14, 5, 'version', 10, 7.5, '3.14']], [[3, 30, 31, 4]], [[4, 5, 6, 9]], [[7]], [[0, 2, 1, 0]], [[[3, 4, 5, [5, 6, [7, 8, [9, 10]]]], 1]], [[1, 13, [3, 4, [5, 6, [7, 8, [9, 10]]]], 1, 1]], [[3, 1, [3, 4], 2, [3, 4], 5, 10, 2, 3]], [[25, {'y': [26]}, {'y': [26]}, 25]], [[8, 9]], [['Python', 7.5, 5, 'version', 10, 7.5, 2, '3.14', 'version']], [[1, [3, 4, [5, 6, [7, 8, [9, 10]]]], 12, 1]], [[25, {'y': [26, 27, 28], 'z': {'a': 29, 'b': 30}}, 25, 25]], [[4, 4, 7, 6, 9, 8]], [[26, 28, 27]], [[8, 13, 12, 7, 8, 9]], [[0, 1, [3, 4, [5, 6, [7, 8, [9, 10]]]], 1, 1]], [[6, 7, 5, 8, 9, 8, 6]], [[25, {'y': [26, 27, 27, 28], 'z': {'a': 29, 'b': 30}}, 25, 25]], [[25, {'y': [26, 27, 28, 28], 'z': {'a': 29, 'b': 30}}]], [['3.14', False, 7.5]], [[9, 8, 8, 9, 8]], [[4, 4]], [[25, 25, 25]], [[3, 1, 2, 9, [3, 4, [5, 6, [7, 8, [9, 10]]]]]], [[3, 1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]], 3, 2, 3, 2]], [[1, 10, 9, 9, 9, 9]], [[3, 6, 30, 31, 30, 30]], [['Python', 3.14, 5, 6, 'version', 10, 7.5, '3.14', 10]], [[1, 1, [3, 4, [5, 6, [7, 8, [9, 10]]], 4], 2, [3, 4, [5, 6, [7, 8, [9, 10]]], 4], 1]], [[3, 30, 0, 31]]]
results = [5, 25, 50, 12, 10, 2, 3, 6, 9, 25, 13, 9, 3, 30, 10, 3, 30, 5, 1, 13, 3, 30, 11, 1, 25, 9, 13, 25, 0, 26, 6, 2, 12, 9, 25, 8, 13, 12, 2, 25, 25, 2, 9, 0, 2, 9, 1, 13, 29, 30, 13, 9, 1, 30, 1, 3, 30, 12, 12, 2, 1, 13, 26, 1, 30, 10, 28, 30, 1, 31, 1, 12, 25, 26, 3, 25, 25, 2, 29, 9, 10, 31, 9, 7, 2, 1, 13, 10, 25, 9, 10, 12, 25, 9, 28, 13, 1, 9, 25, 25, False, 9, 4, 25, 9, 3, 10, 31, 10, 2, 31]

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
        func_name = "max_val"
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
        for test_case in ["assert max_val(['Python', 3, 2, 4, 5, 'version'])==5", "assert max_val(['Python', 15, 20, 25])==25", "assert max_val(['Python', 30, 20, 40, 50, 'version'])==50"]:
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
