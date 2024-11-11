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
inputs = [[['red', 'black', 'white', 'green', 'orange'], 'ack'], [['red', 'black', 'white', 'green', 'orange'], 'abc'], [['red', 'black', 'white', 'green', 'orange'], 'ange'], [[], 'abc'], [[], ''], [[], 'abac'], [[], 'aabac'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'aabac'], [[], 'acbc'], [[], 'aabaac'], [[], 'acbacbcc'], [['aabac', '', 'aabac'], 'aabac'], [['acbc', 'acbacbcc'], 'acbacbcc'], [['acbc', 'acbacbcc'], 'acbacbccacbacbcc'], [['acabcbc', 'acbacbcc'], 'acbacbccacbacbcc'], [['mHUIYqZU', 'acabcbc', 'acbacbcc'], 'acbacbccacbacbcc'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'aacbac'], [['acbacbccacbacbcc', 'acbacbcc'], 'acbacbccaacbacbcc'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'aabaac'], [['acabcbc', 'acbabcbc', 'acbacbcc'], 'acbacbccacbacbcc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'acbacbccaacbacbcc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'acbacbccaaccbacbcc'], [['amHUIYqZUcbc', 'acbc', 'acbacbcc'], 'acbacbccacbacbcc'], [['acabcbc', 'acbacbcc', 'acbacbcc'], 'acbacbccacbacbcc'], [[], 'abcbacbcc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'mHUIYqZU'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'amHUIYqZUcbc', 'abc', 'acbacbccacbacbcc'], 'acbacbccaaccbacbcc'], [['acbacbccacbcacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'acbacbccaaccbacbcc'], [['acbacbccacbcacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'acbacbccaaccacbacbccaaccbacbccbacbcc'], [[], 'aacbacacbacbccacbacbcc'], [['acbacbccacbacbcc', 'acbacbcc'], 'acbacbccaacbaccc'], [[], 'accbc'], [[], 'acbacbccacbcacbcc'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'aacb'], [['', 'aabac', 'mHUIYqZU'], 'aabaac'], [['aabac', 'abc', 'aabac', 'mHUIYqZU'], 'aabaac'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'mHUIYqZU'], [['acbaccbcc'], 'acbacbccaacbacbcc'], [['acbacbccacbacbcc', 'mHUIYqZU'], 'abcaacb'], [['acabcbc', 'acbacbccaacbacbcc', 'acbacbcc'], 'acbacbccacbacbcc'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac'], 'acbaccbccaacb'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'acbaccbccaacb'], [['acabcbc', 'acbacbcc', 'acbacbcc'], 'acbacbccaaccacbacbccaaccbacbccbacbcc'], [['acacbc', 'acbacbcc'], 'acbacbcc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'mHUIZU'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'aacbb'], [['acabcbc', 'acbabcbc', 'acbacbcc'], 'acbacbccacbacacbacbccaacbacbccbcc'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'mHUIYamHUIYqZUcbcqZU'], [['acbacbccacbacbcc', 'amHUIYqZUcbc', 'acbc', 'acbacbcc'], 'acbacbccacbacbcc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'acbacbccaaccbacbaacbacacbacbccacbacbcccc'], [[], 'acbcbacbcc'], [['acbacbccaaccacbacbccaaccbacbccbacbcc', 'acabcbc', 'acbabcbc', 'acbacbcc'], 'acbacbccacbacacbacbccaacbacbccbcc'], [['aabac', '', 'mHUIYqZU'], 'aacbac'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], ''], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc'], 'mHUIYmHUIYqZUqZU'], [['acbacbccacbcacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc', 'acbacbcc'], 'acbacbccaaccacbacbccaaccbacbccbacbcc'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'mHaacbacacbacbccacbacbccUIYamHUIYqZUcbcqZU', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'mHUIYamHUIYqZUcbcqZU'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'acbaccbccaacb'], [['acabcbc', 'acbabcbc', 'acbacbcc', 'acbabcbc'], 'acbacbccacbacacbacbccaacbacbccbcc'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'aacbac'], [['aacbabcbcabac', 'aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'mHUIYqZU'], [['aabac', '', 'mHUIYqZU'], 'aabaacbbaac'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbc', 'aacbacacbacbccacbacbcc', 'acbacbcc'], 'mHUIYqZU'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'amHUIYqZUcbc', 'acbcbacbcc', 'abc', 'acbacbccacbacbcc'], 'acbacbccaaccbacbcc'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'acbc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbcabcaacbcacbacbcc'], 'acbacbccaaccbacbaacbacacbacbccacbacbcccc'], [['acabcbc', 'acbabcbc', 'acbacbcc'], 'acbaccbccaacb'], [['acbacbccacbacbcc', 'acbacbcc'], 'acbacbccaacba'], [['acabcbc', 'acbabcbc', 'acbacbcc', 'acabcbc'], 'acbaccbccaacb'], [['acbacbccacbacbcc', 'mHUIYqZU'], 'amHUIZUbcaacb'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'abcaacb', 'mHUIYamHUIYqZUcbcqZU'], 'mHUIYamHUIYqZUcbcqZU'], [['acbacbccaaccacbacbccaaccbacbccbacbcc', 'acabcbc', 'acbabcbc', 'acbacbcc'], 'acbacbccacbacacbacbacbccaaccacbacbccaaccbacbccbacbccacbccaacbacbccbcc'], [['aabac', '', 'mHUIZU', 'aabac', 'mHUIYqZU'], 'aabaac'], [['acbacbccacbacbcc', 'amHUIYqZUcbc', 'acbc', 'acbacbcc'], 'acbacbcccacbacbcc'], [['acbacbccacbcacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc', 'acbacbccacbcacbcc'], 'acbacbccaaccbacbcc'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'aaabaac'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'aacbacacbacbccacbacbcc'], 'abc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'amHUIYqZUcbc'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'acbaccbabcbacbccccaacb'], [['aabac', 'aaac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'aacbac'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU', 'aabac'], 'acbaccbabcbacbccccaacb'], [['acabcbc', 'acbacbcc', 'acbacbcc', 'acbacbcc'], 'amHUIYqZUcbc'], [['aabaacbacbccacbcacbccc', 'mHUaacbacacbacbccacbacbcIYqZU', '', 'mHUIZU', 'aabac', 'mHUIYqZU'], 'acbacbccaacbaccc'], [['aabac', '', 'mHUIaacbabcbcabacYqZU'], 'aacbac'], [['acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbacbccacbacbcc'], 'acbacbccaaccbacbaacbacacbacbccacbacbcccc'], [['acbacbccaaccacbacbccaaccbacbccbacbcc', 'acabcbc', 'acbabcbc', 'acbacbcc'], 'acbacbccacbacacbacbacbccaaccacbacbccaaccbacbcccbacbccacbccaacbacbccbcc'], [['aabac', 'acbacbcc'], 'acbacbcc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'aacbacacbacbccacbacbcc'], 'aabc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbccacc', 'acbacbcc', 'acbacbccacbacbcc'], 'mHUIYqZU'], [['aabac', '', 'aabac', 'mHUIYqZU'], 'aacbacabcbcac'], [['acbacbccacbacacbacbccaacbacbccbcc', 'acbacbccaaccbacbcc'], 'aabaacbbaac'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'aacbacacbacbccacbacbcc'], 'abbc'], [['acbacbccacbcacbcc', 'acbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'aacbacacbacbccacbacbcc'], 'a'], [['accbc', 'aabac', '', 'aabac', 'mHUIYqZU'], 'aacb'], [['acbacbccaaccacbacbccaaccbacbccbacbcc', 'acabcbc', 'acbabcbc'], 'acbacbccacbacacbacbacbccaaccacbacbccaaccbacbcccbacbccacbccaacbacbccbcc'], [['aabac', '', 'mHUIZU', 'aabac', 'mHUIYqZU'], 'acbacbcccacbacbcc'], [['acbacbccacbcacbcc', 'aacbbacbacbccacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc', 'acbaccbcc', 'acbacbccacbacbcc'], 'amHUIYqZUcbc'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'abcaacb', 'mHUIYamHUIYqZUcbcqZU'], 'mHUIYamHUIYqZmUcbcqZU'], [[], 'aacbbacbacbccacbacbcc'], [['acbacbccacbcacbcc', 'acbacbcacbaccbccaacbcacbacbcc', 'aacbacacbacbccacbacbcc', 'acbacbcc'], 'mHUIYmHUIYqZUqZU'], [['aabac', '', 'mHUIYqZU'], 'aabaacbaac'], [['acabcbc', 'acbabccbc', 'acbacbcc'], 'acbacbccacbacacbacbccaacbacbccbcc'], [[], 'acaabaacbbaacbc'], [['acbacbccacbacbcc', 'mHUIYqZU', 'mHUIYqZU'], 'amHUIZUbcaacb'], [['aabac', 'aabac', 'mHUIYqZU', 'mHUIYamHUIYqZUcbcqZU', 'aabac', 'aabac', 'mHUIYamHUIYqZUcbcqZU'], 'acbacbcabcaacbcacbacbcc']]
results = [True, False, True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "find_substring"
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
        for test_case in ['assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True', 'assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False', 'assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True']:
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
