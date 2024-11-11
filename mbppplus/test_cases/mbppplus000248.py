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
inputs = [[[1, 4, 3, 5], [1, 2]], [[1, 2, 1], [1, 2, 1]], [[1, 0, 2, 2], [2, 2, 0]], [[], []], [[], [1, 2, 3]], [[1, 2, 3], []], [[1, 2, 3, 4, 5], [1, 3, 5]], [[1, 2, 3, 4, 5], [1, 2, 3]], [[1, 2, 3, 4, 5], [3, 4, 5]], [[1, 2, 3, 4, 5], [2, 4]], [[1, 2, 4, 3, 2, 1], [4, 3]], [[1, 2, 3, 4, 5], [6, 7, 8]], [[1, 1, 1, 1, 1], [1, 1, 1]], [[True, False, True, True, False, True, True, False], [True, 5, 'pKVtiZ', True, True, -66]], [[1, 1, 2, 3, 4, 5], [1, 3, 5]], [[4, 1, 3], [4, 1, 3]], [[True, True, True], []], [[1, 3, 4, 5], [2, 4]], [[1, 1], [1, 1]], [[3, 4, 5, 5], [3, 4, 5, 5]], [[-46.57347103376453, 3.1226647009953297, -30.45147357338469, -82.59243850873601, 48.432211942516204, 75.37283925638667], [3, 2, 2, 3]], [[5, 1, 3, 3], [5, 1, 3, 3]], [[True, 'pKVtiZ', True, True, -66], [True, 'pKVtiZ', True, True, -66]], [[1, 2, 3, 4, 5, 2], [6, 7, 8]], [[1, 2, 3, 3], [1, 2, 3, 3]], [[1, 3, 4, 5, 5], [1, 3, 4, 5, 5]], [[1, 3, 3, 4, 5, 5], [1, 3, 3, 4, 5, 5]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 2, 1, 1], [False, 1, 1, 1]], [[-41, -69, False, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}], [-41, -69, False, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}]], [[True, 'pKVtiZ', True, True, -66, 'pKVtiZ'], [True, 'pKVtiZ', True, True, -66, 'pKVtiZ']], [[5, 1, 3, 3, 3], [5, 1, 3, 3, 3]], [[1, 2, 3, 4, 5, 2], [1, 2, 3, 4, 5, 2]], [[3, 5], [3, 5]], [[1, 2, 3, 4, 3], [1, 2, 3, 4, 3]], [[1, 2, 3, 4, 3, 2], [1, 2, 3, 4, 3, 2]], [[3], [3]], [[1, 2, 2, 4, 5], [1, 2, 2, 4, 5]], [[False, 4, -99, -84, -69], []], [[3, 4, 5, -41], [3, 4, 5, -41]], [[-41, -69, False, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}, False], [-41, -69, False, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}, False]], [[1, 2, 3, 2, 4, 5, 2], [1, 2, 3, 2, 4, 5, 2]], [[3, -69, 5, -41], [3, -69, 5, -41]], [[5], [5]], [[True, False, False, True, False, False, False, False, False, False], [2, 3]], [[-42, -69, True, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}], [-42, -69, True, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}]], [[8, 1, 1, 1, 1, 1, 1], [8, 1, 1, 1, 1, 1, 1]], [[83, False, {'-37': 'pKVptiZ', '65': 'pKVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, {'-37': 'pKVptiZ', '65': 'pKVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, -77.86017743246624, False], [83, False, {'-37': 'pKVptiZ', '65': 'pKVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, {'-37': 'pKVptiZ', '65': 'pKVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, -77.86017743246624, False]], [[True, False, False, True, False, False, False, False, False, False], [True, False, False, True, False, False, False, False, False, False]], [[], [-41, 5, -27, -81, -41, 7, -56, -66, -98]], [[83, False, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, -77.86017743246624, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, False], [83, False, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, -77.86017743246624, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, False]], [[4, 5, 83, 5], [4, 5, 83, 5]], [[1, 1, 1, 1, 2, 1, 1], [1, 1, 1]], [[2, 4, 1, 3], [2, 4, 1, 3]], [[True, 'pKVtiZ', True, True, -66, 'pKVtiZ', 'pKVtiZ'], [True, 'pKVtiZ', True, True, -66, 'pKVtiZ', 'pKVtiZ']], [[1, 1, 1, 1, 1], [1, 1, 1, 1]], [[83, False, 4, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, -77.86017743246624, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, False], [83, False, 4, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, -77.86017743246624, {'-37': 'pKVptiZ', '65': 'pKpVtiZ', '9': 'pKVtiZ', '3': 'ZWwH', '-12': 'pKVtiZ'}, False]], [[1, 2, -41, 4, 3, 2], [1, 2, -41, 4, 3, 2]], [[2], [2]], [[2, 4], [2, 4]], [[-84, 3, 3, 4, 5, 5], [-84, 3, 3, 4, 5, 5]], [[True, 'pKVtiZ', True, True, 'pKVtiZ', 'pKVtiZ'], [True, 'pKVtiZ', True, True, 'pKVtiZ', 'pKVtiZ']], [['pKVtiZ', True, True, 'pKVtiZ'], ['pKVtiZ', True, True, 'pKVtiZ']], [[True, True, True], [True, True, True]], [[-41, -69, False, False, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}, False], [-41, -69, False, False, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}, False]], [[1, 2, 3, 4, 5, 1, 2], [1, 2, 3, 4, 5, 1, 2]], [[1, 3, 3], [1, 3, 3]], [[True, 'pKVtiZ', True, True, -66, -66, 'pKVtiZ'], [True, 'pKVtiZ', True, True, -66, -66, 'pKVtiZ']], [[9, 1, 3, 4, 5, 5], [9, 1, 3, 4, 5, 5]], [[1, -99, 2, 3, -69, 2, 4, 5], [1, -99, 2, 3, -69, 2, 4, 5]], [[1, 3, 2, 4, 5], [1, 3, 2, 4, 5]], [[1, 8, 2, 3], []], [[5, 1, 3, 3, 3, 5], [5, 1, 3, 3, 3, 5]], [[1, 2, 3, 4, 5], [3, 5]], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[5, -1, 0, 3, 3], [5, -1, 0, 3, 3]], [[2, 4, 1, 3, 3], [2, 4, 1, 3, 3]], [[1, 3, 2, 4, 5, 4], [1, 3, 2, 4, 5, 4]], [[4, 1, 8, 3], [4, 1, 8, 3]], [['kvYsHUDga', 'ZWwH', 'JKq', 'FDmCp', 'pKpVtiZ'], []], [[1, 3, 4, 9, 5], [1, 3, 4, 9, 5]], [[-41, -69, True, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}, False], [-41, -69, True, {'-99': -42.77556548447436, '3': 3.1226647009953297, '8': -46.57347103376453, '2': -46.57347103376453, '5': 59.33643533503681, '-37': 48.432211942516204}, False]], [[True, 5, 'pKVtiZ', True, True, -66, -66], [True, 5, 'pKVtiZ', True, True, -66, -66]], [[-69, False], [-69, False]], [[2, -42, 4, 4], [2, -42, 4, 4]], [[9, 1, 3, 4, 5, 5, 5], [9, 1, 3, 4, 5, 5, 5]], [[1, 1, 65, 1, 1, 1], [1, 1, 1]], [[2, -69, False], [2, -69, False]], [[False, False, 4, -99, -84, -69], []], [[-69, True, False], [-69, True, False]], [[4, 3], [4, 3]], [[8, 1, 1, 1, 1, 1], [8, 1, 1, 1, 1, 1]], [[-66, 1, 8, 3], [-66, 1, 8, 3]], [[8, 1, 1, -37, -98, 1, 1], [8, 1, 1, -37, -98, 1, 1]], [[True, False, True, True, False, True, False], [True, 5, 'pKVtiZ', True, True, -66]], [[8, 83, 1, 1, -37, -98, 1, 1], [8, 83, 1, 1, -37, -98, 1, 1]], [[True, False, False, False, False, False, False, False, False], [True, False, False, False, False, False, False, False, False]], [['kvYsHUDga', 'ZWwH', 'JKq', 'FDmCp', 'pKpVtiZ'], [-4.874268149645673, -77.86017743246624, -33.718853590345745, -77.86017743246624, -21.16888114566433, -46.57347103376453, -46.57347103376453, -46.57347103376453, 75.37283925638667, 67.81478209152664]], [[1, 2, -41, 4, 3, 2, 1], [1, 2, -41, 4, 3, 2, 1]], [[1, 1, 65, 1, 1, 1], [1, 1, 65, 1, 1, 1]], [['vbL', 'SohtgNm'], []], [[1, 1, 2, 3, 4, 5, 2], [1, 1, 2, 3, 4, 5, 2]], [[8, 1, 1, -85, 1, 1, 1, 1, 1], [8, 1, 1, -85, 1, 1, 1, 1, 1]], [[8, 1, -85, 1, 1, 1, 1, 1], [8, 1, -85, 1, 1, 1, 1, 1]], [[2, False], [2, False]], [[1, 3, 3, 3], [1, 3, 3, 3]], [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]], [[True, False, False, True, False, False, False, False, True], []], [[1, 2, 4], [1, 2, 4]], [[-82, -69, -58.58022067422433], [-82, -69, -58.58022067422433]], [[3, 4, 4], [3, 4, 4]], [[1, 2, 0, -41, 4, 3, 2], [1, 2, 0, -41, 4, 3, 2]], [[-82, 5, -66], [-82, 5, -66]]]
results = [False, True, False, True, False, True, True, True, True, True, True, False, True, False, True, True, True, False, True, True, False, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

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
        func_name = "is_Sub_Array"
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
        for test_case in ['assert is_Sub_Array([1,4,3,5],[1,2]) == False', 'assert is_Sub_Array([1,2,1],[1,2,1]) == True', 'assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False']:
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
