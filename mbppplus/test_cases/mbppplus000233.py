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
inputs = [[[5, 4, 7, 2, 1], 5], [[7, 2, 8, 1, 0, 5, 11], 7], [[1, 2, 3], 3], [[], 0], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10], [[2, 4, 6, 8], 4], [[2, 4, 6, 8], 0], [[2, 4, 6, 8], -2], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2], 10], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1], [[1, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10], [[10, 1, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7], [[2, 4, 6, 6, 8], 4], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2], [[2, 6, 8], -2], [[2, 4, 6, 8, 4, 2], 4], [[2, 4, 6, 6, 8], 3], [[1, 8, 2, 3, 4, 5, 6, 7, 8, -2, 9, 10], 7], [[5, 2, 6, 8], -3], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3], [[2, 4, 6, 8, 4], 0], [[2, 4, 5, 6, 8], -2], [[-3, 2, 4, 6, 8], 0], [[2, 4, 5, 6, 8], -1], [[2, 4, -2, 6, 8], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9], [[2, -2, 6, 8], 2], [[-3, 2, 4, 8], 0], [[1, 8, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8], [[1, 4, 6, 6, 8], -2], [[2, 4, 6, 8, 4, 4], 0], [[2, 4, 6, 6, 8, 8], -2], [[2, 4, 6, 6, 1, 8, 6], 1], [[2, 4, 6, 6, 8, 8, 2], -3], [[-3, 2, 4, 6, 6, 8], 3], [[2, 4, 6, 8, 4, 4], -1], [[2, 4, 6, 8, 4, 3, 2], 4], [[-3, 2, 4, 6, 6, 8, 8], 3], [[2, 3, 6, 6, 1, 8, 6], 1], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6], 1], [[-3, 2, 4, 6, 6, 8, 8], -3], [[2, 0, 4, 6, 8, 4], 0], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], 1], [[2, 4, 6, 6, 8], 2], [[2, 4, 1, 6, 8, 4, 2], 4], [[1, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], [[2, -2, 6, 8], 1], [[1, 2, 3, 4, 5, 6, 8, 7, 8, 9], 10], [[2, 4, 6, 8, 4, 4, 8], -1], [[8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0], [[2, 4, 1, 8], 4], [[1, 4, 6, 6, 8, 6], -2], [[2, 8], -1], [[2, 3, 6, 6, 1, 8, 6], 4], [[2, 4, 5, 6, 8, 4, 4], -1], [[0, 2, 4, 6], 4], [[-3, 2, 4, 10, 6, 6, 8], 7], [[8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4], 0], [[2, 4, 6, 6, 8], -1], [[1, 7, 2, 3, 5, 6, 7, 8, 9, 10], 8], [[-3, 2, 4, 6, 6, 8, -3, 8], 4], [[-3, 2, 4, 6, 6, 8, -3, 8], -3], [[-2, 6, 8], 1], [[1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 1], 1], [[2, 4, 9, 6, 6, 8], -1], [[2, 4, 6, 6, 8, 8, 2, 2], -3], [[2, 4, -2, 6, 2, 8], 2], [[0, 2, 4, 6, 0], 1], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 10], 10], [[2, 4, -2, 6, 8, 4], 2], [[9, 2, 4, 6, 6, 8], 4], [[4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2], [[2, 4, 6, 8, 4, 4, 8, 8], -1], [[2, 4, 6, 8, 8], -2], [[2, 4, -2, 6, 2, -3, 8], 2], [[2, 4, 6, 6, 8], -2], [[2, 4, 6, 8, 4, 4, 8], 0], [[1, 2, 2, 4, 10, 5, 6, 7, 8, 9, 10, 6], 1], [[8, 1, 3, 4, 5, 6, 7, 8, 9, 10, 4], 0], [[2, 4, 6, 8, 4, 3, 8, 2], 3], [[2, 4, 6, 6, 1, 8], 3], [[2, 4, 6, 6, 8, 8, 2], 7], [[-3, 2, 4, -3, 6, 6, 8, -3, 8], -3], [[2, 5, 4, 5, 6, 8, 4], 7], [[-2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 4], 0], [[2, 4, -2, 6, 8], 1], [[-3, 2, 4, 6, 6, 8, 4], 3], [[10, 1, 8, 2, 3, 5, 6, 7, 8, 9, 10], 6], [[2, 4, 1, 6, 8, 4, 2], 3], [[8, 1, 2, 3, 4, 5, 6, 8, 9, 10], 0], [[2, 6, 8], -1], [[2, 4, 6, 6, 8, 4], -1], [[-14, 2, -25, 0], 0], [[2, 4, 6, 6, 8], 5], [[2, 4, 6, 6], 3], [[8, 1, 2, 3, 4, 5, 6, 8, 9, 10, 6], 1], [[2, 4, 7, 8, 8], -2], [[2, 5, 6, 8], -2], [[10, 1, 8, 2, 3, 5, 6, 7, 8, 10, 10], 6], [[10, 1, 8, 2, 3, 5, 6, 7, 8, 9, 10], 10], [[-3, 2, 4, 6, 8, 8], -1], [[10, 0, -3, 2, 9, 6], 5], [[2, 4, -25, 8, 4, 4], 0], [[2, 4, 7, 8, 7, 8], -2], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6], 2], [[1, 7, 3, 4, 5, 5, 7, 8, 9, 10], 5]]
results = [6, 12, 2, 0, 25, 0, 0, 0, 25, 0, 25, 12, 0, 1, 0, 0, 0, 12, 0, 2, 0, 0, 0, 0, 0, 20, 0, 0, 16, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 6, 0, 25, 0, 0, 3, 0, 0, 3, 0, 0, 6, 0, 0, 15, 3, 0, 0, 0, 0, 0, 0, 0, 25, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 2, 9, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 25, 0, 6, 0, 0, 1, 4]

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
        func_name = "find_Odd_Pair"
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
        for test_case in ['assert find_Odd_Pair([5,4,7,2,1],5) == 6', 'assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12', 'assert find_Odd_Pair([1,2,3],3) == 2']:
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
