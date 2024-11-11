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
inputs = [[5], [6], [7], [10], [11], [True], [False], [12], [13], [9], [14], [8], [15], [16], [73], [17], [74], [75], [76], [29], [78], [18], [77], [19], [72], [28], [30], [55], [56], [3], [2], [57], [79], [4], [20], [31], [1], [71], [84], [54], [95], [85], [53], [39], [58], [80], [70], [59], [52], [32], [40], [38], [83], [82], [26], [60], [61], [62], [37], [33], [86], [81], [66], [41], [36], [96], [27], [35], [87], [69], [88], [97], [68], [65], [21], [34], [64], [94], [89], [67], [42], [98], [100], [22], [99], [90], [91], [43], [101], [0], [92], [63], [25], [23], [44], [51], [93], [24], [102], [50], [45]]
results = [35.0, 56.0, 84.0, 220.0, 286.0, 1.0, 0.0, 364.0, 455.0, 165.0, 560.0, 120.0, 680.0, 816.0, 67525.0, 969.0, 70300.0, 73150.0, 76076.0, 4495.0, 82160.0, 1140.0, 79079.0, 1330.0, 64824.0, 4060.0, 4960.0, 29260.0, 30856.0, 10.0, 4.0, 32509.0, 85320.0, 20.0, 1540.0, 5456.0, 1.0, 62196.0, 102340.0, 27720.0, 147440.0, 105995.0, 26235.0, 10660.0, 34220.0, 88560.0, 59640.0, 35990.0, 24804.0, 5984.0, 11480.0, 9880.0, 98770.0, 95284.0, 3276.0, 37820.0, 39711.0, 41664.0, 9139.0, 6545.0, 109736.0, 91881.0, 50116.0, 12341.0, 8436.0, 152096.0, 3654.0, 7770.0, 113564.0, 57155.0, 117480.0, 156849.0, 54740.0, 47905.0, 1771.0, 7140.0, 45760.0, 142880.0, 121485.0, 52394.0, 13244.0, 161700.0, 171700.0, 2024.0, 166650.0, 125580.0, 129766.0, 14190.0, 176851.0, 0.0, 134044.0, 43680.0, 2925.0, 2300.0, 15180.0, 23426.0, 138415.0, 2600.0, 182104.0, 22100.0, 16215.0]

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
        func_name = "tetrahedral_number"
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
        for test_case in ['assert tetrahedral_number(5) == 35', 'assert tetrahedral_number(6) == 56', 'assert tetrahedral_number(7) == 84']:
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
