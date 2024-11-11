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
inputs = [[[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]], [[1, 2, 4, 6, 8, 10, 12, 14, 20, 17]], [[1, 2, 4, 6, 8, 10, 15, 14, 20]], [[]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 12]], [[9, 4, 7, 3, 1, 6, 8, 2, 5]], [[2, 2, 3, 4, 1, 1, 3, 4]], [[10, 8, 5, 7, 2, 4, 9, 6, 3, 1]], [[2, 3, 4, 1, 4, 1, 3, 4]], [[92.95564823643227, -98.33857708861429, -2.290411094930974, -82.09915106558478, -60.68800671675019, -60.68800671675019]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 12, 6]], [[9, 4, 7, 3, 1, 6, 8, 2, 5, 8]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 12, 13, 6, 10]], [[9, 4, 7, 3, 1, 5, 8, 2, 5]], [['AwjEwVgE', '', 'iTVHG', 'USyZK', 'EPA']], [[2, 2, 10, 3, 4, 1, 1, 3, 4]], [[9, 4, 7, 7, 3, 1, 6, 8, 2, 5, 2, 7]], [['AwjEwVgE', '', 'iTVHG', 'EPA']], [['AwjEwVgE', 'iiTVHG', 'EPA']], [[9, 4, 9, 7, 7, 3, 1, 6, 8, 2, 5, 2, 7]], [[2, 2, 10, 3, 4, 1, 1, 3, 3, 4]], [[2, 2, 10, 4, 1, 1, 3, 4]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 12, 6, 6, 12]], [[2, 2, 10, 3, 5, 1, 1, 3, 4]], [['AwjEwVgE', 'AwjEwVgE', 'iiGTVHG', 'iTVHG']], [[2, 2, 10, 3, 4, 1, 3, 3, 4]], [['AwjEwVgE', 'iTVHG', 'USyZK', 'EPA', 'USyZK']], [[2, 2, 10, 3, 5, 1, 1, 3, 4, 2]], [['AwjEwVgE', '', 'iTVHG', 'EPA', 'EPA', 'EPA', '']], [['AwjEwVgE', 'iiGTVHG', 'AwjEwVgE', 'iTVHG']], [[2, 2, 10, 3, 4, 1, 1, 3, 3, 9, 4]], [['', 'iTVHG', 'EPA']], [[1, 2, 4, 5, 4, 6, 8, 10, 10, 12, 12]], [['AwjEwVgE', '', 'USyZK', 'EPA']], [[2, 8, 2, 10, 3, 4, 1, 1, 3, 3, 4, 2, 1]], [[2, 10, 4, 1, 1, 3, 4]], [[2, 11, 2, 10, 2, 3, 4, 9, 1, 3, 3, 4]], [['iiTVHG']], [[9, 4, 7, 3, 6, 8, 2, 5, 8, 9]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 12, 6, 6, 12, 4]], [[2, 10, 3, 5, 1, 1, 3, 4, 2]], [[1, 4, 4, 6, 8, 10, 10, 12, 12, 10, 6, 12, 5]], [[10, 4, 1, 1, 4]], [[2, 3, 1, 4, 1, 3]], [[9, 4, 7, 7, 3, 1, 6, 8, 13, 5, 2, 7]], [[2, 10, 3, 4, 1, 1, 11, 4]], [['AwjEwVgE', '', 'iTVHG', 'EPA', 'EPA', 'EPA', 'PEPA', '']], [[10, 8, 5, 4, 2, 4, 9, 6, 3, 1]], [[2, 10, 5, 3, 5, 1, 1, 3, 4, 2]], [[9, 4, 7, 3, 1, 6, 8, 5, 8]], [['iiTVHG', 'iiTVHG']], [['AwjEwVgE', 'AwjEwVVgE', '', 'iTVHG', 'USyZK', 'EPA']], [[2, 10, 3, 5, 1, 1, 3, 4, 3]], [['AwjEwVgE', '', 'iTVHG', 'EPA', 'EPA', 'EPA', 'PEPA', '', 'EPA']], [['iiTVTHG', 'iiTVHG']], [[2, 2, 1, 4, 1, 3]], [['EPA', 'AwjEwVgE', 'EPA', 'AwjEwVgE']], [[10, 4, 1, 1, 4, 4]], [[1, 2, 4, 6, 8, 10, 10, 7, 12, 12, 6, 12, 2]], [['PEPA', 'iiTVHG']], [[2, 3, 4, 1, 4, 1, 1, 4, 2, 1]], [['AwjEwVgE', 'iTVHG', 'iTVHG']], [[10, 4, 1, 1, 4, 4, 10]], [[1, 2, 4, 5, 4, 6, 8, 10, 10, 6, 12]], [['AwjEwVgE', 'iiGTVHG', 'AwjVEwVgE', 'iTVHG', 'AwjEwVgE']], [[10, 4, 1, 4, 4, 10]], [[1, 3, 4, 6, 8, 10, 10, 12, 12, 6]], [['iiTVHG', 'iiTVTHG']], [[2, 3, 4, 1, 4, 1, 0, 4, 2, 1]], [[9, 4, 9, 7, 7, 3, 1, 6, 8, 2, 5, 2, 7, 6]], [['AwjEwVgE', 'iiTVHG']], [['AwjEwVgE', 'iTVHG', 'yUSyZK', 'EPA', 'USyZK']], [['iiTVTHG', 'iiTVHG', 'iiTVTHG']], [['AwjEwVgE', '', 'AwjEwVgyUSyZKE', 'iTVHG', 'USyZK', 'EPA', 'AwjEwVVgE']], [[2, 2, 2, 3, 4, 1, 1, 3, 4, 4]], [['AwjEwVgE', 'iiGTVHG', '', 'AwjVEwVgE', 'iTVHG', 'AwjEwVgE', 'iiGTVHG']], [[9, 4, 7, 3, 1, 6, 8, 8]], [['EPA', 'AwjEwVgE', 'EPA', 'EPA']], [[9, 4, 9, 7, 7, 3, 1, 6, 8, 2, 5, 2, 7, 8]], [[2, 11, 2, 10, 3, 4, 9, 1, 3, 5, 3, 4, 4]], [[2, 2, 10, 3, 5, 3, 1, 1, 3, 4, 3]], [[2, 3, 4, 1, 4, 1, 1, 4, 5, 1]], [[2, 10, 3, 5, 1, 1, 11, 3, 4]], [[2, 3, 8, 2, 1, 4, 1, 3]], [[2, 10, 5, 3, 5, 1, 1, 3, 4, 1]], [[10, 4, 1, 2, 4, 7, 10]], [['iiTG']], [['AwjEwVgE', 'AwjEwVVgE', '', 'iTVHG', 'UySyZK', 'EPA']], [[9, 4, 7, 3, 1, 6, 8, 2, 5, 2, 7, 9, 7]], [[1, 2, 4, 6, 8, 10, 10, 7, 12, 12, 6, 12, 2, 12]], [[1, 6, 2, 4, 4, 6, 8, 10, 10, 12, 12, 6, 4]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 6]], [[2, 3, 4, 1, 4, 1, 0, 5, 2, 1]], [[2, 10, 5, 1, 1, 11, 3, 4, 5]], [[10, 4, 1, 1, 2, 4, 10]], [[2, 11, 10, 3, 5, 1, 1, 3, 4]], [[2, 2, 10, 3, 5, 6, 1, 1, 3, 4, 3]], [[1, 2, 4, 4, 6, 8, 10, 10, 12, 12, 6, 6, 12, 10]], [[9, 4, 7, 3, 1, 6, 8, 5, 5, 8]], [[2, 11, 10, 3, 5, 1, 1, 3, 4, 10]], [[2, 2, 10, 2, 5, 6, 1, 1, 3, 3]], [[10, 4, 11, 1, 1, 4, 4, 10]], [[2, 10, 3, 5, 1, 11, 3, 4]], [[2, 10, 4, 7, 1, 1, 3, 4, 4]], [[10, 4, 11, 1, 2, 4, 4, 10]], [[9, 4, 7, 1, 5, 8, 2, 5, 1]], [[1, 4, 6, 8, 10, 12, 12, 10, 6, 12, 5, 12]], [['AwjEwVgE', 'iTVHG', 'USyZK', 'EPA', 'AwAwjEwVgyUSyZKEwVgE', 'USyZK']]]
results = [True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "issort_list"
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
        for test_case in ['assert issort_list([1,2,4,6,8,10,12,14,16,17])==True', 'assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 20, 17])==False', 'assert issort_list([1, 2, 4, 6, 8, 10,15,14,20])==False']:
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
