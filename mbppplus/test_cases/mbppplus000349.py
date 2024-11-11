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
inputs = [[[2, 1, 4, 3, 6, 7, 6, 3]], [[4, 1, 2]], [[1, 2, 3]], [[2, 5, 4, 3, 6, 7, 8, 9]], [[1, 3, 5, 7, 9, 11, 13, 15]], [[2, 13, 5, 4, 3, 6, 7, 8, 9]], [[1, 3, 5, 7, 15, 9, 11, 13, 15]], [[2, 5, 4, 3, 6, 7, 8]], [[2, 13, 5, 4, 4, 3, 6, 7, 8, 13]], [[2, 5, 4, 3, 3, 6, 8, 8, 8, 9]], [[2, 13, 5, 15, 4, 11, 3, 6, 7, 8, 9]], [[2, 9, 5, 4, 4, 3, 6, 13, 7, 8, 13]], [[1, 3, 5, 7, 15, 9, 11, 13, 15, 3]], [[2, 5, 4, 3, 7, 8, 9, 5]], [[2, 9, 5, 4, 5, 3, 6, 13, 7, 8, 13]], [[1, 3, 5, 7, 15, 9, 11, 13, 15, 3, 3]], [[2, 13, 5, 15, 4, 7, 11, 3, 6, 7, 8, 9]], [[2, 13, 5, 15, 4, 4, 11, 3, 6, 7, 8, 9]], [[2, 5, 4, 3, 7, 8]], [[2, 13, 5, 15, 7, 11, 3, 6, 7, 8, 9, 3]], [[2, 13, 5, 15, 4, 4, 11, 3, 6, 7, 8, 9, 5]], [[2, 13, 5, 15, 4, 11, 3, 6, 7, 8, 9, 5]], [[3, 9, 5, 4, 4, 3, 3, 6, 13, 7, 8, 13]], [[2, 5, 4, 3, 6, 8, 9, 7]], [[1, 5, 6, 15, 9, 11, 13, 15, 3]], [[3, 5, 7, 15, 9, 11, 13, 15, 3]], [[1, 3, 5, 7, 15, 9, 13, 11, 13, 15]], [[3, 9, 5, 4, 4, 3, 3, 6, 13, 7, 8, 3]], [[1, 5, 6, 15, 9, 11, 13, 15, 8]], [[1, 5, 4, 3, 3, 6, 8, 8, 8, 9]], [[2, 13, 5, 15, 4, 4, 11, 3, 11, 6, 7, 8, 9, 5]], [[3, 13, 5, 15, 4, 4, 11, 3, 6, 7, 8, 9, 9]], [[3, 13, 5, 15, 4, 4, 11, 3, 6, 8, 8, 9, 9]], [[1, 3, 3, 5, 7, 15, 11, 9, 11, 13, 15]], [[2, 9, 5, 7, 4, 3, 6, 13, 7, 8, 13]], [[2, 13, 5, 4, 4, 3, 1, 7, 8, 13]], [[1, 5, 4, 3, 3, 6, 8, 8, 8]], [[2, 5, 15, 4, 7, 11, 3, 6, 7, 8, 9]], [[2, 9, 5, 5, 4, 3, 6, 13, 7, 8, 13]], [[1, 5, 4, 3, 3, 6, 3, 10, 8, 8, 8, 9]], [[1, 5, 4, 3, 3, 6, 8, 8, 11, 8, 9]], [[3, 13, 5, 15, 4, 11, 3, 6, 7, 8, 9, 9]], [[2, 13, 15, 4, 7, 11, 3, 6, 7, 8, 9]], [[1, 3, 3, 5, 7, 7, 15, 11, 9, 11, 13, 15, 5]], [[1, 5, 4, 3, 6, 8, 9, 7]], [[1, 3, 5, 7, 15, 9, 11, 4, 13, 15, 3, 3]], [[2, 9, 5, 4, 4, 6, 13, 7, 8, 13]], [[3, 9, 5, 7, 4, 3, 3, 6, 13, 7, 8, 13, 3]], [[3, 9, 2, 5, 4, 6, 4, 3, 3, 6, 13, 7, 8, 3]], [[1, 3, 7, 9, 11, 15]], [[1, 5, 4, 3, 3, 8, 8, 8, 9, 8, 4]], [[1, 3, 5, 5, 7, 9, 11, 13, 15]], [[2, 13, 5, 15, 15, 11, 3, 6, 7, 8, 9, 3]], [[1, 3, 3, 5, 7, 7, 15, 11, 9, 11, 13, 15, 9, 5]], [[1, 5, 6, 15, 9, 11, 7, 13, 15, 8]], [[2, 13, 5, 15, 4, 4, 11, 3, 6, 7, 8, 9, 5, 3]], [[1, 5, 6, 9, 11, 7, 13, 15, 8, 15]], [[1, 5, 4, 3, 3, 6, 8, 8, 11, 8, 9, 3]], [[13, 5, 15, 4, 4, 11, 3, 11, 6, 7, 8, 9, 5]], [[10, 1, 5, 6, 9, 11, 7, 13, 15, 8, 15]], [[3, 5, 7, 15, 9, 11, 13, 15, 3, 3]], [[2, 13, 5, 4, 3, 6, 3, 7, 8, 5, 5]], [[1, 3, 7, 9, 11, 15, 3]], [[3, 9, 4, 4, 3, 3, 6, 13, 7, 8, 13, 4]], [[2, 9, 5, 4, 5, 3, 6, 12, 13, 7, 8, 13, 2]], [[3, 5, 7, 15, 9, 11, 13, 15, 3, 13]], [[1, 5, 4, 3, 6, 8, 8, 8]], [[1, 3, 5, 7, 15, 9, 11, 4, 15, 3, 3]], [[3, 9, 5, 7, 4, 3, 3, 6, 13, 7, 8, 13, 3, 3]], [[1, 3, 5, 7, 15, 9, 13, 11, 12, 13, 15]], [[2, 13, 5, 15, 4, 4, 10, 3, 6, 7, 8, 9]], [[1, 5, 6, 15, 9, 11, 13, 10, 3]], [[3, 5, 7, 15, 9, 13, 11, 13, 15, 15]], [[1, 5, 15, 9, 11, 13, 10, 3]], [[2, 5, 4, 3, 7, 8, 5, 5]], [[15, 1, 3, 5, 15, 15, 9, 11, 16, 11, 13, 15]], [[1, 5, 4, 3, 3, 6, 8, 8, 8, 8]], [[1, 3, 5, 7, 15, 9, 11, 13, 15, 3, 15]], [[1, 3, 5, 7, 9, 11, 13, 15, 3, 3]], [[1, 5, 6, 9, 11, 13, 10, 3]], [[1, 5, 4, 3, 2, 3, 6, 3, 10, 8, 8, 8, 9]], [[2, 9, 5, 5, 5, 3, 6, 12, 13, 9, 8, 13, 2]], [[3, 9, 5, 7, 4, 3, 3, 6, 13, 2, 8, 13, 3, 2]], [[2, 5, 2, 3, 3, 6, 8, 8, 8, 9]], [[1, 5, 6, 15, 9, 11, 13, 15, 8, 15]], [[2, 4, 3, 7, 8, 10, 5]], [[2, 13, 13, 5, 4, 3, 6, 7, 8, 9, 7]], [[3, 5, 7, 15, 9, 13, 11, 13, 15]], [[2, 5, 4, 3, 3, 8, 6, 8, 8, 8, 9]], [[1, 15, 5, 6, 15, 9, 11, 13, 15, 8, 15]], [[2, 9, 5, 5, 4, 3, 6, 13, 7, 8, 13, 8, 2]], [[2, 13, 13, 5, 4, 6, 7, 8, 9, 7]], [[1, 5, 4, 11, 3, 6, 8]], [[1, 5, 15, 9, 11, 13, 15, 8, 15]], [[2, 13, 5, 15, 7, 11, 3, 6, 7, 8, 9]], [[10, 1, 5, 6, 9, 11, 7, 13, 15, 8, 7, 15]], [[3, 9, 3, 5, 7, 4, 3, 6, 13, 7, 8, 13, 3, 3]], [[1, 15, 11, 5, 6, 15, 9, 11, 13, 15, 8, 15]], [[2, 5, 4, 3, 7, 8, 9, 5, 5, 5]], [[1, 5, 6, 15, 9, 11, 7, 15, 8]], [[1, 5, 6, 9, 11, 7, 15, 7, 15]], [[3, 9, 5, 7, 4, 3, 3, 6, 13, 7, 8, 13, 3, 5]], [[7, 13, 5, 15, 15, 11, 3, 6, 7, 8, 9, 3]], [[1, 3, 5, 5, 7, 1, 11, 13, 15]], [[2, 13, 5, 15, 4, 11, 6, 7, 8, 9, 11, 4]]]
results = [True, True, False, True, True, False, True, True, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, True, True, True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, True, False, False, True, False, False, False, True, False, True, False, False, True, False, False, False, True, False, False, True, True, False, True, False, True, True, True, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, False, True, True, False, False, True, False]

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
        func_name = "odd_position"
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
        for test_case in ['assert odd_position([2,1,4,3,6,7,6,3]) == True', 'assert odd_position([4,1,2]) == True', 'assert odd_position([1,2,3]) == False']:
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
