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
inputs = [[[1, 2, 3]], [[-1, 2, 3, 4]], [[2, 3, 6]], [[-10, -5, -3, -1, -7]], [[-10, -5, -4, -3, -1, -7, -4]], [[-10, -5, -1, -7]], [[-10, -5, -4, -3, -1, -7, -4, -5]], [[-10, -5, -4, -3, -7, -4]], [[-10, -3, -1, -7, -5]], [[-10, -5, -4, -3, -6, -4]], [[-10, -5, -4, -5, -3, -6, -4]], [[-10, -5, -3, -1, -7, -3]], [[-10, -5, -4, -3, -6, -1, -7, -4, -7]], [[-10, -5, -4, -5, -9, -3, -6, -4, -5]], [[-10, -5, -4, -5, -9, -3, -6, -4, -5, -4]], [[-10, -5, -4, -3, -6, -4, -6]], [[-10, -3, -7, -5]], [[-2, -10, -5, -4, -3, -1, -7, -4]], [[-10, -5, -1, -4]], [[-2, -10, -3, -1, -7, -5]], [[-4, -5, -3, -1, -7]], [[-10, -3, -5, -7, -5]], [[-10, -5, -4, -3, -1, -7, -4, -5, -3]], [[-10, -5, -4, -1, -7, -4, -5, -3]], [[-4, -5, -3, -1, -7, -1]], [[-10, -5, -4, -3, -4, -6, -4, -10]], [[-4, -5, -3, -1, -7, -7]], [[-4, -5, -1, -7, -7]], [[-5, -5, -2, -7]], [[-10, -5, -4, -3, -6, -7, -4, -7]], [[-10, -5, -3, -2, -7]], [[-2, -5, -3, -2, -7]], [[-2, -10, -3, -1, -7, -2, -5]], [[-4, -5, -3, -1, -10, -1]], [[-4, -5, -3, -1, -10]], [[-10, -5, -4, -4, -1, -7, -4, -5, -3]], [[-5, -4, -7, -1, -7, -4, -5, -3]], [[-10, -5, -4, -5, -9, -3, -6, -4, -5, -10]], [[-10, -5, -4, -2, -4, -6, -4, -10]], [[-10, -5, -4, -4, -1, -7, -4, -5, -3, -3]], [[-10, -5, -4, -5, -7, -3, -6, -4]], [[-8, -4, -5, -3, -1, -7, -7]], [[-10, -5, -1, -4, -10]], [[-4, -5, -1, -10, -1]], [[-5, -5, -3, -1, -7]], [[-10, -5, -5, -5]], [[-9, -10, -3, -7, -5]], [[-10, -5, -4, -3, -6, -4, -10]], [[-10, -5, -4, -5, -3, -3, -4]], [[-4, -5, -1, -10, -1, -1]], [[-10, -7, -5]], [[-10, -5, -5, -7, -5, -3, -6, -4]], [[-4, -5, -3, -1, -4]], [[-4, -5, -3, -1, -5, -10]], [[-10, -5, -4, -1, -9, -7, -4, -5, -3]], [[-10, -4, -5, -7, -5]], [[-2, -10, -3, -1, -7, -5, -5]], [[-4, -3, -10]], [[-2, -5, -3, -2, -7, -5]], [[-6, -2]], [[-10, -5, -3, -4, -3, -4, -6, -4, -10]], [[-10, -5, -4, -1, -9, -7, -3, -5, -3, -5]], [[-5, -5, -7]], [[-10, -5, -4, -1, -7, -4, -5, -3, -5]], [[-10, -5, -4, -2, -4, -6, -10, -10]], [[-6, -5, -4, -7, -1, -7, -4, -5, -3]], [[-5, -5, -3, -6, -7]], [[-1, -5, -1, -4, -10]], [[-10, -5, -4, -2, -4, -6, -10]], [[-10, -5, -1, -4, -5]], [[-9, -10, -3, -9, -5]], [[-5, -1, -4]], [[-9, -2, -10, -3, -7, -2]], [[-10, -5, -5, -3, -5]], [[-10, -5, -4, -3, -1, -7, -4, -10]], [[-10, -5, -4, -4, -1, -7, -4, -5, -1, -3]], [[-10, -5, -4, -5, -9, -3, -6, -4, -5, -6, -4]], [[-10, -4, -5, -4, -5, -3, -4, -5]], [[-9, -10, -3, -9, -5, -10, -9]], [[-10, -5, -4, -1, -9, -7, -3, -5, -8, -3, -5]], [[-10, -8, -4, -3, -1, -7, -4]], [[-4, -5, -1, -7]], [[-9, -10, -5, -4, -3, -1, -7, -4, -5, -3, -3]], [[-9, -10, -5, -5, -7, -5, -8, -3, -6, -4]], [[-2, -4, -9, -3, -1, -7, -2, -5]], [[-10, -5, -4, -4, -7, -3, -6, -4]], [[-5, -5, -3, -9, -1, -7]], [[-2, -10, -4, -4, -3, -1, -7, -4]], [[-6, -5, -9, -7, -1, -7, -4, -5, -3]], [[-10, -4, -7, -5]], [[-10, -4, -4, -2, -10]], [[-6, -5, -9, -7, -1, -7, -4, -5, -3, -6]], [[-10, -4, -5, -7, -5, -7]], [[-10, -5, -4, -5, -7, -3, -6, -4, -3]], [[-10, -5, -4, -5, -7, -3, -6, -1, -4]], [[-10, -5, -3, -1, -8, -7, -8]], [[-10, -4, -7, -5, -7]], [[-10, -5, -4, -5, -9, -6, -4, -5, -6, -4, -6, -6]], [[-10, -5, -4, -4, -1, -7, -4, -5, -5, -3]], [[-10, -5, -9, -1, -4, -5]], [[-10, -5, -4, -4, -1, -7, -4, -3, -3, -3]], [[-9, -10, -5, -4, -11, -3, -1, -7, -4, -5, -3, -3, -5]], [[-5, -10, -5, -7, -5, -6, -4]], [[-9, -10, -3, -9, -5, -5]]]
results = [4, 3, 8, -11, -11, -11, -11, -13, -11, -13, -13, -11, -11, -13, -13, -13, -13, -11, -11, -11, -8, -13, -11, -11, -8, -13, -8, -8, -9, -13, -12, -9, -11, -11, -11, -11, -8, -13, -12, -11, -13, -9, -11, -11, -8, -15, -13, -13, -13, -11, -15, -13, -6, -11, -11, -14, -11, -13, -9, -8, -13, -11, -12, -11, -12, -8, -10, -11, -12, -11, -13, -6, -12, -13, -11, -11, -13, -13, -13, -11, -11, -8, -11, -13, -10, -13, -10, -11, -10, -14, -12, -10, -14, -13, -11, -11, -14, -14, -11, -11, -11, -12, -14, -13]

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
        func_name = "big_sum"
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
        for test_case in ['assert big_sum([1,2,3]) == 4', 'assert big_sum([-1,2,3,4]) == 3', 'assert big_sum([2,3,6]) == 8']:
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
