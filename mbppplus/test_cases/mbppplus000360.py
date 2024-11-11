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
inputs = [[[3, 2, 1]], [[1, 2, 3]], [[2, 1, 4]], [[2, 1, 4, 2, 6, 1, 8, 2, 10, 1, 12]], [[2, 7, 4, 9, 6, 12, 8]], [[2, 1, 4, 6, 8, 2, 10, 12]], [[1, 2, 3, 4, 5, 6]], [[1, 2, 4, 6, 8, 10, 12]], [[1, 3, 5, 7, 9, 11, 13]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 9]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 11, 13]], [[1]], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]], [[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]], [[1, 2, 4, 6, 2, 10, 12]], [[2, 1, 4, 3, 7, 6, 5, 8, 7, 10, 9]], [[2, 10]], [[2, 1, 4, 3, 6, 5, 8, 7, 8, 10, 11, 13]], [[2, 7, 4, 9, 20, 6, 12, 8, 2, 2]], [[3, 11, 10, 11, 10]], [[2, 1, 4, 3, 6, 5, 9, 8, 7, 8, 10, 11, 13, 10]], [[1, 2, 4, 6, 21, 2, 10, 12]], [[1, 4, 3, 6, 5, 8, 7, 8, 10, 11, 13, 3]], [[2, 7, 5, 9, 6, 12, 8, 12]], [[2, 7, 4, 9, 20, 6, 12, 8, 2, 2, 4, 4]], [[1, 10]], [[1, 2, 4, 8, 10, 12, 8]], [[2, 7, 5, 4, 9, 20, 6, 12, 8, 2, 2]], [[1, 2, 3, 0, 4, 5, 6, 5, 2]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 2, 2]], [[18, 1, 2, 4, 6, 8, 9, 12]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 11, 13, 2, 8]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 7, 2, 2]], [[1, 2, 4, 6, 2, 10, 9]], [[1, 2, 8, 4, 6, 2, 10, 9, 4]], [[2]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 11, 13, 2, 8, 6]], [[1, 2, 4, 22, 6, 8, 10, 12, 18, 6]], [[2, 1, 4, 3, 6, 5, 9, 8, 7, 8, 10, 11, 13, 10, 6]], [[2, 1, 4, 3, 6, 5, 8, 10, 11, 13]], [[1, 2, 4, 6, 10, 9]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 7, 2, 7]], [[9]], [[1, 7, 2, 4, 22, 6, 8, 10, 12, 18, 6]], [[1, 1, 4, 3, 6, 5, 8, 7, 10, 11, 13, 2, 8, 6, 1, 2]], [[3, 11, 10, 11, 10, 10]], [[2, 7, 4, 9, 20, 6, 12, 8, 2, 2, 7]], [[1, 2, 4, 6, 2, 10, 12, 1]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 11, 2, 8, 6]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 6]], [[7, 2]], [[2, 4, 2, 10, 12, 1]], [[1, 3, 5, 7, 9, 11, 0]], [[1, 2, 4, 6, 21, 2, 10, 12, 1]], [[2, 7, 5, 9, 22, 8, 12]], [[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 29]], [[2, 1, 4, 2, 6, 1, 8, 10, 1, 12, 1]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 7, 2, 2, 7]], [[2, 1, 4, 3, 5, 8, 7, 10, 9]], [[6, 2, 6, 6]], [[2, 12, 7, 29, 4, 9, 20, 18, 6, 12, 8, 7, 2, 2, 13, 7]], [[25, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 7, 2, 2]], [[1, 3, 5, 7, 9, 11, 13, 13, 7]], [[2, 7, 5, 9, 22, 8, 12, 22, 2]], [[2, 7, 5, 4, 9, 20, 18, 6, 12, 8, 2, 2]], [[1, 2, 4, 6, 2, 10, 12, 10]], [[2, 1, 4, 3, 7, 6, 5, 8, 7, 8, 10, 9]], [[2, 1, 4, 3, 6, 5, 9, 8, 8, 10, 11, 13, 10]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 7, 2, 2, 7, 7]], [[1, 3, 5, 7, 9, 11]], [[6, 6, 6, 6]], [[2, 7, 5, 4, 9, 20, 13, 6, 12, 8, 2, 2]], [[2, 1, 4, 3, 6, 5, 8, 7, 10, 11, 13, 2, 12, 8]], [[2, 7, 5, 4, 9, 20, 18, 6, 12, 8, 2, 2, 2]], [[2, 7, 9, 12, 8, 13]], [[1, 2, 4, 6, 15, 2, 12, 10]], [[6, 6, 6, 6, 6]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 2, 2, 20]], [[1, 15, 4, 8, 10, 12, 8]], [[2, 1, 3, 6, 5, 9, 8, 4, 8, 11, 13, 10]], [[2, 2, 4, 6, 21, 2, 10, 12, 1]], [[18, 1, 2, 4, 6, 8, 9, 12, 8]], [[1, 2, 4, 6, 2, 10, 12, 10, 10]], [[2, 7, 5, 22, 9, 6, 13, 8, 12, 8]], [[19, 21, 2, 3, 0, 4, 5, 6, 5, 2]], [[]], [[2, 1, 4, 6, 8, 2, 10, 2, 12]], [[12, 7, 5, 9, 20, 18, 6, 12, 8, 7, 2, 2]], [[2, 1, 4, 3, 7, 6, 5, 8, 7, 29, 8, 9]], [[1, 3, 23, 7, 9, 11, 13]], [[2, 1, 4, 2, 6, 1, 8, 10, 1, 9, 12, 1, 9]], [[3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 20, 25, 27, 29]], [[1, 3, 5, 7, 9, 11, -1]], [[1, 3, 5, 9, 11, 13, 13, 7, 5, 7, 1]], [[2, 12, 7, 4, 9, 20, 18, 6, 12, 8, 7, 2, 7]], [[1, 2, 6, 4, 8, 10, 12, 8, 2]], [[1, 2, 7, 6, 4, 8, 10, 12, 8]], [[2, 1, 4, 3, 7, 6, 5, 8, 7, 10, 29, 9]], [[2, 4, 10, 12, 19, 19]], [[3, 11, 29, 10, 11, 10, 10]], [[2, 3, 4, 3, 6, 4, 5, 8, 7, 10, 9]], [[2, 1, 3, 6, 5, 9, 8, 8, 11, 13, 10, 10]], [[2, 1, 19, 3, 7, 6, 5, 8, 7, 29, 8, 9]], [[2, 7, 9, 12, 8, 12]], [[6, 6, 6, 6, 4, 6]], [[2, 4, 6, 2, 10]], [[1, 7, 4, 9, 20, 6, 12, 8, 2, 2]], [[1, 2, 4, 22, 6, 8, 10, 12, 18, 10]], [[2, 12, 7, 5, 4, 9, 20, 18, 6, 12, 8, 8, 2, 2]], [[2, 7, 5, 9, 22, 8, 27, 12, 22, 2]], [[2, 7, 5, 2, 4, 9, 20, 6, 12, 8, 2, 2]], [[6, 6, 6]], [[1, 6, 3, 5, 7, 9, 11, 0]], [[3, 11, 29, 10, 11, 10, 10, 10]]]
results = [False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "even_position"
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
        for test_case in ['assert even_position([3,2,1]) == False', 'assert even_position([1,2,3]) == False', 'assert even_position([2,1,4]) == True']:
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
