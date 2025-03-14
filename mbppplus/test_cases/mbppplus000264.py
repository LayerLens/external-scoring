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
inputs = [[[1, 3, 5, 7, 4, 1, 6, 8]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[1, 5, 7, 9, 10]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]], [[1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 18, 20]], [[2, 5, 3, 6, 1, 4, 9, 8, 7]], [[13, 12, 15, 11, 10, 19, 16, 14, 18, 17]], [[22, 23, 27, 24, 26, 25, 32, 31, 29, 30, 28]], [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]], [[22, 23, 27, 24, 26, 25, 32, 31, 29, 30, 28, 25]], [[1, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], [[1, 6, 2, 3, 4, 5, 7, 8, 8, 10, 11, 12]], [[30, 2, 3, 4, 5, 6, 7, 8, 31, 10, 11, 12, 11]], [[30, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 11, 4]], [[22, 23, 27, 24, 26, 25, 32, 29, 30, 28, 25]], [[30, 1, 3, 4, 5, 6, 7, 31, 10, 11, 12, 11]], [[1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 18, 20, 16]], [[30, 2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 11]], [[13, 12, 15, 11, 10, 19, 16, 18, 17]], [[1, 3, 7, 5, 2, 4, 6, 8, 7, 9, 11, 19, 13, 15, 16, 18, 20, 16, 19]], [[13, 12, 12, 15, 13, 10, 19, 16, 14, 18, 17, 13]], [[1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 18, 20, 16, 6]], [[30, 2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30]], [[28, 22, 23, 27, 24, 26, 25, 32, 31, 29, 30, 28, 25]], [[13, 12, 15, 11, 19, 16, 18, 18, 17]], [[30, 2, 3, 4, 5, 6, 7, 4, 31, 10, 10, 11, 12, 11, 30]], [[20, 7, 7, 7, 7, 7, 26, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]], [[22, 23, 27, 24, 26, 25, 32, 31, 29, 30, 27, 25]], [[1, 3, 5, 2, 4, 8, 6, 8, 7, 9, 11, 13, 15, 16, 18, 20]], [[1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 2, 20]], [[1, 3, 5, 2, 4, 8, 6, 8, 7, 6, 9, 11, 13, 15, 16, 18, 20]], [[30, 2, 3, 15, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30]], [[1, 2, 3, 4, 5, 6, 28, 8, 9, 10, 11, 12]], [[2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30, 7]], [[2, 3, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30, 7]], [[13, 12, 12, 15, 13, 10, 19, 16, 14, 18, 17]], [[28, 22, 23, 27, 24, 26, 25, 31, 29, 30, 28, 27, 25]], [[23, 27, 24, 26, 25, 32, 31, 29, 30, 27, 25]], [[12, 30, 1, 3, 4, 5, 6, 7, 31, 10, 11, 16, 12, 11]], [[22, 23, 27, 24, 26, 25, 32, 31, 29, 30, 28, 25, 25]], [[30, 2, 3, 5, 6, 7, 4, 31, 10, 11, 12, 11]], [[22, 23, 24, 26, 25, 32, 31, 29, 33, 30, 28, 25, 25]], [[4, 6, 2, 3, 4, 5, 7, 8, 8, 10, 11, 12]], [[1, 27, 3, 7, 5, 2, 4, 6, 8, 8, 9, 11, 19, 13, 15, 17, 16, 18, 20, 16, 19]], [[1, 3, 5, 2, 4, 6, 8, 7, 6, 18, 9, 11, 13, 15, 16, 2, 20, 16]], [[1, 3, 7, 5, 2, 4, 6, 8, 7, 9, 11, 19, 13, 15, 16, 18, 20, 16, 19, 2]], [[1, 2, 3, 4, 5, 28, 8, 9, 10, 11, 12]], [[1, 6, 2, 3, 4, 5, 7, 8, 8, 10, 11, 12, 8, 1]], [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]], [[7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7]], [[1, 5, 2, 3, 4, 5, 28, 8, 9, 10, 11, 12, 28]], [[30, 8, 2, 3, 5, 6, 7, 4, 31, 10, 11, 12, 11]], [[1, 6, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]], [[14, 22, 23, 24, 26, 25, 32, 31, 29, 33, 30, 28, 25, 25]], [[13, 31, 12, 15, 13, 10, 19, 16, 14, 18, 17, 13]], [[22, 23, 24, 25, 32, 31, 29, 33, 30, 28, 25, 15]], [[1, 5, 2, 3, 4, 5, 28, 8, 9, 10, 11, 12, 28, 5]], [[30, 2, 9, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30]], [[1, 3, 5, 2, 4, 8, 6, 8, 7, 9, 32, 11, 13, 15, 16, 18, 20]], [[20, 7, 7, 7, 7, 7, 26, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8]], [[13, 12, 13, 8, 13, 10, 19, 16, 14, 18, 17, 13]], [[30, 2, 3, 4, 5, 6, 7, 8, 31, 3, 10, 11, 12, 12]], [[1, 6, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 12]], [[1, 6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]], [[1, 5, 2, 3, 4, 5, 28, 8, 9, 10, 25, 11, 12, 28]], [[4, 6, 2, 3, 10, 4, 5, 7, 8, 8, 10, 11, 12]], [[1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 6, 10]], [[23, 27, 24, 9, 25, 32, 31, 29, 30, 27, 25]], [[20, 7, 7, 7, 7, 26, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7]], [[28, 22, 23, 27, 24, 26, 25, 31, 29, 30, 28, 27, 25, 22]], [[20, 7, 7, 7, 7, 26, 7, 30, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 8]], [[4, 2, 3, 4, 5, 7, 8, 8, 10, 11, 12]], [[20, 7, 24, 7, 7, 26, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7]], [[23, 30, 2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30]], [[20, 7, 24, 7, 7, 26, 7, 7, 7, 7, 8, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 7]], [[2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 12, 9, 7, 4]], [[1, 6, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 12, 7]], [[30, 3, 4, 5, 6, 7, 8, 31, 10, 11, 12, 11]], [[13, 25, 12, 15, 11, 19, 16, 18, 18, 17]], [[22, 23, 27, 24, 26, 25, 32, 31, 29, 30]], [[23, 27, 24, 9, 30, 25, 32, 31, 29, 30, 27, 25]], [[20, 7, 7, 7, 7, 7, 26, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8, 7, 7]], [[13, 31, 12, 15, 13, 10, 19, 16, 18, 17, 13]], [[7, 7, 8, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7]], [[17, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 18, 20, 11, 4]], [[23, 27, 24, 9, 25, 17, 32, 31, 29, 30, 27, 25]], [[30, 2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 4]], [[2, 3, 4, 6, 7, 4, 31, 10, 11, 12, 12, 9, 7, 4, 7]], [[1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 18, 20, 3]], [[22, 23, 27, 24, 26, 25, 31, 29, 30, 28, 27, 25]], [[13, 12, 12, 14, 13, 10, 19, 16, 14, 18, 17]], [[1, 6, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 7]], [[30, 3, 4, 5, 6, 7, 8, 31, 10, 11, 12, 11, 4]], [[30, 3, 4, 5, 6, 7, 8, 10, 11, 12, 11]], [[1, 3, 5, 2, 4, 6, 8, 7, 9, 11, 13, 15, 16, 4, 12, 2, 20, 13, 2]], [[23, 24, 9, 25, 32, 31, 29, 30, 27, 23]], [[20, 7, 24, 7, 7, 26, 7, 7, 7, 7, 9, 8, 8, 8, 8, 7, 8, 8, 8, 8, 7]], [[1, 17, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]], [[1, 6, 2, 3, 4, 6, 7, 8, 9, 10, 11, 11]], [[30, 2, 3, 4, 5, 6, 7, 8, 10, 11, 33, 11, 4]], [[7, 7, 8, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8]], [[2, 3, 5, 6, 7, 4, 31, 10, 11, 12, 11, 30, 7, 7]], [[1, 8, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 7]], [[30, 1, 3, 4, 5, 6, 7, 31, 10, 11, 16, 12, 11]], [[2, 3, 4, 5, 6, 7, 4, 31, 10, 11, 12, 12, 9, 7, 4, 9]], [[30, 3, 4, 5, 6, 7, 8, 10, 11, 12, 11, 12]], [[31, 30, 1, 3, 4, 5, 6, 7, 31, 10, 11, 16, 12, 11]], [[30, 8, 2, 3, 5, 7, 7, 4, 31, 10, 11, 12, 11]]]
results = [3, 1, 9, 1, 1, 1, -3, -1, -1, 1, -1, 5, 5, 27, 27, -1, 29, 1, 27, -1, 1, -1, 1, 27, 5, -1, 27, 13, -1, 1, 1, 1, 27, 1, -1, -1, -1, 5, 1, 11, -1, 27, -1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 27, 5, -9, -1, -1, 1, 21, 1, 13, -1, 27, 5, 5, 1, 1, 1, 1, 13, 5, 13, 1, 13, 7, 13, -1, 5, 27, -1, -1, 1, 13, -1, 1, -15, 1, 27, -1, 1, -1, -1, 5, 27, 27, 1, 1, 13, 1, 5, 27, 1, -1, 7, 29, -1, 27, -1, 27]

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
        func_name = "diff_even_odd"
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
        for test_case in ['assert diff_even_odd([1,3,5,7,4,1,6,8])==3', 'assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1', 'assert diff_even_odd([1,5,7,9,10])==9']:
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
