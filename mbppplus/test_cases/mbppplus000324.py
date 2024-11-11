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
inputs = [[(10, 4, 5, 6, None)], [(7, 8, 9, 11, 14)], [(1, 2, 3, 4, None)], [(2,)], [([1, 2], [3, 4], [5, None])], [([None, None, None], [None, None, None], [None, None, None])], [([1, 2, 3], [4, 5, 6], [7, 8, 9, None])], [([[None], [None]], [[None], [None]])], [([], [])], [([1, [2, 3]], [4, [None, 5]])], [([[1, [2, [3, [4, [5, [6, [7, [8, [9, None]]]]]]]]]],)], [([None, [None, [None, [None, [None, [None, [None, [None, [None, None]]]]]]]]],)], [(None, [None, [None, [None, [None, [None]]]]])], [([[None], [1, 2], [3, None]], [None, [4, 5]], [[6, None], [None, 7]])], [([[None, 1, 2, 3], [4, None, 5, 6]], [[None, 7, 8, None], [None, 9, None, 10]])], [([[None, None, None], [1, 2, 3], [None, None, None]], [[4, None, 5], [None, None, None], [None, 6, None]])], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [[6, None], [None, 7]])], [(10, 4, 5, 6, None, [])], [(1, 2, 3, 4, None, [None])], [([1, 2], [3, 4], [5, None], [])], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [[6, None], [None, 7]], [])], [([1, [2, 3]], [4, [None, 5]], [None, [None, 6]])], [()], [([1, 2], [3, None], [4, None, 5], [None, None], [6, 7, None, None])], [([None, None, 1], [2, None, None], [None, 3, None], [4, None, 5, 6])], [([None, None, None, None], [1, 2, 3], [None, None, None], [4, 5, 6])], [([[None, None, None], [1, 2, 3], [None, None, None]], [[4, None, 5], [None, None, None], [None, 6, None]], [[7, None, None], [None, None, None], [None, None, None]])], [([1, 2], [3, None], [4, 5], [None, 6], [7, 8], [None, None])], [([[None], [1, 2], [3, None]], [None, [4, 5]], [[6, None], [None, 7]], [[None], [8, 9], [None, None]])], [([[None, None], [[None, None], [None, None]]], [[None, None], [[None, None], [None, None]]])], [([[None, None, [None, [None, None]]], None], [[None, None, [None, None]], None])], [([1, 2], [3, None], [4, 5], [None, 6], [7, 8], [None, None, 6], [None, None])], [([4, 5, 6], [7, 8, 9, None], [7, 8, 9, None])], [([5, 6], [1, 2, 3], [4, 5, 6], [7, 8, 9, None, 8])], [([1, [2, 3]], [4, [None, 5]], [1, [2, 3]])], [([4, 5, 6], [7, 8, 9, None])], [([4, 4, 6], [7, 8, 9, None], [7, 8, 9, None])], [([], [9, ['EmZMRTPX', 'ntSnaH', 'mtiRiOL', 'quzN', 'YeCzezCHd']], [])], [([1, 2, 2], [3, 4], [5, None])], [([[4, None, 5], [None, None, None], [None, 6, None], [4, None, 5]], [[4, None, 5], [None, None, None], [None, 6, None]])], [([1, [2, 3]], [1, 1, [2, 3]], [4, [None, 5]], [1, [2, 3]])], [([1, [2, 3]], [1, [2, 3]])], [([1, 2], [3, None], [None, None], [7, 7, None, None])], [([1, 2], [3, 4], [5, None], [3, 4])], [([1, 2, 2], [3, 4], [5, None], [5, None])], [([7, 8, 9, None, 8], [4, 4, 6], [7, 8, 9, None], [7, 8, 9, None])], [([1, [2, 3]], [4, [None, 5]], [1, [2, 3]], [4, [None, 5]])], [([[1, [2, [3, [4, [5, [6, [7, [8, [9, None]]]]]]]]]], [[1, [2, [3, [4, [5, [6, [7, [8, [9, None]]]]]]]]]])], [([1, 2], [3, 4], [6, None], [3, 4], [1, 2])], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [[6, 7, None], [6, None], [None, 7]])], [([1, 2, 2], [1, 2, 2, 2], [3, 4], [5, None], [5, None])], [([None, None, 1], [2, None, None], [None, 3, None], [None, 3, None], [1, 4, None, 5, 6])], [([1, [2, 3]], [1, [6, 3]], [1, 1, [2, 3]], [4, [None, 5]], [1, [2, 3]], [1, 1, [2, 3]])], [([[None, None, None], [1, 2, 3], [None, None, None]], [[4, None, 5], [6, None], [None, None, None], [None, 6, None]], [[7, None, None], [None, None, None], [None, None, None]])], [([1, 2], [3, 4], [5, None], [5, 10, None], ['gvL', 'EmZMRTPX', 'DpLWe', 'quzN', 'ZoPZGHEV', 'YeCzezCHd', 'mtiRiOL'])], [(10, 5, 6, None, [])], [([None, [4, 5]], [[6, None], [None, 7]], [[None], [8, 9], [None, None]])], [([4, 4, 6], [9, 7, 8, 9, None])], [([2, None, None], [None, 3, None], [4, None, 5, 6])], [(6, 5, 6, None, [])], [([1, 2], [3, 4], [5, None, None], [])], [(False, False, False, True, True)], [(None, [None, [None, [None, [None, [None]]]]], None)], [([None, None, 1], [2, None, None], [4, None, 5, 6], [4, None, 5, 6])], [([4, None, 1, 6], [2, None, None], [None, None, 1], [2, None, None], [4, None, 5, 6], [4, None, 5, 6], [4, None, 5, 6])], [([None, None, 1], [2, None, None, None], [4, None, 5, 6], [4, None, 5, 6])], [([4, 4, [None, 5]], [1, [2, 3]], [4, [None, 5]])], [([7, 8, 9, None, 8], [4, 4, 6], [7, 8, 9, None], [7, None, 8, 9, None], [7, 8, 9, None])], [([7, 8, 9, None, 8], [4, 4, 6], [7, 8, 9, None], [7, None, 8, 9, None], [7, 8, 9, None, 9], [7, 8, 9, None])], [([[None, None, None], [1, 2, 3], [None, None, None]], [[4, None, 5], [None, None, None], [None, None, 6, None]])], [(10, 5, 6, None, [], 10)], [([2, None, None], [2, None, None], [None, 3, None], [3, None, None], [4, None, 5, 6])], [([1, [2, 3], 1], [4, [None, 5]])], [([1], [4, [None, 5]], [1, [2, 3]], [1, [2, 3]])], [([None, None, None, None, None], [1, 2, 3], [None, None, None], [4, 5, 6])], [([None, [[None, [None, [None]]]]], None, [None, [None, [None, [None, [None]]]]], None)], [([2, None, None], [None, 3, None], [None, 3, None], [1, 4, None, 5, 6])], [([4, [None, 5], 4], [1, [2, 3]], [4, [None, 5]], [1, [2, 3]])], [(10, 5, 6, None, [], None)], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [[6, None], [None, 7]], [], [])], [([1, 2, 2], [1, 2, 2, 2], [3, 4], [5, None], [5, None], [1, 2, 2, 2])], [([[None, None, None], [1, 2, 3], [None, None, None], [None, None, None]], [[4, None, 5], [None, None, None], [None, 6, None]], [[7, None, None], [None, None, None], [None, None, None]], [[None, None, None], [1, 2, 3], [None, None, None], [None, None, None]], [[7, None, None], [None, None, None], [None, None, None]])], [(None, [None, [None, [None, [None, [None]]]]], None, [None, [None, [None, [None, [None]]]]])], [(5, 6, None, [])], [([1, 2], [3, 4], [5, None], [1, 1, 2], [1, 2])], [([1, [2, 3], 1], [4, [None, 5, 5], [None, 5]])], [([1, 2], [3, 6, 4], [5, None], [1, 1, 2], [1, 2])], [([1, [2, 3]], [4, [None, 5]], [1, [2]])], [([4, 4, [None, 5]], [1, [2, 3]], [4, [None, 5]], [1, [2, 3]])], [([3, None], [4, 5], [7, 8], [None, None])], [([[4, 5], [None, None]], [[6, None], [None, 7]], ['gvL', 'gvL', 'YeCzezCHd', 'YeCzezCHd'], [])], [(10, 5, 6, None, [], None, None)], [([[2, 3], 1, [2, 3]], [4, 4, [None, 5]], [1, [2, 3]], [4, [None, 5]])], [([1, [2, 3]], [1, [2, 3]], [4, [None, 5]])], [([3, 4, 3], [5, None], [])], [([3, 6, 4], [5], [1, 1, 2], [1, 2])], [([2, None, None], [None, 3, None], [None, 3, None, 3], [1, 4, None, 5, 6])], [([[None], [1, 2], [3, None]], [None, [4, 5]], [[6, None], [None, 7]], [None, [4, 5]], [[None], [1, 2], [3, None]])], [([1, [2, 3], 1], [2, [None, 5, 5], [None, 5]], [4, [None, 5, 5], [5]], [4, [None, 5, 5], [None, 5]])], [([7, 8, 9, None, 8], [7, 8, 9, None], [4, 4, 6], [7, 8, 9, None], [7, 8, 9, None])], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [78.89143771814926, -52.4240616339394, -72.56566507053195, -0.2817304158930085, -93.71004156385187, -15.10076750277966, 80.74945111800932, -63.35966765379977], [[6, None], [None, 7]], [], [])], [([4, None, 1, 6], [2, None, None], [None, None, 1], [2, None, None], [4, None, 5, 6], [4, None, 5, 6], [4, None, 5, 6, 6])], [(6, 5, 6, None, [], 6)], [([[None], [1, 2], [3, None]], [[6, None], [None, 7]])], [([1, 2], [3, None], [4, 5], [None, 6], [7, 8], [None, None], [None, 6])], [([[None], [1, 2], [3, None]], [[5, 4, 5], [None, None]], [[6, None], [None, 7]], [])], [([1, [2, 3]], [1, [2, 3]], [4, [None, 5]], [1, [2, 3]])], [(-15.10076750277966, [True, False, False, True], 'p', 'quzN', -85, 'ZoPZGHEV')], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [[6, None], [None, 7]], [[None], [1, 2], [3, None]])], [([None, [[None, [None, [None]]]]], None, [None, [None, [None, [None, [None]]]], None], None)], [([None, None, 1], [2, None, None], [4, None, 5, 6, 4], [4, None, 5, 6])], [([[None]], [[None], [None]])], [([3, 4], [None], [5, None], [5, None])], [([[2, 3], 1, [2, 3]], [4, 4, [None, 5]], [1, [2, 3], [2, 3]], [4, [None, 5]])], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [])], [([1, 2, 2], [5, None], [5, None])], [([7, 8, 9, None, 8], [7, 8, 9, None, None], [7, 8, 9, None], [4, 4, 6], [7, 8, 9, None], [7, 8, 9, None])], [([3, 6, 4], [5, None, None], [])], [([[4, 5], [None, None]], [[6, None], [None, 7]], ['gvL', 'gvL', 'YeCzezCHd', 'YeCzezCHd'], [], [])], [([1, [2, 3], 1], [2, [None, 5, 5], [None, 5]], [4, [None, 5, 5], [5]])], [([[None], [1, 2], [3, None]], [[4, 5], [None, None]], [78.89143771814926, -52.4240616339394, -72.56566507053195, -0.2817304158930085, -82.47988549016725, -93.71004156385187, -15.10076750277966, 80.74945111800932, -63.35966765379977], [[6, None], [None, 7]], [], [])], [([5, 6], [1, 2, 3], [4, 5, 6], [7, 4, 5, 6], [7, 8, 9, None, 8, 8], [7, 8, 9, None, 8, 8])], [([], [9, ['EmZMRTPX', 'ntSnaH', 'mtiRiOL', 'quzN', 'YeCzezCHd']], [], [9, ['EmZMRTPX', 'ntSnaH', 'mtiRiOL', 'quzN', 'YeCzezCHd']])], [([1], [False, [2, 3]], [4, [None, 5]], [1, [2, 3]], [1, [2, 3]])], [([1, [2, 3], 1], [5, 4, [None, 5]])], [(6, 5, 6, None, [], 4, 6)], [([4, 5], [4, 6], [8, 7, 8, 9, None], [7, 8, 9, None])], [([4, [None, 5], 4], [1, [2, 3]], [4, [None, 5]], [1, [2, 3]], [1, [2, 3]])], [([2, None, None], [None, 3, None], [3, None], [1, 4, None, 5, 6])], [([7, 5, 9, None, 8], [7, 8, 9, None], [4, 4, 6], [7, 8, 9, None], [7, 8, 9, None])], [([None, [4, 5]], [[6, None], [None, 7]], [[None], [8, 9], [None, None]], [[None], [8, 9], [None, None]])]]
results = [True, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False]

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
        func_name = "check_none"
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
        for test_case in ['assert check_none((10, 4, 5, 6, None)) == True', 'assert check_none((7, 8, 9, 11, 14)) == False', 'assert check_none((1, 2, 3, 4, None)) == True']:
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
