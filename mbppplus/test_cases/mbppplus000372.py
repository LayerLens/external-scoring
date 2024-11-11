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
inputs = [[[1, 2, 3]], [[1, 2, 1, 4]], [[1, 1]], [[2, 2, 2, 2, 2]], [[1, 2, 3, 4, 5]], [[0, 0, 0, 0, 0]], [[1, 3, 5, 7, 9]], [[2, 4, 6, 8, 10]], [[2, -2, -2, -2, -2]], [[1, -2, 3, -4, 5]], [[-1, 2, 3, 5]], [[1, -2, 3, 5]], [[0, 2, 3, 5]], [[1, 3, 5, 7, 9, 1]], [[0, 9, 4, 5]], [[0, 2, 9, 3, 5]], [[-1, 2, 3, 4]], [[1, 3, 5]], [[1, -2, 1, 3, -4, 5]], [[1, 2, 3, 4, 3]], [[3, 3, 1, 2, 2, 2]], [[1, -2, 1, 3, -4, 5, -4]], [[-1, 2, 3, 4, 4]], [[1, 3, 5, 7]], [[-1, 2, 3, 5, 4, 4, 3]], [[-1, 2, 3, 2, 5, 3]], [[9, 5]], [[10, 0, 9, 4, 5, 9]], [[0, 2, 0, 2, 3, 5]], [[1, 3, 5, 3]], [[1, 1, 4, 3, 1]], [[-1, 7, 2, 3, 5]], [[1, 3, 5, 7, 7]], [[1, 1, 3, 10, 5, 3]], [[2, -2, -2, -2, -2, -2, -2]], [[3, 3, 1, 2, 4, 2, 2]], [[9, 1]], [[1, 10, 5, 3]], [[0, 9, 4, 5, 5]], [[0, 0, 0, 0, 0, 0, 0]], [[1, 1, 3, 10, 9, 5, 3, 9]], [[1, 1, 2, 5, 7]], [[1, 3, 7, 3, 3]], [[-1, 2, 3, 2, 5, 3, 3]], [[3, 1, 3, 7, 3, 3]], [[0, 0, 0, 1, 0, 0]], [[1, -2, 1, 3, -4, 5, -4, 1]], [[1, 10, 5, 2, 3]], [[0, 2, 9]], [[1, 2, 4, 3, 1]], [[2, 4, 6, 8, 10, 2]], [[-1, 7, 2, 3, 5, 3]], [[0, -1, 2, 9]], [[-1, 2, 3, 5, 4, 5, 3]], [[1, 1, 2, 1, 7, 1]], [[1, 1, 3, 10, 9, 5, 3, 3, 9]], [[1, 3, 8, 3]], [[1, 3, 5, 7, 9, 3]], [[1, 2, 3, 3]], [[2, -2, -2, -2, -2, -2]], [[1, 3, 7, 7]], [[3, 3, 1, 2, 1, 2, 2]], [[-1, 2, 3]], [[1, 10, 5]], [[0, 0, 0, 0, 0, 0, 0, 0]], [[8, 1, 3, 5, 4]], [[0, 0, 0, 0, 0, 0]], [[-1, 7, 2, 3, 5, 7]], [[3, 3, 1, 2, 10, 2, 2]], [[2, 9, -2, -2, -2, -2, -2]], [[1, 4, 3, 6]], [[1, 1, 3, -4, 5, -4, 1, 3]], [[7, 1, 5, 7, 9]], [[9, -1, -2, 5]], [[-1, 2, 3, 2]], [[1, 1, 2, 1, 5, 7]], [[0, 0, 0, 1, 0, 0, 0]], [[1, 1, 2, 1, 5, 7, 6, 2]], [[3, 3, 1, 2, -2, 2]], [[1, 5, 5, 3]], [[3, 6, 1, 2, 1, 2, 2]], [[-1, 1, 5, -2, 2, 3]], [[3, 5]], [[-2, 1, 3, -4, 5, -4, 1]], [[1, 4, 3, 1]], [[-1, 2, 3, 6, 4]], [[2, 4, 6, 9, 8, 10, 2]], [[3, 3, 1, 2, 2]], [[2, 3, 10, 5, 3]], [[4, -2, 4, 3, -4, 5, -2]], [[2, 10, 2, 3]], [[2, 1, 3, 8, 3, 3]], [[1, 0, 0, 0, 0]], [[2, 1, 3, 5, 7, 9, 1]], [[3, 1, 3, 7, 4, 3, 3]], [[0, 2, 9, 0, -1, 5]], [[3, 6, 1, 2, 1, -2, 2]], [[1, -2, 1, 3, -4, 5, -4, 1, -4]], [[1, 4, 5, 7]], [[0, -1, 0, 0, 0, 0]], [[-2, 0, 9, 4, 5]], [[-1, 2, 2, 3, 2, 2]], [[3, 3, 5]], [[2, 3, 6, 4, 3]], [[1, 3, 2, 3, 5, 5, 3]], [[-2, 0, 9, 4, 5, 0]], [[2, 4, 6, 8, 10, 2, 4]], [[1, 1, 2, 2, 5, 7]], [[3, 3, 1, 2, 10, 2, 2, 2]], [[-1, 2, 3, 2, 5, 3, 9, 3]], [[5, 2, 2, 2, 2, 2, 2]], [[3, 3, 1, 2, -4, 10, 2, 2, 2]]]
results = [True, True, False, True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True, True, False, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True]

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
        func_name = "is_product_even"
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
        for test_case in ['assert is_product_even([1,2,3])', 'assert is_product_even([1,2,1,4])', 'assert not is_product_even([1,1])']:
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
