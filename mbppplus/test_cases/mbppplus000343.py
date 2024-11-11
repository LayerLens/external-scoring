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
inputs = [[[1, 1, 1, 1], 2], [[1, 5, 7, -1, 5], 6], [[1, -2, 3], 1], [[-1, -2, 3], -3], [[], 0], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8], [[], 5], [[-1, 0, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 0], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], 0], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 4], 8], [[-1, 0, 1, 2, 3, 4, 5, 7, 8, 9], 8], [[97.69700646889478], 5], [[-1, 6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], 1], [[], -1], [[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 8], [[-1, 0, 1, 2, 3, 4, 5, 7, 8, 9], 9], [[-1, 0, 1, 2, 3, 4, 5, 7, 8, 9], 4], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1], [[-1, 1, 2, 4, 5, 6, 8, 9], 8], [[-1, 1, 2, 3, 4, 5, 7, 8, 9], 8], [[True, False, False, True, True, False, True, True, True], 1], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 4], 2], [[True, False, False, True, True, False, True, True, True], 2], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], -1], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3], 4], [[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1], [[97.69700646889478], 6], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 7], -1], [[-1, 0, 6, 1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 7], 8], [[-1, 0, 1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 9, 4], 2], [[-1, 0, 1, 2, 3, 8, 5, 6, 7, 8, 9, 3], 4], [[True, False, True, True, False, True, True, True, True, True], 3], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 9, 1], 8], [[9, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 2], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 5], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 9, 1], -1], [[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9], [[97.69700646889478, 97.69700646889478], 6], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7], [[-1, 1, 1, 4, 5, 6, 8, 9], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 4], [[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 4], 8], [[-1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 8], [[-1, 8, 0, 1, 2, 3, 4, 5, 7, 8, 9], 9], [[-1, 8, 0, 1, 2, 3, 4, 5, 7, 8, 9], 10], [[], 6], [[-1, 0, 1, 2, 3, 4, 5, 7, 8, 9], 7], [[-1, 0, 1, 2, 3, 4, 5, 7, 8, 9, -1], 8], [[97.69700646889478], 7], [[-1, -1, 1, 1, 4, 5, 6, 8, 9], 8], [[-1, 6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 6], 1], [[-1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 2], [[-1, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 4], [[-1, 1, 2, 3, 4, 5, 7, 8, 9, 9, 4], 8], [[-1, 0, 1, 2, 3, 8, 5, 6, 7, 8, 9, 3], 5], [[True, False, False, True, True, False, True, True, False, True], 2], [[4, 24, 20], 1], [[True, False, True, True, False, False, True, True, True, True, True], 3], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 9, 1], 9], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 5], 9], [[-1, 0, 1, 2, 3, 8, 5, 6, 7, 8, 9, 3], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 3], [[-1, 0, 1, 2, 3, 4, 5, 10, 7, 8, 1, 9, 9, 1], -2], [[-1, 0, 1, 2, 3, 4, 5, 7, 8, 9, -1], -2], [[97.69700646889478, 97.69700646889478], 8], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 5, 5], 8], [[0, 1, 2, 3, 6, 8, 5, 6, 7, 8, 9, 3], 5], [[5, -1, 1, 2, 4, 5, 6, 8, 9], 8], [[-1, 1, 24, 2, 3, 4, 5, 6, 7, 8, 9], 1], [[-1, 1, 24, 2, 3, 4, 5, 6, 7, 8, 9], 2], [[97.69700646889478, 97.23101051556709], 8], [[-1, 0, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8], 8], [[-1, 0, 6, 1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 6], 9], [[5, 24, 24, -1, 1, 2, 4, 5, 6, 8, 9], 8], [[97.35909695921131, 97.69700646889478], 7], [[-1, 0, 1, 3, 20, 3, 4, 5, 6, -2, 7, 8], 3], [[-1, -1, 1, 1, 4, 5, 6, 8, 9, -1], 8], [[-1, 0, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8], 9], [[], 8], [[-73, 8, -86, -19], 5], [[-1, -73, 1, 2, 3, 4, 5, 7, 8, 9, -1], -2], [[6, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 5, 5, 6], 3], [[-1, 0, 2, 2, 3, 4, 5, 6, 7, 8, 1, 9, 9, 1], 2], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 9, 9, 1], 6], [[-1, 0, 1, 3, 4, 5, 6, 7, 8, 9, 1, 7], -1], [[-1, 0, 1, 2, 3, 8, 5, 6, 8, 9, 3, 8], 5], [[-1, 2, 2, 4, 5, 6, 8, 9], 7], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4], [[-1, -1, 1, 1, 4, 5, 6, 9, -1, 1], 7], [[-1, 0, 1, 2, 3, 8, 5, 6, 7, 8, 9, 3, 8], 8], [[False, True, True, False], 1], [[-1, 0, 6, 1, 2, 3, 4, 5, 6, 7, 8, 8], 9], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1], -2], [[-1, 0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9], 8], [[5, -1, 1, 2, 4, 5, 6, 8, 9, 5], 8], [[True, False, False, True, True, False, False, True, True, True], 1], [[-1, 8, 0, 1, 2, 3, 4, 5, 7, 8, 9], 6], [[-1, 0, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 5, 5], 2], [[9, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], -19], [[9, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8], -1], [[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4], 9], [[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4], 1]]
results = [6.0, 3.0, 1.0, 1.0, 0.0, 5.0, 0.0, 6.0, 6.0, 1.0, 1.0, 2.0, 7.0, 4.0, 0.0, 3.0, 0.0, 4.0, 4.0, 4.0, 3.0, 2.0, 2.0, 3.0, 18.0, 2.0, 15.0, 1.0, 4.0, 1.0, 0.0, 1.0, 8.0, 3.0, 3.0, 0.0, 8.0, 2.0, 7.0, 1.0, 4.0, 0.0, 5.0, 1.0, 6.0, 3.0, 6.0, 6.0, 5.0, 4.0, 0.0, 4.0, 5.0, 0.0, 2.0, 3.0, 2.0, 4.0, 5.0, 4.0, 15.0, 0.0, 0.0, 8.0, 7.0, 7.0, 3.0, 0.0, 1.0, 0.0, 8.0, 3.0, 2.0, 1.0, 1.0, 0.0, 7.0, 8.0, 2.0, 0.0, 4.0, 3.0, 7.0, 0.0, 0.0, 1.0, 3.0, 4.0, 6.0, 1.0, 4.0, 3.0, 3.0, 3.0, 8.0, 4.0, 6.0, 0.0, 6.0, 2.0, 24.0, 3.0, 3.0, 0.0, 1.0, 7.0, 1.0]

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
        func_name = "get_pairs_count"
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
        for test_case in ['assert get_pairs_count([1,1,1,1],2) == 6', 'assert get_pairs_count([1,5,7,-1,5],6) == 3', 'assert get_pairs_count([1,-2,3],1) == 1', 'assert get_pairs_count([-1,-2,3],-3) == 1']:
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
