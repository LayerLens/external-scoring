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
inputs = [[(1, 4, 5, 6, 1, 4)], [(1, 4, 5, 6)], [(2, 3, 4, 5, 6)], [()], [(1,)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)], [(1, 1, 1, 1, 1, 1, 1, 1, 1, 2)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)], [(1, 2, 3.14, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3.14, 4, 5, 6, 7, 8, 9, 10)], [(1, 'a', True, 3.14)], [(7, 8, 37, 3, -71, -36)], [(7, 9, 37, 3, -71, -36)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)], [(10, 9, 8, 7, 6, 5, 4, 3, 1, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 3, 1)], [(0, 1)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6)], [(61, 1, 34, -53, -71, False)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 8, 7, 6, 5, 4, 3, 2, 1, 6)], [(10, 9, 8, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 2)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 2, 1, 6)], [(1, 2, 3.14, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3.14, 4, 5, 6, 8, 9, 10)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 6)], [(10, 9, 8, 7, 6, 5, 6, 3, 2, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 3, 1)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 8, 7, 6, 5, 4, 3, 2, 1, 6, 3)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 8, 7, 6, 5, 4, 3, 2, 0, 1, 6, 3)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 3, 1, 6)], [(0, 1, 1)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 10, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)], [(0, 1, 0)], [(1, 0)], [(10, 9, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6)], [(6, 8, 8, 37, 3, -71, -36)], [(1, 2, 3.14, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3.14, 4, 5, 6, 9, 10)], [(6, 0, 1, 1)], [(1, 0, 1, 1)], [(7, 8, 3, -71, -36)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 4, 3, 2, 1, 6)], [(6, 0, 1, 1, 1)], [(10, 9, 8, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 3, 1, 9)], [(6, 0, 1, 1, 1, 1)], [(1, 2, 0, 1, 1)], [(10, 1)], [(10, 9, 9, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6)], [(5, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 6, 10, 9, 8, 7, 6, 5, 4, 3, 3, 1, 7)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 61, 10, 9, 8, 7, 6, 5, 4, 2, 1, 6, 6)], [(10, 7, 7, 1)], [(1, 0, 1, 1, 1)]]
results = [False, True, True, True, True, True, False, False, False, False, False, True, True, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False]

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
        func_name = "check_distinct"
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
        for test_case in ['assert check_distinct((1, 4, 5, 6, 1, 4)) == False', 'assert check_distinct((1, 4, 5, 6)) == True', 'assert check_distinct((2, 3, 4, 5, 6)) == True']:
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
