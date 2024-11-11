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
inputs = [[(1, 2, 3), (2, 3, 4)], [(4, 5, 6), (3, 4, 5)], [(11, 12, 13), (10, 11, 12)], [(5, 10, 15, 20), (4, 8, 16, 25)], [(3, 7, 11, 15, 19), (2, 6, 10, 14, 18)], [(0, 1, 2, 3, 4, 5), (-1, 0, 1, 2, 3, 4)], [(), ()], [(1, 2, 3), (4, 5, 6)], [(0, 10, 20), (-1, 9, 21)], [(100, 200, 300), (99, 199, 299)], [(-1, -2, -3), (-4, -5, -6)], [(10, 20, 30, 40), (11, 19, 31, 39)], [(-10, -20, -30, -40), (-11, -19, -31, -39)], [(1, 2, 3), (3, 2, 1)], [(10, 20, 30, 40), (10, 19, 31, 39)], [(100, 200, 300), (100, 200, 299)], [(3, 7, 11, 15, 19), (2, 6, 10, 15, 18)], [(-1, -2, -3), (-4, -5, -3)], [(1, 2, 3), (1, 2, 3)], [(4, 5, 6), (4, 5, 6)], [(7, 8, 9, 10), (7, 8, 9, 10)], [(4, 5, 6), (5, 6, 7)], [(7, 8, 9, 10), (8, 9, 10, 11)], [(1, 2, 3), (2, 1, 4)], [(4, 5, 6), (6, 4, 7)], [(4, 5, 6, 6), (4, 5, 6, 6)], [(0, 10, -6), (-1, 9, 21)], [(1, 99, 3), (1, 2, 3)], [(10, 19, 31, 39), (10, 19, 31, 39)], [(7, 8, 9, -10, 7), (7, 8, 9, 11, 10)], [(-40, 5, 7), (5, 6, 7)], [(7, 8, 9, 10), (-31, 9, 10, 11)], [(-1, 0, 1, 2, 3, 4), (0, 1, 2, 3, 4, 5)], [(1, -5, 3), (1, 2, 3)], [(4, 5, 39, 6), (4, 5, 39, 6)], [(1, 2, 3), (4, 5, -31)], [(0, 1, 2, 3, 4, 5, 3), (0, 1, 2, 3, 4, 5, 3)], [(4, 5, 7), (5, 6, 7)], [(-1, -30, 1, 3, 4), (-1, 0, 2, 3, 4)], [(2, 6, 10, 14, 18), (2, 6, 10, 14, 18)], [(10, 20, 30, 25), (10, 20, 30, 25)], [(-2, 2, 1, 4), (-2, 2, 1, 4)], [(0, 1, 2, 39, 4, 5, 3), (0, 1, 2, 3, 4, 5, 3)], [(1, 2, -6), (1, 2, 3)], [(2, 7, 10, 14, 18), (2, 6, 10, 14, 18)], [(10, 19, 31, 39), (11, 19, 31, 39)], [(5, 10, 15, 20), (5, 10, 15, 20)], [(2, 6, 10, 14, 18, 6), (2, 6, 10, 14, 18, 10)], [(1, -5, 3), (1, -5, 3)], [(100, 200, 299), (100, 200, 299)], [(2, 1, 4), (2, 1, 4)], [(5, 6, 6), (5, 6, 7)], [(4, 5, 6, 5), (4, 5, 6, 6)], [(4, 39, 6), (4, 39, 6)], [(2, 6, 10, -4, 18), (2, 6, 10, -4, 18)], [(3, 7, -39, 15, 19), (11, 6, 10, 15, 18)], [(7, 8, 9, -10, 7), (7, 8, 9, 10, 9)], [(0, 10, 20), (0, 10, 20)], [(-11, -19, -30, -31, -39), (-10, -20, -30, -40, -20)], [(4, 6, 6), (4, 6, 6)], [(6, 39, 39, 6), (6, -40, 39, 6)], [(-1, -6, 1, 3, 4), (-1, -30, 1, 3, 4)], [(0, 10, 20), (0, 10, 19)], [(-6, 6, 7), (-6, 6, 7)], [(10, 20, 30, 25), (11, 20, 30, 25)], [(-5, 6, 7), (-6, 6, 7)], [(5, 6, 7), (5, 6, 7)], [(4, 6, 6), (15, 6, 6)], [(-11, 6, 7), (5, 6, 7)], [(2, 3), (2, 3)], [(3, 0, 11, 15, 19), (3, 0, 11, 15, 19)], [(-6, 7, 7), (-6, 6, 7)], [(0, 20, 20), (0, 10, 20)], [(99, 19, 31, 39), (11, 19, 31, 39)], [(3, 7, 11, 15, 3, 19), (2, 6, 10, 10, 15, 18)], [(-1, 2, 1, 3, 4), (-1, -30, 2, 3, 5)], [(0, 10, 20), (-1, 10, 21)], [(-1, 2, 1, 3, 4), (-1, 2, 1, 3, 4)], [(2, 6, 10, 14, 18, 6), (2, 6, 10, 14, 18, 6)], [(39, 39, 6, 39), (6, 39, 39, 6)], [(10, 20, 30, 40), (10, -30, 31, 39)], [(10, 19, 31, 39), (11, 19, -40, 39)], [(-31, 10, 10, 11), (-31, 10, 10, 11)], [(19, 31, 39, 39), (11, 19, 3, 39)], [(4, 3, 5, 6, 6), (4, 3, 5, 6, 6)], [(15, 6, 6, 6), (15, 6, 6, 6)], [(7, 8, 9, -10, 7, 9), (7, 30, 9, -10, 7, 9)], [(20, 30, 40, 30), (20, 30, 40, 30)], [(11, 31, 39), (11, 31, 39)], [(-11, 30, 7), (5, 6, 7)], [(-40, 5, 7), (-40, 5, 7)], [(0, 20, -1, 20), (0, 20, -1, 20)], [(10, 19, -1, 39), (10, 20, 30, 40)], [(-2, 5, 6), (-11, 6, 7)], [(10, 20, 29, 40), (10, 20, 29, 40)], [(0, 0, 10, 20), (0, 10, 20, 0)], [(10, 30, 31, 39), (10, 19, 31, 39)], [(10, 31, 39), (10, 31, 39)], [(3, 0, 1, 2, 3, 4, 5), (3, 0, 1, 2, 3, 4, 5)], [(2, 1, 4), (2, 1, 99)], [(5, -40, 6, 7, 5), (5, 99, 6, 7, 5)], [(-11, -19, -31, -39), (-10, -20, -40, -20)], [(4, 16, 6, 6), (4, 5, 6, 5)], [(-5, 5, 6), (5, 6, 7)], [(10, 19, 31, 39), (11, 18, -40, 39)], [(15, 6, 6), (15, 6, 6)], [(0, 1, 2, 3, 4, 5), (-1, 0, 1, 29, 3, 4)], [(11, 32, 31, 39), (11, 31, 39, 11)], [(2, 6, 10, 15), (2, 6, 10, 15)], [(4, 5, 5), (5, 6, 7)], [(-1, -6, 1, 3, 4), (-1, -30, 1, -20, 4)], [(14, 6, 6), (15, 6, 6)], [(-1, 2, 1, 31, 4), (-1, 2, 1, 3, 4)], [(4, -39, 6), (4, 5, 6)], [(14, 6, 6), (14, 6, 6)], [(-6, 3, 7), (-6, 3, 7)], [(2, 6, 10, 14, 18, 10), (300, 6, 10, 14, 18, 9)], [(-6, 6, 7), (-6, 6, 29)], [(-6, 7, 7), (-6, 7, 7)], [(6, 7, 7), (-11, 6, 6)], [(10, 20, 8, 40), (10, 20, 30, 40)], [(5, 4, 99, 6, 7, 5), (5, 99, 6, 7, 5, 5)], [(2, 10, 14, 18, 2), (2, 10, 14, 18, 2)], [(-1, 0, 1, 2, 3, 4), (0, 1, 2, 3, 3, 5)], [(1, -4, 3), (1, 2, 3)]]
results = [False, True, True, False, True, True, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False]

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
        func_name = "check_smaller"
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
        for test_case in ['assert check_smaller((1, 2, 3), (2, 3, 4)) == False', 'assert check_smaller((4, 5, 6), (3, 4, 5)) == True', 'assert check_smaller((11, 12, 13), (10, 11, 12)) == True']:
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
