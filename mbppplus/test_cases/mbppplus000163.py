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
inputs = [[10], [12], [15], [125], [255], [1000], [98765], [1], [3], [5], [7], [9], [0], [8], [True], [124], [1001], [98764], [92], [2], [False], [254], [127], [128], [6], [123], [98766], [4], [122], [1002], [126], [1003], [129], [130], [1004], [67], [253], [68], [69], [70], [98767], [98768], [121], [11], [31], [1005], [120], [91], [252], [131], [132], [66], [119], [999], [28], [98769], [251], [89], [256], [29], [98770], [30], [32], [117], [257], [118], [33], [46], [90], [47], [250], [87], [94], [133], [116], [49], [27], [50], [93], [35], [34], [258], [71], [72], [1006], [86], [115], [36], [21], [51], [48], [114], [73], [259], [98763], [98771], [95], [113], [52], [26], [53], [260], [261], [25], [249], [13], [24], [262], [88], [23]]
results = [14, 14, 15, 127, 255, 1016, 115149, 1, 3, 7, 7, 13, 0, 12, True, 126, 1017, 115148, 124, 3, False, 255, 127, 192, 7, 127, 115150, 6, 126, 1018, 127, 1019, 193, 194, 1020, 99, 255, 100, 101, 102, 115151, 115152, 125, 15, 31, 1021, 124, 123, 254, 195, 196, 98, 127, 1015, 30, 115153, 255, 121, 384, 31, 115154, 31, 48, 125, 385, 126, 49, 62, 122, 63, 254, 119, 126, 197, 124, 57, 31, 58, 125, 51, 50, 386, 103, 104, 1022, 118, 123, 52, 29, 59, 56, 122, 105, 387, 115147, 115155, 127, 121, 60, 30, 61, 388, 389, 29, 253, 15, 28, 390, 120, 31]

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
        func_name = "set_left_most_unset_bit"
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
        for test_case in ['assert set_left_most_unset_bit(10) == 14', 'assert set_left_most_unset_bit(12) == 14', 'assert set_left_most_unset_bit(15) == 15']:
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
