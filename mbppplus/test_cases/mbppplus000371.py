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
inputs = [[10], [36], [14], [196], [125], [15625], [-9], [-5686748], [123456789], [987654321], [2147483647], [9223372036854775807], [-8], [987654320], [-5686747], [123456788], [-7], [84], [False], [83], [9223372036854775806], [2147483646], [2147483645], [82], [85], [True], [98], [987654319], [9223372036854775808], [86], [-10], [97], [-11], [987654322], [9223372036854775805], [123456787], [-6], [123456786], [987654318], [-82], [67], [-83], [87], [123456791], [987654323], [123456790], [68], [-80], [23], [123456792], [99], [69], [2147483644], [70], [2147483648], [81], [-5686746], [37], [987654317], [22], [-5686745], [-75], [29], [88], [64], [123456793], [28], [2147483643], [987654316], [987654324], [987654315], [987654314], [2147483649], [9223372036854775809], [-5], [63], [-4], [62], [80], [123456794], [-12], [39], [24], [-81], [987654325], [38], [95], [40], [-74], [30], [-44], [15], [-73], [987654326], [16], [25], [41], [26], [-1], [123456785], [65], [94], [71], [-76], [21], [-43], [96], [-13], [27], [-22]]
results = [False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "is_perfect_square"
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
        for test_case in ['assert not is_perfect_square(10)', 'assert is_perfect_square(36)', 'assert not is_perfect_square(14)', 'assert is_perfect_square(14*14)', 'assert not is_perfect_square(125)', 'assert is_perfect_square(125*125)']:
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
