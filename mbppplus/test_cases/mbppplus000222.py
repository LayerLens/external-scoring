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
inputs = [[[100, 10, 5, 25, 35, 14], 11], [[1, 1, 1], 1], [[1, 2, 1], 2], [[1000000, 2000000, 3000000], 10000], [[1000000, 2000000, 3000000], 10001], [[2000000, 3000000], 10001], [[1000000, 2000000], 10001], [[1000000, 2000000, 3000000], 1000000], [[1000000, 2000000, 3000000], 3000000], [[2000000, 10001, 3000000], 2000000], [[1000000, 3000000], 3000000], [[1000000, 2000000, 3000000], 2000000], [[1000000, 2000000, 3000000, 1000000], 2000000], [[2000000, 3000000, 3000000], 10001], [[2000000, 1000001, 1000000, 2000000], 10001], [[2000000, 3000000, 3000000], 10002], [[2000000, 3000001, 3000000], 10002], [[1000000, 2000000, 3000000, 1000000], 1000001], [[2000000, 10001, 3000000], 3000000], [[1000000, 2000000, 2000000], 10001], [[1000000, 2000000, 3000000, 2000000], 1000001], [[2000000, 10001, 3000000], 10001], [[1000000, 2000000, 10002, 3000000], 3000000], [[2000000], 10001], [[1000000], 3000000], [[1000000, 2000000, 3000000, 2000000, 1000000], 1000001], [[10000, 2000000, 3000000], 2000000], [[1000001, 1000000, 2000000], 10001], [[2000000, 10001, 3000000], 1000000], [[1000001, 1000000, 1000000], 10001], [[1000000, 2000000, 10002, 3000000, 10002], 3000000], [[1000001, 1000000], 10000], [[2000000, 3000000, 2000000, 1000000], 1000000], [[2000000, 10001, 3000000, 10001], 10001], [[2000000, 3000000], 10002], [[1000000, 1000000, 2000000, 3000000, 1000000], 2000000], [[2000001], 10001], [[3000000], 10001], [[1000001, 1000000, 3000000], 3000000], [[1000000, 2000000, 3000000, 1000000], 10000], [[2000000, 3000000, 1999999, 1000000, 1999999], 1000000], [[2000000, 10002, 3000000], 3000000], [[2000000, 2000000, 1000001, 1000000, 2000000], 10001], [[2000000, 10001, 3000000], 3000001], [[2000000, 3000000], 10000], [[10000, 3000000], 2000000], [[2999999, 10000, 2000000, 3000000], 2000000], [[1000000, 2000000, 3000000, 2000000], 10001], [[1000000, 2000000, 3000000, 1000000], 10001], [[2000000, 1000001, 3000000], 1000000], [[2000000, 10001, 3000000, 10001], 10002], [[1000001, 1000000, 1000001], 10001], [[1000001, 1000000, 1000000, 1000000], 10000], [[2000000, 2000000, 3000000], 3000000], [[1000000, 3000000, 2000000, 3000000], 10001], [[3000000, 2000001], 10001], [[1000000, 3000000, 2000001, 3000000], 10001], [[1000001, 3000000, 2000001, 3000000], 10001], [[1000001, 1000000], 10002], [[1000001, 1000000, 2000000], 1000000], [[1000001, 1000000, 10000, 3000000], 3000000], [[1000001, 1000000, 1000000], 10000], [[2000000, 1000001, 2999999], 1000000], [[2000000, 2000000, 1000001, 1000000, 1000001, 2000000], 2000001], [[3000000, 3000000], 10001], [[2000000, 3000000], 1999999], [[1000000, 3000000, 3000000], 10001], [[1000000, 2000000, 3000000, 1000000, 2000000], 10001], [[3000001, 3000000], 10002], [[2000000, 2999999, 10001, 3000000], 3000001], [[1000000, 2000000, 3000000, 1000000, 1000000], 2000000], [[1000001, 1000000, 1000001], 10000], [[2000000, 3000000, 10001, 3000000], 1000001], [[1999999], 10002], [[2000000, 1000001, 3000000], 2999999], [[1000001, 1000000, 1000000, 1000000, 1000000], 10000], [[2000000, 1000001, 1000000, 2000000], 10002], [[2000000, 2999999, 10001, 3000000], 1999999], [[1000000, 3000001, 2000000, 3000000, 1000000, 10002], 2000000], [[2000000, 2999999, 10001, 3000000], 1000000], [[1000000, 2000000], 10000], [[2000000, 1000001, 3000000], 999999], [[999999], 1000000], [[2000000, 2000000, 1000001, 1000000, 1000001, 2000000, 1000001], 2000001], [[1000000, 3000000, 2000001, 3000000], 10002], [[1000000, 2000000, 3000000, 1000000, 1000000], 1999999], [[2000000, 1000001, 2000001, 2000000], 2999999], [[2000000, 3000000, 10001, 3000001], 2000000], [[2000000, 2999999, 10001, 3000000], 999999], [[1000001, 1000000, 3000000], 3000001], [[1000001, 1000000, 1000001], 2000000], [[1000001], 10002], [[2999999, 2000000, 1000001, 3000000], 1000000], [[2000000, 10001, 3000000, 10002], 10001], [[2000000, 3000000, 3000000, 10001, 3000000], 1000000], [[1000000, 3000000, 2000001, 3000000, 1000000], 10001], [[2999999, 1000000], 10001], [[1000000, 1000000, 1000001], 10001], [[2000000, 10001, 3000000], 3000002], [[2000000, 3000000, 10001, 3000000], 2999999], [[10000, 3000000, 3000000], 2000000], [[1000000, 2000000, 3000000, 1000000], 10002], [[2999999, 10000, 2000000, 3000000, 2000000], 1000001], [[10000, 3000000, 3000000], 1999999]]
results = [9, 0, 0, 0, 600, 9995, 9999, 0, 0, 0, 0, 0, 0, 1800, 404, 8796, 8748, 6, 0, 400, 12, 0, 0, 9801, 1000000, 999989, 0, 198, 0, 99, 0, 0, 0, 0, 9954, 0, 9802, 9701, 0, 0, 0, 0, 9209, 2006668, 0, 0, 0, 12, 6, 0, 9954, 9999, 0, 0, 18, 9695, 918, 2709, 9794, 0, 0, 0, 0, 1750001, 9992, 1000001, 900, 8801, 9330, 1986666, 0, 0, 819983, 9601, 1666667, 0, 6656, 1507500, 0, 0, 0, 12, 999999, 1875001, 5550, 375000, 1518519, 0, 120012, 1333334, 1000000, 9803, 0, 0, 0, 8210, 97, 99, 1026670, 1006667, 0, 384, 480000, 22500]

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
        func_name = "find_remainder"
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
        for test_case in ['assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9', 'assert find_remainder([1,1,1],1) == 0', 'assert find_remainder([1,2,1],2) == 0']:
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
