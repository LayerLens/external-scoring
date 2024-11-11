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
inputs = [[[1, 1, 2, 2, 3]], [[1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8]], [[1, 2, 2, 3, 3, 4, 4]], [[]], [[2, 2, 2, 2, 2, 2]], [[1, 1, 1, 1, 1, 1]], [[6]], [[1, 2, 3, 4, 5, 6]], [[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]], [[5]], [[1, 1, 4, 4, 5, 6]], [[0, 1, 4, 4, 5, 6]], [[4, 5, 5]], [[4, 4, 5]], [[1, 1, 4, 4, 6]], [[0, 1, 4, 4, 5]], [[2, 2, 2, 2, 2]], [[1, 1, 4, 6]], [[0, 4, 4, 5, 6]], [[4, 5]], [[1, 1, 4, 4, 5]], [[1, 1, 1, 1, 1]], [[1, 2, 4, 6]], [[5, 5]], [[4, 5, 5, 5]], [[1, 1, 1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1, 1, 1, 1]], [[2, 2, 2, 2, 2, 2, 2, 2]], [[2, 2, 2, 2, 2, 2, 2, 2, 2]], [[1, 1, 1]], [[1, 1, 4, 4]], [[0, 1, 4, 4, 8]], [[2, 2, 2, 2, 2, 2, 2, 15]], [[4, 4, 4]], [[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]], [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]], [[False, False]], [[6, 6, 6]], [[1, 4, 4]], [[5, 5, 5]], [[4, 5, 5, 5, 5]], [[1, 4]], [[1, 1]], [[6, 6]], [[1, 1, 1, 1, 1, 1, 1, 1, 1]], [[2, 2, 2, 2, 2, 2, 2, 2, 15]], [[1, 2, 3, 3, 4, 5, 6]], [[0, 4, 4, 8]], [[1, 1, 4]], [[1, 4, 6]], [[0, 1, 1, 1, 1, 1, 1, 1, 1]], [[4, 6]], [[False, True]], [[1, 1, 11]], [[1, 1, 2]], [[0, 1, 4, 8]], [[0, 4, 4, 4, 6, 6]], [[2, 2, 2, 2, 2, 2, 2, 2, 2, 15]], [[1, 5]], [[4, 4, 4, 4, 4]], [[3, 5, 5]], [[5, 5, 5, 5]], [[1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 15, 15]], [[1, 3, 5, 5, 6]], [[0, 4, 8]], [[4, 4, 6]], [[0, 1, 4, 4, 6]], [[1, 1, 4, 4, 5, 5]], [[1, 1, 2, 2]], [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [[1, 1, 11, 11]], [[True]], [[4, 4]], [[False, True, True, True, True, True]], [[5, 11]], [[1, 1, 1, 4, 4]], [[4, 4, 4, 4]], [[2, 2, 2, 2, 2, 2, 2]], [[1, 2, 4, 6, 6]], [[4, 4, 8]], [[0, 2, 2, 2, 2]], [[1, 2, 3, 3, 11]], [[4, 4, 6, 6]], [[3, 5]], [[2, 5]], [[0, 1, 1, 1, 1, 1, 1, 1]], [[3, 6]], [[1, 4, 4, 6]], [[0, 2, 2, 2]], [[0, 1, 1]], [[1, 3, 4, 7]], [[1, 4, 6, 6]], [[1, 4, 4, 4]], [[False]], [[1, 1, 10, 11, 11]], [[0, 4, 5, 5]], [[0, 1, 4, 5, 6]], [[1, 4, 4, 5, 6]], [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [[1, 1, 6, 6, 6]], [[4]], [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [[1, 1, 12]], [[0, 2, 6, 6]], [[9]], [[1, 1, 1, 4, 4, 4]], [[1, 11, 11]], [[1, 1, 4, 4, 5, 9]], [[3, 6, 6]], [[1, 3, 3, 5, 13]]]
results = [3, 8, 1, 0, 0, 0, 6, 7, 11, 5, 3, 2, 4, 5, 6, 4, 2, 2, 3, 1, 5, 1, 1, 0, 1, 1, 0, 0, 2, 1, 0, 9, 13, 4, 12, 2, 0, 6, 1, 5, 4, 5, 0, 0, 1, 15, 4, 8, 4, 3, 0, 2, 1, 11, 2, 13, 4, 13, 4, 4, 3, 0, 10, 4, 12, 6, 7, 0, 0, 1, 0, 1, 0, 1, 14, 1, 0, 2, 7, 8, 0, 8, 0, 6, 7, 1, 5, 7, 2, 0, 1, 5, 5, 0, 10, 4, 6, 2, 1, 6, 4, 0, 12, 2, 9, 5, 1, 12, 3, 9]

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
        func_name = "search"
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
        for test_case in ['assert search([1,1,2,2,3]) == 3', 'assert search([1,1,3,3,4,4,5,5,7,7,8]) == 8', 'assert search([1,2,2,3,3,4,4]) == 1']:
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
