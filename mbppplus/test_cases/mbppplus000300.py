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
inputs = [[10], [15], [18], [1000000], [0], [999999], [1000001], [1], [999998], [999997], [2], [1000002], [False], [True], [80], [3], [81], [999996], [1000003], [1000004], [79], [82], [1000005], [78], [999995], [68], [1000006], [83], [84], [67], [77], [999994], [4], [999993], [1000007], [999992], [61], [1000008], [99], [69], [98], [60], [999991], [85], [66], [100], [1000009], [86], [53], [87], [88], [97], [54], [89], [23], [76], [90], [64], [5], [62], [999990], [22], [51], [999989], [65], [12], [70], [71], [52], [63], [91], [50], [11], [55], [74], [56], [101], [57], [20], [27], [73], [26], [28], [25], [21], [13], [29], [58], [30], [1000010], [14], [19], [9], [49], [31], [48], [1000011], [6], [24], [92], [59], [75], [72]]
results = [325, 750, 1089, 3499997500000, 0, 3499990500006, 3500004500001, 1, 3499983500019, 3499976500039, 9, 3500011500009, 0, 1, 22200, 24, 22761, 3499969500066, 3500018500024, 3500025500046, 21646, 23329, 3500032500075, 21099, 3499962500100, 16014, 3500039500111, 23904, 24486, 15544, 20559, 3499955500141, 46, 3499948500189, 3500046500154, 3499941500244, 12871, 3500053500204, 34056, 16491, 33369, 12450, 3499934500306, 25075, 15081, 34750, 3500060500261, 25671, 9699, 26274, 26884, 32689, 10071, 27501, 1794, 20026, 28125, 14176, 75, 13299, 3499927500375, 1639, 8976, 3499920500451, 14625, 474, 16975, 17466, 9334, 13734, 28756, 8625, 396, 10450, 18981, 10836, 35451, 11229, 1350, 2484, 18469, 2301, 2674, 2125, 1491, 559, 2871, 11629, 3075, 3500067500325, 651, 1216, 261, 8281, 3286, 7944, 3500074500396, 111, 1956, 29394, 12036, 19500, 17964]

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
        func_name = "is_nonagonal"
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
        for test_case in ['assert is_nonagonal(10) == 325', 'assert is_nonagonal(15) == 750', 'assert is_nonagonal(18) == 1089']:
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
