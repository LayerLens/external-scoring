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
inputs = [[3, 1], [4, 1], [5, 3], [0, 0], [1, 1], [1, 2], [1, 0], [0, 2], [0, 1], [2, 1], [2, 0], [2, 2], [2, 3], [3, 2], [1, 3], [0, 3], [2, 4], [1, 4], [4, 2], [4, 4], [4, 0], [3, 0], [0, 4], [3, 4], [5, 4], [3, 3], [5, 2], [4, 5], [5, 0], [1, 5], [False, True], [5, 5], [5, 1], [True, True], [6, 6], [2, 6], [0, 5], [6, 2], [4, 3], [6, 1], [3, 5], [7, 3], [4, 6], [7, 4], [5, 6], [5, 7], [6, 3], [6, 7], [0, 6], [False, False], [3, 6], [6, 4], [7, 6], [0, 7], [7, 2], [8, 7], [8, 2], [6, 5], [True, False], [7, 0], [2, 7], [8, 5], [6, 0], [0, 8], [4, 8], [7, 1], [8, 1], [7, 7], [4, 7], [2, 5], [8, 4], [10, 9], [9, 9], [10, 3], [10, 10], [3, 9], [10, 2], [2, 8], [8, 3], [5, 8], [9, 10], [8, 8], [2, 9], [4, 9], [9, 6], [7, 8], [8, 9], [1, 8], [1, 10], [11, 10], [5, 9], [11, 9], [5, 11], [9, 2], [7, 5], [8, 0], [6, 8], [1, 9], [8, 6], [9, 8], [9, 4]]
results = [4, 11, 26, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 11, 0, 1, 1, 0, 0, 1, 0, 66, 0, 1, 0, 0, 0, 26, 0, 0, 0, 0, 302, 1, 57, 0, 2416, 0, 1191, 0, 0, 302, 0, 0, 0, 0, 57, 1, 0, 1191, 1, 4293, 1, 1, 1, 0, 4293, 1, 0, 0, 120, 247, 0, 0, 0, 15619, 1, 0, 455192, 0, 0, 47840, 0, 15619, 0, 0, 0, 0, 0, 14608, 0, 0, 0, 0, 1, 0, 2036, 0, 14608, 120, 1, 0, 0, 247, 1, 156190]

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
        func_name = "eulerian_num"
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
        for test_case in ['assert eulerian_num(3, 1) == 4', 'assert eulerian_num(4, 1) == 11', 'assert eulerian_num(5, 3) == 26']:
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
