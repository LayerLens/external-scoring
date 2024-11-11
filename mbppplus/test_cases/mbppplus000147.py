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
inputs = [[[10, 20, -30, -1], 4, 3], [[-1, 10, 20], 3, 2], [[-1, -2, -3], 3, 3], [[5, -2, 10, 4, -7, 3], 6, 5], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 2], [[5, -2, 11, 4, -7, 3], 6, 5], [[5, -2, 10, 5, -7, 3], 6, 6], [[5, -2, 10, 5, -7, 3], 6, 1], [[5, -2, 10, 5, -7, 3, 10], 7, 6], [[5, -2, 10, 5, -7, 3, 10], 7, 10], [[5, -2, 10, 5, -7, 3, 10], 7, 5], [[5, -2, 10, 5, -7, 3, 10], 7, 9], [[5, -2, 11, 4, -7, 3], 6, 4], [[5, -2, 10, 4, -7, 3], 6, 4], [[5, -2, 10, -7, 3, 5], 6, 1], [[5, -2, 10, 5, -7, 4, 10], 7, 6], [[5, -2, 10, -7, 3, 5], 6, 3], [[5, -2, 10, 5, -7, 4, 10], 7, 7], [[1, 2, 3, -4, -5, 6, 7, -8, 10, 10], 10, 2], [[9, -2, 10, 5, -7, 3, 10], 7, 5], [[5, -2, 10, 4, -7, 3], 6, 6], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 1], [[5, -2, 10, 5, -7, 3, 10], 7, 7], [[5, -2, 10, 5, -7, 3, 10], 7, 4], [[-7, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 1], [[5, -2, 10, 4, -7, 3, 10], 7, 5], [[-7, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 11], [[-7, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 10], [[6, -2, 9, -7, 3, 5], 6, 3], [[5, -2, 10, 4, -7, 3, 10], 7, 6], [[6, -2, 9, -7, 3, 5], 6, 6], [[5, -2, 10, 5, -7, 3], 6, 9], [[5, -2, 10, 5, -7, 3, 10], 7, 1], [[5, -2, 10, 5, -4, 3, 10], 7, 7], [[6, -2, 9, -7, 3, 5], 6, 2], [[-2, -3, 9, -7, 3, 5], 6, 3], [[6, -2, 10, 4, -7, 3, 10], 7, 6], [[1, 2, 11, -4, -5, 6, 7, -8, 9, 10], 10, 1], [[5, -2, 5, -7, 4, 10], 6, 6], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 10], [[1, 2, 3, -4, -5, 6, 7, -8, 10, 10], 10, 3], [[-7, 2, 3, -4, 1, 6, 7, -8, 9, 10], 10, 11], [[4, -2, 10, -7, 3, 5], 6, 3], [[5, -2, 10, -7, 3, 5], 6, 6], [[5, -1, 10, 4, -7, 3], 6, 4], [[5, -2, 10, 5, -7, 3, 10], 7, 11], [[1, 2, 3, -4, -5, 6, 7, -8, 10, 10], 10, 4], [[9, -2, 10, 5, -7, 3, 10], 7, 6], [[5, -1, 10, 3, -7, 3], 6, 4], [[6, -2, 10, 4, -8, 3, 10], 7, 6], [[5, -2, 10, 4, -7, 3], 6, 11], [[5, -2, 10, 5, -7, 3], 6, 2], [[5, -2, 10, 5, -8, 3], 6, 9], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10, 7], 11, 1], [[6, -2, 10, 4, -8, 3, 10, 10], 8, 6], [[1, 11, 2, 3, -4, -5, 7, -8, 10, 10], 10, 10], [[5, -2, 10, 4, -7, 3, 10], 7, 4], [[5, -2, 10, 5, -7, 3], 6, 10], [[5, -2, 10, 4, -7, 3, -2], 7, 3], [[1, 11, 2, 3, -4, -5, 7, -8, 10, 10], 10, 5], [[-7, 2, 3, -4, -5, 6, 6, -8, 9, 10], 10, 1], [[5, -2, 10, 5, -7, 3, 9], 7, 5], [[5, -2, 10, -7, 3, 5], 6, 7], [[5, -2, 10, 4, -7, 3, 10], 7, 7], [[-7, 2, 3, -4, -5, 6, 6, -8, 9, 10, 6], 11, 1], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 4], [[9, -2, 10, 5, -7, 3, 10], 7, 7], [[-7, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 8], [[9, -2, 10, 4, -7, 3, 10], 7, 5], [[6, -2, 10, 4, -7, 3, 10], 7, 5], [[5, -1, 10, 3, -7, 3], 6, 3], [[1, 2, 11, -4, -5, 6, 7, -8, 9, 10], 10, 10], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 9], [[9, -2, 10, 4, -7, 3, 10], 7, 4], [[5, -2, 10, -7, 3, 5], 6, 5], [[5, -2, 10, 4, -7, 3], 6, 7], [[5, -2, 10, 4, 4, 3], 6, 11], [[-2, -3, 9, -7, -1, 5], 6, 3], [[5, -2, -2, 5, -7, 3, 10], 7, 11], [[5, -2, 10, 4, -7, 3, 8], 7, 7], [[6, -2, 10, 5, -4, 3, 10], 7, 7], [[6, -2, 10, 4, -7, 3, 10], 7, 4], [[1, 2, 3, -4, -5, 6, 7, -8, 10, 10], 10, 10], [[9, -2, 10, 4, -7, 3], 6, 7], [[5, -2, 10, 3, 3, 5], 6, 6], [[-2, 10, 5, -8, 3], 5, 9], [[5, -2, 10, 5, -7, 3], 6, 5], [[6, -1, 9, -7, 3, 5], 6, 3], [[5, -2, -2, 5, -7, 3, 10], 7, 12], [[1, 2, 3, -4, -5, 6, 7, -8, 9, 10], 10, 11], [[5, -2, 5, -7, 4, 10], 6, 7], [[5, -2, 10, 4, -6, 3], 6, 2], [[6, -2, 10, 4, -7, 3, 10], 7, 7], [[-2, -3, 9, -1, -1, 5], 6, 3], [[-2, -3, 9, -7, -1, 5], 6, 4], [[5, -2, 11, 4, -7, 3], 6, 3], [[1, 2, 3, -3, -5, 6, 7, -8, 10, 10], 10, 10], [[7, -2, 10, 4, -7, 3, 10], 7, 6], [[5, -2, 10, 5, -7, 3], 6, 11], [[9, -2, 10, 5, -7, 3, 10], 7, 2], [[5, -2, 10, 5, -7, 3], 6, 7], [[5, -2, 10, 5, -7, 3, 10], 7, 12], [[6, -3, 10, 5, -4, 3, 10], 7, 7], [[6, -1, 9, -4, 3, 5], 6, 3], [[-7, 2, 3, -4, -5, 6, -7, -8, 9, 10], 10, 8]]
results = [30, 59, -1, 69, 45, 74, 88, 18, 144, 240, 120, 216, 60, 56, 14, 150, 42, 175, 47, 140, 82, 24, 168, 96, 24, 115, 154, 141, 42, 138, 84, 130, 24, 189, 28, 20, 144, 29, 90, 213, 69, 216, 39, 84, 60, 264, 91, 168, 56, 138, 147, 32, 122, 31, 198, 270, 92, 144, 39, 135, 23, 115, 98, 161, 29, 87, 196, 115, 135, 120, 43, 290, 192, 108, 70, 95, 264, 11, 133, 147, 196, 96, 223, 123, 144, 79, 74, 45, 145, 234, 105, 31, 168, 26, 12, 46, 232, 150, 158, 56, 102, 288, 189, 54, 19]

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
        func_name = "max_sub_array_sum_repeated"
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
        for test_case in ['assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30', 'assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59', 'assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1']:
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
