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
inputs = [[[1, 2, 4]], [[1, 2, 1, 2]], [[1, 7]], [[4, 3, 2, 1, 9, 10, 7]], [[0, -1, 5, 10, -3, 2, 8, -6, 4]], [[-10, -20, -30, -40, -50, -60]], [[-5, -3, -2, -1, -4, -9, -6, -7, -8]], [[]], [[71, -68, 32, -50, -6, 70, -24, 86, -30]], [[0, -1, 5, 10, -3, 2, 8, 9, -6, 4]], [[-10, -20, -3, -40, -50, -60]], [[4, 3, 2, 1, 9, 10, 7, 3]], [[-5, -3, -2, -1, -4, -6, -7, -8]], [[-5, -2, -2, -1, -4, -6, -7, -8, -5]], [[4, 3, 2, 1, 9, 10, 10, 7, 2]], [[0, 5, 10, -3, 2, 8, 9, -6, 4]], [[0, -1, 5, 10, -4, 2, 8, -6, 4, -6]], [[0, 5, 10, -3, 2, 8, 9, -6, 4, 2]], [[-2, 0, 21, 70, -5, -9, -7, -60]], [[71, -2, 0, 21, 70, -5, -9, -6, -60, 70]], [[0, 9, 5, 10, -3, 2, 8, 9, -6, 4, 2]], [[0, 9, 5, 10, 2, 8, 9, -6, 4, 2, 2]], [[0, -1, 5, 10, -3, 2, 8, -6]], [[71, 21, 0, 21, 70, -5, -9, -6, -60, 70]], [[4, 3, 2, 1, 9, 10, 7, 4]], [[0, 9, 5, 10, 2, 8, 9, -6, 4, 2, 2, 9, -6]], [[0, 9, 5, 10, 2, 8, 9, 4, 2, 2]], [[-2, 0, 21, -9, -7, -60]], [[-5, -3, -2, -1, -3, -7, -6, -7, -8, -1]], [[4, 3, 2, 1, 9, -4, 10, 7, 2, 2]], [[0, 5, 10, -3, 2, 8, 10, -6, 4, 2, 2]], [[0, 5, -3, 2, 8, 10, -6, 4, 2, 2]], [[-5, -3, -7, -1, -3, -7, -6, -7, -8, -1]], [[-20, -3, -40, -50, -60]], [[False, True, False]], [[0, 5, 10, -3, 2, 8, 10, -6, 4, 2, 2, 8]], [[-5, -3, -2, -1, -3, -7, -6, -7, -8, -1, -7]], [[4, 3, 2, 9, 10, 7, 3]], [[-5, -2, 2, -2, -1, -4, -6, 70, -7, -8, -5]], [[8, 4, 3, 2, 1, 9, 10, 7, 4]], [[0, 5, 10, -3, 2, 8, 9, -7, 4, 2]], [[-5, -2, 2, -1, -4, -6, 70, -7, -24, -5, -2]], [[8, 4, 3, 2, 1, 9, 10, 7, 8, 4]], [[-60, 3, 2, 1, 9, 10, 7, 3]], [[-5, -3, -7, -1, -3, -7, -6, -7, -8, -1, -7]], [[0, 5, 10, -3, 2, 8, 10, -6, 4, 2, 2, 8, 5]], [[4, 3, -2, 2, 1, 9, 10, 7, 3]], [[True, True]], [[0, 9, 5, 10, 9, 4, 2, 2]], [[-5, -3, -2, -1, -3, 21, -7, -6, -7, -8, -1, -2, -3]], [[0, -1, 5, -3, 2, 8, 9, -6, 4]], [[-5, -3, -7, -1, -3, 3, -7, -6, -7, -8, -1, -7]], [[0, -1, 5, 10, 2, 8, -6, 4, -6, -6]], [[-5, -3, -7, 0, -7, -6, -7, -8, -1, -7]], [[0, 5, 4, 10, -3, 2, 8, 9, -6, 4, 2]], [[8, 4, 3, 2, 1, 9, 7, -60]], [[-5, -3, -1, -3, -7, -6, -7, -8, -1]], [[8, 4, 3, 2, 1, 8, 10, 7, 3]], [[0, 9, 5, 10, 2, 8, 9, -6, 4, 2, -1]], [[False]], [[-5, -3, -3, -1, -3, 21, -7, -6, -7, -8, -1, -2, -3, -7]], [[0, 5, 10, -3, 2, 8, 9, -7, 4, 2, 4, 0]], [[False, True, True, True, True]], [[0, 9, -1, 5, 10, -3, 2, 8, -6, 4]], [[0, -1, 5, 10, 2, 8, 4, -6, -6]], [[0, 9, 5, 10, 2, 8, 9, -6, 4, 2, -1, 5]], [[-5, -3, -2, -1, -3, -7, -4, -6, -7, -8, -1]], [[-5, -3, -2, -1, -3, -7, -6, -7, 86, -1]], [[4, 3, 2, 5, 9, 10, -20, 4]], [[-60, 3, 2, 1, 9, 10, -2, 3]], [[0, 9, 5, -5, 10, -3, 2, 8, 9, -6, 4, 2]], [[4, 3, 1, 9, 7, 3]], [[71, 86, -68, 32, -50, 70, -6, 70, -24, 86, 10, -24]], [[-5, 8, -3, -7, -1, -3, -7, -6, -7, -8, -1, -7]], [[0, 9, 5, 10, -3, 2, 8, 9, -6, 4, 2, 0]], [[-5, -3, -2, -1, -3, -7, -6, -7, 86, 87, -1]], [[4, -50, 2, 1, 9, 10, 7, 9, 7]], [[0, 9, 5, 10, -1, 2, 8, 9, -6, 4, 2, -1]], [[-10, -20, -30, -50, -60]], [[-2, 1, 0, 21, -9, -7, -60, 1]], [[0, 9, 5, 10, 2, 1, 8, 9, 4, 2, 2]], [[False, True, True, True]], [[8, 4, 3, 2, 1, 32, 9, 10, 7, 4, 7]], [[-20, -3, -40, -50, -40, -60]], [[-5, -3, -7, 0, -7, -6, -7, -6, -8, -1, -7]], [[0, 5, 1, 10, -3, 2, 8, 10, -6, 4, 2, 2, 8, 5, 2]], [[0, 9, 5, 9, 4, 2, 3, -3, 2]], [[4, 3, 2, 1, 9, 10, -2, 3]], [[-5, 86, -3, -2, -1, -3, -7, -6, -7, -4, 86, -1]], [[-20, -4, -40, -50, -60]], [[-2, 0, 21, -9, -7, -60, 1]], [[87, 0, 9, -1, 5, 10, -3, 2, 8, -6, 4]], [[0, 9, 5, 10, 70, 2, 8, 9, -6, 4, 2, 2, 2]], [[-5, -3, -7, 0, -7, -6, -7, -7, 0, -8, -1, -7]], [[False, True, True, False, True]], [[-5, 21, 8, -3, -7, -1, -3, -7, -6, -7, -8, -1, -7]], [[8, 4, 3, 2, 1, 32, 9, 10, 4, 7]], [[0, 5, 10, -3, 2, 8, 10, -6, 4, 4, 2, 3, 8, -60, 5, 2]], [[71, 0, 70, -5, -9, -6, -60, 70]], [[-5, -3, -1, -2, -1, -4, -6, -7, -8]], [[0, 5, 10, -3, 2, 8, 9, 9, -6, 4, 2]], [[0, 9, 5, 10, 2, 1, 8, 9, 4, -9, 2, 9]], [[0, 5, -2, 5, -3, 2, 8, 9, -6, 4]], [[8, 4, 3, 2, 1, 9, 7, -60, 2]], [[0, 9, 5, 10, 2, 3, 8, 9, -6, 4, 2, -1]], [[71, 5, 21, 70, -5, -9, -6, -60, 70, -5]], [[-5, -3, -2, -1, -3, -2, -4, -6, -7, -8, -1, -8]], [[4, -50, 2, 1, 9, 9, 7, 9, 7]]]
results = [14, 15, 8, 218, 212, -980, -405, 0, 599, 362, -818, 306, -244, -365, 491, 307, 207, 373, 461, 1218, 558, 654, 158, 1425, 310, 944, 633, -149, -485, 412, 494, 299, -545, -652, 2, 621, -668, 256, 660, 436, 361, 532, 606, 50, -738, 811, 348, 2, 356, -392, 204, -749, 221, -569, 504, 7, -405, 419, 636, 0, -557, 554, 16, 334, 255, 752, -636, 361, 161, -13, 551, 131, 3496, -762, 658, 1564, 75, 692, -640, -360, 750, 8, 1258, -995, -778, 1160, 330, 243, 1239, -656, -324, 956, 2481, -894, 12, -610, 952, 144, 580, -307, 596, 776, 262, -143, 773, 1223, -722, 63]

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
        func_name = "odd_length_sum"
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
        for test_case in ['assert odd_length_sum([1,2,4]) == 14', 'assert odd_length_sum([1,2,1,2]) == 15', 'assert odd_length_sum([1,7]) == 8']:
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
