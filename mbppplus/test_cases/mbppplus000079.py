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
inputs = [[10], [5], [7], [100], [1000], [10000], [9999], [9998], [10001], [99], [9997], [1001], [10002], [9996], [101], [True], [90], [98], [97], [1002], [10003], [102], [1003], [62], [1004], [False], [96], [103], [9995], [104], [63], [64], [91], [61], [1005], [89], [1006], [60], [105], [66], [59], [65], [87], [88], [10004], [9994], [58], [106], [1007], [22], [92], [10005], [10006], [86], [93], [67], [57], [23], [9993], [68], [85], [39], [21], [84], [94], [40], [83], [999], [1008], [20], [41], [42], [10007], [38], [56], [6], [1009], [107], [69], [82], [55], [9992], [24], [12], [8], [11], [108], [95], [25], [1], [9], [19], [36], [0], [81], [52], [51], [109], [10008], [110], [1010], [10009], [43]]
results = [190, 45, 91, 19900, 1999000, 199990000, 199950003, 199910010, 200030001, 19503, 199870021, 2003001, 200070006, 199830036, 20301, 1, 16110, 19110, 18721, 2007006, 200110015, 20706, 2011015, 7626, 2015028, 0, 18336, 21115, 199790055, 21528, 7875, 8128, 16471, 7381, 2019045, 15753, 2023066, 7140, 21945, 8646, 6903, 8385, 15051, 15400, 200150028, 199750078, 6670, 22366, 2027091, 946, 16836, 200190045, 200230066, 14706, 17205, 8911, 6441, 1035, 199710105, 9180, 14365, 3003, 861, 14028, 17578, 3160, 13695, 1995003, 2031120, 780, 3321, 3486, 200270091, 2850, 6216, 66, 2035153, 22791, 9453, 13366, 5995, 199670136, 1128, 276, 120, 231, 23220, 17955, 1225, 1, 153, 703, 2556, 0, 13041, 5356, 5151, 23653, 200310120, 24090, 2039190, 200350153, 3655]

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
        func_name = "hexagonal_num"
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
        for test_case in ['assert hexagonal_num(10) == 190', 'assert hexagonal_num(5) == 45', 'assert hexagonal_num(7) == 91']:
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
