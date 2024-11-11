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
inputs = [[(3, 4, 5, 6), (5, 7, 4, 10)], [(1, 2, 3, 4), (3, 4, 5, 6)], [(11, 12, 13, 14), (13, 15, 16, 17)], [(1, 1, 2, 3, 4), (2, 3, 3, 4, 5)], [(5, 7, 7, 4, 10), (3, 4, 5, 6, 6)], [(1, 2, 3, 4), (5, 6, 7, 8)], [(10, 20, 30, 40), (40, 50, 60, 70)], [(1, 1, 2, 2, 3, 3), (3, 3, 4, 4, 5, 5)], [(7, 8, 9, 10), (1, 2, 3, 4)], [(5, 15, 25, 35), (35, 45, 55, 65)], [(1,), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(1, 2, 3, 4, 5, 6, 7), (7, 8, 9, 10, 11, 12)], [(1, 2, 3), (4, 5, 6)], [(1, 2, 3), (3, 4, 5)], [(1, 1, 2, 2, 3, 3, 4, 4), (2, 3, 3, 4, 4, 5, 5, 6)], [(), (1, 2, 3)], [(1, 2, 3), ()], [(1, 2, 3), (1,)], [(1, 2, 3), (3, 2, 1)], [(1, 2, 3), (2, 4, 6)], [(1, 2, 3), (4, 5, 6, 7)], [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], [(1, 2, 3, 4, 5, 6, 7, 8, 9), (9, 8, 7, 6, 5, 4, 3, 2, 1)], [(1, 3, 5, 7, 9, 11, 13, 15), (2, 4, 6, 8, 10, 12, 14, 16)], [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)], [(1, 1, 2, 2, 3, 3, 4, 4), (5, 5, 6, 6, 7, 7, 8, 8)], [(1, 3, 3, 5, 7, 7, 9, 11, 13, 13, 15), (2, 4, 6, 8, 8, 10, 12, 14, 16)], [(1, 3, 5, 7, 9, 11, 13, 15), (2, 2, 4, 6, 6, 8, 10, 12, 14, 14, 16, 16)], [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (2, 4, 6, 8, 10, 12, 14, 16)], [(10, 20, 30, 30, 40), (40, 50, 60, 70)], [(), (2, 2, 3)], [(), ()], [(6, 7, 8, 9, 10, 6), (6, 7, 8, 9, 10, 7)], [(35, 45, 55, 65), (35, 45, 55, 65)], [(1, 1, 2, 3, 3), (3, 3, 4, 4, 5, 5)], [(1,), (1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(0, 2, 3), (4, 5, 6, 7)], [(10, 20, 30, 30, 40), (40, 50, 60, 70, 70)], [(1, 2, 3, 4, 5), (1, 2, 3, 4)], [(1, 2, 3), (2, 3)], [(), (True, False, True, False, True, False)], [(1, 2, 3, 5, 5), (1, 2, 3, 5, 5)], [(1, 1, 2, 2, 3, 3, 4, 4, 3), (1, 1, 2, 2, 3, 3, 4, 4)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 8), (9, 8, 7, 6, 5, 4, 3, 2, 1)], [(1, 1, 2, 2, 3, 3, 4, 4), (5, 6, 5, 6, 6, 7, 7, 8, 8)], [(1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(10, 20, 30, 40, 10), (10, 20, 30, 40)], [(2, 2, 3), (2, 2, 3)], [(1, 2, 50, 3, 4, 5, 6, 7, 8, 9, 9), (9, 8, 7, 6, 5, 4, 3, 2, 1)], [(1, 3, 5, 7, 30, 9, 11, 13, 15), (2, 4, 6, 8, 10, 12, 14, 16)], [(1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(8, 5, 6, 5, 6, 6, 7, 12, 8, 8), (5, 6, 5, 6, 6, 7, 12, 8, 11)], [(1, 3, 5, 7, 9, 11, 13, 15), (1, 3, 5, 7, 9, 11, 13, 15)], [(35, 36, 35, 45, 55), (36, 35, 45, 55)], [(1, 2, 3, 1), (4, 5, 6)], [(40, 50, 61, 70), (40, 50, 60, 70)], [(40, 50, 60, 70, 70), (40, 50, 60, 70, 70)], [(1, 2, 3, 3), (1, 2, 3)], [(2, 2, 3, 3), (2, 2, 3)], [(1, 2, 3), (11, 20, 1, 99, 2, 35, 1, 86)], [(1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(10, 20, 30, 41, 20), (40, 50, 60, 70)], [(9, 16, 8, 7, 6, 5, 4, 3, 2, 1), (9, 16, 8, 7, 6, 5, 4, 3, 2, 1)], [(95.3833483813928,), (95.3833483813928,)], [(8, 6, 5, 6, 6, 7, 12, 8, 8), (5, 6, 5, 6, 6, 7, 12, 8, 11)], [(1, 60, 3), (1, 2, 3)], [(9,), (0,)], [(2, 5, 6), (2, 4, 6)], [(2, 3, 5, 3, 4, 5), (2, 3, 3, 4, 5)], [(5, 6, 6, 7, 7, 8, 8, 6), (5, 6, 6, 7, 7, 8, 8, 6)], [(1, 2, 70, 70), (11, 20, 1, 99, 2, 35, 1, 86)], [(36, 1, 2, 3, 3), (1, 3, 3)], [(0, 1), (0, 0)], [(2, 60, 6, 8, 10, 12, 14, 16), (1, 3, 5, 30, 30, 9, 11, 13, 15)], [(1, 2, 3, 4), (5, 6, 7, 8, 8)], [(5, 15, 25, 35), (36, 45, 55, 65)], [(6, 7, 8, 9, 10, 6), (6, 7, 8, 9, 10, 6)], [(0, 1, 1), (0, 0)], [(2, 60, 6, 8, 10, 12, 14, 16), (2, 60, 6, 8, 10, 12, 14, 16)], [(35, 45, 55, 65, 65), (35, 45, 55, 65, 65)], [(1, 1, 2, 2, 3, 3, 4, 4), (1, 1, 2, 2, 3, 3, 4, 4)], [(1, 1, 3, 5, 5), (1, 2, 3, 5, 5)], [(1, 2, 2, 3, 3, 4, 4), (1, 1, 2, 2, 3, 3, 4, 4)], [(10, 20, 30, 30), (40, 50, 60, 70)], [(11, 20, 99, 2, 35, 1, 45, 86), (11, 20, 1, 99, 2, 35, 1, 45, 86, 35)], [(69, 40, 50, 60, 70, 70), (40, 50, 60, 70, 70)], [(6, 7, 8, 9, 10), (1, 2, 3, 4, 5)], [(11, 20, 1, 99, 2, 35, 1, 87, 86), (11, 20, 1, 99, 2, 35, 1, 86)], [(4, 5, 6, 7, 4), (4, 5, 6, 7)], [(20, 30, 40), (20, 30, 14, 40)], [(1, 1, 2, 3, 3), (3, 0, 4, 4, 5, 5)], [(2, 3, 5, 3, 4, 5), (2, 3, 5, 3, 4, 5)], [(7, 8, 9, 2, 10), (7, 8, 9, 10)], [(11, 20, 99, 2, 35, 0, 45, 86), (11, 20, 99, 2, 35, 1, 45, 86)], [(1, 40, 3, 3, 5, 7, 7, 9, 11, 13, 13, 15), (1, 3, 3, 5, 7, 7, 9, 11, 13, 13, 15)], [(1, 1, 2, 3, 1), (1, 1, 2, 3, 3, 1)], [(1, 3, 3, 5, 7, 7, 9, 11, 13, 13, 15), (1, 40, 3, 3, 5, 7, 7, 9, 11, 13, 60, 15)], [(1, 3, 5, 7, 9, 11, 13, 15), (2, 4, 6, 8, 10, 12, 14, 16, 8)], [(2, 3), (4, 5, 6, 7)], [(2, 3), (2, 4, 6)], [(7, 8, 9, 2, 10), (7, 8, 9, 10, 9)], [(1, 2, 3), (1, 2, 3)], [(1, 3), (1, 3, 3)], [(5, 6, 5, 6, 6, 9, 7, 11, 8, 11, 11), (5, 6, 5, 6, 6, 9, 7, 12, 8, 11)], [(2, 4, 5, 8, 10, 12, 14, 16), (2, 4, 6, 8, 10, 12, 14, 16)], [(10, 20, 30, 40), (41, 40, 50, 60, 70)], [(1,), (87, 1)], [(2, 4, 6), (2, 6)], [(1, 2, 2, 3), (1, 2, 3)], [(1, 2, 3, 4, 3), (5, 6, 7, 8)], [(5, 5, 6, 7, 7, 8, 8, 6), (5, 5, 6, 6, 7, 7, 8, 8)], [(1, 1, 2, 2, 3, 3, 4, 4), (5, 6, 5, 6, 6, 7, 7, 30, 8)], [(3, 4, 3), (3, 4)], [(10, 20, 30, 30, 30), (40, 50, 60, 70)], [(20, 30, 30), (40, 50, 60, 70)], [(4, 5, 30, 7), (4, 5, 6, 7)], [(1, 1, 2, 2, 3, 3, 4, 4, 3), (6, 1, 2, 2, 3, 3, 4, 4)], [(-14, -59, -4, 74, 36), ()], [(1,), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(1, 2, 3, 4), (5, 6, 87, 7, 9)], [(1, 2, 3, 1), (5, 5, 6)], [(1, 1), (1,)], [(9, 16, 8, 7, 6, 5, 4, 3, 2, 1), (30, 16, 8, 7, 6, 5, 4, 3, 2, 1)], [(35, 45, 55, 65), (45, 55, 65)], [(2, 3), (41, 2, 4, 6)], [(2, 3), (4, 6)], [(2, 3, 3, 4, 4), (2, 3, 3, 4, 5)], [(5, 6, 5, 6, 6, 7, 7, 8, 8), (5, 6, 5, 6, 6, 7, 7, 8, 8)], [(5, -14, 1), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)], [(1, 2, 3, 4), (1, 2, 3, 4)], [(2, 3, 3, 4, 4), (2, 3, 3, 4, 4)], [(1, 2, 3, 2), (11, 20, 1, 99, 2, 35, 1, 86)]]
results = [(3, 4, 5, 6, 7, 10), (1, 2, 3, 4, 5, 6), (11, 12, 13, 14, 15, 16, 17), (1, 2, 3, 4, 5), (3, 4, 5, 6, 7, 10), (1, 2, 3, 4, 5, 6, 7, 8), (10, 20, 30, 40, 50, 60, 70), (1, 2, 3, 4, 5), (1, 2, 3, 4, 7, 8, 9, 10), (5, 15, 25, 35, 45, 55, 65), (1,), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), (1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5, 6), (1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3), (1, 2, 3, 4, 6), (1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), (1, 2, 4, 6, 8, 10, 12, 14, 16), (10, 20, 30, 40, 50, 60, 70), (2, 3), (), (6, 7, 8, 9, 10), (35, 45, 55, 65), (1, 2, 3, 4, 5), (1, 2), (0, 2, 3, 4, 5, 6, 7), (10, 20, 30, 40, 50, 60, 70), (1, 2, 3, 4, 5), (1, 2, 3), (False, True), (1, 2, 3, 5), (1, 2, 3, 4), (1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8), (1, 2), (10, 20, 30, 40), (2, 3), (1, 2, 3, 4, 5, 6, 7, 8, 9, 50), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 30), (1, 9), (5, 6, 7, 8, 11, 12), (1, 3, 5, 7, 9, 11, 13, 15), (35, 36, 45, 55), (1, 2, 3, 4, 5, 6), (40, 50, 60, 61, 70), (40, 50, 60, 70), (1, 2, 3), (2, 3), (1, 2, 3, 11, 20, 35, 86, 99), (1, 8), (10, 20, 30, 40, 41, 50, 60, 70), (1, 2, 3, 4, 5, 6, 7, 8, 9, 16), (95.3833483813928,), (5, 6, 7, 8, 11, 12), (1, 2, 3, 60), (0, 9), (2, 4, 5, 6), (2, 3, 4, 5), (5, 6, 7, 8), (1, 2, 11, 20, 35, 70, 86, 99), (1, 2, 3, 36), (0, 1), (1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 30, 60), (1, 2, 3, 4, 5, 6, 7, 8), (5, 15, 25, 35, 36, 45, 55, 65), (6, 7, 8, 9, 10), (0, 1), (2, 6, 8, 10, 12, 14, 16, 60), (35, 45, 55, 65), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 4), (10, 20, 30, 40, 50, 60, 70), (1, 2, 11, 20, 35, 45, 86, 99), (40, 50, 60, 69, 70), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 11, 20, 35, 86, 87, 99), (4, 5, 6, 7), (14, 20, 30, 40), (0, 1, 2, 3, 4, 5), (2, 3, 4, 5), (2, 7, 8, 9, 10), (0, 1, 2, 11, 20, 35, 45, 86, 99), (1, 3, 5, 7, 9, 11, 13, 15, 40), (1, 2, 3), (1, 3, 5, 7, 9, 11, 13, 15, 40, 60), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), (2, 3, 4, 5, 6, 7), (2, 3, 4, 6), (2, 7, 8, 9, 10), (1, 2, 3), (1, 3), (5, 6, 7, 8, 9, 11, 12), (2, 4, 5, 6, 8, 10, 12, 14, 16), (10, 20, 30, 40, 41, 50, 60, 70), (1, 87), (2, 4, 6), (1, 2, 3), (1, 2, 3, 4, 5, 6, 7, 8), (5, 6, 7, 8), (1, 2, 3, 4, 5, 6, 7, 8, 30), (3, 4), (10, 20, 30, 40, 50, 60, 70), (20, 30, 40, 50, 60, 70), (4, 5, 6, 7, 30), (1, 2, 3, 4, 6), (-59, -14, -4, 36, 74), (1,), (1, 2, 3, 4, 5, 6, 7, 9, 87), (1, 2, 3, 5, 6), (1,), (1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 30), (35, 45, 55, 65), (2, 3, 4, 6, 41), (2, 3, 4, 6), (2, 3, 4, 5), (5, 6, 7, 8), (-14, 1, 5), (1, 2, 3, 4), (2, 3, 4), (1, 2, 3, 11, 20, 35, 86, 99)]

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
        func_name = "union_elements"
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
        for test_case in ['assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)', 'assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)', 'assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)']:
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
