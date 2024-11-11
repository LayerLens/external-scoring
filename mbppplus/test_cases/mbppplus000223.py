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
inputs = [[[1, 2, 3, 4, 5]], [[1, 2, 3, 5, 6]], [[1, 2, 1]], [[4, 1, 9, 5, 2]], [[4, 9, 5, 2]], [[4, 5, 1, 9, 5, 2]], [[4, 5, 1, 9, 5, 2, 2]], [[4, 4, 9, 5, 2]], [[4, 5, 1, 9, 5, 2, 2, 2]], [[5, 1, 9, 5, 2]], [[4, 1, 9, 5, 2, 9]], [[4, 5, 1, 9, 5, 2, 2, 5]], [[5, 1, 9, 1, 2]], [[4, 2, 4, 9, 5, 2]], [[4, 1, 0, 9, 5, 2, 9]], [[4, 9, 5, 3]], [[0, 9, 2, 9]], [[4, 1, 5, 2, 9]], [[4, 5, 1, 9, 5, 5, 2, 2]], [[4, 5, 1, 9, 5, 2, 1]], [[4, 5, 1, 9, 6, 2, 2]], [[1, 4, 5, 2]], [[4, 5, 1, 5, 5, 2, 1, 5]], [[5, 1, 9, 1, 1, 2]], [[4, 9, 5, 2, 9]], [[0, 4, 2, 9]], [[4, 9, 1, 5]], [[1, 5, 1, 9, 4, 5, 2]], [[1, 5, 1, 9, 2, 4, 5, 2]], [[5, 1, 3, 1, 1, 2]], [[9, 2, 9, 9, 0, 0, 9]], [[5, 1, 9, 5, 2, 9]], [[6, 5, 1, 5, 5, 2, 1, 5]], [[4, 2, 3, 4, 9, 5, 2]], [[4, 2, 9, 3, 2]], [[4, 2, 9, 3, 2, 9]], [[2, 9, 2, 9, 9, 0, 0, 9]], [[2, 4, 5, 1, 0, 2, 9, 5, 2, 2, 5]], [[4, 3, 5, 1, 9, 5, 5, 2, 2]], [[4, 9, 5]], [[1, 4, 9, 2]], [[4, 5, 1, 6, 5, 2, 1, 5]], [[6, 5, 1, 9, 2, 4, 2]], [[3, 2, 4, 9, 5, 2]], [[4, 1, 9, 5]], [[4, 9, 1, 4, 9]], [[4, 2, 9, 2, 3, 2, 9]], [[1, 4, 2]], [[4, 5, 1, 9, 5, 5, 9, 2]], [[4, 5, 1, 6, 5, 2, 1, 5, 6]], [[4, 5, 1, 9, 5, 2, 1, 9]], [[4, 3, 1, 0, 9, 5, 2, 9]], [[4, 9, 5, 3, 5, 3]], [[5, 1, 5, 2]], [[4, 5, 3, 9, 5, 2]], [[4, 5, 1, 9, 5, 2, 9]], [[4, 3, 3, 4, 5, 2]], [[5, 5, 1, 9, 5, 2]], [[4, 2, 3, 4, 9, 5, 2, 9, 3]], [[4, 2, 9, 2, 3, 2, 9, 2]], [[4, 6, 6, 3, 9, 5, 2, 5]], [[5, 9, 5, 2, 9]], [[4, 2, 6, 3, 4, 9, 5, 2, 9, 3]], [[4, 2, 9, 2, 9, 9]], [[4, 5, 1, 9, 5, 2, 1, 1]], [[2, 9, 2, 9, 9, 0, 0, 9, 0]], [[2, 9, 9, 0, 0, 9]], [[4, 5, 5, 9, 5, 2, 2, 2]], [[4, 4, 2, 3, 4, 9, 5, 2, 9, 3]], [[1, 5, 2]], [[1, 5, 1, 9, 2, 4, 2]], [[2, 4, 5, 1, 0, 2, 9, 5, 2, 2, 4, 5]], [[4, 5, 1, 9, 5, 2, 8]], [[1, 4, 5]], [[2, 9, 9, 9, 0, 0, 9, 0]], [[1, 4, 9, 8, 2, 2]], [[4]], [[5, 1, 5, 1, 9, 2, 4, 5, 2, 1]], [[4, 3, 5, 1, 10, 9, 5, 2, 1, 1]], [[1, 1, 9, 2, 4, 6, 2]], [[4, 1, 5, 2, 9, 4]], [[4, 1, 9, 0, 9, 2, 9]], [[5, 1, 9, 5, 5, 2]], [[1, 5, 1, 9, 2, 4, 2, 2]], [[4, 5, 1, 9, 1, 8, 2, 2]], [[4, 1, 9, 10]], [[4, 3, 5, 1, 9, 5, 5, 2, 2, 2]], [[6, 6, 1, 9, 4, 2]], [[4, 1, 9, 5, 5, 2, 2]], [[4, 9, 10, 5, 3, 5, 3]], [[5, 1, 9, 2]], [[6, 6, 1, 9, 4, 1]], [[4, 1, 5, 8, 2, 9, 4]], [[4, 5, 1, 6, 5, 2, 1, 5, 5]], [[6, 6, 1, 9, 1, 6, 6]], [[4, 6, 5, 1, 9, 5, 2, 2, 2]], [[1, 5, 1, 9, 2, 4, 2, 8, 2, 1]], [[4, 5, 1, 1]], [[4, 5, 1, 4, 1]], [[4, 1, 5, 8, 2, 9]], [[0, 4, 9]], [[4, 1, 1]], [[4, 5, 1, 5, 5, 5, 9, 2]], [[4, 2, 9, 2, 9, 9, 2, 2, 9]]]
results = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "check_Consecutive"
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
        for test_case in ['assert check_Consecutive([1,2,3,4,5]) == True', 'assert check_Consecutive([1,2,3,5,6]) == False', 'assert check_Consecutive([1,2,1]) == False']:
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
