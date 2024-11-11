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
inputs = [[[1, 101, 2, 3, 100, 4, 5], 7, 4, 6], [[1, 101, 2, 3, 100, 4, 5], 7, 2, 5], [[11, 15, 19, 21, 26, 28, 31], 7, 2, 4], [[5, 2, 4, 1, 3, 6], 6, 1, 3], [[5, 2, 4, 1, 3, 6], 6, 2, 3], [[5, 2, 4, 1, 3, 6], 6, 1, 2], [[5, 2, 4, 1, 3, 6], 6, 1, 5], [[5, 2, 4, 1, 3, 6], 6, 0, 3], [[5, 2, 5, 1, 3, 6], 6, 1, 3], [[5, 2, 5, 1, 3, 6], 6, 2, 3], [[5, 2, 4, 1, 3, 6], 6, 2, 4], [[4, 2, 4, 1, 3, 6], 6, 1, 2], [[3, 2, 4, 1, 3, 6], 6, 2, 3], [[5, 2, 4, 1, 3, 5], 6, 1, 2], [[5, 2, 4, 1, 3, 5], 6, 1, 4], [[5, 2, 4, 1, 3, 5], 6, 1, 5], [[5, 2, 4, 1, 3, 3], 6, 0, 3], [[5, 2, 4, 1, 3, 6], 6, 1, 4], [[5, 2, 4, 1, 3, 1], 6, 0, 3], [[5, 2, 4, 1, 3, 5], 6, 1, 3], [[5, 2, 5, 1, 3, 6], 6, 0, 3], [[4, 2, 4, 1, 3, 6], 6, 0, 2], [[5, 2, 5, 1, 3, 6], 6, 2, 4], [[5, 2, 4, 1, 1, 6], 6, 1, 2], [[5, 2, 5, 1, 3, 6], 6, 2, 5], [[5, 2, 5, 1, 3, 6], 6, 1, 5], [[5, 2, 4, 1, 3, 5], 6, 2, 3], [[5, 2, 5, 1, 3, 6], 6, 1, 4], [[5, 2, 4, 1, 3, 5], 6, 2, 4], [[5, 2, 4, 0, 1, 3, 6], 7, 1, 2], [[5, 2, 5, 1, 3, 6], 6, 0, 1], [[5, 3, 5, 1, 3, 6], 6, 1, 4], [[5, 2, 4, 2, 3, 5], 6, 1, 4], [[5, 2, 5, 1, 2, 6], 6, 0, 1], [[5, 3, 5, 1, 3, 6], 6, 2, 5], [[5, 3, 5, 1, 3, 6], 6, 1, 5], [[4, 3, 5, 1, 3, 6], 6, 1, 5], [[5, 2, 5, 1, 3, 6], 6, 3, 5], [[5, 2, 5, 1, 3, 6], 6, 1, 2], [[5, 3, 5, 1, 3, 6], 6, 2, 4], [[5, 2, 5, 1, 3, 6], 6, 0, 5], [[5, 2, 4, 1, 1, 6], 6, 1, 3], [[5, 2, 4, 1, 3, 5], 6, 2, 5], [[5, 2, 2, 1, 3, 6], 6, 1, 4], [[5, 2, 5, 1, 3, 6], 6, 0, 4], [[4, 3, 5, 1, 3, 6], 6, 1, 3], [[5, 2, 2, 1, 3, 6], 6, 0, 4], [[5, 2, 4, 2, 3, 5], 6, 1, 3], [[4, 2, 5, 1, 3, 6], 6, 1, 3], [[4, 2, 4, 0, 1, 3, 6], 7, 1, 2], [[5, 2, 4, 1, 3, 7], 6, 0, 3], [[5, 2, 4, 1, 3, 1], 6, 0, 4], [[5, 2, 2, 1, 3, 6], 6, 0, 5], [[5, 2, 4, 2, 3, 5], 6, 1, 5], [[5, 3, 5, 1, 3, 6], 6, 3, 4], [[5, 3, 5, 1, 3, 6], 6, 1, 2], [[5, 2, 4, 1, 3, 3], 6, 0, 4], [[5, 2, 5, 1, 3, 2], 6, 0, 4], [[5, 2, 5, 1, 3, 6, 5], 7, 2, 4], [[5, 2, 4, 0, 1, 3, 6], 7, 0, 2], [[5, 2, 4, 1, 3, 1], 6, 1, 3], [[5, 2, 4, 0, 3, 6], 6, 2, 4], [[5, 2, 5, 1, 3, 6], 6, 3, 4], [[5, 2, 5, 1, 3, 2], 6, 1, 4], [[2, 5, 2, 1, 3, 6], 6, 0, 4], [[5, 2, 4, 1, 3, 1], 6, 0, 2], [[5, 3, 5, 1, 3, 6], 6, 0, 4], [[4, 3, 5, 1, 2, 6], 6, 1, 3], [[5, 2, 4, 1, 2, 6], 6, 1, 2], [[4, 2, 5, 1, 3, 6], 6, 0, 3], [[5, 2, 4, 0, 1, 3, 6], 7, 0, 3], [[5, 2, 4, 1, 3, 3], 6, 0, 5], [[5, 2, 4, 1, 2, 6], 6, 1, 5], [[5, 3, 5, 1, 3, 3], 6, 1, 4], [[5, 2, 4, 1, 3, 6], 6, 2, 5], [[5, 2, 4, 1, 3, 3], 6, 0, 2], [[5, 3, 5, 1, 3, 6], 6, 0, 5], [[5, 3, 5, 1, 3, 3], 6, 2, 4], [[5, 4, 1, 3, 3, 3], 6, 0, 4], [[4, 3, 5, 1, 3, 6], 6, 1, 4], [[5, 3, 5, 0, 3, 6], 6, 0, 4], [[5, 2, 4, 1, 3, 1], 6, 0, 1], [[5, 2, 5, 0, 3, 6], 6, 0, 1], [[5, 3, 5, 1, 3, 6], 6, 3, 5], [[4, 3, 5, 1, 2, 6], 6, 1, 2], [[5, 2, 4, 1, 3, 1], 6, 0, 5], [[5, 3, 5, 2, 3, 6], 6, 2, 5], [[5, 3, 5, 1, 2, 6], 6, 3, 4], [[0, 5, 4, 1, 3, 3], 6, 0, 5], [[4, 3, 4, 1, 2, 6], 6, 1, 3], [[5, 2, 4, 3, 6, 3], 6, 1, 5], [[4, 3, 5, 1, 3, 6], 6, 3, 4], [[5, 2, 1, 3, 1], 5, 0, 2], [[5, 2, 5, 1, 3, 2], 6, 0, 3], [[5, 2, 4, 1, 3, 6], 6, 0, 2], [[5, 7, 4, 1, 3, 3], 6, 0, 5], [[5, 2, 5, 1, 3, 6, 5], 7, 1, 2], [[4, 3, 5, 0, 3, 6], 6, 0, 4], [[4, 3, 5, 1, 3, 6], 6, 3, 5], [[5, 3, 5, 1, 2, 6], 6, 3, 5], [[5, 2, 5, 1, 3, 6, 5], 7, 2, 6], [[5, 2, 4, 1, 3, 5], 6, 3, 5], [[5, 2, 4, 1, 3, 1], 6, 2, 3], [[5, 2, 4, 2, 7, 5], 6, 1, 4]]
results = [11, 7, 71, 1, 1, 6, 11, 1, 1, 1, 5, 6, 1, 6, 5, 7, 1, 5, 1, 1, 1, 4, 5, 6, 13, 11, 1, 5, 5, 6, 2, 3, 5, 2, 14, 11, 10, 13, 7, 3, 11, 1, 11, 5, 3, 1, 3, 2, 1, 6, 1, 3, 11, 7, 4, 8, 3, 3, 5, 4, 1, 5, 5, 5, 5, 4, 3, 1, 6, 1, 0, 3, 11, 3, 12, 4, 11, 3, 3, 3, 3, 2, 2, 14, 9, 1, 14, 3, 3, 1, 5, 4, 1, 1, 4, 3, 7, 3, 15, 14, 7, 11, 1, 12]

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
        func_name = "max_sum_increasing_subseq"
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
        for test_case in ['assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11', 'assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7', 'assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71']:
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
