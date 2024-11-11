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
inputs = [[12345], [1212112], [1212], [12345678901234567890], [98765432109876543210], [-1212], [-12345], [-12345678901234567890], [987654321098765432109876543210], [-123456789012345678901234567890], [123456789012345678901234567890], [-987654321098765432109876543210], [9876543210987654321098765432110], [9876543210987654321098765432101], [-9876543210987654321098765432110], [-9876543210987654321098765432101], [-1000], [1001], [0], [-65], [1002], [-12345678901234567889], [True], [-56], [98765432109876543209], [9876543210987654321098765432102], [-64], [-9876543210987654321098765432100], [-12344], [-63], [987654321098765432109876543211], [False], [-999], [98765432109876543211], [-57], [-66], [-55], [-123456789012345678901234567891], [-987654321098765432109876543211], [123456789012345678901234567891], [-67], [-39], [61], [987654321098765432109876543209], [-12343], [987654321098765432109876543208], [-54], [-58], [987654321098765432109876543212], [9876543210987654321098765432103], [-12345678901234567891], [-62], [-9876543210987654321098765432111], [-12345678901234567888], [12345678901234567891], [12345678901234567892], [1], [987654321098765432109876543214], [98765432109876543212], [-9876543210987654321098765432102], [-9876543210987654321098765432099], [81], [987654321098765432109876543213], [9876543210987654321098765432105], [-9876543210987654321098765432112], [123456789012345678901234567889], [9876543210987654321098765432104], [-59], [-61], [-9876543210987654321098765432098], [-1213], [96], [1000], [98765432109876543208], [12345678901234567889], [-123456789012345678901234567892], [-38], [-987654321098765432109876543208], [-123456789012345678901234567893], [-987654321098765432109876543212], [12345678901234567893], [999], [-60], [987654321098765432109876543215], [-40], [-53], [100], [82], [-12346], [80], [-52], [-78], [-123456789012345678901234567889], [-12342], [60], [-68], [9876543210987654321098765432100], [-9876543210987654321098765432113], [-123456789012345678901234567888], [1003], [47], [79], [59], [9876543210987654321098765432108], [36], [37], [9876543210987654321098765432107], [2], [12345678901234567894], [98765432109876543213], [-12347], [-1211], [-88], [1004], [98765432109876543214], [-51], [-998], [-50], [-9876543210987654321098765432109]]
results = [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False]

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
        func_name = "is_Diff"
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
        for test_case in ['assert is_Diff (12345) == False', 'assert is_Diff(1212112) == True', 'assert is_Diff(1212) == False']:
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
