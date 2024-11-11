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
inputs = [[10, 15], [100, 150], [4, 6], [27, 81], [12, 18], [123, 456], [555, 1111], [987, 654], [10, 3], [987654321, 123456789], [555, 456], [987654322, 81], [555, 987654322], [3, 987654321], [555, 555], [123, 1111], [987654321, 987654321], [456, 456], [81, 555], [123456790, 123456790], [123456789, 987654322], [123, 3], [12, 1111], [123456789, 81], [555, 554], [81, 456], [455, 456], [81, 457], [555, 987654323], [556, 553], [80, 456], [555, 553], [123456789, 456], [456, 987654323], [987, 986], [987654320, 987654321], [987654323, 987654322], [987654323, 987654323], [987654322, 987654321], [987654323, 10], [455, 987654320], [987654322, 987654322], [123456789, 123456790], [554, 457], [26, 82], [11, 3], [986, 987654323], [123, 123], [555, 81], [987654324, 987], [987654321, 18], [987654319, 987654318], [654, 654], [123456790, 455], [3, 987654322], [80, 987654321], [553, 553], [556, 457], [988, 654], [455, 123456789], [654, 987654321], [123456790, 654], [11, 123], [556, 1111], [27, 26], [80, 124], [556, 456], [987, 987], [457, 456], [553, 80], [81, 458], [123456789, 123456789], [457, 457], [457, 3], [123456789, 986], [985, 987], [986, 986], [987654320, 987654320], [456, 458], [2, 3], [124, 987654323], [987654320, 81], [12, 12], [987654321, 987654320], [125, 555], [81, 2], [654, 81], [654, 123456788], [987654319, 80], [81, 554], [457, 554], [987654323, 456], [456, 26], [81, 81], [556, 556], [654, 80], [987654319, 986], [123, 4], [556, 987654320], [456, 556], [987654320, 456], [987654321, 2], [126, 2], [556, 987654322], [18, 123456789], [2, 654], [457, 987654323], [985, 456], [2, 18], [3, 556]]
results = [6.0, 93.0, 3.0, 40.0, 12.0, 4.0, 1, 4.0, 1, 13.0, 4.0, 1, 1, 4.0, 912.0, 1, 1515470502.0, 1200.0, 4.0, 228228912.0, 1, 4.0, 1, 13.0, 1, 4.0, 1, 1, 1, 1, 15.0, 1, 4.0, 1, 1, 1, 1, 987654324.0, 1, 1, 6.0, 1483596972.0, 1, 1, 3.0, 1, 1, 168.0, 4.0, 4.0, 13.0, 1, 1320.0, 6.0, 1, 1, 640.0, 1, 3.0, 1, 4.0, 3.0, 1, 1, 1, 7.0, 7.0, 1536.0, 1, 1, 1, 178422816.0, 458.0, 1, 1, 1, 1620.0, 2358365424.0, 3.0, 1, 1, 1, 28.0, 1, 6.0, 1, 4.0, 3.0, 1, 1, 1, 1, 3.0, 121.0, 980.0, 3.0, 1, 1, 7.0, 7.0, 15.0, 1, 3.0, 3.0, 13.0, 3.0, 1, 1, 3.0, 1]

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
        func_name = "sum"
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
        for test_case in ['assert sum(10,15) == 6', 'assert sum(100,150) == 93', 'assert sum(4,6) == 3']:
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
