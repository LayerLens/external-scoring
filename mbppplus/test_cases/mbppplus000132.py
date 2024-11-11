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
inputs = [[[5, 6, 12, 1, 18, 8]], [[3, 20, 17, 9, 2, 10, 18, 13, 6, 18]], [[5, 6, 12, 1]], [[]], [[2]], [[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]], [[1, 3, 5, 7, 9]], [[3, 1, 8, 6, 2, 4, 9, 7]], [[3, 1, 8, 6, 2, 3, 9, 7]], [[1, 3, 7, 9]], [[1, 2, 3, 7, 9, 1]], [[3, 1, 8, 6, 2, 2, 3, 9, 7, 3]], [[3, 1, 8, 7, 6, 2, 4, 9, 7]], [[128, 1, 8, 6, 4, 9, 7]], [[1024, 2, 3, 7, 9]], [[1, 3, 7]], [[9, 90]], [[1, 3, 7, 0, 1, 1]], [[1024, 7, 9, 1]], [[128, 1, 8, 6, 4, 90, 7, 128]], [[1, 2, 90, 7, 10, 2]], [[3, 1, 8, 6, 3, 9, 7]], [[3, 1, 6, 2, 4, 9, 7]], [[1, 8, 3, 7]], [[256, 1, 8, 6, 2, 3, 9, 7, 3]], [[128, 1, 8, 6, 4, 9, 0, 7]], [[0, 256, 1, 8, 6, 2, 3, 8, 7, 3, 3]], [[1, 2, 3, 7, 9, 1, 2]], [[3, 1, 5, 7, 6, 2, 4, 9, 7]], [[3]], [[3, 1, 2, 4, 9, 7]], [[3, 1, 8, 6, 2, 3, 3, 9, 7]], [[128, 2, 8, 6, 90, 7, 128]], [[1, 3, 7, 0, 1, 0]], [[1, 3, 2, 7]], [[1, 3, 5, 7, 9, 1]], [[128, 1, 1, 6, 8, 6, 0, 7]], [[2, 4, 8, 16, 32, 64, 128, 128, 512, 1024]], [[3, 1, 8, 6, 2, 2, 3, 9, 7, 3, 3]], [[1, 8, 3, 7, 1]], [[3, 4, 8, 32, 64, 128, 128, 1024, 1024]], [[1, 2, 9, 7, 10, 2]], [[128, 1, 8, 6, 4, 10, 0, 7, 1]], [[1, 5, 7, 1]], [[1, 9, 7, 10, 2]], [[3, 1, 2, 8, 6, 2, 4, 9, 7, 1, 4]], [[1, 8, 3, 1, 1]], [[128, 1, 8, 32, 4, 9, 0, 7]], [[3, 1, 10, 8, 6, 2, 4, 9, 7, 3]], [[1, 5, 7, 9]], [[128, 2, 8, 6, 4, 9, 7]], [[3, 1, 8, 6, 2, 2, 3, 9, 2, 7, 3]], [[1, 5, 7, 9, 9]], [[1, 7, 5, 7, 9]], [[128, 8, 1, 8, 6, 4, 90, 7, 128]], [[1, 8, 3, 1, 128, 1]], [[3, 1, 8, 6, 2, 2, 3, 9, 3, 1]], [[1024, 2, 7, 9]], [[1024, 1, 2, 7, 9]], [[129, 1, 1, 6, 8, 6, 0, 7, 128]], [[1, 8, 3, 1, 128, 1, 3]], [[1024, 1, 2, 7, 9, 7]], [[1024, 7, 9]], [[32, 1, 8, 3, 2, 128, 1, 3]], [[1, 9, 7, 9, 2]], [[512, 8, 256, 3, 1, 1]], [[128, 1, 8, 6, 4, 90, 7, 5, 128]], [[4, 1, 2, 4, 9, 7]], [[3, 9, 1, 2, 8, 6, 4, 8, 7, 1, 4]], [[3, 3, 1, 10, 8, 6, 2, 4, 9, 7, 3]], [[128, 1, 6, 9, 8, 6, 0, 7]], [[1, 9, 7, 10, 2, 9]], [[4, 1, 9, 7, 9, 2, 7]], [[4, 1, 4, 9, 7, 1]], [[5, 1, 9, 8, 7, 6, 1, 4, 9, 7]], [[1, 5, 7, 9, 7]], [[128, 1, 6, 9, 8, 1024, 0, 7, 6]], [[256, 1, 8, 6, 2, 3, 9, 7, 2, 3]], [[128, 1, 8, 6, 4, 10, 0, 7, 1, 128]], [[32, 1, 8, 6, 2, 3, 3, 9, 7]], [[16, 1, 8, 6, 2, 4, 9, 7]], [[3, 1, 2, 4, 9, 7, 7]], [[1, 1024, 2, 3, 7, 9, 1]], [[128, 1, 8, 6, 7, 4, 90, 7]], [[1, 8, 7, 9, 2]], [[1024, 7, 3, 1024]], [[1, 3, 7, 8, 0, 1, 1]], [[1, 7, 10, 7, 9]], [[128, 1, 1, 6, 8, 6, 0, 7, 128]], [[128, 1, 6, 8, 9, 8, 1024, 0, 7, 6, 0, 6]], [[1, 9, 8, 7, 9, 2]], [[1, 512, 7, 10, 9]], [[3, 1, 8, 6, 2, 2, 3, 9, 7, 3, 2, 3]], [[1, 3, 7, 1, 0]], [[4, 1, 8, 6, 2, 2, 3, 9, 7, 3, 7, 3]], [[256, 1, 8, 6, 2, 3, 9, 8, 3]], [[32, 1, 8, 3, 2, 128, 10, 3, 10]], [[1024, 9, 5]], [[3, 1, 8, 6, 2, 2, 3, 2, 9, 7, 3, 3]], [[7, 1]], [[129, 1, 1, 6, 8, 6, 0, 128]], [[1, 3, 7, 0, 1, 1, 7]], [[3, 9, 1, 2, 8, 0, 4, 8, 7, 1, 4, 9]], [[4, 1, 9, 6, 9, 2, 16]], [[128, 1, 8, 8, 32, 4, 9, 0, 7]], [[3, 1, 7, 6, 2, 2, 3, 9, 1, 7, 3, 2, 3]], [[1, 3, 4, 5, 7, 9, 1]], [[4, 1, 7, 6, 2, 2, 3, 9, 1, 7, 3, 2, 3, 3]]]
results = [30, 26, 12, 0, 2, 682, 0, 10, 10, 0, 0, 10, 18, 140, 1024, 0, 0, 0, 1024, 140, 100, 8, 10, 0, 266, 140, 6, 2, 10, 0, 2, 10, 354, 0, 2, 0, 136, 682, 10, 0, 1224, 10, 140, 0, 2, 16, 0, 140, 20, 0, 140, 12, 0, 0, 352, 128, 10, 1024, 1026, 136, 128, 1026, 1024, 42, 2, 768, 268, 6, 16, 10, 142, 2, 4, 8, 0, 0, 148, 268, 140, 42, 26, 2, 2, 226, 2, 1024, 0, 10, 264, 1158, 8, 0, 12, 0, 14, 266, 62, 1024, 10, 0, 8, 0, 16, 20, 168, 2, 4, 6]

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
        func_name = "sum_even_and_even_index"
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
        for test_case in ['assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30', 'assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26', 'assert sum_even_and_even_index([5, 6, 12, 1]) == 12']:
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
