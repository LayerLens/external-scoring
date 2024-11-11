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
inputs = [[123], [456], [12], [0], [9999999999999999], [12345678901234567890], [1], [9999999999999998], [12345678901234567889], [12345678901234567888], [10000000000000000], [12345678901234567887], [10000000000000001], [12345678901234567885], [12345678901234567886], [9999999999999997], [2], [12345678901234567891], [75], [76], [74], [12345678901234567892], [3], [77], [73], [12345678901234567893], [26], [95], [96], [78], [10000000000000003], [94], [12345678901234567894], [12345678901234567884], [79], [25], [10000000000000002], [12345678901234567883], [80], [12345678901234567895], [12345678901234567896], [71], [9999999999999996], [72], [12345678901234567882], [88], [27], [10000000000000004], [4], [89], [10000000000000005], [5], [97], [87], [98], [24], [90], [10000000000000006], [12345678901234567897], [62], [70], [28], [23], [69], [93], [86], [10000000000000007], [68], [61], [92], [22], [12345678901234567881], [9999999999999995], [55], [10000000000000008], [9999999999999994], [81], [21], [99], [85], [6], [54], [12345678901234567898], [91], [20], [19], [53], [8], [67], [82], [9999999999999993], [56], [49], [63], [64], [30], [12345678901234567899], [65], [66], [42], [12345678901234567880], [29], [9], [48], [60], [31]]
results = [1, 4, 1, 0, 9, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 9, 2, 1, 7, 7, 7, 1, 3, 7, 7, 1, 2, 9, 9, 7, 1, 9, 1, 1, 7, 2, 1, 1, 8, 1, 1, 7, 9, 7, 1, 8, 2, 1, 4, 8, 1, 5, 9, 8, 9, 2, 9, 1, 1, 6, 7, 2, 2, 6, 9, 8, 1, 6, 6, 9, 2, 1, 9, 5, 1, 9, 8, 2, 9, 8, 6, 5, 1, 9, 2, 1, 5, 8, 6, 8, 9, 5, 4, 6, 6, 3, 1, 6, 6, 4, 1, 2, 9, 4, 6, 3]

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
        func_name = "first_Digit"
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
        for test_case in ['assert first_Digit(123) == 1', 'assert first_Digit(456) == 4', 'assert first_Digit(12) == 1']:
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
