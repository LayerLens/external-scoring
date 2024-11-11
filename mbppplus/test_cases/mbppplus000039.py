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
inputs = [[10], [2], [9], [1000000], [True], [1000001], [1000002], [999999], [79], [999998], [999997], [80], [1000003], [81], [78], [82], [999996], [77], [84], [83], [999995], [85], [999994], [76], [999993], [86], [75], [1000004], [74], [88], [93], [94], [92], [999992], [87], [999991], [91], [999989], [89], [999987], [90], [97], [52], [96], [53], [95], [999990], [1000005], [999986], [98], [999985], [51], [999984], [54], [50], [999982], [999988], [73], [999981], [49], [99], [38], [48], [37], [20], [21], [36], [72], [35], [55], [999983], [100], [70], [71], [1000006], [33], [19], [31], [32], [22], [30], [23], [101], [18], [24], [34], [56], [47], [102], [17], [29], [57], [69], [39], [103], [40], [58], [999980], [15], [104], [16], [28], [105], [27]]
results = [271, 7, 217, 2999997000001, 1, 3000003000001, 3000009000007, 2999991000007, 18487, 2999985000019, 2999979000037, 18961, 3000015000019, 19441, 18019, 19927, 2999973000061, 17557, 20917, 20419, 2999967000091, 21421, 2999961000127, 17101, 2999955000169, 21931, 16651, 3000021000037, 16207, 22969, 25669, 26227, 25117, 2999949000217, 22447, 2999943000271, 24571, 2999931000397, 23497, 2999919000547, 24031, 27937, 7957, 27361, 8269, 26791, 2999937000331, 3000027000061, 2999913000631, 28519, 2999907000721, 7651, 2999901000817, 8587, 7351, 2999889001027, 2999925000469, 15769, 2999883001141, 7057, 29107, 4219, 6769, 3997, 1141, 1261, 3781, 15337, 3571, 8911, 2999895000919, 29701, 14491, 14911, 3000033000091, 3169, 1027, 2791, 2977, 1387, 2611, 1519, 30301, 919, 1657, 3367, 9241, 6487, 30907, 817, 2437, 9577, 14077, 4447, 31519, 4681, 9919, 2999877001261, 631, 32137, 721, 2269, 32761, 2107]

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
        func_name = "centered_hexagonal_number"
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
        for test_case in ['assert centered_hexagonal_number(10) == 271', 'assert centered_hexagonal_number(2) == 7', 'assert centered_hexagonal_number(9) == 217']:
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
