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
inputs = [[[1, 2, 3]], [[15, 12, 13, 10]], [[0, 1, 2]], [[10, -5, 3, 7, -2]], [[10, -5, 3, 7, -2, -2]], [[10, -5, -5, 3, 7, -2]], [[10, -5, -5, 3, -2]], [[-2, 10, -5, 3, 7, -2]], [[-2, 10, -5, 3, 7, -3, -2]], [[10, -5, 3, -2]], [[-5, 3, 7, -2, -2]], [[10, 10, -5, 3, 7, -2, -2, 7]], [[-2, 10, -5, 3, 7, 7, -3, -2]], [[-5, 3, 7, 7, -2]], [[-5, -4, 3, 7, 7, -2]], [[-5, 3, 7, 7, -2, -2]], [[-6, 3, 7, 8, -2]], [[-2, -1, 10, -5, 3, 7, -1, -2]], [[10, 3, -5, 3, -2]], [[10, -5, 3, -6, -2]], [[10, -5, 9, 3, 7, -2, 7]], [[10, 10, -5, 3, 7, -2, -2]], [[10, -5, 3, 7, -2, -2, 7, -5]], [[-2, -5, -4, 3, 7, 7, -5, -2]], [[-5, -4, 3, 7, 3, -2]], [[-5, 3, 7, 7, -2, -2, 7]], [[-5, 3, 7, 7, -2, -4, -2]], [[10, -5, 9, 3, 7, -2, 7, 3]], [[9, 3, -5, 3, -2]], [[-5, 3, -2]], [[-5, -4, -5, 3, 7, 7, -2]], [[-5, -2]], [[9, 3, 7, 7, -2, -4, -2]], [[-5, -5, -6, 3, -2, -2]], [[-2, -1, 10, -5, 3, 7, -2, -1, -2]], [[10, -5, 3, 7, -2, 10]], [[10, -5, -5, -2, 3, -2]], [[-2, -5, 3]], [[-5, -3]], [[10, 3, -5, 3, 3, -2]], [[10, -5, 3, 7, -2, 7, -2]], [[-2, -5, -4, 3, 7, 7, -3, -5, -2]], [[-5, 3, 8, 7]], [[10, -5, 3, 8, -2]], [[10, -4, 3, 7, -2, 10]], [[-2, 10, -5, 3, 7, 7, -3, -2, -5]], [[10, -5, -5, 3, 7, -2, -2]], [[-2, 10, -5, 3, -1, 9, 7, -3, -2, -5]], [[-5, -5, -6, 3, -2, -2, -2, -2]], [[9, 3, 9, -5, 3, -2]], [[10, -5, -3, 7, -2, -2]], [[9, 10, 3, 7, -2, -4, -2]], [[-3]], [[-5, 3, 7, -2, -2, -5]], [[10, 3, -5, 3, -3]], [[10, 11, -5, 3, 7, -2]], [[-5, 3, 3, -2]], [[10, -5, 7, 3, -6, -2]], [[-5, -4, -3]], [[10, 11, 3, 7, -2]], [[-5, 8, -5, 3, 7, 7, -2]], [[8, 3, 12, 9, -5, 3, -2]], [[9, 3, 3, -2]], [[10, -5, -3, 11, -2, -2, 7]], [[11, -2, 10, 3, -1, 9, 7, -3, -2, -5]], [[-5, 3, 7, -1, -2, -4, -2]], [[10, -5, 3, -1, 9, 7, -3, -2, -5, 7]], [[9, 10, 3, 7, -2, -4, -2, -2]], [[-5, -2, 3, -2, 7, -2, -2]], [[9, 3, 9, -5, 3, -2, 9]], [[10, -5, 6, 7, -5]], [[10, -5, -5, 3, 7, -2, -1, -2]], [[10, -5, -5, 3, 7]], [[-5, 3, 7, -1, -2, 8, -4, -2]], [[-2, -1, 10, -5, 3, 7, -2, -1, -2, 10]], [[-2, -5, 3, 7, 7, -3, -2, -5]], [[10, -5, -5, 3, 7, -2, -2, -2]], [[9, 7, 7, -2, -4, -2]], [[10, 10, 3, 7, -2, -2, 7]], [[-2, 10, -4, 3, -1, 9, 6, -3, -2, -5]], [[-2, 10, -5, 3, 7]], [[-5, 3, 7, 7, 6, -2, -2, 7, 7]], [[6, -5, -2]], [[-5, -3, -3]], [[-2, 10, -4, 3, -1, 9, 6, -3, -2, -5, -4]], [[10, -5, 9, 3, -2, 7, 10]], [[9, 3, -5, -2]], [[10, -5, 3, 7, -2, 7]], [[-2, 10, -5, 7]], [[10, -5, 9, 3, 7, -2, -4, 7]], [[-4]], [[-5]], [[10, 7, -5, 3, 7, -2, 7, -5, -2]], [[10, -3, 9, 3, 7, -2, 7, 3]], [[10, -5, 3, 7]], [[10, -4, 3, 7, -2, 10, 7, -2]], [[10, 10, -5, 3, 7, -2, -2, 3]], [[-5, -1, -5, 3, 7, 7, -2]], [[10, -5, 9, 3, 6, -2, 7, 3, 3]], [[10, -5, 3, 7, -2, 10, 7, -2]], [[-2, -1, 10, -5, 3, 7, -2, -1, -2, 10, -2]], [[10, -5, -2, 3, 8, 10]], [[10, -3, 9, 3, 7, -2, -3, 7, 3, -2]], [[]]]
results = [6, 50, 3, 13, 11, 8, 1, 11, 8, 6, 1, 28, 15, 10, 6, 8, 10, 9, 9, 0, 29, 21, 13, -1, 2, 15, 4, 32, 8, -4, 1, -7, 18, -17, 7, 23, -1, -4, -8, 12, 18, -4, 13, 14, 24, 10, 6, 11, -21, 17, 5, 21, -3, -4, 8, 24, -1, 7, -12, 29, 13, 28, 13, 16, 27, -4, 20, 19, -3, 26, 13, 5, 10, 4, 17, 0, 4, 15, 33, 11, 13, 28, -1, -11, 7, 32, 5, 20, 10, 25, -4, -5, 20, 34, 15, 29, 24, 4, 34, 28, 15, 24, 29, 0]

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
        func_name = "_sum"
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
        for test_case in ['assert _sum([1, 2, 3]) == 6', 'assert _sum([15, 12, 13, 10]) == 50', 'assert _sum([0, 1, 2]) == 3']:
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
