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
inputs = [[['red', 'green', 'green'], ['a', 'b', 'b']], [['red', 'green', 'greenn'], ['a', 'b', 'b']], [['red', 'green', 'greenn'], ['a', 'b']], [['red', 'green', 'blue'], ['a', 'b', 'c']], [['red', 'red', 'red'], ['a', 'a', 'a']], [['red', 'blue', 'green'], ['a', 'b', 'c']], [['red', 'green', 'blue', 'red'], ['a', 'b', 'c', 'a']], [['red', 'red', 'blue', 'blue'], ['a', 'a', 'b', 'b']], [['red', 'green', 'green', 'blue'], ['a', 'b', 'b', 'c']], [['red', 'red', 'red', 'red'], ['a', 'a', 'a', 'a']], [['red', 'red', 'green', 'blue'], ['a', 'a', 'b', 'c']], [['red', 'green', 'green', 'green'], ['a', 'b', 'b', 'b']], [[], ['a', 'b', 'c']], [[], []], [['red', 'green', 'blue', 'yellow'], ['a', 'b', 'b', 'c']], [['red', 'green', 'blue', 'yellow'], ['a', 'b', 'c', 'a']], [['red', 'red', 'red', 'red', 'red', 'red'], ['a', 'b', 'c', 'a', 'b', 'c']], [['red', 'green', 'blue', 'red', 'green', 'blue'], ['a', 'b', 'c', 'a', 'b', 'c']], [['red', 'green', 'blue', 'red', 'red', 'red'], ['a', 'b', 'c', 'a', 'b', 'c']], [['red', 'green', 'blue', 'red', 'blue', 'green'], ['a', 'b', 'c', 'a', 'b', 'c']], [['a', 'b', 'cc', 'c', 'a'], ['a', 'b', 'cc', 'c', 'a']], [['red', 'green', 'yellow'], ['a', 'b', 'c', 'a']], [['b', 'c', 'a', 'b', 'c'], ['red', 'red', 'red', 'red', 'bluered', 'red']], [['blue', 'red', 'red', 'red', 'red'], ['a', 'a', 'a', 'a']], [['a', 'a', 'b', 'b', 'b'], ['a', 'a', 'b', 'b', 'b']], [['blue', 'red', 'red', 'red', 'red'], ['ared', 'a']], [['red', 'red', 'red', 'red', 'red', 'red'], ['a', 'b', 'ared', 'c', 'a', 'b', 'c']], [['red', 'green', 'blue', 'red', 'red', 'red', 'red'], ['a', 'b', 'ccc', 'a', 'b']], [['red', 'green', 'bluue', 'red', 'red', 'red'], ['red', 'green', 'bluue', 'red', 'red', 'red']], [['red', 'red', 'red'], ['red', 'red', 'red']], [[False, True, False], [False, True, False]], [['red', 'green', 'blue', 'yellow'], ['red', 'green', 'blue', 'yellow']], [['a', 'b', '', 'c'], ['a', 'b', '', 'c']], [['ared', 'a'], ['blue', 'red', 'red', 'red', 'red']], [['blue', 'red', 'red', 'red', 'red'], ['blue', 'red', 'red', 'red', 'red']], [['bluered', 'red', 'yellow', 'red', 'reyellow', 'cc', 'red'], ['bluered', 'red', 'yellow', 'red', 'reyellow', 'cc', 'red']], [['ared', 'rred', 'green'], ['ared', 'rred', 'green']], [[False], [False]], [['red', 'green', 'green', 'green'], ['ccc', 'b', 'b', 'b']], [['blueccc', 'blue', 'red', 'red', 'red', 'cc'], ['bluue', 'a', 'a', 'a', 'a']], [['red', 'green', 'bluue', 'red', 'red'], ['red', 'green', 'bluue', 'red', 'red']], [['red', 'green', 'blue', 'eblue', 'yellow', 'blue'], ['red', 'green', 'blue', 'eblue', 'yellow', 'blue']], [['blueccc', 'blue', 'red', 'red', 'red', 'cc'], ['bluue', 'a', 'a', 'a']], [['a', 'a', 'b', 'bblueccc', 'b', 'b'], ['a', 'a', 'b', 'bblueccc', 'b', 'b']], [['red', 'green', 'blue', 'yellow'], ['a', 'b', 'c', 'a', 'a']], [['blue', 'red', 'red', 'red', 'red'], ['a', 'a', 'cc', 'a']], [['blueccc', 'ared', 'a'], ['blue', 'red', 'red', 'red', 'red']], [[False, True, False, False], [False, True, False, False]], [['belue', 'red', 'red', 'green', 'blue', 'red'], ['belue', 'red', 'red', 'green', 'blue', 'red']], [['red', 'greeen', 'blue', 'red', 'red', 'red', 'red', 'red'], ['red', 'greeen', 'blue', 'red', 'red', 'red', 'red', 'red']], [['red', 'green', 'blue', 'yellow'], ['a', 'b', 'c', 'a', 'a', 'aa']], [['red', 'blue', 'green'], ['a', 'byellow', 'c']], [['red', 'green', 'green'], ['ccc', 'b', 'b', 'b']], [['red', 'green', 'blue', 'red', 'blue', 'green'], ['b', 'c', 'a', 'b', 'c']], [['blueccc', 'blue', 'red', 'red', 'blcccueccc', 'red', 'cc'], ['blueccc', 'blue', 'red', 'red', 'blcccueccc', 'red', 'cc']], [['red', 'rred', 'green', 'blue', 'yellw', 'eblue', 'yellow', 'blue'], ['red', 'rred', 'green', 'blue', 'yellw', 'eblue', 'yellow', 'blue']], [['gbluered', 'yellow', 'red', 'blue', 'green'], ['gbluered', 'yellow', 'red', 'blue', 'green']], [[True, False], [True, False]], [['red', 'green', 'red'], ['a', 'b', 'c', 'a']], [['belue', 'a'], ['belue', 'a']], [['green', 'rred', 'yellw', 'green'], ['green', 'rred', 'yellw', 'green']], [['bluaredue', 'red', 'green', 'bluue', 'red', 'red', 'red'], ['bluaredue', 'red', 'green', 'bluue', 'red', 'red', 'red']], [['bluue', 'a', 'a', 'a'], ['bluue', 'a', 'a', 'a']], [['a', 'bb', 'c', 'a'], ['a', 'bb', 'c', 'a']], [['a', 'b', 'c', 'a', 'b', 'c'], ['a', 'b', 'c', 'a', 'b', 'c']], [['red', 'greeen', 'blue', 'red', 'red', 'red', 'red', 'red', 'greeen'], ['red', 'greeen', 'blue', 'red', 'red', 'red', 'red', 'red', 'greeen']], [['blueccc', 'blue', 'red', 'red', 'blueccc', 'red', 'cc', 'red', 'red', 'blueccc'], ['blueccc', 'blue', 'red', 'red', 'blueccc', 'red', 'cc', 'red', 'red', 'blueccc']], [['a', 'red', 'b', 'rred', 'c'], ['a', 'red', 'b', 'rred', 'c']], [['a', 'b', 'c', 'a', 'a', 'aa'], ['red', 'green', 'blue', 'yellow']], [['red', 'green', 'red'], ['a', 'b', 'c', 'a', 'a']], [['ared', 'rred', 'green', 'green'], ['ared', 'rred', 'green', 'green']], [['red', 'blue', 'yellow', 'red'], ['red', 'blue', 'yellow', 'red']], [['red', 'green', 'blue', 'bluue', 'red', 'red', 'red'], ['red', 'green', 'blue', 'bluue', 'red', 'red', 'red']], [['red', 'red', 'gbegen', 'gbeen', 'blue'], ['a', 'a', 'b', 'c']], [['red', 'green', 'blue', 'red', 'red', 'red', 'green', 'green'], ['red', 'green', 'blue', 'red', 'red', 'red', 'green', 'green']], [['green', 'c', 'yellw', 'green', 'green'], ['green', 'c', 'yellw', 'green', 'green']], [['red', 'green', 'blue', 'bluue', 'red', 'red'], ['red', 'green', 'blue', 'bluue', 'red', 'red']], [['a', 'b', 'aa', 'c', 'a'], ['a', 'b', 'aa', 'c', 'a']], [['red', 'greeen', 'red', 'red', 'red', 'red', 'red'], ['red', 'greeen', 'red', 'red', 'red', 'red', 'red']], [['red', 'red', 'red', 'red', 'red', 'yellow', 'red'], ['red', 'red', 'red', 'red', 'red', 'yellow', 'red']], [['green', 'rred', 'yellw'], ['green', 'rred', 'yellw']], [['gbluered', 'yellow', 'belue', 'blue', 'green'], ['gbluered', 'yellow', 'belue', 'blue', 'green']], [['gbluered', 'yellow', 'red', 'blue', 'green', 'red'], ['gbluered', 'yellow', 'red', 'blue', 'green', 'red']], [['red', 'green', 'blue', 'red', 'red', 'dred', 'red'], ['red', 'green', 'blue', 'red', 'red', 'dred', 'red']], [['gbluered', 'yellow', 'byellow', 'breyellowyellow', 'blue', 'green', 'red'], ['gbluered', 'yellow', 'byellow', 'breyellowyellow', 'blue', 'green', 'red']], [['red', 'green', 'blue', 'red', 'red', 'red'], ['red', 'green', 'blue', 'red', 'red', 'red']], [['red', 'green', 'yellow'], ['red', 'green', 'yellow']], [['gbegen', 'a', 'b', '', 'c'], ['gbegen', 'a', 'b', '', 'c']], [['blue', 'red', 'red', 'blueccc', 'cc', 'red', 'red', 'blueccc'], ['blue', 'red', 'red', 'blueccc', 'cc', 'red', 'red', 'blueccc']], [['red', 'green', 'blue', 'yellow'], ['a', 'b', 'b', 'c', 'b', 'a']], [['red', 'green', 'blue', 'red', 'blue', 'green'], ['b', 'c', 'bb', 'a', 'b', 'c']], [['green', 'blue', 'yellow', 'green'], ['a', 'b', 'c', 'a', 'a']], [['green', 'blue', 'bluue', 'red', 'red', 'red'], ['green', 'blue', 'bluue', 'red', 'red', 'red']], [['red', 'red', 'red', 'gbegen'], ['a', 'a', 'a', 'a']], [['red', 'red', 'rebd', 'red', 'bluered', 'red', 'red'], ['red', 'red', 'rebd', 'red', 'bluered', 'red', 'red']], [['red', 'green', 'blue', 'eblue', 'yellw', 'yellow', 'blue', 'blue'], ['red', 'green', 'blue', 'eblue', 'yellw', 'yellow', 'blue', 'blue']], [['aa', 'bluue', 'a', 'a', 'a'], ['aa', 'bluue', 'a', 'a', 'a']], [['red', 'rred', 'green', 'blue', 'yellw', 'eblue', 'yelolow', 'blue'], ['red', 'rred', 'green', 'blue', 'yellw', 'eblue', 'yelolow', 'blue']], [['a', 'b', '', 'c', 'a', 'a', 'aa'], ['red', 'green', 'blue', 'yellow']], [['red', 'green', 'red', 'green', 'blue'], ['red', 'green', 'red', 'green', 'blue']], [['red', 'green', 'blue', 'yellow'], ['a', 'b', 'c', 'green', 'a', 'a']], [['red', 'yellow', 'red'], ['red', 'yellow', 'red']], [['red', 'green', 'green', 'green', 'green'], ['red', 'green', 'green', 'green', 'green']], [['green', 'rred', 'yellw', 'breyellowyellow', 'green'], ['green', 'rred', 'yellw', 'breyellowyellow', 'green']], [['green', 'blue', 'yellow', 'green'], ['a', 'b', 'c', 'a']], [['reed', 'blue', 'red', 'red', 'red'], ['reed', 'blue', 'red', 'red', 'red']], [['blueccc', 'blue', 'red', 'red', 'blueccc', 'red', 'cc', 'red', 'blueccc', 'red'], ['blueccc', 'blue', 'red', 'red', 'blueccc', 'red', 'cc', 'red', 'blueccc', 'red']], [['red', 'green', 'green', 'green', 'bb'], ['ccc', 'b', 'b', 'b', 'ccc']], [['b', 'green', 'rred', 'yellw', 'breyellowyellow', 'breyellowyellow', 'green'], ['b', 'green', 'rred', 'yellw', 'breyellowyellow', 'breyellowyellow', 'green']], [['gbluered', 'yellow', 'bb', 'belue', 'rebd', 'blue', 'green', 'yellow'], ['gbluered', 'yellow', 'bb', 'belue', 'rebd', 'blue', 'green', 'yellow']], [['red', 'greeen', 'blue', 'red', 'red', 'reyellowd', 'red'], ['red', 'greeen', 'blue', 'red', 'red', 'reyellowd', 'red']], [['red', 'blue', 'yellow', 'yellow'], ['red', 'blue', 'yellow', 'yellow']], [['red', 'green', 'eblue', 'blue'], ['a', 'b', 'b', 'c']], [['red', 'green', 'gbluered', 'blue', 'bluue', 'gbluered', 'red', 'red'], ['red', 'green', 'gbluered', 'blue', 'bluue', 'gbluered', 'red', 'red']], [['ared'], ['blue', 'red', 'red', 'red', 'red']], [['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], ['a', 'b', 'ared', 'c', 'a', 'b', 'c', 'a']], [['red', 'red', 'red', 'red', 'red', 'red', 'red', 'rrebded'], ['a', 'b', 'ared', 'c', 'a', 'b', 'c', 'a']], [['a', 'b', 'abluered', 'aa', 'c', 'aa', 'aa'], ['a', 'b', 'abluered', 'aa', 'c', 'aa', 'aa']], [['a', '', 'a', 'b', 'b'], ['a', '', 'a', 'b', 'b']], [['gbegen', 'a', 'b', 'c', 'c'], ['gbegen', 'a', 'b', 'c', 'c']]]
results = [True, False, False, True, True, True, True, True, True, True, True, True, False, True, False, False, True, True, False, False, True, False, False, False, True, False, False, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, False, False, False, True, True, True, False, True, False, False, True, True, True, True, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, True, False, True, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, False, True, False, True, False, True, True, True]

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
        func_name = "is_samepatterns"
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
        for test_case in ['assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True', 'assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False', 'assert is_samepatterns(["red","green","greenn"], ["a","b"])==False']:
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
