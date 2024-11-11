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
inputs = [[[(1, 3), (5, 6, 7), (2, 6)]], [[(2, 4), (6, 7, 8), (3, 7)]], [[(3, 5), (7, 8, 9), (4, 8)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(3, 5, -2, -4, 6), (-1, 2, -3)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0, 0)]], [[(10, -5), (-3, -8, 2), (7, -2)]], [[(10, 100, 1000), (10000, 100000, 1000000), (-1, -10, -100, -1000)]], [[(1, 2, 3), (4, 5, 6), (7, 8, 9)]], [[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]], [[(10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120), (130, 140, 150), (160, 170, 180)]], [[]], [[(1000000, 2000000, 3000000)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(10, -5), (7, -2)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(180, 7, -2)]], [[(10, -5, -5), (10, -5), (7, -2)]], [[(1, 2, 3, 3, 5, 6, 7, 8, 9, 10)]], [[(10, -5, -5), (10, -4), (7, -2)]], [[(1000000, 1999999), (1000000, 2000000, 3000000)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0, 1, 0)]], [[(10, -4), (7, -2, 7)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0)]], [[(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)]], [[(10, -4), (7, -2, 7), (7, -2, 7)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(1, 2, 3), (4, 5, 6), (7, 8, 9, 9)]], [[(7, 9, 9), (1, 2, 3, 1), (7, 8, 9, 9)]], [[(10, -5, -5), (10, -5), (7, -2), (10, -5)]], [[(1, 2, 3), (4, 5, 6), (170, 7, 8, 9), (7, 8, 140, 9)]], [[(10, -5)]], [[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (18, 12), (13, 14), (15, 16), (17, 18), (19, 20)]], [[(3, 5, -2, -4, 6, -4), (3, 5, -2, -4, 6), (-1, 2, -3)]], [[(1, 2, 3, 1), (7, 9, 9, 9), (7, 8, 9, 9)]], [[(1, 2, 3), (7, 80, 8, 9), (5, 6), (7, 8, 9)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)]], [[(10, 20, 30), (40, 50, 60), (70, 80, 90), (70, 80, 90), (100, 110, 120), (130, 140, 150), (160, 170, 180)]], [[(10, -5), (7, 140), (7, -2), (10, -5)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0)]], [[(7, 9, 9, 9, 9), (7, 8, 9, 9)]], [[(10, 20, 30), (40, 50, 60), (70, 80, 90), (70, 80, 90), (100, 110, 119), (130, 140, 150), (160, 170, 180, 160)]], [[(10, -4), (7, -2, 7), (-2, 7), (-2, 7)]], [[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (18, 17, 18), (19, 20)]], [[(10, -5, -5), (9, -6, -5), (7, -2)]], [[(10, -5, -5), (10, -4), (-1, 7, 8, -2), (-1, 7, 8, -2)]], [[(1, 2, 3), (170, 7, 8, 9), (7, 8, 140, 9)]], [[(160, 2000001, 1000000, 2000000, 3000000), (2000001, 1000000, 120, 3000000), (2000001, 1000000, 2000000, 3000000), (2000000, 3000000)]], [[(0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(10, -5), (7, -2), (7, -2)]], [[(10, -5, -5), (10, -5), (7, -2, 6, -2), (7, -2, -2), (10, -5), (10, -5, -5), (10, -5, -5)]], [[(3, 5, -2, -4, 6), (-1, 3000000, -3)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0, 0)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 6), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(10, -5, -5), (10, -5), (7, -2), (10, -5), (-5, -5)]], [[(3, 5, -2, -4, 6), (3, 5, -2, -4, 6)]], [[(1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(10, -5), (7, 140), (10, -5)]], [[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (18, 17, 18), (19, 20), (3, 4)]], [[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 11), (13, 14), (15, 16), (17, 18), (19, 20), (11,)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4)]], [[(-1, 7, 8, -2), (-1, 7, 8, -2)]], [[(1, 2, 3), (1, 3), (4, 5, 6), (7, 8, 9, 9)]], [[(0, 0, 0), (0, 0, 20, 0, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0)]], [[(1, 2, 3, 4, 5, 6, 8, 9, 10), (2, 1, 2, 3, 4, 5, 6, 8, 9, 10), (1, 2, 3, 4, 5, 6, 8, 9, 10)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10, 9), (1, 3, 4, 5, 6, 7, 8, 9, 10, 9), (1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4)]], [[(10, -5, -5), (9, -6, -5), (9, -7, -5), (7, -2)]], [[(1, 2, 3), (7, 8, 140, 9), (7, 8, 140, 9)]], [[(1, 2, 3), (7, 80, 8, 9), (100000, 6)]], [[(10, -4), (10,), (7, -2, 7)]], [[(10, 20, 30), (40, 50, 60), (160, 170), (70, 80, 90), (100, 110, 120), (130, 140, 150), (160, 170, 180)]], [[(1, 2, 3, 4, 6, 7, 8, 9, 10, 4), (1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4)]], [[(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0)]], [[(3, 5, -2, -4, 6)]], [[(3, 5, -2, -4, 6, -4)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 18, 9, 10)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10, 9), (1, 3, 4, 5, 6, 7, 8, 9, 10, 9), (1, 3, 4, 5, 160, 6, 7, 8, 9, 40, 10), (1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4), (1, 3, 4, 5, 6, 7, 8, 9, 10, 9)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)]], [[(0, 0, 0, 0), (0, 0, 0, 0, 0)]], [[(3, 5, -2, -4, 6, 3), (3, 5, -4, 6), (3, 5, -2, -4, 6)]], [[(1, 2, 3), (1, 3), (4, 5, 6), (3,), (7, 8, 9, 9), (4, 5, 6)]], [[(10, -4), (10,), (7, -2, 7), (10,)]], [[(10, -4), (7, -2, 7), (7, 7), (10, -4)]], [[(180, -2)]], [[(180, -2), (180, -2)]], [[(0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)]], [[(0, 0, 0), (0, 20, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0)]], [[(10, -5, -5), (10, -5), (9, 10, -5, -5), (7, -2), (10, -5)]], [[(10, -5, -5), (10, -4), (-1, 7, 8, -2)]], [[(7, 9, 9), (1, 2, 3, 1)]], [[(1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10)]], [[(1, 2, 3, 1), (7, 9, 9, 9, 9), (7, 8, 9, 9)]], [[(10, -5, -5), (9, -6, -5), (9, -7, -5), (6, -2), (9, -6, -5)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0)]], [[(4, 5, 6), (7, 8, 9, 9)]], [[(-1, 7, 8, -2), (-1, 13, 7, 8, -2), (-1, 7, 8, -2)]], [[(1, 2, 3)]], [[(-1, 7, 8, -2), (-1, 13, 7, 8, -2), (-1, 7, 8, -2, 8), (-1, 7, 8, -2)]], [[(0, 0, 0), (0, 0, 20, 0, 0), (0, 0, 0, 40, 0), (0, 0, 20, 0), (0, 0, 0, 0, 0, 0)]], [[(0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0)]], [[(3, 5, -2, -4, 6, -4), (3, 5, -2, -4, 6), (-1, 2, -3), (3, 5, -2, -4, 6, -4), (3, 5, -2, -4, 6)]], [[(10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120), (130, 140, 150)]], [[(10, -4), (), (7, -2, 7), (10,)]], [[(0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0)]], [[(1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 18, 9, 10)]], [[(0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0)]], [[(0, 0, 0, 0, 0), (0, 0, 0), (0, 0, 0, 0), (0, 0, 180, 20, 0), (0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0)]], [[(180, -2), (180, -2), (180, -2)]], [[(1, 2, 3, 4, 5, 6, 8, 8, 9, 10, 4)]]]
results = [30, 37, 44, 55, 6, 0, 1, 1109999, 45, 210, 1710, 0, 6000000, 165, 10, 108, 185, 10, 54, 11, 8999999, 1, 18, 20, 20, 30, 120, 54, 65, 15, 379, 5, 217, 10, 74, 145, 110, 0, 1950, 162, 0, 76, 2109, 28, 228, 3, 30, 364, 27000283, 0, 163, 15, 22, 3000004, 20, 161, 5, 16, 184, 167, 157, 235, 220, 112, 24, 58, 40, 146, 295, 0, 334, 100116, 28, 2040, 166, 20, 8, 4, 173, 610, 269, 175, 0, 29, 76, 38, 38, 178, 356, 0, 40, 24, 18, 32, 249, 83, -3, 20, 48, 49, 6, 69, 80, 0, 22, 1200, 28, 0, 171, 0, 200, 534, 60]

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
        func_name = "cummulative_sum"
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
        for test_case in ['assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30', 'assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37', 'assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44']:
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