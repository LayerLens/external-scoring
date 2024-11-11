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
inputs = [[[1, 2, 3, 4, 5]], [[1, 2, 3, 4, 4]], [[1, 1, 2, 2, 3, 3, 4, 4, 5]], [[2, 5, 1, 4, 3, 6, 7, 8, 9, 10]], [[]], [[-81, True, False]], [[-81, False, True, False]], [[2, 5, 1, 4, 3, 3, 6, False, 7, 8, 9, 10, 7]], [[False, -81, True, False]], [[False, -81, True, True, False, True]], [[False, -81, True, True, False, True, True]], [[-82, True, False]], [[False, -81, True, False, True, True, True]], [[5, 1, 4, 3, 6, 7, 8, 9, 10]], [[False, True, True, False, True, True]], [[-81, False, False]], [[2, 5, 1, 6, 4, 3, 6, 7, 8, 9, 10]], [[True, True, -81, True, False, True, True, True]], [[False, -81, True, False, True, True, True, False]], [[True, False, -81, False, True, True, True]], [[True, False, False, True, True, True, True]], [[2, 5, 1, 4, 3, 3, 6, False, 3, 8, 9, 10, 7]], [[False, -81, False, True, True, True, True]], [[-81, True, True, False, False]], [[False, False, True, True, False, True, True]], [[False, False, False]], [[False, -81, True, False, True]], [[True, False, False, True, True, True, True, True, True]], [[True, False, True, True, True, True, True, True]], [[True, True, True, -81, True, False, True, True, True]], [[2, 5, 1, 4, 3, 6, 7, 9, 10, 10]], [[-81, False, False, False, -81]], [[True, True, True, -81, True, False, True, True, True, True]], [[False, -81, True, False, True, True, True, False, -81, False]], [[False, True, False]], [[False, 9, False, True, False, True, True, True, False]], [[2, 1, 4, 3, 3, 6, False, 7, 8, 9, 10, 7]], [[False, -81, True, False, True, True, False, True, False]], [[False, False, -81, True, False, True]], [[-56, 3, 7, 10, 3, 7]], [[-56, 3, -82, 10, 3, 7]], [[False, False]], [[True, False, False, True, True, True, True, True]], [[False, False, -81, True, True, False, True, True]], [[-56, 3, -82, 4, 10, 3, 7, 10]], [[False, -81, True, False, True, True, True, True]], [[2, 5, 1, 4, 3, 1, 7, 9, 10, 10]], [[2, 5, 1, 6, 4, 3, 6, 7, 5, 9, 10, 7]], [[2, 5, 1, 4, 3, 6, 7, 8, 9, 10, 3]], [[-81, False, False, False]], [[False, -81, False, True, True, True, True, True]], [[-56, 3, 10, -56, 3, 7]], [[False, -81, True, True, False, True, True, True, True]], [[2, 5, 1, 6, 3, 4, 3, 6, 7, 9, 10, 8]], [[False, False, -81, False, False, False, False, True, False]], [[True, False, True, False]], [[-82, True, False, False, False]], [[2, -82, 1, 10, 3, 3, 6, False, 7, 8, 9, 10, 7, 10]], [[2, 5, 1, 9, 4, 3, 3, 6, False, 2, 8, 9, 10, 7, 3]], [[2, 5, 3, 4, 3, 3, 6, False, 3, 8, 9, 10, 7]], [[False, -81, True, False, True, True, False, True, False, False, False]], [[2, 5, 1, 9, 4, 3, 3, 6, False, 2, 8, 9, 10, 3]], [[2, -82, 1, 10, 4, 3, 6, False, 7, 8, 9, 10, 7, 10]], [[False, False, True, False, False, True, True]], [[2, 5, 1, False, 3, 4, 3, 6, 7, 9, 10, 8]], [[2, 5, 1, 6, 5, 3, 6, 7, 9, 10, 8, 9]], [[2, 5, 1, False, 3, 4, 3, 6, 7, 9, 10, 8, 3]], [[False, True, False, -81, True, True, False, True, True]], [[5, 1, 4, 3, 6, 7, 8, 9, 11]], [[False, -81, False]], [[False, -81, True, False, True, True, True, False, False, -81]], [[False, -81, True, False, True, -81]], [[2, 5, 1, 9, 4, 3, 6, False, 2, 8, 9, 10, 7, 3]], [[True, -81, True, True, False, True, True, True, True]], [[True, False, -81, False, True, True]], [[2, 5, 1, 4, 3, 6, 7, 8, 9, 10, 3, 9]], [[False, -81, True, False, True, False, True, False]], [[False, False, True, False, True]], [[2, 1, 3, 3, 6, False, 7, 8, 9, 10, 7]], [[False, True, False, True, False, True, False]], [[2, 5, 1, 9, 6, 4, 3, 6, 7, 4, 9, 10, 7]], [[False, -81, True, False, True, False]], [[2, 1, 3, 3, 6, 8, False, 7, 8, 9, 10, 7]], [[5, 9, 6, 4, 3, 6, 7, 4, 9, 10, 7]], [[-80, False, True, False, True]], [[False, False, True, False, True, False]], [[5, 1, 4, 3, 6, 7, 8, 9, 11, 3]], [[False, -81, True, False, True, True, False, False]], [[5, 1, 4, 3, 6, 7, 8, 9, 10, 3, 9, 6]], [[5, 1, 4, 3, 6, 7, 5, 9, 10, 7, 8]], [[-81, True, False, True, True, False, -81, False]], [[-82, True, False, False]], [[5, 9, 6, 4, 3, 6, 7, 4, 9, 8, 7]], [[True, -81, True, True, False, True, True, True, True, True]], [[False, -81, False, True, True, True, True, True, True]], [[-56, 3, 7, 10, 11, 3, 7, 3]], [[True, False, -81, False, False, False, False, False, True, False]], [[2, 1, 3, 3, 6, False, 8, False, 7, 8, 9, 10, 7]], [[-82, 7, True, False, False, False]], [[10, 2, 5, 1, 4, 3, 3, 6, False, 7, 8, 5, 9, 10, 7]], [[False, True, False, True]], [[-81, True, False, False, False, -81]], [[-81, True, False, True, True, False, True, False, False, False]], [[10, 2, 5, 1, False, 3, 3, 6, False, 7, 8, 5, 9, 10, 7]], [[False, True, False, False]]]
results = [False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

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
        func_name = "test_duplicate"
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
        for test_case in ['assert test_duplicate(([1,2,3,4,5]))==False', 'assert test_duplicate(([1,2,3,4, 4]))==True', 'assert test_duplicate([1,1,2,2,3,3,4,4,5])==True']:
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
