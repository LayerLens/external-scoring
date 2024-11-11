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
inputs = [[2, 5], [5, 7], [7, 13], [1, 10000], [100, 100000], [0, 10000], [100, 100], [1, 1], [101, 99999], [1, 10001], [100, 10000], [0, 100], [99, 100], [0, 0], [100, 101], [0, 1], [99, 99], [10001, 10001], [10000, 99999], [99, 100000], [101, 101], [0, 99], [2, 2], [10000, 100000], [99, 101], [100000, 100000], [101, 9999], [False, False], [10000, 10000], [98, 100], [1, 100], [2, 99999], [99, 9999], [99, 10000], [97, 101], [101, 10001], [97, 99], [10000, 10001], [1, 100000], [9999, 99999], [10001, 100000], [False, True], [99998, 99999], [2, 10000], [96, 97], [97, 10000], [0, 100000], [101, 10000], [True, True], [9999, 10001], [98, 98], [0, 99999], [2, 100001], [99999, 99999], [10000, 10002], [97, 99999], [1, 101], [9999, 9999], [96, 99], [9999, 99998], [98, 101], [97, 100000], [1, 98], [97, 97], [1, 10002], [99, 99999], [9999, 10000], [100, 99999], [99998, 99998], [0, 98], [0, 99998], [2, 100000], [98, 9999], [101, 10002], [101, 9998], [98, 99], [96, 98], [97, 98], [100, 10001], [10001, 99999], [96, 96], [9998, 9999], [100, 10002], [98, 100000], [1, 99999], [98, 10000], [100, 9999], [2, 97], [0, 2], [9999, 10002], [1, 2], [99, 100001], [10002, 10002], [101, 102], [10002, 100001], [9998, 9998], [0, 96], [101, 99998], [99997, 99998], [98, 99999], [10001, 10002], [97, 10001], [99997, 99999], [100001, 100001], [99997, 99997]]
results = [8, 12, 40, 25000000, 2499997500, 25000000, 0, 1, 2499997500, 25010001, 24997500, 2500, 99, 0, 101, 1, 99, 10001, 2475000000, 2499997599, 101, 2500, 0, 2475000000, 200, 0, 24997500, 0, 0, 99, 2500, 2499999999, 24997599, 24997599, 297, 25007501, 196, 10001, 2500000000, 2475009999, 2475000000, 1, 99999, 24999999, 97, 24997696, 2500000000, 24997500, 1, 20000, 0, 2500000000, 2500100000, 99999, 10001, 2499997696, 2601, 9999, 196, 2474910000, 200, 2499997696, 2401, 97, 25010001, 2499997599, 9999, 2499997500, 0, 2401, 2499900001, 2499999999, 24997599, 25007501, 24987501, 99, 97, 97, 25007501, 2475000000, 0, 9999, 25007501, 2499997599, 2500000000, 24997599, 24997500, 2400, 1, 20000, 1, 2500097600, 0, 101, 2475090000, 0, 2304, 2499897501, 99997, 2499997599, 10001, 25007697, 199996, 100001, 99997]

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
        func_name = "sum_odd"
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
        for test_case in ['assert sum_in_range(2,5) == 8', 'assert sum_in_range(5,7) == 12', 'assert sum_in_range(7,13) == 40']:
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
