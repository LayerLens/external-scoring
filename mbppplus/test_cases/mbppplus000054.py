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
inputs = [[[12, 3, 5, 7, 19], 2], [[17, 24, 8, 23], 3], [[16, 21, 25, 36, 4], 4], [[100, 99, 98, 97, 96], 5], [[50, 40, 30, 20, 10], 1], [[1000, 999, 998, 997, 996], 3], [[1000000, 500000, 100000, 50000, 10000], 4], [[50, 40, 30, 20, 10, 40], 1], [[100, 99, 98, 20, 97, 96], 5], [[100, 99, 98, 20, 97, 96], 6], [[100, 99, 98, 97, 96, 98], 5], [[51, 40, 99, 41, 30, 41, 20, 10], 1], [[500000, 100000, 50000, 10000], 4], [[1000, 999, 998, 997, 996, 999], 3], [[100, 99, 98, 97, 96], 4], [[100, 100, 98, 20, 97, 96, 100], 7], [[500000, 500000, 100000, 50000, 10000], 4], [[50, 40, 10, 20, 10, 40], 4], [[100, 99, 98, 98, 97, 96], 5], [[100, 99, 98, 20, 97], 5], [[100, 99, 96, 20, 97, 96], 6], [[100, 99, 96, 20, 97, 96], 5], [[100, 99, 99, 98, 97, 96], 4], [[51, 40, 99, 41, 30, 41, 20, 10], 7], [[100, 96, 20, 97, 96], 4], [[1000, 3, 999, 998, 997, 996, 999], 3], [[999, 100, 99, 98, 97, 96], 5], [[100, 99, 99, 98, 97], 4], [[1000, 3, 999, 998, 997, 996, 999], 4], [[100, 99, 99, 98, 96], 4], [[100, 99, 98, 99, 20, 97], 5], [[100, 99, 98, 20, 97, 100], 5], [[1000, 999, 998, 997, 996, 999], 4], [[51, 40, 99, 20, 41, 30, 41, 20, 10], 1], [[100, 99, 98, 97, 96, 98], 6], [[1000, 3, 999, 998, 997, 996, 998], 4], [[7, 100, 100, 98, 20, 97, 96, 100], 7], [[100, 99, 98, 97, 1000000, 96], 4], [[100, 19, 96, 20, 97, 96], 4], [[7, 100, 100, 98, 97, 19, 96, 100], 7], [[100, 99, 98, 20, 7, 97, 100], 4], [[100, 99, 98, 20, 96, 96], 5], [[500000, 100000, 50000, 10000], 3], [[7, 100, 100, 98, 97, 19, 96, 100], 8], [[7, 100, 100, 98, 97, 19, 96, 100], 3], [[51, 40, 99, 41, 30, 20, 10], 1], [[50, 997, 40, 30, 20, 10], 1], [[100, 99, 98, 97, 1000000, 96], 2], [[100, 95, 1, 98, 97, 1000000, 96], 4], [[51, 40, 99, 41, 30, 20, 10], 2], [[100, 100, 98, 20, 97, 96, 10000], 1], [[100, 99, 99, 98, 97], 5], [[100, 99, 98, 98, 97, 96], 6], [[100, 100, 98, 20, 97], 5], [[100, 99, 96, 19, 97, 96], 4], [[50, 40, 30, 20, 11], 1], [[100, 96, 99, 97, 20, 97, 96], 7], [[100, 99, 96, 10000, 20, 96], 3], [[50, 40, 30, 20, 7], 1], [[1000, 3, 999, 998, 997, 996, 999, 999], 3], [[100, 99, 98, 98, 97, 96, 100], 5], [[50, 40, 6, 20, 10, 40], 2], [[7, 100, 100, 98, 20, 97, 96, 100, 97], 7], [[100, 99, 96, 19, 97, 96, 99], 4], [[100, 99, 98, 4, 96, 96], 5], [[100, 99, 98, 20, 95, 96], 5], [[100, 19, 96, 20, 97, 96, 96], 4], [[41, 100, 100, 98, 20, 97, 96, 10000], 1], [[7, 100, 100, 6, 98, 97, 19, 96, 100], 8], [[7, 100, 100, 98, 20, 97, 96, 100, 100], 7], [[50, 997, 97, 40, 30, 20, 10], 1], [[100, 96, 20, 96, 96], 5], [[1000, 998, 997, 996, 999], 3], [[7, 51, 100, 98, 20, 97, 96, 100], 7], [[100, 19, 30, 20, 97, 96], 4], [[1000, 3, 999, 998, 997, 5, 996, 999], 3], [[7, 100, 100, 98, 11, 97, 96, 100, 100], 7], [[100, 99, 96, 20, 97, 95], 6], [[7, 100, 100, 98, 20, 97, 96, 100, 100], 6], [[100, 98, 98, 97, 96], 5], [[100, 99, 98, 98, 97, 96, 100, 99], 5], [[50, 40, 20, 10, 40], 1], [[51, 40, 99, 41, 30, 41, 20, 10], 6], [[51, 40, 99, 20, 41, 30, 41, 20, 10], 7], [[7, 100, 100, 98, 20, 30, 96, 100], 7], [[7, 51, 100, 98, 20, 30, 97, 96, 100], 7], [[101, 99, 98, 97, 96], 4], [[100, 99, 99, 98, 96], 3], [[50, 40, 20, 10, 40, 20], 1], [[50, 40, 20, 7], 1], [[100, 99, 98, 20, 95, 96], 4], [[7, 100, 100, 98, 20, 97, 10000, 96, 100], 7], [[97, 100, 99, 98, 97, 96, 98], 6], [[100, 96, 20, 97, 998, 96], 4], [[51, 3, 999, 998, 997, 996, 999], 3], [[101, 99, 98, 97, 96], 1], [[7, 100, 41, 98, 20, 30, 96, 100], 7], [[7, 100, 100, 96, 97, 19, 96, 100], 8], [[7, 51, 100, 20, 20, 97, 96, 100], 7], [[6, 7, 100, 100, 98, 97, 19, 96, 100], 7], [[100, 99, 98, 4, 96], 5], [[51, 3, 999, 998, 997, 996, 999], 4], [[7, 100, 98, 97, 19, 96, 100, 100], 7], [[100, 99, 98, 20, 7, 97, 100], 5], [[1000000, 100, 96, 20, 97, 96], 4], [[100, 99, 98, 20, 95], 5], [[1000, 998, 997, 996], 3]]
results = [3, 8, 36, 96, 50, 998, 50000, 50, 97, 96, 96, 51, 10000, 998, 97, 100, 50000, 20, 97, 97, 96, 97, 98, 20, 97, 999, 97, 98, 998, 98, 20, 97, 997, 51, 98, 998, 96, 97, 20, 96, 20, 96, 50000, 100, 100, 51, 50, 99, 98, 40, 100, 97, 96, 97, 19, 50, 96, 96, 50, 999, 97, 40, 96, 19, 96, 95, 20, 41, 96, 96, 50, 96, 997, 96, 20, 999, 96, 95, 97, 96, 97, 50, 41, 41, 96, 97, 97, 99, 50, 50, 20, 10000, 96, 97, 999, 101, 96, 100, 96, 19, 96, 998, 100, 7, 20, 95, 997]

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
        func_name = "kth_element"
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
        for test_case in ['assert kth_element([12,3,5,7,19], 2) == 3', 'assert kth_element([17,24,8,23], 3) == 8', 'assert kth_element([16,21,25,36,4], 4) == 36']:
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
