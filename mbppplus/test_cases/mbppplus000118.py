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
inputs = [[[1, 2, 'abc', 1.2]], [[1, 2, 3]], [[1, 1.2, 4, 5.1]], [[1, [2, 3], 'abc', {'4': 5}, [6, 7]]], [[]], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [[[1, 2], [3, 4], [5, 6], [7, 8]]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[[9]]]]], [[1, 2, 3, 4, 5]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]], [[1, [2, [3, [4, [5]]]]]], [[[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]]], [[[['a', 'b'], ['c', 'd']], [['e', 'f'], ['g', 'h']]]], [[[[1, 'a'], ['b', 2]], [[3, 'c'], ['d', 4]]]], [[[[1, 2], [3, 4]], [[[5, 6]]]]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]], [[[[1, 2], [3, 4]], [[5, 6]], [[[9]]]]], [[11, 1]], [[11, 1, 1]], [[[1, 2], [1, 4], [5, 6], [7, 8], [5, 6]]], [[[1, 4], [5, 6], [7, 8], [5, 6]]], [[[3, 4], [5, 6], [7, 8]]], [[[3, 4, 3], [5, 6], [7, 8]]], [[[[1], [2], [3]], [[7], [8], [9]]]], [['kPNXDG', 'SHDvQ', 'f', 'g', 'abc', 'LBmjm', 'Us', 'abc', 'a']], [['kPNXDG', 'SHDvQ', 'f', 'g', 'abc', 'LBmjm', 'Us', 'abbc', 'a', 'g']], [[[[1, 2], [3, 4]], [[5, 6]], [], []]], [[[[1, 2, 3], [4, 6]], [[1, 2, 3], [4, 6]], [[10, 11, 12]], [[10, 11, 12]]]], [[[[[9], [9]]], [[1, 2], [3, 4]], [[5, 6]], [[[9], [9]]], [[[9], [9]]]]], [[1, [2, 3, 2], 'abc', {'4': 5}, [6, 7]]], [[[[1], [2], [3]], [[7], [8], [9]], [[7], [8], [9]]]], [[1, [2, 3], [2, 7], 'abc', {'4': 5}, [6, 7]]], [[[[1, 'a'], ['b', 2], [1, 'a']], [[3, 'c'], ['d', 4], ['d', 4]]]], [[[[1, 2, 3], [4, 6]], [[1, 2, 3], [4, 6]], [], [], []]], [[1, [2, 3], [2, 7], 'abc', {'4': 5}, [6, 7], [2, 3]]], [[1, [2, 3], [2, 7], 'abc', {'4': 5}, [7], [2, 3]]], [[[[1, 1], [], [1, 1], [2], []], [[7], [8], [9]], [[1, 1], [], [1, 1], [2], []], [[1, 1], [], [1, 1], [2], []], [[7], [8], [9]]]], [[[3, 4], [5, 6], [7], [7]]], [[[[1, 2, 3], [4, 6]], [[1, 2, 3], [4, 6]], [], [], [], []]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g'], [[1, 2, 3], [4, 6]], [], []]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g'], [[1, 2, 3], [4, 6]], [], [], []]], [[[['a', 'b'], ['c', 'd'], ['a', 'b']], [['e', 'f'], ['g', 'h']]]], [[[[1, 2, 3], [4, 5, 6]]]], [[[[1, 2, 3], [4, 6]], [[1, 2, 3], [4, 6]], [False, 3, 'kPNXDG', 9, ['e'], None], [], [True, True, False, False, False, False, False, False, True]]], [[[['cc', 'd'], ['a', 'b'], ['cc', 'd']], [['e', 'f'], ['g', 'h']]]], [[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]], [[[2, 3], 'abc', {'4': 5}, [6, 7]]], [[1, 1]], [[[3, 4], [5, 6, 5], [5, 6, 5], [7, 11]]], [[[[1, 'a'], ['b', 2]], [[3, 'c'], ['dd', 4]], [[3, 'c'], ['dd', 4]]]], [[[[1], [2, 2], [3]], [[4], [5], [6]], [[7], [8], [9]]]], [[[[1, 2], [3, 4]], [[[5, 6]]], [[[5, 6]]]]], [[[[1, 2], [3, 4]], [[5, 6], [5, 6]], [], []]], [[[[1, 2], [3, 4]], [], [], [], []]], [[11, 1, 0]], [[[1, 2], [5, 6, 5], [1, 4], [5, 6, 5], [7, 8, 8], [5, 6, 5], [5, 6, 5]]], [[[[1, 2], [3, 4]], [[5, 6]], [], [[5, 6]], []]], [[[[1, 'a'], ['b', 2]], [[3, 'c'], ['dd', 4]]]], [[[[1, 2, 3], [4, 5], [4, 5]], [[1, 2, 3], [4, 5], [4, 5]], [[1, 2, 3], [4, 5], [4, 5]]]], [[[4], [5, 6, 5, 5], [5, 6, 5, 5], [5, 6, 5, 5], [7, 11]]], [[1, [2, [3, [4, [5]]]], [2, [3, [4, [5]]]]]], [[[3, 4], [5, 6], [], []]], [['kPNXDG', 'SHDvQ', 'f', 'g', 'abc', 'LBmjm', 'Us', 'abc', 'a', 'abc']], [[[4], [5, 6, 5, 5], [5, 6, 5, 5], [7, 11], [5, 6, 5, 5]]], [[[[1, 2], [3, 4]], [[5, 6], [5, 6], [5, 6]], [[5, 6], [5, 6], [5, 6]], [], []]], [[1]], [[[['c'], ['c'], ['d', 4]], [[1, 'a'], ['b', 2]], [['c'], ['c'], ['d', 4]]]], [[[[1, 2, 3], [4, 6]], [[1, 2, 3], [4, 6]], [False, 3, 'kPNXDG', 9, ['e'], None], [], [True, True, False, False, False, False, False, False, False, True]]], [[[2, 4], [5, 6], [], []]], [[[[1, 2, 3], [4, 6]], [], []]], [[[['e', 'f'], ['g', 'h'], ['e', 'f']], [['cc', 'd'], ['a', 'b'], ['cc', 'd']], [['e', 'f'], ['g', 'h'], ['e', 'f']], [['e', 'f'], ['g', 'h'], ['e', 'f']]]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[5, 6], [7, 8]]]], [[[[[9], [9], [9]]], [], [[1, 2], [3, 4]], [], [[[9], [9], [9]]], [[[9], [9], [9]]]]], [[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]], [['kPNXDG', 'SHDvQ', 'g', 'abc', 'LBmjm', 'Us', 'abc', 'a']], [[[[1, 2], [3, 4]], [], [True, False, False, True, False, True, True, True, True, False], [], [], []]], [[[[5, 6], [1, 2, 3], [5, 6], [1, 2, 3]], [[5, 6], [1, 2, 3], [5, 6], [1, 2, 3]], [[5, 6], [1, 2, 3], [5, 6], [1, 2, 3]]]], [[[['e', 'f'], ['g', '', 'h'], ['e', 'f']], [['a', 'bb'], ['cc', 'd'], ['a', 'bb'], ['cc', 'd']], [['a', 'bb'], ['cc', 'd'], ['a', 'bb'], ['cc', 'd']], [['e', 'f'], ['g', '', 'h'], ['e', 'f']], [['e', 'f'], ['g', '', 'h'], ['e', 'f']], [['e', 'f'], ['g', '', 'h'], ['e', 'f']], [['e', 'f'], ['g', '', 'h'], ['e', 'f']]]], [[[1, 2], [1, 4], [5, 6], [7, 8], [5, 6], [1, 2]]], [[[[1, 2]], [[5, 6], [7, 8]], [[[9]]]]], [[1, [2, 3], {'4': 13}, [2, 7], 'abc', {'4': 13}, 15, [6, 7]]], [[[1, 2], [1, 4], [5, 6], [5, 6]]], [[1, [2, 3], '', {'4': 5}, [6, 7]]], [[[[1, 2], [3, 4]], [True, False, False, True, False, True, True, True, True, False], [], [], []]], [['kPNXDG', 'SHDvQ', 'g', 'abc', 'LBmjm', 'Us', 'abc', 'a', 'SHDvQ']], [[[[1, 2], [8, 3, 4]], [[5, 6]], [[1, 2], [8, 3, 4]], [[[9]]], [[1, 2], [8, 3, 4]]]], [[[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]], [[7], [8], [9]]]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[5, 6], [7, 8]], [[5, 6], [7, 8]]]], [[4]], [[[3, 4, 3], [5, 6], [7, 8], [5, 6]]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g', 'JUVQOY'], [[1, 2, 3], [4, 6]], [], ['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g', 'JUVQOY'], [], [[[59, 11, 30]], False, 11.194887701191348, -32.617974916245785, False, -30, 'h', False], []]], [[[['e', 'f'], ['hh', 'g', '', 'h']], [['e', 'f'], ['hh', 'g', '', 'h']], [['a', 'bb'], ['cc', 'd'], ['a', 'bb'], ['cc', 'd']], [['a', 'bb'], ['cc', 'd'], ['a', 'bb'], ['cc', 'd']], [['e', 'f'], ['hh', 'g', '', 'h']], [['e', 'f'], ['hh', 'g', '', 'h']], [['e', 'f'], ['hh', 'g', '', 'h']], [['e', 'f'], ['hh', 'g', '', 'h']]]], [[[[1, 2], [8, 3, 4]], [[5, 6]], [[1, 2], [8, 3, 4]], [[[9]]]]], [[11]], [[[[1], [2], [3]], [[7], [8], [9]], [[1], [2], [3]]]], [[[3, 4, 3], [5, 6], [7, 8], [5, 6], [5, 6]]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g'], [[1, 2, 3], [4, 6]], [True, False, False, True, True, False, True], [], []]], [[[[1, 2], [3, 4]], [[5, 6], [5, 6]], [], [], []]], [[[3, 11, 3], [5, 6], [3, 11, 3], [7, 8]]], [[[['a', 'b'], ['c', 'd']], [['c', 'e', 'f'], ['c', 'e', 'f'], ['g', 'h']], [['c', 'e', 'f'], ['c', 'e', 'f'], ['g', 'h']]]], [[[2], {'4': 5}, [6, 7]]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g'], [[1, 2, 3], [4, 6]], [True, False, False, True, True, False, True], [], ['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g']]], [[[[1, 2, 3], [4, 6]], [[1, 2, 3], [4, 6]], [[13, 10, 11, 12], [13, 10, 11, 12]], [[13, 10, 11, 12], [13, 10, 11, 12]]]], [[[], [], [], [False, [True, True], 8.958597109125321, [-32.617974916245785, -32.617974916245785], 'vxnCJetyq', -57.174621216111944, -51, 50, 11.194887701191348]]], [[[['e', 'f'], ['g', 'h']], [['e', 'f'], ['g', 'h']]]], [[-32.617974916245785, 56.289568976775286, 65.82961136010562, 65.82961136010562]], [[[[1, 2], [8, 3, 4]], [[5, 6]], [[1, 2], [8, 3, 4]], [[1, 2], [8, 3, 4]]]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g'], [[4, 6]], [True, False, False, True, True, False, True], [], [], []]], [[[4, 5, 6, 6], [1, 2, 3], [4, 5, 6, 6], [7, 8, 9], [1, 2, 3]]], [[['abbc', 'abbc', 'SHDvQ', 'JUVQOY', 'ysuXY', 'g'], [[4, 6]], [True, False, False, True, True, False, True], [], [], [True, True, False, True]]], [[[3, 4], [6, 6], [6, 6], [7, 8]]], [['kPNXDG', 'SHDvQ', 'g', 'abc', 'LBmjm', 'Us', 'abc', 'SHDvQ']], [[[[1, 1, 3], [4, 5, 6]]]], [['kPNXDG', 'SHDvQ', 'f', 'g', 'abc', 'Us', 'abc', 'a', 'abc']], [[[[1], [2], [3]]]], [['kPNXDG', 'aa', 'SHDvQ', 'f', 'g', 'abc', 'LBmjm', 'Us', 'abbc', 'a', 'g', 'a']]]
results = [2, 3, 2, 1, 0, 0, 0, 0, 0, 5, 0, 1, 0, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        func_name = "count_integer"
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
        for test_case in ["assert count_integer([1,2,'abc',1.2]) == 2", 'assert count_integer([1,2,3]) == 3', 'assert count_integer([1,1.2,4,5.1]) == 2']:
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
