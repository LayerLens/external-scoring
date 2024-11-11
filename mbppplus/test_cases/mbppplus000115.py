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
inputs = [[(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4], [(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10], [(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8], [(5, 10, 15, 20, 25, 30), 15], [(1.5, 2.3, 4.7, 1.5, 7.8, 9.1, 1.5), 1.5], [('apple', 'banana', 'cherry', 'apple', 'banana', 'apple'), 'apple'], [('apple', 1, 3.14, 'banana', 1, 'apple', 'banana', 3.14), 'apple'], [(), 10], [(), 'apple'], [(), ''], [(['apple', 'banana'], ['cherry', 'apple', 'banana'], ['apple', 'cherry']), 'apple'], [(), 5], [([1, 2, 3], [4, 5, 6], [7, 8, 9, 10]), [1, 2, 3]], [(1, 'hello', True, 5.5, [1, 2, 3], [4, 5, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False), 'hello'], [(10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True), 'apple'], [(), []], [(['cherry', 'apple', 'banana'], ['apple', 'cherry']), 'apple'], [(1, True, 5.5, [1, 2, 3], [4, 5, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False), 'hello'], [(5, 10, 15, 25, 30), 7], [(1, 2, 3), [1, 5, 2, 3]], [(7, 10, 15, 20, 25, 30), 15], [(1, 2, 3), [1, 5, 2, 3, 2]], [(5, 10, 15, 20, 25, 30), 16], [(24, 1, 2, 25, 3), [1, 5, 2, 5, 3, 2]], [(0, 24, 1, 2, 3), [1, 5, 2, 5, 3, 2]], [(5, 10, 15, 20, 25, 30), [5, 10, 15, 20, 25, 30]], [(10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True), [10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True]], [(10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True), [10, 15, 9, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True]], [([1, 2, 3], [4, 5, 6]), [[1, 2, 3], [4, 5, 6], [7, 8, 9, 20]]], [(1, 5, 2, 5, 3, 2), [1, 5, 2, 5, 3, 2]], [('banana',), 10], [(5, 10, 15, 20, 25, 30), 25], [(), 'aepple'], [(1, 5, 2, 3), [1, 5, 2, 3]], [(0, 24, 1, 2, 3), [0, 24, 1, 2, 3]], [(5, 6, 10, 15, 20, 25, 30), 16], [(1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False), [[4, 6], 1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False]], [(None, 74, None, 5.5, False, 'cherry', 9.1, -51, True), []], [(1, 5, 2, 5, 3, 2), [1, 5, 2, 5, 3, 2, 2]], [('apple', 'a', 'JMv', 'MzMX'), 5], [('baJMva', 'banana', 'banana'), 10], [(None, 74, None, 5.5, False, 'cherry', 9.1, -51, True), [True, False, False, False]], [(1, 'hello', True, 5.5, [1, 2, 3], [4, 5, 6], {'a': 1, 'b': 3}, True, 'hello', 'hello', False), 'hello'], [(False, True, True), []], [(56.56098853425999, 69, 8), []], [('banana',), ['banana']], [('apple', 'a', 'JJMv', 'MzMX', 'apple'), ['apple', 'a', 'JMv', 'MzMX', 'apple']], [('apple', 'banana', 'chrerry', 'apple', 'banana', 'apple'), 'apple'], [(7.20597881844995, 5.5, 5.5, 12.262087321967073, 2.3, -43.60056353102604), []], [(False, False, True, False, True, False, True, False), 'aepple'], [(1, 5, 3), [1, 5, 2, 3]], [(), -51], [(10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True, True), [10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True]], [(['cherry', 'apple', 'banana'], ['apple', 'cherry']), [['cherry', 'apple', 'banana'], ['apple', 'cherry']]], [('apple', 1, 3.14, 'banana', 1, 'apple', 'banana', 6, 3.14), 'apple'], [('a', 'MzMX', 'apple'), ['apple', 'a', 'JMv', 'MzMX', 'apple', 'apple']], [([1, 2, 3], [4, 5, 6], [4, 5, 6]), [[1, 2, 3], [4, 5, 6]]], [(1, 5, 2, 6, 5, 3, 2), [1, 5, 2, 5, 3, 2]], [('apple', 7, 3.14, 1, 'apple', 'banana', 6, 3.14), 'cherry'], [('apple', 1, 3.14, 'banana', 1, 'apple', 'banana', 3.14, 'apple'), 'cherry'], [(1, 2, 5, 3), [1, 5, 2, 3]], [(1.5, 2.3, 4.7, 1.019517386952951, 7.8, 9.1, 1.5), 1.5], [(1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False), [[4, 6], 1, True, 5.5, [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False]], [([1, 2, 3], [4, 5, 6], [7, 8, 9, 10], [4, 5, 6]), [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]], [('bananaapple', 'a', 'JJMv', 'MzMX', 'apple'), ['apple', 'a', 'JJMv', 'MzMX', 'apple']], [('apple', 'a', 'MzMX', 'a'), 5], [(False, False, True, True, False), []], [('a', 'MzMX', 'aaepplepple'), ['a', 'MzMX', 'apple']], [('apple', 'banana', 'chrerrhelloy', 'chrerry', 'banana', 'baanana', 'apple'), ['apple', 'banana', 'chrerry', 'banana', 'apple']], [(1, 2, 3, 2), [1, 5, 2, 3, 2]], [('MzMX', 'aaepplepple'), ['a', 'MzMX', 'a', 'apple']], [(30, 0, 24, 1, 2, 3, 0, 2), [30, 0, 24, 1, 2, 3, 0]], [('baJMva', 'banana', 'banana'), 1], [('apple', 'a', 'JJMv', 'aaaepplepple', 'MzMX', 'apple', 'apple'), ['apple', 'a', 'JJMv', 'MzMX', 'apple', 'apple']], [('MzMX', 'aaepplepple'), ['a', 'MzMX', 'apple']], [(5, 6, 10, 15, 25, 30), 17], [(30, 0, 24, 1, 2, 3, 25, 0, 2), [30, 0, 24, 1, 2, 3, 25, 0, 2]], [(2.3, 7.20597881844995, 5.5, 5.5, 12.262087321967073, 2.3, -43.60056353102604, 12.262087321967073), [2.3, 7.20597881844995, 5.5, 5.5, 12.262087321967073, 2.3, -43.60056353102604]], [(), [['apple', 'cherry']]], [(24, 1, 2, 25, 3), [24, 1, 2, 24, 3]], [(1, 2, 3, 3, 2, 3), [1, 5, 2, 3, 2]], [('apple', 3.14, 'banana', 1, 'apple', 'banana', 6, 3.14), ['apple', 1, 3.14, 'banana', 1, 'apple', 'banana', 6, 3.14]], [(0, 24, 1, 2, 3, 24), [3, 0, 24, 1, 2, 3]], [(56.56098853425999, 69, 8), [74, 20, False, -89]], [(1, 5, 2, 2, 5), [1, 2, 3]], [(1, 2, 5, 3, 2), [1, 5, 2, 3]], [(30, 0, 24, 1, 2, 3, 25, 0, 2), [30, 0, 1, 2, 3, 25, 0, 2]], [(1, 2, 7), [1, 2, 2]], [(1, 6, 2, 3), [1, 2, 4, 5, 3]], [(1, 2, 3), [1, 2, 3, 2]], [(5, 6, 10, 15, 20, 25, 31, 30), 6], [(False, False, True, False, True, False, False, True, False), [False, False, True, False, True, False, False, True, False]], [(24, 1, 2, 26, 3), [24, 1, 2, 26, 3, 26]], [('apple', 1, 3.14, 'banana', 1, 'apple', 'banana', 'appple', 3.14, 'apple'), ['apple', 1, 3.14, 'banana', 1, 'apple', 3.14, 'apple']], [(1, 5, 2, 3), [3, 1, 5, 2, 3]], [(30, 0, 24, 1, 2, 4, 0), [30, 24, 1, 2, 3, 0]], [(30, 0, 24, 1, 2, 3, 0, 2), [30, 0, 24, 1, 2, 2, 3, 0, 2]], [(10, 15, 20, 'apple', 'banana', 'apple', True, False, True, True, 'apple'), [10, 15, 9, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True]], [(5, 6, 10, 15, 20, 25, 31, 30), -51], [(30, 0, 24, 1, 2, 3, 0, 2), [30, 0, 24, 1, 2, 3, 0, 2]], [(10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True), [10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True]], [('apple', 'banana', 'chrerry', 'apple', 'banana', 'apple'), 'applehello'], [(1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', False), [1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False]], [(7, 10, 15, 20, 25), 9], [(0, 24, 1, 2, 3, 0, 2), [30, 0, 24, 1, 2, 3, 0]], [(1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', False, 'hello'), [1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False]], [(10, 15, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True, True, 'apple'), [10, 15, 9, 20, 'apple', 'banana', 'apple', 'cherry', True, False, True]], [([1, 2, 3], [4, 6], [7, 8, 9, 10], [4, 5, 6]), [[1, 2, 3], [4, 6, 5, 6], [7, 8, 9, 10]]], [(24, 1, 2, 26, 3, 26), [24, 1, 2, 26, 3, 26]], [('apple', 'banana', 1, 'apple', 'banana', 6, 3.14), ['apple', 1, 3.14, 'banana', 1, 'apple', 'banana', 6, 3.14]], [(1, 2, 3, 2), [1, 2, 3, 2]], [([1, 2, 3], [1, 2, 3], [4, 5, 6, 4], [4, 5, 7], [7, 8, 9, 10], [4, 5, 6]), [[1, 2, 3], [4, 5, 6, 4], [4, 5, 7], [7, 8, 9, 10], [4, 5, 6]]], [('apple', 'a', 'JMv', 'MzMX'), False], [(1, True, 5.5, [1, 16, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', False), [1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False, 1]], [(1, True, 5.5, [1, 2, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', 'hello', False, 25), [1, True, 5.5, [1, 0, 16, 3], [4, 6], {'a': 1, 'b': 2}, True, 'hello', False]]]
results = [0, 3, 4, 1, 3, 3, 2, 0, 0, 0, 0, 0, 1, 3, 2, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        func_name = "count_X"
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
        for test_case in ['assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0', 'assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3', 'assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4']:
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
