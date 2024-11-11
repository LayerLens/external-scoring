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
inputs = [[('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e'), 'r'], [('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e'), '5'], [('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e'), 3], [(), 5], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), ['a', 'b', 'c']], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), {'name': 'John', 'age': 25}], [(['a', 'b', 'c'], ['name', 'age', 25], True, 42.5), 'd'], [(), 'element'], [(['a', ['b', 'c'], 'd'], ['e', ['f', 'g'], 'h']), ['f', 'g']], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25}, True, 42.5), {'name': 'John', 'age': 25}], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5), {'name': 'John', 'age': 25}], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5), {'name': 'John'}], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, True, 42.5, {'age': 25}), {'name': 'John', 'age': 25, 'b': 'Jnameohn'}], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), {'name': 'John', 'age': 25, 'nanme': 'Jnohn'}], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25}, True), {'name': 'John', 'age': 25}], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.5), [['abc', 123, [1, 2, 3]], True, 42.5]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), ['a', 'b', 'c', 'a']], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), {'name': 'John'}], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25, 'nname': 25}, True, 42.5), {'name': 'John', 'age': 25}], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25, 'nname': 25}, True, True, 42.5), {'name': 'John', 'age': 25}], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5, 42.5), [['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5]], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5, {'age': 25}, {'age': 25}), {'name': 'John', 'age': 25, 'b': 'Jnameohn'}], [(), [-63, 81, True]], [(True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25, 'nname': 25}, True, False, 42.5), [['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25, 'nname': 25}, True, False, 42.5]], [(False, 38, 96, -63), [-63, 81, True, True]], [(42.5, ['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25, 'nname': 25}, True, 42.5), {'name': 'John', 'age': 25, 'a': 'hJohn'}], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, 42.5]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), ['a', 'aabc', 'b', 'c']], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.5]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]]), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.5]], [(False, True, False, False, True, True, False), 'element'], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.964943519254135]], [(['abc', 123, [1, 2, 3]], {'age': 25}, True), {}], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), ['aabc', 'b', 'c']], [(42.964943519254135, 42.5, 53.132901816322374, 42.5), [42.964943519254135, 42.5, 53.132901816322374, 42.5]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], False, ['acbc', [1, 2, 3]], 42.964943519254135]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, ['a', 'b', 'c']), [False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5, True), [['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5, 42.5]], [(False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, False, True, 42.5), [False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, False, True, 42.5]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), {'name': 'John', 'age': 25, 'agae': 'Jonamehn'}], [(), [-63, 81, True, True]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 43.45102708398019, True]], [(True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 43.45102708398019, True, 43.45102708398019]], [(False, ['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], False, 42.964943519254135]], [(['abc', 123, [1, 2, 3]], True, 43.45102708398019, True), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135]], [(51.13966106560641, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), {'name': 'John', 'age': 25}], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 43.45102708398019, False, True]], [(True, 42.5), [['abc', 123, [1, 2, 3]], True, 42.5]], [(True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, True), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, True]], [(['abc', 123, [1, 2, 3]], False, True, 42.5), [['abc', 123, [1, 2, 3]], False, True, 42.5]], [(['abc', 123, [1, 2, 3]], {'age': 26}, True, ['abc', 123, [1, 2, 3]]), {}], [(False, 96, -63), [-63, 81, True, True]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], [123, [1, 2, 3]], 42.964943519254135), [True, 42.5]], [(51.13966106560641, 2, -50.96670632000566, 15, 42.5, 99.96452985516729, True, 2), 5], [(['abc', 123, 123, [1, 2, 3]], True, 43.45102708398019, True), [['abc', 123, [1, 2, 3]], True, 43.45102708398019, True]], [({'age': 25}, 61.19815696347994, True, 42.5, 42.5), [['abc', 123, [1, 2, 3]], {'age': 25}, 61.19815696347994, True, 42.5, 42.5]], [(False, 38, 96, -63), [81, True, True]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], True), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 43.45102708398019, True]], [(['abc', 123, [1, 2, 3]], False, True, 43.45102708398019, True), [['abc', 123, [1, 2, 3]], True, 43.45102708398019, True]], [(False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['abc', 123, [1, 2, 3]], True, [[1, 2, 3]], ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135, 42.964943519254135]], [(['a', 'b', 'c', 'a'], {'name': 'John', 'age': 25}, True, 42.5), [['a', 'b', 'c', 'a'], {'name': 'John', 'age': 25}, True, 42.5]], [(True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, True), [True, ['a', 'b', 'c'], False, {'name': 'John', 'age': 25}, True, 42.5, True]], [(['abc', 123, [1, 2, 3]], False, True, 43.45102708398019, True), [['abc', 123, [1, 2, 3]], 43.45102708398019, True]], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25}, True, False, 53.132901816322374), [['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25}, True, False, 42.5, ['abc', 123, [1, 2, 3]]]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['abc', 'ab', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], False, 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], False, 42.964943519254135]], [(False, ['a', 'b', 'c'], {'name': 'John', 'age': 81}, False, {'name': 'John', 'age': 81}, True, 42.5), [False, ['a', 'b', 'c'], {'name': 'John', 'age': 81}, False, True, 42.5, False]], [(False, 38, 96, -63), [False, 38, 96, False]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3], 'abc']), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]]]], [(False, ['a', 'b', 'c'], {'name': 'John'}, False, {'name': 'John'}, True, {'name': 'John'}, 42.5, {'name': 'John'}), [False, ['a', 'b', 'c'], {'name': 'John'}, False, {'name': 'John'}, True, 42.5, {'name': 'John'}]], [(False, ['a', 'b', 'c'], False, {'name': 'John', 'age': 81}, False, True, False, False, 42.5, False), [False, ['a', 'b', 'c'], False, {'name': 'John', 'age': 81}, False, True, False, 42.5, False]], [(True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, True]], [(False, True, False, False, True, True, True, False), [False, True, False, False, True, True, False]], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, True, 42.5, {'age': 25}, True), {'name': 'John', 'age': 25, 'b': 'Jnameohn'}], [(True, [[1, 2, 3]], ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, [[1, 2, 3]], 42.964943519254135]], [(['abc', 123, [1, 2, 3]], True, True, 42.5), [['abc', 123, [1, 2, 3]], False, True, 42.5]], [(['abc', 123, [1, 2, 3]], True, ['abc', 123, [1, 2, 3], 'abc'], 42.5), [['abc', 123, [1, 2, 3]], True, 42.5]], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5), [['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5]], [(False, False, 38, 96, False), [False, 38, 96, False]], [(False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, True]], [(['abc', 123, [1, 2, 3]], {'name': 'John', 'age': 25}, True, 42.5), {}], [(['abc', 123, [1, 2, 3]], False, True, 43.45102708398019, True), [['abc', 123, [1, 2, 3]], ['abc', [1, 2, 3]], True, True, 43.45102708398019, True]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', [1, 2, 3], 'abc'], ['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 43.45102708398019, True]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, ['a', 'b', 'c'], True), [False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5]], [(['abc', 123, [1, 2, 3]], False, True, 42.5), [['abc', 123, [1, 2, 3]], False, True, 42.5, False]], [(51.13966106560641, 2, -50.96670632000566, 15, 42.5, 99.96452985516729, True, 2), [51.13966106560641, 2, -50.96670632000566, 15, 42.5, 99.96452985516729, True, 2, -50.96670632000566]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], True), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], True]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, ['a', 'b', 'c']), [['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, ['a', 'b', 'c']]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5), ['b', 'c', 'a']], [(['abc', 123, [1, 2, 3]], True, 42.5, 42.5), [['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5, 42.5]], [(['abc', 123, [1, 2, 3]], ['abc', [1, 2, 3], 'abc']), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], ['abc', 123, [1, 2, 3]]]], [(-63, 81, True, True), [-63, 81, True, True]], [(['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 53.132901816322374), ['a', 'aabc', 'b', 'b']], [(False, ['abc', 123, [1, 2, 3]], True, True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], False, 42.964943519254135]], [(['abc', 123, [1, 2, 3]], ['abc', [1, 2, 3], 'abc'], ['abc', 123, [1, 2, 3]]), [['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], ['abc', 123, [1, 2, 3]]]], [(['a', ['b', 'c', 'c'], 'd'], ['e', ['f', 'g'], 'h']), ['f', 'g']], [(38, 96, -63), [False, 38, 96, False]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], [123, [1, 2, 3]], True), [[123, -63, [1, 2, 3]], ['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], True]], [(['abc', 123, [1, 2, 3]], {'age': 25}, True, 42.5, {'age': 25}, True, {'age': 25}), {'name': 'e', 'age': 25, 'b': 'Jnameohn'}], [(['a', 'b', 'c', 'a'], ['', 'b', 'c', 'a'], {'name': 'John', 'age': 25}, True, 42.5), [['a', 'b', 'c', 'a'], {'name': 'John', 'age': 25}, True, 42.5]], [(['a', 'aabcb', 'c', 'aabcb'], ['a', 'b', 'c'], ['a', 'aabcb', 'c'], {'name': 'John', 'age': 25}, True, ['a', 'b', 'c']), [['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, ['a', 'b', 'c']]], [(False, False, 38, 96, False), [False, False, False, 38, 96, False]], [(['abc', 123, [1, 2, 3]], True, ['abc', [1, 2, 3]], 42.964943519254135), [['abc', 123, [1, 2, 3]], True, ['abcc', [1, 2, 3]], 42.964943519254135]], [(False, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, False, 42.5), [True, ['a', 'b', 'c'], {'name': 'John', 'age': 25}, True, 42.5, True]], [(51.13966106560641, 2, -50.96670632000566, 15, 42.5, 99.96452985516729, True, 2, 51.13966106560641), 5]]
results = [True, False, True, False, True, True, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "check_tuplex"
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
        for test_case in ['assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),\'r\')==True', 'assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),\'5\')==False', 'assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True']:
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
