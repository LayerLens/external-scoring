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
inputs = [[[1, 2, 3, 4, 5, 6]], [[2, 3, 4, 5, 10, 15]], [[2, 10, 4, 5, 3, 15]], [[8, 3, 9, 6, 7, 5, 1]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [[]], [[10, 9, 8, 7, 6, 5, 4, 3, 2, 6, 1, 9]], [[4, 2, 3, 16, 5, 6, 7, 8, 10]], [[10, 9, 7, 6, 5, 4, 3, 2, 6, 1, 15, 9, 7]], [[-80, 19, 31, 4, 18, 5, 7]], [[4, 2, 11, 3, 16, 5, 6, 7, 8, 10, 11]], [[-80, 19, 4, 18, 5, 7]], [[-80, -80, 19, 31, 4, 18, 5, 7, 5, 5]], [[10, 9, 8, 7, 5, 4, 3, 2, 6, 1, 9]], [[10, 9, 8, 7, 5, 4, 3, 2, 6, 1, 9, 6]], [[10, 9, 7, 6, 5, 4, 3, 2, 1]], [[10, 9, 8, 7, 5, 4, 12, 3, 2, 6, 1, 9, 6, 1]], [[-80, 19, 31, 4, 18, 30, 5, 7]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 3]], [[10, 9, 8, 6, 5, 4, 3, 2, 6, 1, 9, 4]], [[10, 9, 8, 7, 5, 4, 3, 2, 6, 1, 9, 10, 4]], [[10, 9, 8, 7, 6, 20, 5, 4, 3, 2, 6, 1, 9]], [[4, 10, 9, 7, 0, 6, 5, 4, 3, 2, 1]], [[10, 9, 8, 7, 6, 5, 4, 30, 3, 2, 1]], [[-80, 19, 31, 4, 18, 5, 7, 19]], [[4, 2, 11, 3, 16, 5, 6, 7, 8, 10, 11, 2, 11]], [[10, 9, 7, 6, 20, 4, 3, 2, 6, 1, 9]], [[-80, 5, 19, 31, 4, 18, 5, 7]], [[8, 8, 3, 9, 6, 7, 5, 1]], [[10, 9, 8, 7, 5, 4, 12, 3, 2, 6, 1, 9, 1]], [[-80, 9, 8, 7, 6, 5, 4, 3, 2, 1]], [[-80, 19, 31, 4, 18, 30, 12, 7, 18]], [[4, 2, 11, 3, 16, 5, 6, 7, 8, 10, 11, 7]], [[4, 10, 9, 8, 0, 6, 5, 4, 3, 2, 1, 9]], [[-80, -80, 19, 31, 4, 18, 5, 5, 5]], [[-80, 5, 31, 4, 18, 19, 7]], [[1, 2, 3, 4, 5, 6, 7, 8, 31, 10]], [[-80, 31, -80, 19, 31, 4, 18, 5, 7, 5, 5, 5, 5]], [[-80, 19, 4, 5, 18, 5, 7]], [[-80, 19, 5, 18, 6, 7]], [[-80, 5, 19, 31, 4, 18, 5, 7, 5]], [[-80, 19, 4, 8, 5, 7]], [[-80, 19, 4, 18, 5, 7, 19]], [[-80, 19, 5, 0, 18, 6, 7, -80]], [[10, 8, 7, 5, 16, 3, 2, 6, 1, 9, 6]], [[-80, -80, 19, 31, 4, 18, 5, 7, 5, 5, 5]], [[4, 2, 3, 16, 5, 6, 7, 31, 8, 10]], [[10, 9, 7, 6, 5, 4, 1, 3, 2, 1]], [[-80, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 2]], [[-80, 31, -80, 19, 31, 4, 18, 5, 7, 5, 4, 5, 5]], [[-80, 4, 31, 4, 18, 5, 7, 19]], [[4, 11, 3, 16, 5, 6, 7, 8, 10, 11, 7]], [[10, 9, 8, 7, 6, 8, 5, 4, 3, 2, 1]], [[10, 9, 8, 7, 5, 4, 12, 3, 2, 6, 20, 1, 9, 1]], [[-80, 18, 5, 31, 4, 18, 19, 7]], [[4, 2, 3, 16, 5, 6, 7, 6, 10]], [[3, 4, 5, 6, 7, 8, 9, 6, 5]], [[10, 9, 8, 7, 5, 4, 12, 3, 2, 16, 1, 9, 6, 1, 9]], [[10, 9, 8, 7, 6, 5, 30, 3, 2, 1]], [[4, 2, 11, 3, 16, 31, 7, 8, 11, 7]], [[4, 2, 11, 3, 16, 5, 6, 7, 8, 10, 11, 4]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 5, 12, 13, 14, 16, 17, 18, 19]], [[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20]], [[4, 11, 3, 16, 5, 6, 7, 10, 11, 7, 5, 7]], [[10, 9, 8, 7, 5, 4, 3, 2, 1, 6, 1, 9, 10, 4]], [[9, 8, 7, 5, 4, 12, 3, 2, 6, 20, 1, 9, 1]], [[4, 2, 3, 16, 5, 6, 7, 31, 8, 10, 3]], [[4, 2, 7, 11, 3, 16, 31, 7, 8, 11, 7]], [[-80, -80, 19, 30, 4, 10, 18, 5, 7, 5, 5, 5]], [[10, 9, 8, 7, 5, 4, 12, 3, 2, 16, 1, 9, 6, 1, 10, 9]], [[-80, 19, 14, 5, 18, 5, 7, 19, 14]], [[10, 9, 8, 7, 5, 4, 12, 3, 2, 16, 0, 1, 9, 6, 10, 9, 12]], [[-80, 31, -80, 19, 31, 4, 18, 5, 7, 5, 4, 5, 5, 19]], [[4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 3]], [[-80, -80, 19, 31, 4, 5, 5, 5]], [[-80, 4, 31, 4, 17, 5, 7, 19, 31]], [[-80, 9, 8, 7, 6, 4, 3, 2, 1]], [[10, 9, 6, 5, 4, 1, 3, 3, 2, 1]], [[-80, -80, 19, 31, 4, 18, 5, 14, 5, 5]], [[18, 10, 9, 8, 7, 5, 4, 12, 3, 2, 16, 1, 9, 6, 1, 9]], [[10, 11, 10, 9, 8, 7, 5, 9, 3, 2, 6, 1, 9]], [[-80, 19, 4, 5, 5, 18, 5, 7]], [[4, 18, 7, 3, 3, 16, 5, 6, 7, 6, 10]], [[-80, 9, 8, 7, 6, 5, 4, 3, 1, 2, 2]], [[19, 2, 11, 3, 15, 5, 6, 7, 8, 10, 11, 2, 11]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 31, 3]], [[-80, 9, 8, 7, 5, 4, 3, 2, 1, 2, 2]], [[8, 10, 9, 8, 7, 6, 8, 5, 30, 3, 2, 1]], [[-80, 9, 8, 7, 5, 4, 3, 2, 1, 2, 2, 2]], [[-80, 5, 31, 4, 18, 7]], [[-80, 4, 31, 4, 17, 6, 32, 7, 19, 31]], [[10, 9, 8, 6, 5, 4, 3, 2, 16, 6, 1, 8, 10, 4]], [[1, 2, 6, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 3, 3]], [[1, 2, 3, 4, 5, 6, 7, 8, 5, 9, 10, 3, 4, 3, 3]], [[-80, -80, 19, 31, 4, 18, 5, 7, 5]], [[-80, -80, 19, 31, 4, 18, 5, 14, 5, 5, -80]], [[-80, 9, 8, 7, 5, 4, 3, 2, 2, 2, 14, 2]], [[4, 2, 7, 11, 3, 16, 31, 7, 8, 11, 14]], [[-80, 19, 31, 4, 5, 18, 5, 7]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], [[4, 11, 3, 16, 5, 6, 7, 10, 11, 7, 5, 7, 6]], [[-80, 31, -80, 19, 31, 4, 11, 5, 7, 5, 4, 5, 5]], [[1, 6, 2, 6, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 3, 3]], [[10, 9, 7, 6, 5, 4, 3, 2, 6, 1, 15, 9, 7, 4]], [[-80, 9, 8, 7, 5, 4, 3, 2, 2, 2, 14, 2, 2]], [[-80, 5, 19, 31, 8, 18, 5, 7, 5]]]
results = [True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False]

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
        func_name = "check_min_heap_helper"
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
        for test_case in ['assert check_min_heap([1, 2, 3, 4, 5, 6]) == True', 'assert check_min_heap([2, 3, 4, 5, 10, 15]) == True', 'assert check_min_heap([2, 10, 4, 5, 3, 15]) == False']:
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
