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
inputs = [[[1, 3, 5]], [[2, 4, 1, 3]], [[8, 9, 1]], [[1, 2, 3, 4, 5]], [[2, 3, 4, 6, 7]], [[4, 5, 6, 8, 9]], [[11, 13, 15, 17, 19, 21, 23, 25, 27, 29]], [[2, 4, 6, 8, 10, 1, 3, 5, 7, 9]], [[1, 2, 4, 7, 4, 5]], [[2, 3, 3, 4, 6, 7]], [[2, 4, 6, 8, 10, 1, 3, 7, 9]], [[2, 4, 6, 8, 10, 1, 3, 7, 9, 3]], [[2, 1, 2, 3, 4, 5]], [[2, 1, 2, 3, 4, 27, 5, 1]], [[4, 5, 6, 8, 9, 5]], [[2, 3, 3, 4, 17, 6, 7]], [[2, 1, 2, 2, 3, 4, 5]], [[11, 13, 15, 17, 19, 23, 25, 27, 11, 29, 19]], [[3, 4, 6, 8, 10, 1, 3, 7, 8, 7, 9]], [[2, 4, 6, 10, 1, 3, 5, 7, 9]], [[4, 6, 8, 10, 1, 3, 7, 8, 7, 9]], [[2, 1, 2, 2, 3, 4, 5, 3]], [[1, 2, 4, 7, 4, 5, 2]], [[3, 4, 6, 8, 10, 23, 1, 3, 7, 8, 7, 9]], [[2, 3, 4, 6, 7, 4]], [[2, 4, 6, 10, 1, 5, 7, 9]], [[11, 13, 21, 17, 19, 21, 23, 27, 29]], [[4, 5, 6, 8, 9, 5, 8]], [[1, 1, 4, 7, 4, 5]], [[1, 1, 4, 7, 4, 5, 1]], [[2, 1, 2, 2, 3, 4, 5, 2]], [[11, 13, 15, 17, 19, 21, 23, 25, 7, 29]], [[1, 2, 7, 4, 5]], [[2, 4, 6, 10, 2, 3, 5, 7, 9]], [[3, 4, 23, 6, 8, 10, 1, 3, 7, 8, 7, 9]], [[4, 5, 6, 23, 8, 9, 5, 5]], [[2, 3, 4, 6, 19, 4]], [[4, 8, 10, 1, 3, 7, 8, 7, 9]], [[2, 3, 3, 4, 6, 19, 4]], [[4, 1, 2, 4, 7, 4, 5, 2]], [[2, 4, 6, 10, 1, 3, 5, 7, 9, 2, 2]], [[2, 3, 4, 5, 19, 4]], [[13, 1, 4, 7, 4, 5, 2]], [[2, 4, 6, 10, 1, 3, 5, 7, 9, 2, 2, 2]], [[2, 1, 2, 3, 4, 27, 5, 1, 4]], [[2, 1, 3, 3, 4, 5, 2]], [[1, 4, 7, 4, 5]], [[3, 4, 23, 6, 8, 10, 3, 7, 8, 7, 3]], [[2, 1, 2, 2, 3, 4, 5, 2, 4]], [[1, 4, 7, 4, 5, 1]], [[11, 13, 15, 17, 19, 21, 23, 27, 25, 7, 29]], [[4, 6, 8, 2, 10, 1, 3, 7, 8, 7, 9]], [[2, 3, 4, 7]], [[2, 23, 4, 7, 7, 7, 7]], [[2, 2, 1, 2, 2, 3, 4, 5, 5]], [[3, 4, 6, 8, 10, 1, 3, 27, 8, 7, 9]], [[1, 2, 3, 4, 5, 3]], [[2, 3, 5, 4, 6, 7, 4]], [[2, 2, 3, 4, 15, 5, 3, 5]], [[1, 2, 3, 3, 5, 3]], [[6, 1, 4, 7, 4, 5]], [[11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 21]], [[13, 15, 17, 19, 21, 23, 25, 27, 29, 29]], [[4, 6, 8, 10, 1, 3, 5, 7, 9, 8]], [[11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 11]], [[2, 1, 2, 3, 4]], [[12, 13, 15, 17, 19, 21, 23, 25, 29, 11]], [[2, 3, 3, 7, 6, 19, 4, 4]], [[11, 13, 10, 15, 17, 19, 21, 23, 25, 27, 29, 21]], [[2, 4, 6, 10, 2, 3, 5, 9]], [[11, 13, 15, 17, 19, 21, 23, 25, 19, 29]], [[2, 3, 3, 7, 6, 18, 4, 4, 3]], [[3, 6, 8, 1, 3, 7, 8, 7, 9]], [[3, 4, 23, 6, 8, 10, 3, 7, 8, 7]], [[2, 27, 6, 10, 1, 3, 5, 7, 9, 2, 2]], [[3, 4, 23, 8, 10, 3, 29, 8, 7, 3]], [[12, 13, 15, 17, 19, 21, 23, 27, 25, 7, 29]], [[1, 4, 7, 4, 5, 4]], [[27, 11, 13, 15, 17, 19, 21, 23, 25, 19, 29]], [[11, 13, 29, 17, 19, 21, 23, 25, 27, 29, 11, 17]], [[3, 4, 23, 8, 10, 3, 29, 27, 8, 7, 3]], [[2, 4, 6, 6, 8, 10, 1, 3, 5, 7, 9]], [[3, 4, 6, 8, 10, 1, 3, 7, 8, 9, 9]], [[2, 1, 3, 3, 4, 5, 2, 2]], [[4, 5, 7, 6, 8, 9]], [[2, 3, 3, 7, 6, 9, 4, 4]], [[1, 4, 7, 4, 5, 4, 4]], [[4, 1, 2, 4, 4, 5, 2]], [[4, 5, 6, 8, 9, 5, 6]], [[11, 13, 15, 20, 17, 19, 21, 23, 25, 27, 21]], [[3, 4, 8, 10, 3, 29, 27, 8, 7, 3]], [[12, 15, 17, 19, 21, 23, 10, 27, 25, 7, 29]], [[2, 1, 2, 4, 4, 5]], [[3, 6, 8, 10, 1, 3, 7, 8, 7, 9]], [[2, 4, 6, 8, 10, 1, 3, 7, 6, 9, 3, 8]], [[4, 23, 6, 8, 10, 3, 7, 8, 7]], [[3, 4, 7, 10, 1, 3, 7, 8, 7, 9]], [[13, 15, 19, 21, 23, 26, 27, 29, 29, 26]], [[11, 13, 7, 29, 17, 19, 21, 23, 25, 27, 29, 11, 17]], [[2, 4, 6, 8, 10, 1, 3, 7]], [[1, 1, 5, 7, 4, 5]], [[4, 5, 7, 6, 8, 9, 9]], [[1, 1, 3, 3, 5, 3]], [[2, 1, 2, 3, 4, 27, 5, 1, 2]], [[12, 13, 15, 17, 19, 23, 25, 27, 11, 19, 12]], [[3, 4, 6, 8, 10, 1, 3, 27, 8, 7, 9, 4]], [[3, 4, 23, 6, 8, 10, 1, 3, 7, 8, 7, 9, 1, 6]], [[11, 13, 21, 17, 19, 21, 23, 27, 29, 21]]]
results = [1, 1, 9, 1, 3, 5, 11, 1, 1, 3, 1, 1, 1, 1, 5, 3, 1, 11, 3, 1, 1, 1, 1, 3, 3, 1, 11, 5, 1, 1, 1, 11, 1, 3, 3, 5, 3, 1, 3, 1, 1, 3, 13, 1, 1, 1, 1, 3, 1, 1, 11, 1, 3, 23, 1, 3, 1, 3, 3, 1, 1, 11, 13, 1, 11, 1, 13, 3, 11, 3, 11, 3, 3, 3, 27, 3, 13, 1, 27, 11, 3, 1, 3, 1, 5, 3, 1, 1, 5, 11, 3, 15, 1, 3, 1, 23, 3, 13, 11, 1, 1, 5, 1, 1, 13, 3, 3, 11]

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
        func_name = "first_odd"
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
        for test_case in ['assert first_odd([1,3,5]) == 1', 'assert first_odd([2,4,1,3]) == 1', 'assert first_odd ([8,9,1]) == 9']:
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
