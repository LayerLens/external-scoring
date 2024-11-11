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
inputs = [[('ID', 'is', 4, 'UTS')], [('QWE', 'is', 4, 'RTY')], [('ZEN', 'is', 4, 'OP')], [('The', 'quick', 'brown', 'fox')], [()], [(42,)], [(None, None, None, None)], [(None, 42, 'foo', True)], [('hello-world', 'hello', '-', 'world')], [(10, 'Hello', True, 3.14, [1, 2, 3], {'a': 1, 'b': 2})], [(['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'])], [({'a': 1, 'b': 2},)], [([1, 2], [3, 4], [5, 6])], [([1, 2, 3], ['a', 'b', 'c'], [[True, False], ['x', 'y', 'z']])], [(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'])], [('quichk', 'The', 'quick', 'brown', 'fox')], [(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'])], [(False,)], [(10, 'Hello', True, 3.14, [1, 2, 3], {'a': 1, 'b': 2}, True)], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'])], [({'a': 5, 'b': 2},)], [('The', 'quick', 'gbrown', 'fox')], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'], ['a', 'b', 'c'])], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['d', 'cd', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'])], [(['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'], ['UTS', 'is', None])], [(None, 42, 'foo', True, 'foo')], [('awesome', 'quick', 'brown', 'y')], [([5, 6], [3, 4])], [(['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'], ['Python', 'is', 'awesome'])], [(10, 'Hello', True, 3.14, [1, 2, 3])], [('quick', 'brown', 'y')], [(['d', 'Python', 'is', 'awesome'], ['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'], ['Python', 'is', 'awesome'])], [(['aa', 'a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'])], [(['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'], ['Python', 'is', 'awesome'], ['ID', 'is', 4])], [('ID', 'hello-world', 'hello', '-', 'world')], [(10, 'Hello', False, 3.14, [1, 2, 3], {'a': 1, 'b': 2})], [({'b': 2},)], [({'a': 1, 'b': 2, 'aa': 0},)], [([1, 1, 3], [1, 2, 3], ['a', 'b', 'c'], [[True, False], ['x', 'y', 'z']])], [(None, None, None, None, None, None)], [('quichk', 'awesome', 'The', 'quick', 'brown', 'fox')], [({'a': 5, 'b': 42},)], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'], ['aa', 'a', 'b', 'c'])], [([5, 6, 5], [3, 4])], [([1, 1, 3], [1, 2, 3], ['a', 'b', 'c'], [[True, False], ['x', 'y', 'z']], [[True, False], ['x', 'y', 'z']])], [('The', 'quick', 'fox')], [(42, 42)], [(10, 'Helo', True, 3.14, [1, 2, 3])], [(None, 42, 'foo', True, 5, 'foo')], [('brown', 'y', 'brown')], [({'a': 5, 'b': 5},)], [(None, 42, 'foo', True, 'foo', True)], [(['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'], ['UTS', 'is', None], ['UTS', 'is', None])], [(None, 42, 42, 'foo', True, 5, 'foo')], [('quichk', 'awesome', 'The', 'quick', 'brown', 'fox', 'fox')], [(5, 5)], [([1, 2], [3, 4], [1, 2], [5, 6])], [(['a', 'b', 'c'], ['d', 'e', 'f'], ['d', 'UTS', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'])], [(42, 5, 42)], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i', 'i'], ['g', 'h', 'i'])], [('quichk', 'awesome', 'quick', 'brown', 'fox', 'fox')], [(10, True, 'Hello', True, 3.14, [1, 2, 3], {'a': 1, 'b': 2})], [(['ID', 'is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'], [None, 'UTS', 'is', None])], [(4,)], [(5, 10, 42)], [(None, 42, 42, 'foo', True, 5, 'foo', 43, 'foo')], [(5,)], [([1, 2, 3, 3], [1, 1, 3], [1, 2, 3], ['a', 'c'], [[True, False], ['x', 'y', 'z']], [[True, False], ['x', 'y', 'z']])], [('quichk', 'awesome', 'quick', 'brown', 'fox', 'fox', 'fox')], [(True, 5, 5)], [(None, 42, 'ffoo', True, 'foo')], [([True], None, -88, 96.91126492184753, 'PcXu', False)], [(10, 'Helo', True, 3.14, [1, 2, 3], 'Helo')], [([1, 2], [3, 4], [1, 2])], [('awesome', 'quick', 'brown', 'y', 'y')], [('hello-world', 'hello', '-', 'world', 'world')], [(5, 42)], [(None, 42, 'foo', True, 5, 'foo', None)], [(None, 42, 42, 'fo', True, 5, 'foo')], [(4, 'Hello', True, 3.14, [1, 2, 3], {'a': 1, 'b': 2}, True)], [(-100, -22, 6, 5, -22)], [('awesome', 'Hello', 'quick', 'brown', 'y', 'y')], [(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'worldi', 'h', 'i'], ['d', 'UTS', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'])], [('brown', 'y', 'brown', 'brown')], [('y', 'y', 'brown')], [(None, None, None, None, None)], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['d', 'cd', 'e', 'f', 'e'], ['g', 'h', 'i'])], [([1, 2], [3, 4])], [([1, 2, 3, 3], [1, 2, 3], ['a', 'c'], [[True, False], ['x', 'y', 'z']], [[True, False], ['x', 'y', 'z']])], [(None, -88, 96.91126492184753, 'PcXu', False)], [({'a': 1, 'b': 6, 'aa': 0},)], [(['is', 4], ['UTS', 'is', None], ['Python', 'is', 'awesome'])], [(['ID', 'is', 4], ['Python', 'is', 'awesome'], ['Python', 'is', 'awesome'])], [('quichk', 'awesome', 'quick', 'brown', 'fox', 'fox', 'Python')], [({'a': 5, 'b': 2}, {'a': 5, 'b': 2}, {'a': 5, 'b': 2})], [('awesome', 'quick', 'brown', 'y', 'y', 'y', 'y')], [(-18, -100, -75, -41, 80, -42, 51, -69, -69)], [('awesome', 'fooHelo', None, 42, 42, 'foo', True, 5, 'foo')], [([3, 4],)], [('awesome', 'quick', 'fo', 'y', 'y', 'y', 'y')], [(True, -69, 10, 5)], [('hello-world', 'hello', 'UTS', '-', 'world', 'world')], [(None, 42, 42, 'foo', True, 'foo')], [(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'Python', 'i'], ['g', 'h', 'i'])], [(-18, -75, -41, 80, -42, 51, -69, -69, -69)], [(['aa', 'a', 'b', 'c'], ['a', 'b', 'c'], ['g', 'h', 'i'], ['g', 'h', 'i'], ['a', 'b', 'c'])], [(None, 42, 42, 'foo', True, 5, 'foo', 43, 'foo', None)], [(10, 'Hello', True, 3.14, 80, [1, 2, 3], {'a': 1, 'b': 2}, True, [1, 2, 3])], [([1, 2, 3, 3], [1, 1, 3], [1, 2, 3], ['a', 'c'], [[True, False], ['x', 'y', 'z'], [True, False]], [[True, False], ['x', 'y', 'z']], [1, 1, 3])], [('brhello-worldwn', 'y', 'brown')], [({'a': 1, 'b': 2, 'aa': 0}, {'a': 1, 'b': 2, 'aa': 0})], [(['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'worldi', 'h', 'i'], ['d', 'UTS', 'e', 'f'], ['g', 'h', 'i'], ['g', 'h', 'i'], ['a', 'b', 'c'])], [(54, -18)], [(None, 42, 42, 'foo', True, 5, 'foo', 43, 'foo', 42)], [('awesome', 'brown', 'y')]]
results = ['ID-is-4-UTS', 'QWE-is-4-RTY', 'ZEN-is-4-OP', 'The-quick-brown-fox', '', '42', 'None-None-None-None', 'None-42-foo-True', 'hello-world-hello---world', "10-Hello-True-3.14-[1, 2, 3]-{'a': 1, 'b': 2}", "['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']", "{'a': 1, 'b': 2}", '[1, 2]-[3, 4]-[5, 6]', "[1, 2, 3]-['a', 'b', 'c']-[[True, False], ['x', 'y', 'z']]", "['a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']", 'quichk-The-quick-brown-fox', "['a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']", 'False', "10-Hello-True-3.14-[1, 2, 3]-{'a': 1, 'b': 2}-True", "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']", "{'a': 5, 'b': 2}", 'The-quick-gbrown-fox', "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']-['a', 'b', 'c']", "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['d', 'cd', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']", "['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']-['UTS', 'is', None]", 'None-42-foo-True-foo', 'awesome-quick-brown-y', '[5, 6]-[3, 4]', "['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']-['Python', 'is', 'awesome']", '10-Hello-True-3.14-[1, 2, 3]', 'quick-brown-y', "['d', 'Python', 'is', 'awesome']-['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']-['Python', 'is', 'awesome']", "['aa', 'a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']", "['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']-['Python', 'is', 'awesome']-['ID', 'is', 4]", 'ID-hello-world-hello---world', "10-Hello-False-3.14-[1, 2, 3]-{'a': 1, 'b': 2}", "{'b': 2}", "{'a': 1, 'b': 2, 'aa': 0}", "[1, 1, 3]-[1, 2, 3]-['a', 'b', 'c']-[[True, False], ['x', 'y', 'z']]", 'None-None-None-None-None-None', 'quichk-awesome-The-quick-brown-fox', "{'a': 5, 'b': 42}", "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']-['aa', 'a', 'b', 'c']", '[5, 6, 5]-[3, 4]', "[1, 1, 3]-[1, 2, 3]-['a', 'b', 'c']-[[True, False], ['x', 'y', 'z']]-[[True, False], ['x', 'y', 'z']]", 'The-quick-fox', '42-42', '10-Helo-True-3.14-[1, 2, 3]', 'None-42-foo-True-5-foo', 'brown-y-brown', "{'a': 5, 'b': 5}", 'None-42-foo-True-foo-True', "['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']-['UTS', 'is', None]-['UTS', 'is', None]", 'None-42-42-foo-True-5-foo', 'quichk-awesome-The-quick-brown-fox-fox', '5-5', '[1, 2]-[3, 4]-[1, 2]-[5, 6]', "['a', 'b', 'c']-['d', 'e', 'f']-['d', 'UTS', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']", '42-5-42', "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['d', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i', 'i']-['g', 'h', 'i']", 'quichk-awesome-quick-brown-fox-fox', "10-True-Hello-True-3.14-[1, 2, 3]-{'a': 1, 'b': 2}", "['ID', 'is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']-[None, 'UTS', 'is', None]", '4', '5-10-42', 'None-42-42-foo-True-5-foo-43-foo', '5', "[1, 2, 3, 3]-[1, 1, 3]-[1, 2, 3]-['a', 'c']-[[True, False], ['x', 'y', 'z']]-[[True, False], ['x', 'y', 'z']]", 'quichk-awesome-quick-brown-fox-fox-fox', 'True-5-5', 'None-42-ffoo-True-foo', '[True]-None--88-96.91126492184753-PcXu-False', '10-Helo-True-3.14-[1, 2, 3]-Helo', '[1, 2]-[3, 4]-[1, 2]', 'awesome-quick-brown-y-y', 'hello-world-hello---world-world', '5-42', 'None-42-foo-True-5-foo-None', 'None-42-42-fo-True-5-foo', "4-Hello-True-3.14-[1, 2, 3]-{'a': 1, 'b': 2}-True", '-100--22-6-5--22', 'awesome-Hello-quick-brown-y-y', "['a', 'b', 'c']-['d', 'e', 'f']-['g', 'worldi', 'h', 'i']-['d', 'UTS', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']", 'brown-y-brown-brown', 'y-y-brown', 'None-None-None-None-None', "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['d', 'cd', 'e', 'f', 'e']-['g', 'h', 'i']", '[1, 2]-[3, 4]', "[1, 2, 3, 3]-[1, 2, 3]-['a', 'c']-[[True, False], ['x', 'y', 'z']]-[[True, False], ['x', 'y', 'z']]", 'None--88-96.91126492184753-PcXu-False', "{'a': 1, 'b': 6, 'aa': 0}", "['is', 4]-['UTS', 'is', None]-['Python', 'is', 'awesome']", "['ID', 'is', 4]-['Python', 'is', 'awesome']-['Python', 'is', 'awesome']", 'quichk-awesome-quick-brown-fox-fox-Python', "{'a': 5, 'b': 2}-{'a': 5, 'b': 2}-{'a': 5, 'b': 2}", 'awesome-quick-brown-y-y-y-y', '-18--100--75--41-80--42-51--69--69', 'awesome-fooHelo-None-42-42-foo-True-5-foo', '[3, 4]', 'awesome-quick-fo-y-y-y-y', 'True--69-10-5', 'hello-world-hello-UTS---world-world', 'None-42-42-foo-True-foo', "['a', 'b', 'c']-['d', 'e', 'f']-['g', 'Python', 'i']-['g', 'h', 'i']", '-18--75--41-80--42-51--69--69--69', "['aa', 'a', 'b', 'c']-['a', 'b', 'c']-['g', 'h', 'i']-['g', 'h', 'i']-['a', 'b', 'c']", 'None-42-42-foo-True-5-foo-43-foo-None', "10-Hello-True-3.14-80-[1, 2, 3]-{'a': 1, 'b': 2}-True-[1, 2, 3]", "[1, 2, 3, 3]-[1, 1, 3]-[1, 2, 3]-['a', 'c']-[[True, False], ['x', 'y', 'z'], [True, False]]-[[True, False], ['x', 'y', 'z']]-[1, 1, 3]", 'brhello-worldwn-y-brown', "{'a': 1, 'b': 2, 'aa': 0}-{'a': 1, 'b': 2, 'aa': 0}", "['a', 'b', 'c']-['d', 'e', 'f']-['g', 'worldi', 'h', 'i']-['d', 'UTS', 'e', 'f']-['g', 'h', 'i']-['g', 'h', 'i']-['a', 'b', 'c']", '54--18', 'None-42-42-foo-True-5-foo-43-foo-42', 'awesome-brown-y']

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
        func_name = "concatenate_tuple"
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
        for test_case in ['assert concatenate_tuple(("ID", "is", 4, "UTS") ) == \'ID-is-4-UTS\'', 'assert concatenate_tuple(("QWE", "is", 4, "RTY") ) == \'QWE-is-4-RTY\'', 'assert concatenate_tuple(("ZEN", "is", 4, "OP") ) == \'ZEN-is-4-OP\'']:
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
