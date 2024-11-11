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
inputs = [[10], [20], [30], [999999999], [1000000000], [1000000001], [False], [True], [1000000002], [999999998], [49], [48], [1000000003], [999999997], [1000000004], [50], [999999996], [1000000005], [999999995], [58], [57], [59], [47], [51], [44], [46], [52], [53], [43], [89], [42], [60], [90], [1000000006], [45], [61], [91], [1000000007], [999999994], [62], [92], [41], [1000000008], [54], [56], [93], [1000000009], [94], [82], [95], [55], [96], [88], [81], [999999993], [63], [80], [1000000010], [97], [83], [40], [1000000011], [999999992], [24], [99], [23], [39], [22], [84], [999999991], [98], [66], [25], [87], [85], [86], [67], [19], [68], [79], [999999990], [64], [1000000012], [69], [70], [78], [26], [72], [999999989], [21], [38], [71], [999999988], [37], [999999987], [73], [65], [28], [1000000013], [36], [18], [1000000014], [15], [27]]
results = [10, 30, 30, 1002105855, 1002105514, 1002105515, False, True, 1002105514, 1002105854, 59, 58, 1002105515, 1002105855, 1002105518, 58, 1002105854, 1002105519, 1002105851, 58, 59, 59, 47, 59, 46, 46, 62, 63, 43, 123, 42, 62, 122, 1002105518, 47, 63, 123, 1002105519, 1002105850, 62, 126, 43, 1002105514, 62, 58, 127, 1002105515, 126, 122, 127, 63, 106, 122, 123, 1002105851, 63, 122, 1002105514, 107, 123, 42, 1002105515, 1002105850, 26, 107, 31, 47, 30, 126, 1002105855, 106, 106, 27, 127, 127, 126, 107, 27, 110, 111, 1002105854, 106, 1002105518, 111, 110, 110, 26, 106, 1002105855, 31, 46, 111, 1002105854, 47, 1002105851, 107, 107, 30, 1002105519, 46, 26, 1002105518, 15, 27]

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
        func_name = "even_bit_set_number"
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
        for test_case in ['assert even_bit_set_number(10) == 10', 'assert even_bit_set_number(20) == 30', 'assert even_bit_set_number(30) == 30']:
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
