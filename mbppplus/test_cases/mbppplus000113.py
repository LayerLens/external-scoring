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
inputs = [[[1, 15, 51, 45, 33, 100, 12, 18, 9]], [[80, 60, 30, 40, 20, 10]], [[2, 3, 14, 16, 21, 23, 29, 30]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1]], [[10, 9, 8, 7, 6, 5, 4, 4, 3, 3, 1, 6]], [[10, 9, 8, 7, 6, 4, 3, 2, 1]], [[10, 8, 7, 6, 5, 4, 4, 3, 3, 1, 6]], [[10, 9, 8, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9]], [[10, 9, 8, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 10]], [[9, 8, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 10]], [[10, 9, 8, 7, 6, 5, 3, 3, 2, 1]], [[1, 9, 8, 7, 7, 5, 4, 4, 3, 3, 1, 6]], [[1, 9, 8, 7, 7, 5, 4, 4, 3, 3, 1, 5, 8]], [[10, 9, 9, 7, 6, 5, 3, 3, 2, 1, 9]], [[6, 9, 6, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9]], [[10, 7, 10, 5, 4, 4, 3, 1, 6]], [[0, 10, 8, 7, 6, 5, 4, 4, 3, 3, 1, 5, 6]], [[10, 8, 8, 7, 6, 5, 3, 3, 2, 10]], [[10, 4, 9, 8, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9]], [[10, 9, 9, 7, 5, 3, 3, 2, 1, 9]], [[10, 4, 9, 8, 7, 6, 5, 9, 4, 4, 3, 6, 9]], [[6, 9, 6, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9, 9, 9]], [[10, 9, 9, 7, 5, 3, 3, 2, 9]], [[0, 10, 7, 7, 6, 5, 4, 4, 3, 3, 1, 5, 6]], [[6, 9, 6, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9, 9]], [[10, 9, 8, 7, 4, 5, 4, 4, 3, 3, 1, 6]], [[1, 5, 9, 8, 7, 7, 5, 4, 0, 3, 3, 1, 6]], [[10, 9, 8, 7, 4, 5, 4, 4, 3, 3, 9, 1, 6]], [[10, 9, 8, 7, 6, 5, 4, 4, 5, 3, 2, 1]], [[10, 9, 8, 7, 4, 4, 3, 2, 1]], [[6, 9, 6, 2, 7, 0, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9]], [[0, 10, 7, 7, 6, 4, 3, 3, 1, 5, 6, 6]], [[6, 9, 6, 2, 7, 0, 6, 5, 9, 4, 4, 3, 3, 1, 6, 6]], [[6, 9, 6, 2, 7, 0, 6, 5, 9, 4, 8, 2, 4, 3, 3, 1, 6, 6, 4]], [[10, 8, 7, 4, 4, 3, 2, 1, 7]], [[10, 9, 9, 7, 5, 3, 3, 2, 0, 9]], [[7, 10, 5, 4, 4, 3, 1, 6]], [[10, 8, 7, 6, 5, 4, 4, 3, 1, 6, 6]], [[10, 9, 9, 7, 6, 5, 4, 4, 3, 2, 1]], [[0, 10, 7, 6, 4, 3, 3, 6, 1, 5, 6, 6]], [[10, 8, 7, 6, 5, 4, 4, 3, 1, 6]], [[10, 9, 8, 9, 7, 5, 3, 3, 2, 1, 9]], [[10, 10, 5, 4, 4, 3, 1, 6, 7]], [[10, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[1, 5, 9, 9, 7, 7, 5, 4, 0, 3, 3, 1, 6]], [[10, 9, 8, 7, 6, 5, 4, 4, 5, 3, 2, 1, 2]], [[10, 6, 9, 8, 7, 6, 5, 4, 5, 3, 2]], [[6, 9, 6, 2, 7, 0, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9, 6]], [[9, 9, 8, 7, 4, 5, 4, 4, 7, 3, 1, 6]], [[10, 9, 8, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9, 9]], [[10, 10, 9, 8, 7, 6, 4, 3, 2, 2]], [[9, 9, 7, 5, 3, 3, 2, 1]], [[10, 9, 8, 7, 6, 5, 4, 4, 5, 3, 2, 1, 2, 5]], [[10, 9, 7, 6, 5, 9, 9, 4, 4, 3, 3, 1, 6, 10]], [[10, 9, 9, 7, 5, 4, 4, 3, 2, 1]], [[10, 9, 9, 7, 9, 5, 3, 3, 2, 1, 9]], [[10, 8, 0, 5, 4, 4, 3, 1, 6, 7]], [[10, 9, 7, 9, 7, 6, 5, 3, 2, 1, 9]], [[1, 9, 8, 7, 7, 5, 4, 3, 3, 1, 6]], [[10, 9, 9, 7, 7, 5, 3, 3, 2, 1, 9, 9]], [[11, 9, 8, 7, 0, 5, 3, 1]], [[True, False]], [[10, 4, 9, 8, 7, 6, 5, 4, 4, 3, 3, 1, 6, 9]], [[10, 7, 9, 9, 7, 5, 3, 2, 9]], [[1, 9, 8, 7, 4, 5, 4, 4, 3, 3, 9, 1, 6]], [[0, 10, 7, 6, 4, 3, 3, 6, 5, 6, 6, 3]], [[10, 9, 9, 7, 6, 5, 4, 9, 3, 2, 1, 9]], [[9, 8, 7, 4, 4, 3, 2, 1]], [[10, 8, 0, 5, 4, 4, 1, 6, 7]], [[10, 1, 8, 7, 6, 5, 4, 3, 11, 1, 11]], [[10, 9, 7, 10, 5, 9, 9, 4, 4, 3, 3, 1, 6, 10]], [[10, 7, 7, 6, 5, 4, 4, 3, 3, 1, 5, 6]], [[True, True, False]], [[10, 8, 8, 7, 4, 6, 5, 3, 3, 2, 10]], [[1, 5, 9, 8, 7, 7, 5, 4, 0, 3, 3, 3, 1, 6]], [[6, 9, 6, 7, 5, 9, 4, 4, 3, 8, 3, 1, 6, 9]], [[10, 9, 7, 5, 4, 4, 3, 2, 1]], [[6, 9, 6, 7, 6, 5, 9, 4, 4, 3, 3, 1, 6, 9, 6, 9]], [[True, True, True, False]], [[10, 9, 8, 7, 4, 5, 4, 4, 3, 0, 7, 1, 6]], [[7, 9, 9, 7, 5, 3, 2, 9]], [[2, 10, 8, 8, 7, 6, 5, 3, 3, 2, 10]], [[10, 4, 9, 8, 7, 5, 9, 4, 4, 3, 6, 9]], [[10, 10, 9, 8, 7, 6, 6, 4, 3, 2, 2]], [[8, 9, 8, 7, 4, 3, 2, 1]], [[10, 9, 7, 5, 4, 4, 3, 2, 2, 4]], [[11, 9, 9, 7, 5, 3, 3, 2, 1, 9]], [[10, 4, 9, 8, 7, 6, 5, 4, 4, 3, 3, 1, 5, 9]], [[10, 9, 7, 5, 3, 4, 3, 2, 4]], [[10, 9, 8, 7, 6, 1, 5, 4, 3, 2, 1]], [[10, 9, 9, 7, 6, 5, 3, 3, 2, 1, 9, 3]], [[1, 9, 8, 7, 4, 5, 4, 4, 3, 3, 9, 1, 6, 3]], [[10, 9, 7, 10, 5, 9, 9, 9, 4, 4, 3, 3, 1, 6, 10]], [[10, 9, 8, 7, 6, 4, 3, 2, 1, 10]], [[1, 9, 8, 7, 7, 4, 4, 4, 3, 3, 1, 5, 8]], [[6, 9, 6, 7, 0, 6, 5, 9, 4, 4, 3, 1, 6, 6]], [[10, 9, 8, 7, 6, 4, 0, 3, 2, 1]], [[1, 9, 8, 4, 5, 4, 4, 3, 3, 9, 1, 6]], [[7, 9, 7, 5, 3, 2, 9]], [[1, 9, 2, 7, 4, 5, 6, 4, 4, 3, 3, 9, 1, 6]], [[1, 9, 8, 7, 4, 5, 4, 4, 3, 1, 6, 3]], [[10, 8, 0, 5, 4, 4, 1, 7]], [[10, 9, 8, 8, 9, 7, 5, 3, 3, 2, 1, 9]]]
results = [194, 210, 138, 55, 55, 53, 50, 44, 53, 53, 43, 51, 38, 38, 43, 41, 30, 44, 41, 53, 37, 52, 41, 36, 36, 41, 47, 43, 47, 55, 44, 41, 31, 41, 41, 35, 36, 30, 44, 47, 31, 44, 45, 23, 55, 35, 55, 54, 41, 37, 53, 49, 27, 55, 45, 41, 37, 31, 43, 38, 37, 44, 1, 53, 36, 38, 31, 47, 34, 28, 44, 39, 36, 1, 41, 43, 36, 41, 41, 1, 47, 33, 43, 46, 49, 42, 40, 38, 53, 40, 55, 43, 38, 39, 50, 33, 41, 50, 31, 33, 33, 38, 28, 45]

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
        func_name = "max_sum"
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
        for test_case in ['assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194', 'assert max_sum([80, 60, 30, 40, 20, 10]) == 210', 'assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138']:
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
