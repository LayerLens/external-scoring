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
inputs = [[[1, -2, -3, 0, 7, -8, -2]], [[6, -3, -10, 0, 2]], [[-2, -40, 0, -2, -3]], [[2, 3, 4, 5, 6]], [[-2, 4, -6, 8, 10, -12, 14, -16]], [[2, 4, 6, 8, 10]], [[-5, -2, -8, -9, -6, -4, -3]], [[-5, -10, -2, -8, -4]], [[-5, -2, -8, -9, -6, -4, -3, -8]], [[2, 4, 6, 8, 10, 6]], [[-10, -2, -8, -4]], [[-5, -10, -2, -8, 5, -4]], [[-2, -2, 4, -6, 8, 10, -12, -16, 8]], [[2, 4, 5, -10]], [[2, 6, 10]], [[-1, -8, -9, -6, -4, -3, -8]], [[-2, -2, 6, -6, 10, -12, -16, 8, 8]], [[-5, -2, -8, -9, -3]], [[-5, -10, -2, -8, 5, -1, -4, -5, -8]], [[-2, -5, -10, -2, -8, 5, -1, -4, -5, -8, -8, -5]], [[-2, -2, -17, 4, -6, 8, 10, -12, -16, 8, -12]], [[-2, -5, -10, -8, 5, -1, -4, -5, -8, -8, -5, -4]], [[-5, -1, -8, -9, -6, -4, -3, -8]], [[-10, -2, -8, 8, -4]], [[-5, -10, -2, -8, 5, -4, 5]], [[-1, -8, -9, -6, -4, -3, -8, -3]], [[-6, -1, -8, -9, -6, -4, -3, -8]], [[-5, -1, -8, -9, -4, -3, -8, -8]], [[-2, -5, -10, -2, -8, 5, -1, -4, -5, -8, -8, -5, -2]], [[2, 3, 4, 5, 6, 4]], [[-5, -10, -2, -8, 5]], [[-2, -1, -2, 4, -6, 8, 10, -12, -16, 8]], [[-10, -2, 8, -4]], [[-2, 4, 8, 10, -12, 6, 14, -16]], [[-2, -2, -6, 8, 10, -12, -16, 8, -6, -2, 10]], [[2, -10, 3, 4, 5, 6, -16]], [[-10, -2, -1, -8, 8, -4]], [[10, -2, 6, -8, 5, -4]], [[-2, -5, -10, -2, -8, 5, -1, -3, -4, -5, -8, -8, -5]], [[2, -10, 2, 4, 5, 6, -16, 5]], [[-5, -2, -8, -9, -6, -8]], [[-10, -2, -2, -8, 8, -4]], [[4, 2, 3, 4, 5, 6]], [[-5, -10, -3, -8, -4]], [[-5, -11, -10, -10, -2, -8, -4]], [[10, -2, 6, -8, 4, -4]], [[-6, -10, -2, 5, -4, 5]], [[-1, -8, -9, -6, -4, -12, 4, -8]], [[-2, -10, -2, -8, 5, -1, -3, -4, -5, -8, -8, -5]], [[-1, -8, -8, -9, -6, -4, -3, -8, -3, -9]], [[2, -8, 5, -10]], [[-2, -5, -10, -8, -1, -4, -5, -8, -8, -5, -4]], [[-11, 2, -8, 5, -10]], [[2, -10, 2, 4, 5, 6, -16, 5, 5]], [[-2, -5, -10, -2, -8, 5, -1, -4, -5, -5, -8]], [[-2, 4, -6, 8, 10, -12, 14, -16, -16]], [[-9, -2, -5, -10, -2, -8, 5, -10, -4, -5, -5, -8, -5]], [[-5, -10, -8, 6]], [[10, 6, -2, 6, -8, 4, -2, -2]], [[2, 7, -10, 2, 6, -16, 5]], [[-5, -2, -8, -9, -6, -4]], [[2, -16, 3, 4, 5, 6, 4, 4]], [[-1, -8, -9, -11, -6, -4, -12, 4, -8]], [[5, 2, 4, 5, 8, 10]], [[-2, -2, -6, 8, 10, -12, -16, -12, 8, -6, -2, 10]], [[2, 5, -10]], [[-5, -10, -3, -8, -10, -4]], [[-5, -11, -10, -2, -8, -4]], [[2, 3, -16, 4, 5, -12]], [[-6, -10, -2, 5, -4, 5, 5]], [[-5, -8, -9, -6]], [[-2, -2, 4, -6, 8, 10, -12, -13, -16, 8, -6]], [[-10, 2, 4, 5, 8, 10, 8]], [[-2, -5, -5, -2, 5, -1, -4, -5, -8, -8, -5, -2]], [[-5, -11, -10, -10, -2, -8, -4, -11]], [[10, 6, -2, 6, -8, 10, 4, -2, -2]], [[-2, -2, -11, 6, -6, 10, -12, -16, 8, 8]], [[-3, -9, -2, -5, -10, -2, -8, 5, -10, -4, -5, -5, -8, -5, -2]], [[-6, -1, -8, -9, -6, -4, -3, -8, -8, -6]], [[-8, 10, -2, 6, -8, 4, -4]], [[-2, 4, -4, -6, 8, 10, -12, 13, -16]], [[-8, 10, -2, 13, -8, 4, -4]], [[-5, -8, -9]], [[-10, -2, -8, -10]], [[-2, -4, -10, -2, -8, 5, -1, -4, -5, -8, -8, -5, -2, -10]], [[-2, -2, -6, 8, 10, -12, 8, -11, 8, -6, -2, 10]], [[-5, -8, -10, -4]], [[-10, -2, -1, -8, 8, -4, -10]], [[-2, 4, -6, 8, 10, -12, 14, -16, 10]], [[-1, -8, -9, -6, -2, -4, -3, -8, -8]], [[-2, -4, -10, -2, -8, 5, -1, -4, -5, -8, -8, -5, -2, -10, -10]], [[-2, -5, -2, 4, -6, 8, 10, -12, -16, 8]], [[2, 4, 5, -10, -10]], [[-6, -1, -8, -9, -6, -4, -3, -13, -8, -6]], [[-2, -5, -5, -2, -1, -4, -5, -8, -8, -5, -6, -2]], [[-2, -5, -10, -2, -8, 5, -1, -4, -5, -8, -8, -5, -10]], [[-5, -11, -10, -10, -17, -2, -8, -4]], [[-10, 8, -4]], [[2, 4, 5, -10, 5]], [[-1, -8, -8, -9, -6, 5, -3, -8, -3, -9]], [[-2, -1, -6, 8, 10, -12, -16, -12, 8, -6, -2, 10]], [[2, 5, -10, 5]], [[2, -10, -8, 3, 4, 5, 6, -16]], [[2, 4, -10]], [[-2, -5, -10, -2, -8, 5, -1, -4, -5, -8, -8, -5, -2, -5]], [[-5, -2, -8, -9, -6, 10, -3, -8]], [[-1, -8, -9, -6, 3, -4, -12, 4]], [[-2, -2, -3, -6, 8, -12, -16, 8, -6, -2, 10, -2]]]
results = [112, 180, 80, 720, 10321920, 3840, 17280, 800, 414720, 23040, 640, 4000, 5898240, 40, 120, 41472, 8847360, 720, 640000, 25600000, 1203240960, 51200000, 207360, 5120, 16000, 124416, 248832, 276480, 102400000, 2880, 4000, 11796480, 160, 5160960, 176947200, 115200, 1280, 4800, 153600000, 384000, 34560, 2560, 2880, 1200, 88000, 3840, 12000, 663552, 15360000, 8957952, 800, 10240000, 880, 1920000, 6400000, 82575360, 2880000000, 480, 92160, 134400, 17280, 5760, 7299072, 16000, 4246732800, 10, 48000, 35200, 23040, 60000, 2160, 460062720, 25600, 3200000, 3872000, 921600, 194641920, 17280000000, 11943936, 122880, 19169280, 266240, 72, 1600, 409600000, 973209600, 1600, 51200, 103219200, 663552, 8192000000, 58982400, 4000, 19408896, 7680000, 512000000, 5984000, 320, 40, 11197440, 2123366400, 10, 57600, 8, 256000000, 207360, 248832, 106168320]

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
        func_name = "max_subarray_product"
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
        for test_case in ['assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112', 'assert max_subarray_product([6, -3, -10, 0, 2]) == 180', 'assert max_subarray_product([-2, -40, 0, -2, -3]) == 80']:
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