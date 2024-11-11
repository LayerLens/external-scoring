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
inputs = [[[2, 4, -6, -9, 11, -12, 14, -5, 17]], [[10, 15, -14, 13, -18, 12, -20]], [[19, -65, 57, 39, 152, -639, 121, 44, 90, -190]], [[]], [[1, 2, 3, 4, 5]], [[-1, -2, -3, -4, -5]], [[10, 15, 14, 13, 18, 12, 20]], [[3, -5, 1, -7, 2, -8, 4, -6]], [[-10]], [[3, -5, 1, -7, 2.5, -8.9, 4, -6]], [[-10, 15, -14.2, 13, -18, 12, -20.7]], [[3, -5, 1, -7, 2.5, -8.9, 4, -6, 1]], [[2, 3, 4, 5]], [[2, 3, -7, 6]], [[3, 2, -5, 1, -7, 2.5, 4, -6, 1]], [[5, 2, 3, 4, 5]], [[10, 15, 14, 13, 18, 12, 20, 20]], [[10, -1, -2, -3, -4, -5]], [[20, 2, 3, 4, 5]], [[3, -5, 1, -7, 2.5, -8.9, 4, -6, 1, 1]], [[10, 15, 14, 13, 13, 18, 12, 20, 20, 15, 18]], [[10, 15, 14, 13, 18, 12, 20, 14, 20]], [[10, -1, -2, -4, -5]], [[-6, 3, -5, 1, -7, 2, -8, 4, 2, -6]], [[3, 2, -5, 1, -7, 4, -6, 1]], [[1, 2, 3, 1, 5, 1]], [[1, 2, 4, 5, 2, 2]], [[0, 2, -5, 1, -7, 4, -6, 1]], [[1, 2, 3, 0, 1, 5, 1]], [[10, 14, 15, 14, 13, 18, 12, 20, 20]], [[10, 15, 14, 1, 13, 18, 12, 20, 14, 20]], [[5, 2, 20, 4, 4, 6]], [[3, 2, -5, 1, -7, 2.5, 4, 10, 1]], [[1, -8, 2, -10, 4, 5, 2, 2]], [[3, -5, 1, -7, -2, 2.5, -8.9, 4, -6, 1, 1]], [[2, 10, 14, 15, 14, 13, 18, 12, 20, 20]], [[-6, 3, -5, 1, -7, 2, -8, 2, 2, -6]], [[0, 2, -5, 1, -7, 4, 1]], [[0, 2, -5, 1, -7, 1, 4, 1, -7]], [[3, -5, 0, -7, 2.5, -8.9, 4, -6]], [[1, 2, 3, 4, 2, 5, 2, 3]], [[-7, 5, 3, -5, 1, -7, 2, -8, 2, 2, -6]], [[-6, 3, -5, 1, -7, -8, 2, -4, 2, -6]], [[0, 2, -5, 1, -5, -7, 1, 4, 1, -7]], [[0, 2, -5, 1, -5, -7, 1, 4, -4, 1, -7]], [[1, 2, 3, 4, 2, 5, 3]], [[10, -1, -2, -3, -4, 9, -5, -4]], [[5, 2, 20, 4, 4]], [[10, -1, -2, -3, -4, 9, -4]], [[0, 2, -5, 1, -7, 4, 1, 4, 1, -7]], [[1, 2, 3, 4, 4]], [[-10, 15, -14.2, 13, -18, 12, -20.7, 12]], [[10, 14, 15, 14, 13, 21, 18, 12, 20, 20]], [[-6, 3, -5, 1, -7, 2, -8, 4, 1, -6]], [[1, 21, 2, 3, 3, 1, 1, 1]], [[3, -5, 0, -7, 2.5, -8.9, 4, -6, 0]], [[-1, -2, -3, -4, -5, -1]], [[10, 14, -5, 15, 14, 13, 21, 18, 12, 20, 20, 14]], [[-10, -10]], [[-10, 15, 16, -14.2, 13, -18, 12, -20.7]], [[-6, 3, -5, -7, 2, -8, 4, 2, -6]], [[-1, -2, -3, -4, -5, -4]], [[3, -5, 1, -7, 2, 16, -8, 4, -6]], [[3, 2, -5, 1, -7, 2.5, 4, -6, 1, 2]], [[3, -5, -6, 1, -7, 2, 16, 0, 4, -6, 1]], [[-1, -2, -3, -4, -5, -5]], [[3, -5, 0, -7, 2.5, -8.9, 4, -6, 0, 4]], [[3, -5, 0, -7, 2.5, -8.686091893944287, 4, -6, 4]], [[10, 15, 14, 13, 14, 12, 20, 10]], [[1, 2, 3, 3, 3, 4, 4]], [[-6, 3, -5, 1, -7, 2, -8, 4, 1, -6, -7]], [[10, -1, -2, -3, -4, 9, -1, -1, -5]], [[10, -2, -1, -2, -3, -4, 9, -1, -1, -5]], [[10, -1, -2, 16, -4, 9, -4]], [[3, -9.674408997541613, -5, 1, -7, 2.5, -8.9, 4, -6, 1, 1]], [[10, -1, -2, -3, -4, -5, 10]], [[3, -5, 1, -7, 2, 16, -8, 20, -6]], [[10, 15, 14, 13, 13, 18, 12, 20, 20, 15, 18, 12]], [[-7, 3, -7, 6]], [[10, 15, 1, 13, 18, 12, 20, 14, 20]], [[3, -5, 1, -7, 2, 16, 4, -6]], [[10, -1, -2, -3, -4, -5, -1]], [[10, -1, -2, -3, -4, 5, -4]], [[2, 3, 4, 5, 2]], [[3, 2, -5, 1, -7, 2.5, 20, 4, 10, 1]], [[10, -1, -2, 16, -4, 9]], [[1, -6, 2, 3, 4, 2, 5, 3]], [[2, 10, 15, 14, 13, 18, 12, 20, 20]], [[-8, 2, -4, -10, 4, 5, 2]], [[10, 15, 14, 1, 13, 18, 13, 12, 20, 14, 19, 20]], [[-1, -2, -5, -3, -4, -5, -1]], [[10, -2, -2, -3, -4, 9, -1, -1]], [[0, 2, -5, 1, -5, -7, 1, 4, -4, 1, -7, 1]], [[10, 15, 13, 18, 12, 20, 20]], [[1, 2, 3, 4, 2, 5, 4]], [[1, 2, 3, 4, 2, 5, 2, 3, 5, 5]], [[1, 2, 3, 4, 2, 5, 4, 2, 2]], [[-18, 2, 3, 1, 5, 1]], [[2, 9, 15, 21, 18, 12, 20, 20]], [[3, 2, 1, -7, 2.5, 4, -6, 1, 1]], [[1, 21, 3, 3, 1, 1, 1]], [[2, 3, 5, 2]], [[2, 5, 3, 5, 2]], [[-1, -3, -4, -5]], [[10, 14, 15, 14, 13, 21, 18, 12, 20, 20, 14]], [[-2, 16, -3, -4, -5]], [[-10, 15, 16, -14.2, 13, -18, 12, -20.7, -18]], [[5, 2, 20, 4, 4, 2]], [[1, 2, 4, 3, 5, 2, 3]], [[3, 2, -5, 1, -7, 4, -6, 1, -6]], [[0, 2, -4, -5, 1, -7, 4, 1, 4, 1, -7]]]
results = [-32, -52, -894, 0, 0, -15, 0, -26, -10, -26.9, -62.900000000000006, -26.9, 0, -7, -18, 0, 0, -15, 0, -26.9, 0, 0, -12, -32, -18, 0, 0, -18, 0, 0, 0, 0, -12, -18, -28.9, 0, -32, -12, -19, -26.9, 0, -33, -36, -24, -28, 0, -19, 0, -14, -19, 0, -62.900000000000006, 0, -32, 0, -26.9, -16, -5, -20, -62.900000000000006, -32, -19, -26, -18, -24, -20, -26.9, -26.686091893944287, 0, 0, -39, -17, -19, -11, -36.57440899754161, -15, -26, 0, -14, 0, -18, -16, -14, 0, -12, -7, -6, 0, -22, 0, -21, -13, -28, 0, 0, 0, 0, -18, 0, -13, 0, 0, 0, -13, 0, -14, -80.9, 0, 0, -24, -23]

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
        func_name = "sum_negativenum"
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
        for test_case in ['assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32', 'assert sum_negativenum([10,15,-14,13,-18,12,-20])==-52', 'assert sum_negativenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==-894']:
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
