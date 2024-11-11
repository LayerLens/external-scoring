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
inputs = [[[5, 4, 7, 2, 1]], [[7, 2, 8, 1, 0, 5, 11]], [[1, 2, 3]], [[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]], [[-3, -2, -1, 0, 1, 2, 3]], [[17, -12, 33, 4, -9, 0, 21, -7, 8, -5]], [[100, -200, 75, -50, 125, -250, 175, -40, 80, -60]], [[1, 2, 1, 3, 2, 1, 3, 4]], [[]], [[17, -98, 3, -2, -71, -250, -40, -250]], [[True, True, True, True, True, True, False, False]], [[17, -98, 3, -2, -71, -250]], [[-250, -2, -1, 0, 1, 2, 3]], [[-3, -2, -1, 0, 2, 3]], [[-3, -2, 80, -12, 2, 3]], [[-2, -2, 80, -12, 3, -2]], [[17, -98, 3, -2, -71, -40, -250, -40]], [[True, False, True, False, False, True, False, True, True]], [[1, 2, 1, 3, 2, 1, 1, 3, 4]], [[17, -98, 3, 18, -2, -71, -250]], [[1, 2, 1, 3, 2, 1, 3, 3, 3]], [[1, 2, 1, 2, 1, 1, 3, 5]], [[1, 2, 1, 3, 2, 1, 1, 3, 4, 3]], [[17, 33, 4, -9, 0, 21, -7, 8, -5]], [[1, 2, 1, 3, 21, 0, 1, 3, 3, 3]], [[1, 2, -40, 1, 3, 2, 1, 4]], [[1, 2, 1, 3, 2, 1, 3, 3, 3, 3]], [[1, 2, 1, 3, 2, 1, 3, 3, 3, 3, 2, 1]], [[1, 2, -40, 1, 3, 2, 1, 4, 2, 3]], [[1, 2, -40, 1, 3, 2, 1, -2]], [[17, 33, 4, -9, 0, 21, 75, 8, -5, -9, 17]], [[1, 2, -12, 1, 3, 2, 1, 4, 2, 3]], [[True, False, True, False, False, False, False, True, True, True]], [[1, 3, 5, 7, 9, 2, 2, 4, 6, 8, 10]], [[1, 2, 1, 3, 2, 1, 3, -12, 4, 1]], [[-3, -50, -1, 0, 2, 3]], [[17, -98, 3, -2, -71, -250, -40, -250, -250]], [[1, 2, 1, 3, 2, 1, 3, 3, 3, 3, 3]], [[-3, -2, 0, 2, 3]], [[-50, -2, 0, 2, 3, 2]], [[1, 2, 1, 3, 2, 1, 3, 4, 2]], [[17, -98, 3, 18, -2, -71, -250, 18]], [[-3, -2, 80, -12, 2, 2, 3]], [[-250, -2, -1, 5, 0, -71, 2, 3]], [[1, 2, 1, 3, 1, 1, 4]], [[100, -98, -50, 125, -250, 175, -40, 80, -60]], [[21, -98, 3, 18, -2, -71, -250, 18, 18]], [[17, -98, 3, 18, -2, -71, -250, -71]], [[True, False, True, False, False, True, True, False]], [[-3, -2, 80, -12, 2, 3, 3]], [[-71, -2, -1, 5, 0, -71, 2, 3]], [[-3, -2, 80, -12, -3, 2, 2, 3]], [[1, 2, 75, 1, 3, 2, 1, 3, 4, 2, 1]], [[17, -98, 3, 18, -2, -71, -250, -71, -2]], [[100, -98, -50, 125, -250, 175, -40, 80, -9, -60]], [[2, 2, 1, 3, 2, 1, 1, 3, 4]], [[1, 2, -40, 1, 3, 2, 1, 4, 3]], [[False, False, False, False]], [[True, False, False, False, False, True, True, False]], [[2, -40, 1, 3, 2, 1, -2]], [[-98, 3, -2, -71, -250, -250, -250]], [[5, -98, 3, -2, -71, -250]], [[-3, 4, -2, 0, 2, 3, 2]], [[-40, 1, 2, 1, 3, 2, 1, 3, 4]], [[17, -98, 3, -2, -71, -40, -250, -40, -71]], [[False, False, False]], [[1, 2, -40, 1, 3, 2, -2]], [[-3, -50, -1, 2, 3]], [[-3, -2, 80, -200, 3]], [[1, 2, 1, 3, 1, 3, 3, 3, 9]], [[1, 2, 3, 2, 1, 3, -12, 4]], [[1, 2, 1, 3, 3, 1, 3, 3, 3]], [[-3, 4, -2, 0, 175, 2, 3, 2, 2]], [[1, 2, 1, 3, 2, 33, 1, 3, 4, 3]], [[-250, -2, -60, 0, 1, 2, 3, -2]], [[-3, -2, -1, 0, 1, 1, 3]], [[100, -98, -50, 125, -250, 175, -40, 80, -9]], [[1, 2, -40, 1, 3, 2, 1, 4, 2, 3, 3]], [[-3, -2, -12, -5, -3, 2, 2, 3]], [[1, 2, 1, 3, 2, 1, 3, 4, 2, 4]], [[5, 1, 2, 1, 3, 2, 1, 1, 9, 3, 4]], [[17, -98, 3, -1, -71, -40, -250, -40, -71]], [[1, 2, 1, 2, 1, 3, 5, 3]], [[1, 2, -40, 1, 3, 2, 1, -41, 4, -3, 3]], [[-3, -2, -1, 0, 1, 2, 3, 0]], [[3, 5, 7, 9, 2, 2, -40, -71, 4, 6, 8, 10, 7]], [[100, -98, -50, 125, -250, 175, -40, 80, -9, -9, -250]], [[17, -98, 3, 18, -2, -71, -250, -71, 17]], [[2, -3, -2, 80, -12, -3, 2, 2, 3]], [[1, 2, 1, 17, 3, 2, 1, 1, 3, 4, 2]], [[-3, -2, -1, 0, 1, 3, 2, 3]], [[2, -40, 1, 3, 2, 4, 2, 3]], [[2, 2, 1, 3, 1, 1, 3, 4]], [[-3, -49, -1, 2, 3]], [[1, 2, 1, 3, 9, 2, 1, 3, 3, 3, 3, 3]], [[-3, -2, -12, -3, 2, 2, 3]], [[1, 2, 1, 3, 2, 1, 5, 3, -12, 4, 1]], [[True, False, True, True, False, False, True, True, False]], [[-3, -2, 80, -12, 2, 80, 3]], [[1, 1, 1, 2, 1, 1, 6, 3]], [[False, False, False, False, True, False]], [[-2, -3, -50, -1, 2, 3]], [[100, -98, -51, 125, 175, -40, 80, -9]], [[-3, 80, -12, 1, 80, 3]], [[17, 33, 4, -9, 0, 75, 8, -5, -9, 75]], [[-40, 0, 2, 1, 3, 2, 1, 4, 4]], [[1, 2, -12, 1, 3, 2, 1, 4, 33, 3]], [[17, -98, 6, -2, -71, -250, -40, -250]], [[17, 33, 4, 2, -9, 0, 75, 8, -5, -9, 75, -5]]]
results = [4, 9, 1, 20, 9, 21, 24, 13, 0, 13, 16, 6, 9, 6, 7, 10, 13, 16, 18, 9, 22, 16, 24, 18, 29, 12, 29, 39, 20, 12, 31, 20, 20, 25, 21, 6, 18, 37, 4, 10, 16, 13, 11, 12, 11, 22, 18, 12, 12, 9, 13, 13, 27, 16, 24, 16, 16, 6, 13, 9, 11, 6, 11, 16, 16, 3, 9, 4, 4, 28, 12, 28, 18, 24, 16, 11, 18, 25, 12, 20, 31, 16, 16, 27, 12, 36, 27, 16, 18, 27, 13, 13, 13, 6, 46, 9, 27, 16, 11, 16, 10, 6, 12, 6, 24, 18, 21, 16, 34]

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
        func_name = "find_even_pair"
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
        for test_case in ['assert find_even_pair([5, 4, 7, 2, 1]) == 4', 'assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9', 'assert find_even_pair([1, 2, 3]) == 1']:
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
