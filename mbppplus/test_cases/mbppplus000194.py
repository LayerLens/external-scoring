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
inputs = [[5, 3, 2], [9, 8, 4], [2, 4, 6], [0, 0, 0], [0, 8, 4], [3, 3, 3], [8, 2, 3], [3, 0, 0], [4, 3, 3], [0, 2, 3], [0, 4, 0], [3, 2, 3], [8, 8, 3], [8, 1, 2], [1, 7, 2], [2, 3, 3], [1, 3, 2], [2, 3, 0], [8, 1, 8], [0, 7, 2], [1, 2, 2], [7, 9, 4], [6, 3, 3], [1, 7, 1], [3, 2, 2], [8, 3, 2], [3, 1, 8], [8, 3, 0], [8, 9, 1], [1, 0, 0], [6, 4, 3], [8, 6, 6], [2, 3, 2], [3, 1, 1], [8, 9, 3], [0, 7, 9], [8, 1, 1], [2, 1, 3], [4, 1, 2], [3, 9, 9], [2, 8, 2], [0, 1, 2], [0, 3, 0], [8, 9, 9], [1, 0, 1], [4, 4, 4], [8, 4, 4], [3, -1, -1], [3, 0, 6], [-1, 0, 3], [2, 2, 3], [1, 4, 0], [-1, -1, -1], [6, 3, 4], [0, 7, 0], [0, 9, 0], [9, 1, 2], [9, 0, 1], [2, 2, 2], [3, 9, 1], [3, 7, 3], [6, 2, 8], [1, 8, 1], [9, 6, 1], [0, 3, 8], [3, -2, -1], [1, 1, 1], [9, 4, -1], [8, 3, 7], [-1, 3, 2], [5, 2, 4], [9, 2, -1], [3, -1, 0], [-2, 1, 1], [-1, 1, 0], [9, 1, 1], [8, 6, 3], [3, 6, 3], [6, 8, 4], [8, 8, 7], [9, 9, 9], [3, 6, 0], [1, 1, 2], [0, 2, 7], [6, 7, 9], [0, 2, 2], [2, 2, 1], [3, 1, 4], [0, 1, 1], [5, 3, 3], [2, 0, 1], [0, 1, -1], [6, 6, 3], [9, -1, 2], [1, 6, 1], [6, 2, 9], [3, 3, -1], [3, -2, 4], [5, 0, 2], [8, 3, 3], [5, 1, 1], [9, 9, 3], [4, 2, 2], [7, 6, 6], [3, -2, 0]]
results = [-198, -2336, -130, 0, 4, -117, -157, -12, -157, 3, 0, -57, -2077, -62, -198, -77, -38, -80, -56, 2, -18, -2292, -237, -199, -58, -318, -16, -320, -2623, -4, -405, -1178, -78, -23, -2621, 9, -63, -13, -30, -975, -518, 2, 0, -2615, -3, -268, -540, -25, -6, 7, -37, -68, 7, -236, 0, 0, -70, -35, -38, -983, -597, -112, -259, -1331, 8, -61, -7, -613, -313, 42, -96, -181, -24, 17, 8, -71, -1181, -441, -1556, -2073, -2943, -444, -6, 7, -1191, 2, -39, -20, 1, -197, -7, -1, -885, -70, -147, -111, -121, -56, -18, -317, -39, -2949, -78, -1030, -60]

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
        func_name = "parabola_directrix"
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
        for test_case in ['assert parabola_directrix(5,3,2)==-198', 'assert parabola_directrix(9,8,4)==-2336', 'assert parabola_directrix(2,4,6)==-130']:
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
