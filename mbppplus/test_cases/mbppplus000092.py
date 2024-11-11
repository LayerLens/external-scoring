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
inputs = [[0], [5], [17], [1], [2], [8], [128], [1000000], [342788], [567990], [999999999999], [987654321098], [1000000000000], [1234567890123], [987654321], [40], [342789], [False], [41], [1000000000001], [1000001], [True], [987654320], [10], [129], [95], [39], [9], [38], [342790], [94], [987654322], [987654321097], [999999999998], [1000000000002], [1000002], [127], [1234567890122], [987654323], [1000003], [55], [52], [56], [567989], [1000000000003], [1000000000004], [567987], [1000004], [567986], [999999999997], [1234567890124], [1000005], [342787], [7], [11], [54], [999999], [96], [567985], [1234567890125], [6], [57], [987654321095], [342791], [93], [999998], [1000006], [342786], [92], [33], [97], [1234567890126], [36], [987654321096], [37], [53], [35], [1000007], [12], [1000000000005], [987654319], [999999999996], [3], [130], [22], [567988], [987654318], [100], [98], [1000000000006], [131], [67], [132], [987654317], [42], [101], [987654321094], [77], [4], [567991], [342792], [987654321099], [1234567890121], [99], [58], [1000000000007], [342785], [1000000000008], [51], [50], [1000000000009], [133], [21]]
results = [1, 8, 32, 1, 2, 8, 128, 1048576, 524288, 1048576, 1099511627776, 1099511627776, 1099511627776, 2199023255552, 1073741824, 64, 524288, 1, 64, 1099511627776, 1048576, True, 1073741824, 16, 256, 128, 64, 16, 64, 524288, 128, 1073741824, 1099511627776, 1099511627776, 1099511627776, 1048576, 128, 2199023255552, 1073741824, 1048576, 64, 64, 64, 1048576, 1099511627776, 1099511627776, 1048576, 1048576, 1048576, 1099511627776, 2199023255552, 1048576, 524288, 8, 16, 64, 1048576, 128, 1048576, 2199023255552, 8, 64, 1099511627776, 524288, 128, 1048576, 1048576, 524288, 128, 64, 128, 2199023255552, 64, 1099511627776, 64, 64, 64, 1048576, 16, 1099511627776, 1073741824, 1099511627776, 4, 256, 32, 1048576, 1073741824, 128, 128, 1099511627776, 256, 128, 256, 1073741824, 64, 128, 1099511627776, 128, 4, 1048576, 524288, 1099511627776, 2199023255552, 128, 64, 1099511627776, 524288, 1099511627776, 64, 64, 1099511627776, 256, 32]

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
        func_name = "next_power_of_2"
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
        for test_case in ['assert next_power_of_2(0) == 1', 'assert next_power_of_2(5) == 8', 'assert next_power_of_2(17) == 32']:
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
