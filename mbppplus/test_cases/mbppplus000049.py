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
inputs = [[15], [12], [9], [79337], [79336], [86], [87], [88], [85], [79335], [79334], [79333], [79332], [True], [89], [79331], [95], [90], [79338], [91], [92], [93], [84], [94], [83], [79330], [82], [46], [47], [44], [48], [49], [81], [43], [42], [96], [41], [45], [97], [79], [78], [79329], [80], [50], [40], [79328], [51], [17], [98], [39], [16], [18], [99], [38], [79327], [19], [20], [79325], [77], [79339], [37], [36], [79324], [79340], [79341], [35], [34], [79323], [73], [79322], [21], [22], [79320], [52], [23], [74], [65], [79326], [79321], [33], [79319], [76], [32], [14], [75], [57], [100], [62], [67], [72], [58], [59], [60], [66], [56], [53], [101], [54], [68], [63], [55], [61], [64]]
results = [4, 6, 3, 2, 16, 4, 4, 8, 4, 24, 4, 2, 24, 1, 2, 6, 4, 12, 16, 4, 6, 4, 12, 4, 2, 8, 4, 4, 2, 6, 10, 3, 5, 2, 8, 12, 2, 6, 2, 2, 8, 8, 10, 6, 8, 24, 4, 2, 6, 4, 5, 6, 6, 4, 4, 2, 6, 12, 4, 8, 2, 9, 12, 12, 8, 4, 4, 8, 2, 8, 4, 4, 32, 6, 2, 4, 4, 32, 4, 4, 2, 6, 6, 4, 6, 4, 9, 4, 2, 12, 4, 2, 12, 8, 8, 2, 2, 8, 6, 6, 4, 2, 7]

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
        func_name = "divisor"
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
        for test_case in ['assert divisor(15) == 4', 'assert divisor(12) == 6', 'assert divisor(9) == 3']:
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
