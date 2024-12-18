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
inputs = [[[-2, -3, 4, -1, -2, 1, 5, -3], 8], [[-3, -4, 5, -2, -3, 2, 6, -4], 8], [[-4, -5, 6, -3, -4, 3, 7, -5], 8], [[], 0], [[-10, -5, -3, -2, -1], 5], [[-100, -50, -30, -20, -10, 5, -3, -2, -1], 9], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 10], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400], 14], [[1000, 900, 800, 700, 600, -1000, -900, -800, -700, -600], 10], [[100, -100, 200, -200, 300, -300, 400, -400, 500, -500], 10], [[-100, 200, -300, 400, -500, 600, -700, 800, -900, 1000], 10], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], 10], [[14, -9, -8, -7, -6, -5, -4, -3, -2, -1], 10], [[-100, -50, -30, -20, -10, 5, -3, -2, -7], -1], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -1], [[-1000, -5, -900, -800, -700, -600, -500, -400, 900, 800, 700, 600, 500, 400], 14], [[-100, -50, -30, -20, -10, 5, -3, -2, -7], -800], [[-100, -50, -30, -20, -10, 5, -3, -2, -7], 0], [[-100, -50, -30, -20, -10, 5, -3, -2, -7, -30], -7], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 9], [[1000, 900, 800, 700, 600, -1000, -900, -800, -700, -600], 9], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400], -800], [[900, 800, 700, 600, -1000, -900, -800, -700, -600], 9], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 400, 800, 700, 600, 500, 400], -800], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -600], [[1000, 900, 800, 600, -1000, -900, -800, -700, -600], 9], [[1000, 900, 800, 700, -400, -1000, -900, -800, -700, -600], 9], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], -20], [[-1000, -800, -700, -600, -500, -400, 1000, 900, 400, 800, 700, 600, 500, 400, 600], -800], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], 9], [[-100, -50, -30, -21, -10, 5, -3, -2, -7], -800], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400], -1000], [[-10, -9, -8, -7, -6, -5, -4, 9, -2, -1], -600], [[14, -9, -8, -7, -6, -5, -4, -3, -2, -1], 9], [[-10, -9, -8, -7, -6, -5, -4, 9, -2], -601], [[14, -9, -8, -7, -6, -5, -4, -3, -2, -1], -400], [[-10, -9, -8, -7, -6, -5, -4, 9, -2], -1], [[-100, -50, -30, -20, -10, 5, -3, -2, -7, -30], -6], [[1000, 900, 800, 700, 600, -1000, -900, -800, -700, -600, 1000], 10], [[-1000, -800, -700, -600, -500, -400, 1000, 900, 400, 800, 700, 600, 500, 400, 600], -801], [[14, -9, -8, -7, -6, -5, -2, -4, -3, -2, -1], 10], [[-10, -9, -8, -7, -6, -5, -4, 9, -2, -5], -1], [[14, -9, -8, -7, -6, -5, -4, -3, -2, -1], -30], [[1000, 900, 800, 700, 600, -1000, -900, -800, -700, -599], -400], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400, 500], 14], [[14, -9, -8, -7, -6, -5, -4, -3, -2, -1], 8], [[-100, -50, -30, -20, -10, 5, -3, -2, -7], -799], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], -3], [[-100, -50, -30, -21, 5, -3, -2, -7, -2], -800], [[14, -50, -30, -20, -10, 5, -3, -2, -1], 9], [[-100, -31, -50, -30, -21, -10, 5, -3, -2, -7], -1000], [[-10, -9, -8, -7, -6, -5, -4, 9, -2], 0], [[-100, -50, -30, -21, -10, 5, -3, -2, 400], -4], [[14, -9, -8, -7, 14, -6, -5, -4, -3, -2, -1], 8], [[-100, -50, -30, -21, -10, 4, -3, -2, 400], -4], [[14, -50, -30, -20, -10, -9, 5, -3, -2, -1, -20], 9], [[14, -9, -8, -7, -6, -5, -2, -4, -3, -2, -1, -9, 14], 10], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400, 1000], -1000], [[-2, -3, -4, -5, -6, -7, -8, -8, -10], -20], [[-10, -9, -8, -7, -6, -5, -4, 9, -2, -9], 0], [[14, -9, -8, -7, -6, -1, -5, -2, -4, -3, -2, -1, -9, 14], 9], [[-100, -50, -21, -10, 5, -3, -2, 400], -4], [[-100, -50, -30, -21, 5, -3, -2, -599, -2], -50], [[900, 800, 700, 600, -1000, -900, -800, -700, -600, -1000], 9], [[-2, -3, -200, -5, -6, -8, -8, -10], -21], [[-100, -50, -30, -20, -10, 5, -3, -2, -700, -7], 0], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -601], [[-100, -30, -21, 5, -3, -2, -7, -2], -800], [[-100, -50, -30, -20, -10, 5, -3, -2, -31, -7], -1], [[900, -4, 700, 600, -1000, -900, -799, -800, -700, -500, -600], 10], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -5, -10], -9], [[-100, -50, -6, -30, -20, -10, 5, -3, -2, -7], -1], [[-1, -3, -4, -5, -6, -7, -8, -9, -10], -3], [[-100, -50, -30, -20, -10, -11, 5, -3, -2, -7], 0], [[-1, -3, -4, -6, -7, -8, -9, -10, -10], -500], [[14, -9, -8, -7, 14, -6, -5, -4, -3, -2, -1, -6], 8], [[-100, -50, -30, -20, -10, 5, -3, -2, -7, -50], 0], [[-100, -50, -30, -20, 5, -10, 5, -3, -2, -7], -32], [[-100, -50, -30, -20, -10, -11, 5, -3, -2, -7, -30], 0], [[1000, 900, -300, 600, -1000, -900, -800, -700, -600], 9], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400], -400], [[-2, -2, -200, -5, -6, -8, -8, -10], -21], [[-900, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400], -300], [[-100, -31, -50, -30, -21, -10, -599, -3, -2, -7], -1000], [[14, -9, -8, -7, -6, -1, -5, -2, -4, -3, -2, -1, -9, 14, -7], 9], [[-1000, -900, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 399, 500, 400], 14], [[100, -100, 200, -200, 300, 5, -300, 400, -400, 500, -500], 10], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], -50], [[-100, -31, -30, -20, -10, -11, 5, -3, -2, -7, -30], 0], [[-100, -31, -11, -50, -30, -21, -10, -599, -3, -2, -7], -1000], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 400, 800, 700, 600, 500, 400], -801], [[14, -9, -8, -7, -7, -5, -4, -3, -2, -1], 10], [[1000, 900, 800, 700, -801, 600, -1000, -900, -800, -700, -600], 9], [[-100, -50, -10, -30, -20, -10, 5, -3, -2, -7], -800], [[14, -50, -30, -20, -10, -9, -10, 5, -3, -2, -1, -20], 9], [[14, -9, -8, -7, 14, -6, -5, -4, -3, -2, -1, -6], 9], [[-10, -9, -8, -7, -6, -5, -4, 600, -2, -1], -400], [[100, -100, 200, -200, 300, -300, 400, 501, -400, 500, -500], 10], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -8], 9], [[14, -9, -8, -7, -6, -5, -2, -4, -3, -2, -1, -9, 14], 9], [[-1000, -900, -800, -700, -600, -500, -400, 1000, 900, 800, 700, 600, 500, 400, 500], -21], [[-1, -2, -4, -5, -6, -7, -8, -9, -10], -20], [[14, -9, -8, -7, 900, 14, -6, -5, -4, -3, -2, -1], -31], [[1000, 900, 800, 700, 600, -1000, -900, -800, -700, -600], -300], [[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, -10], 9], [[14, -9, -8, -7, -7, -5, -4, -3, -2, -1, -7], 10], [[-100, -50, -30, -20, -10, 5, -3, -2, -1], 8], [[-100, -31, -11, -50, -30, -21, -10, -3, -2, -7], -1000], [[-1, -2, -4, -5, -3, -6, -7, -8, -10], -20], [[-100, -9, -8, -7, -6, -1, -5, -2, -4, -3, -2, -1, -9, 14], 9], [[-1, -2, -3, -4, -5, -6, -8, -9, -10], -20], [[-10, -9, -8, -7, -6, -5, -4, 600, -2, -1], -401]]
results = [7, 8, 10, 0, 0, 5, 0, 4900, 4000, 500, 1000, 0, 14, 0, 0, 3900, 0, 0, 0, 0, 4000, 0, 3000, 0, 0, 3300, 3400, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 4000, 0, 14, 0, 0, 0, 4900, 14, 0, 0, 0, 14, 0, 0, 0, 14, 0, 14, 14, 0, 0, 0, 14, 0, 0, 3000, 0, 0, 0, 0, 0, 2196, 0, 0, 0, 0, 0, 14, 0, 0, 0, 2200, 0, 0, 0, 0, 14, 5299, 505, 0, 0, 0, 0, 14, 3400, 0, 14, 14, 0, 1001, 0, 14, 0, 0, 0, 0, 0, 14, 5, 0, 0, 0, 0, 0]

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
        func_name = "max_sub_array_sum"
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
        for test_case in ['assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7', 'assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8', 'assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10']:
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
