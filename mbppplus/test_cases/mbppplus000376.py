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
inputs = [[(10, 4, 5, 6, 8), 6], [(1, 2, 3, 4, 5, 6), 7], [(7, 8, 9, 44, 11, 12), 11], [([1, 2, 3], [4, 5, 6], [7, 8, 9]), [4, 5, 6]], [('apple', 'banana', 'cherry'), 'banana'], [(10, 'hello', True, 3.14), 'hello'], [([], [], []), []], [('a', 'b', 'c'), 'd'], [(1, 2, 3, 1, 2, 3), 3], [(), 5], [([1, 2, 3], 4), [1, 2, 3]], [([1, [2, 3], 4], [5, [6, 7], 8]), [2, 3]], [(10, 'hello', True, [1, 2, 3]), [1, 2, 3]], [(1, 2, 3, 2, 4, 2), 2], [(-10, -20, -30, -40), -30], [(1.5, 2.5, 3.5), 1.5], [([], '', 'apple'), ''], [(), 'banana'], [(), 7], [([1, 2, [3, 4]], 2), 2], [([10, 20], [10, 20]), [10, 20]], [([1, 2, [3, [4, 5]]], [[4, 5], 6]), [[4, 5], 6]], [(['a', 'b', ['c', 'd']], ['c', 'd']), ['c', 'd']], [([1, 2], {'a': 1, 'b': 2}), {'a': 1, 'b': 2}], [(), []], [(2, 3, 1, 2, 3), 3], [(1, 2, 3, 4, 2), 2], [(2, 20, 1, 2, 3), 3], [(1, 3, 2, 3, 4, 2, 3), 2], [(1, 2, 3, 4, 2), [1, 2, 3, 4, 2]], [([1, 2, [3, [4, 5]]], [[4, 5], 6]), [[4, 5], 6, 6]], [([1, [2, 3], 4], [5, [6, 7], 8]), [3]], [([1, [2, 3], 4], [5, [6, 7], 8]), [3, 3]], [(3, 3, 3), [3, 3]], [('xBmhAx', 'rBIbfb', 'xBhmhAx', 'b', 'b'), []], [([1, 2, 3],), [[1, 2, 3]]], [('chcherryerry', 'apple', 'banana', 'cherry'), ['apple', 'banana', 'cherry']], [([1, [2, 3], 4], [5, 8]), [2, 3]], [('chcherryerry', 'apple', 'banana', 'cherry', 'cherry'), ['apple', 'banana', 'cherry']], [(4.348560304127057, 1.5, 2.5, 3.5), [4.348560304127057, 1.5, 2.5, 3.5]], [('chcherryerry', 'banana', 'cherry', 'cherry', 'cherry'), ['apple', 'banana', 'cherry']], [('xBmhAx', 'rBIbfb', 'xBhmhAx', 'b', 'b', 'xBhmhAx'), []], [([10, 20], [10, 20]), [10, 10]], [('chcherryerry', 'banana', 'cherry', 'cherry', 'b', 'cherry'), ['apple', 'banana', 'cherry']], [('xBmhAx', 'rBIbfb', 'xBhmhAx', 'b', 'b'), [28.964266674760978, 19.32979185384636, 1.5, -76.47615018021537, -81.70482776125439]], [([3, [2, 3], 4], [5, [6, 7], 8]), [1, 3]], [(4,), [1, -30, 2, 3]], [(2, 3, 1, 2, 3, 2), 3], [(10, 3), [10, 3]], [([1, [2, 3], 4], [5, [6, 7], 8]), [2, 3, 3]], [([1, [2, 3], 4], [5, [6, 7], 8]), [[1, [2, 3], 4], [5, [6, 7], 8]]], [(2, 20, 1, 1, 2, 3), 3], [(['a', 'b', ['c', 'd']], ['c', 'd']), [['a', 'b', ['c', 'd']], ['c', 'd']]], [([], '', 'apple', ''), 'd'], [([1, 2, 3, 3],), [[1, 2, 3], [1, 2, 3]]], [(1, 2, 3, 4, 2), [9, 1, 2, 3, 3, 2]], [(1, 3, 2, 3, 4, 2, 3), 10], [(1, 2, 3, 4), 2], [([1, [2, 3], 4], [5, [6, 7], 8], [1, [2, 3], 4]), [3, 3]], [([10, 20], [10, 20]), [11, 20]], [(2, 20, 1, 2, 3), 10], [(3, 3), [[1, [2, 3], 4], [5, [6, 7], 8], [1, [2, 3], 4]]], [(10, 3), [3]], [(28.964266674760978, 3.14, 19.32979185384636, 1.5, -76.47615018021537, -81.70482776125439), [28.964266674760978, 19.32979185384636, 1.5, -76.47615018021537, -81.70482776125439]], [(2, 2, 20, 1, 2, 3), 2], [(1, 1, 2, 3, 4, 2, 3), 9], [(-10, -20, -30, -40), [-10, 1, -20, -30, -40]], [([1, [2, 3], 4],), [2, 3]], [(1, 1, 2, 3, 4, 2, 3), [1, 1, 2, 3, 4, 2, 3]], [(), [[1, [2, 3], 4]]], [(1, 3, 2, 3, 4, 2, 3), [1, 3, 2, 2, 4, 2, 3]], [([1, 2, [3, [4, 5]]], [[4, 5], 6]), [[-40, 5], 6]], [(-10, -20, -30), -30], [(3,), [3, 3]], [(7, 1, 3, 2, 3, 4, 2, 3), [1, 3, 2, 2, 4, 2, 3]], [([1, 2, 1], [1, 2], {'a': 1, 'b': 2}, [1, 2, 1]), [[1, 2, 1], [1, 2], {'a': 1, 'b': 2}, [1, 2, 1], [1, 2, 1]]], [([1, 3, [3, [4, 5]]], [[4, 5], 6]), [[4, 5], 6]], [(), ['', 'apple', 'akhIW', 'd', 'c', 'a', 'RmxIIB', 'Ttp']], [('a', 'b', 'cherry'), 'dapple'], [(-10, -20, -30, -40), [-10, 1, -20, -30, -40, -30]], [(-10, 1, 11, -20, -30, -40, 1), [-10, 1, -20, -30, -40, 1, 1]], [('apple', 'banana', 'cherry'), ['apple', 'banana', 'cherry']], [(2, 3, 0, 2, 3, 1), 3], [(1, 3, 2, 3, 4, 2, 3), [1, 3, 2, 20, 2, 4, 2, 3]], [([2, 3, 3],), [[1, 2, 3], [1, 2, 3], [1, 2, 3]]], [(1, 2, 3, 4, 2, 2), [1, 2, 3, 4, 2]], [([1, [2, 3], 4], [5, [6, 7], 8]), [2, 3, 3, 3]], [([10, 20], [10, 20, 20], [10, 20, 20]), [11, 20]], [(1, 1, 2, 3, 4, 2, 3), 8], [([1, [2, 3, 3], 4],), [[1, [2, 3], 4], [1, [2, 3], 4]]], [([], [], []), [{'-73.52218882955222': 2, '-66.96191247748814': 50, '4.348560304127057': 90.88824607409293, '28.964266674760978': True, '1.5': False, '3.14': [False, True, False, True, False], '2.5': True}, 11, 8, {}, 'chcherryerry']], [([1, [2, 3], 4], [5, [6, 7], 8, 5], [5, [6, 7], 8], [1, [2, 3], 4], [1, [2, 3], 4]), [[1, [2, 3], 4], [5, [6, 7], 8, 5], [5, [6, 7], 8], [1, [2, 3], 4], [1, [2, 3], 4]]], [(-77.49409548611021, 2.5, 2.5, 9.624371119653333, 28.964266674760978, -73.52218882955222), 'banana'], [(2, 3), [3]], [([1, [2, 3], 4], [1, [2, 3], 4], [1, [2, 3], 4]), [[1, [2, 3, 3], 4]]], [(-6.114892068502201, -7.851316646059402, -73.52218882955222, 19.32979185384636, 82.27006557582865, -16.21417108166898, 59.653975366495985, 67.76262613952514, 39.06517900991895, 28.964266674760978), [[1, [2, 3], 4]]], [(3,), [3]], [([1, [2, 3], 4], [5, [6, 7], 8]), [[1, [2, 3], 4], [5, 8, [6, 7], 8]]], [([1, 2, 3], [1, 2, 3]), [[1, 2, 3, 3]]], [([1, 2], {'b': 2}, [1, 2]), [[1, 2], {'b': 2}, [1, 2]]], [([1, [2, 3], 4], [5, [6, 7], 8]), [[1, [2, 3], 4], [5, [6, 7], 8, 5]]], [([1, [2, 3]], [5, [6, 7], 8]), [2, 3, 3]], [('xBmhAx', 'rBIbfb', 'xBhmhAx', 'b', 'b', 'xBhmhAx'), ['xBmhAx', 'rBIbfb', 'xBhmhAx', 'b', 'b', 'xBhmhAx']], [(), [1, -30, 2, 3, -30]], [([1, 2, 3], [1, 2, 3], [2, 3], [1, 2, 3]), [[1, 2, 3], [1, 2, 3], [1, 2, 3]]], [(20, -60, 10, -21), 5], [(4.348560304127057, 1.5, 1.0981435370277304, 2.44007671951608, 3.5), [4.348560304127057, 1.5, 2.5, 3.5]], [(2, 3, 2, 2, 2, 0, -20, 4, 2, 3), [2, 3, 2, 2, -20, 4, 2, 3]], [(1, 2, 3, 7, 2, 4, 2, 2), [1, 2, 3, 2, 4, 2]], [(3, 1, 3, 2, 3, -60, 2, 3, 3), [1, 3, 2, 3, -60, 2, 3, 3]], [(2, 3, 1, 2, 3, 2), 4], [([4, 5], 6, 6), [[4, 5], 6, 6]], [(1, 3, 2, 3, 4, 2), [1, 3, 2, 3, 4, 0, 3]], [(3, 1, 3, 2, 3, -60, 2, 3, 3), [1, 3, 2, 2, -60, 2, 3, 3]], [(3, 2), [3, 3, 3]], [(1, 2, 3, 4, 2, 2, 1), [1, 2, 3, 4, 2, 2]], [('chcherryerry', 'apple', 'banana', 'cherry'), ['apple', 'banana', 'cherry', 'banana']], [(3.748269152011608, 1.5, 2.5, 3.5), [4.348560304127057, 1.5, 2.5, 3.5]], [(2, 3, 1, 2, 3), 20], [([1, 2], {'a': 1, 'b': 3}, {'a': 1, 'b': 3}), {'a': 1, 'b': 3, 'xBmhAx': 11}], [(2, 9, 10), [3]], [(1, 3, 2, 3, 4, 1, 3), [1, 3, 2, 3, 4, 0, 3]], [(2, 3, 4, 2, 2, 1), [1, 2, 3, 4, 2, 2]], [(1, 3, 2, 3, 5, 2), [1, 3, 2, 3, 4, 0, 3]]]
results = [True, False, True, True, True, True, True, False, True, False, True, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "check_K"
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
        for test_case in ['assert check_K((10, 4, 5, 6, 8), 6) == True', 'assert check_K((1, 2, 3, 4, 5, 6), 7) == False', 'assert check_K((7, 8, 9, 44, 11, 12), 11) == True']:
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
