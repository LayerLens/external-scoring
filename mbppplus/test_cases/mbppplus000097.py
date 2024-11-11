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
inputs = [[(5, 6, 7, 3, 5, 6)], [(1, 2, '4')], [(3, 2, 1, 4, 5)], [(5.5, 7.3, 9.2, 3.1, 6.4)], [('apple', 'banana', 'cherry', 'date')], [([1, 2, 3], [4, 5, 6], [7, 8, 9])], [({'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 35})], [([1, 2], [3, 4], [5, 6])], [(True, False, False, True)], [(1, 'apple', [3, 4], {'name': 'John'})], [([[1, 2], [3]], [[4, 5], [6]], [[7, 8], [9]])], [([{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 35}], [{'name': 'Alice', 'age': 28}, {'name': 'Eve', 'age': 22}])], [(['red', 'green', 'blue'], ['purple', 'orange', 'yellow'])], [([[1, 2, 3], [4, 5, 6], [8, 9, 7]], [[10, 11, 12], [13, 14, 15]])], [([], [1, 2, '3'], {'1': 'one', '2': 'two', '3': 'three'})], [([], {'1': [1, 2, 3], '2': [4, 5, 6]}, [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])], [([[1, 2, 3], [4, 5, 6], [8, 9, 7]], {'10': [10, 20, 30], '11': [40, 50, 60]}, [[1, 2, 3], [4, 5, 6]])], [([1, 2, 3], {'a': 'apple', 'b': 'banana', 'c': 'cherry'}, [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']])], [([['b', 'a'], ['c', 'd']], [1, 2, 3], [4, 5, 6], [[[1], [2], [3]], [[4], [5], [6]]])], [({'1': 'one'}, {'2': 'two'}, {'3': 'three'})], [([1, 2, 'apple'], [3.14, 'banana', 'cherry'], ['date', 20, True])], [([[1, 2], [3.14, 'banana'], ['c', 'b', 'a']], [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']])], [({'1': 'apple', '2': 'banana', '3': 'cherry'}, {'4': [10, 20, 30], '5': [40, '50', 60]}, [[1, 2, 3], [4, 5, 6]])], [([[], [], []], [[], [], []])], [([[[], []], [[], []]], [[[[], []], [[], []]], [[[], []], [[], []]]])], [([{'1': True, '2': False}, {'3': True, '4': True}], [{'5': False, '6': False}, {'7': False, '8': False}])], [([{'9': [1, 2, 3], '10': [4, 5, 6]}, {'11': [7, 8, 9], '12': [10, 11, 12]}], [{'13': [13, 14, 15], '14': [16, 17, 18]}, {'19': [19, 20, 21], '20': [22, 23, 24]}])], [(1, 'apple')], [(4.0, 5.0, 6.0)], [(1, 'apple', True, [1, 2, 3], {'a': 1, 'b': 2})], [(1.5, 'banana', [1, 2, 3], {'a': 1, 'b': 2}, ['apple', 'banana'])], [('dattwo', 'apple', 'banana', 'cherry', 'date')], [([{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 35}, {'name': 'Jane', 'age': 30}], [{'name': 'Alice', 'age': 28}, {'name': 'Eve', 'age': 22}], [{'name': 'Alice', 'age': 28}, {'name': 'Eve', 'age': 22}])], [([[60, 1, 2], [3.14, 'banana'], ['c', 'b', 'a']], [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']])], [([], [1, 2, '3'])], [('chercry', 'dattwo', 'apple', 'banana', 'cherry', 'date')], [('apple', 'banana', 'cherry', 'ccherry', 'date')], [([], {})], [(30, [3, 4], {'name': 'John'})], [({'1': 'apple', '2': 'banana', '3': 'cherry', '11': 'pple'}, {'4': [10, 20, 30], '5': [40, '50', 60]}, [[1, 2, 3], [4, 5, 6]])], [({'name': 'John', 'age': 25}, {'age': 30}, {'name': 'Bob', 'age': 35})], [(True, True, False, True, False, True, False)], [('chercry', 'dattwo', 'apple', 'banana', 'cherry', 'date', 'banana')], [(1, 'green', 1)], [(2, 1, 'apple', 1, 1)], [(1, 'apple', False, True, [1, 2, 3], {'a': 1, 'b': 2})], [({'1': 'apple', '2': 'banana', '3': 'cherry', '11': 'pple'}, [[1, 2, 3]], {'4': [10, 20, 30], '5': [40, '50', 60]}, [[1, 2, 3]])], [('dattwo', 'apple', 'banana', 'cherry', 'date', 'banana')], [({'1': 'apple', '2': 'banana', '3': 'cherry', '11': 'pplJanee'}, {'4': [10, 20, 30], '5': [40, '50', 60]}, [[1, 2, 3], [4, 5, 6]])], [([[1, 2], [3]], [[4, 5], [6]], [[7, 8], [9]], [[4, 5], [6]])], [(True, True, False, True, False, True, False, False)], [([[], [], []], [[], [], []], [[], [], []])], [(1, 'green', 1, 1)], [({'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob'}, {'name': 'Bob'})], [([{'1': True, '2': False}, {'3': True, '4': True}], [{'1': True, '2': False}, {'3': True, '4': True}])], [('apple', 'banana', 'ccherrry', 'cherry', 'ccherry', 'date')], [([[1, 2, 3]],)], [([{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 35}], [{'name': 'Alice', 'age': 28, 'agge': 'Aliredce'}, {'name': 'Eve', 'age': 22}], [{'name': 'Alice', 'age': 28, 'agge': 'Aliredce'}, {'name': 'Eve', 'age': 22}])], [([1, 2], [3, 4], [5, 6], [5, 6])], [([{'1': True, '2': False}, {'3': True, '4': True}], [{'1': True, '2': False}, {'3': True, '4': True}], [{'5': False, '6': False}, {'7': False, '8': False}])], [([], {'20': -27.237212019107332, '41': 7.3, '-10': 5.5, '9': 3.1, '96': 4.0, '25': 5.0})], [([[1, 2], [3]], [[1, 2], [3]], [[4, 5], [6]], [[7, 8], [9], [9]], [[7, 8], [9]])], [([{'1': False, '2': False}, {'1': False, '2': False}, {'3': True, '4': True}], [{'5': False, '6': False}, {'7': False}], [{'5': False, '6': False}, {'7': False}], [{'1': False, '2': False}, {'1': False, '2': False}, {'3': True, '4': True}], [{'1': False, '2': False}, {'1': False, '2': False}, {'3': True, '4': True}])], [([],)], [([{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 35}], [{'name': 'Alice', 'age': 28, 'agge': 'Aliredce', '3': 'c'}, {'name': 'Alice', 'age': 28, 'agge': 'Aliredce', '3': 'c'}, {'name': 'Eve', 'age': 22}], [{'name': 'Alice', 'age': 28, 'agge': 'Aliredce', '3': 'c'}, {'name': 'Alice', 'age': 28, 'agge': 'Aliredce', '3': 'c'}, {'name': 'Eve', 'age': 22}], [{'name': 'Alice', 'age': 28, 'agge': 'Aliredce', '3': 'c'}, {'name': 'Alice', 'age': 28, 'agge': 'Aliredce', '3': 'c'}, {'name': 'Eve', 'age': 22}])], [([{'3': True}, {'3': True}], [{'3': True}, {'3': True}], [{'3': True}, {'3': True}], [{'3': True}, {'3': True}], [{'3': True}, {'3': True}])], [({'1': 'one'}, {'2': 'two'}, {'3': 'three', '20': 'Alice'}, {'3': 'three', '20': 'Alice'})], [('banana', 'ccherrry', 'cherry', 'ccherry', 'date')], [({'name': 'John', 'age': 25}, {'name': 'Jnane', 'age': 30}, {'name': 'Jnane', 'age': 30}, {'name': 'Bob', 'age': 35})], [([[], [], []],)], [([], {}, [])], [([['b', 'a'], ['c', 'd'], ['b', 'a']], [1, 2, 3], [4, 5, 6, 5], [[[1], [2], [3]], [[4], [5], [6]]])], [([1, 2, 3], {'a': 'apple', 'b': 'banana', 'c': 'cherry'}, [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']], [1, 2, 3])], [([{'3': True}], [{'3': True}], [{'3': True}], [{'3': True}], [{'3': True}])], [({'name': '3John', 'age': 25}, {'age': 17}, {'age': 17}, {'age': 17}, {'name': 'Bob', 'age': 35})], [(False, True, False, True, False, True, False)], [([{'1': True, '2': False}, {'3': True, '4': True}], [{'1': True, '2': False}, {'3': True, '4': True}], [{'5': False, '6': False}, {'7': False, '8': False}], [{'1': True, '2': False}, {'3': True, '4': True}])], [(1.5, 'banana', [1, 2, 3], {'b': 2}, ['apple', 'banana'])], [([{'1': False, '2': False}, {'1': False, '2': False}], [{'5': False, '6': False}, {'7': False}], [{'5': False, '6': False}, {'7': False}], [{'1': False, '2': False}, {'1': False, '2': False}], [{'1': False, '2': False}, {'1': False, '2': False}], [{'1': False, '2': False}, {'1': False, '2': False}], [{'5': False, '6': False}, {'7': False}])], [({'32': 'P', '6': '3John', '96': 'apple', '50': 'oIZ', '9': 'Alice', '-60': 'Jane'}, [], {})], [([2, 3, 4, 4], {'name': 'John'})], [(2, 1, 1, 1)], [([['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []], [['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []], [[], [], []])], [('apple', 'banana', 'cherry', 'cherry', 'date')], [('chercry', 'dattwo', 'apple', 'banana', 'cherry')], [([1, 2, '3', '3'], [], [1, 2, '3'], [93.91696605104102, 9.2, -41.18839790246442, 7.3], {'1': 'one', '2': 'two', '3': 'three'})], [([['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []], [['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []], [[], [], []], [['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []])], [(2, 'green', 1, 1)], [([[60, 1, 2], ['c', 'b', 'a']], [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']], [[60, 1, 2], ['c', 'b', 'a']], [[60, 1, 2], ['c', 'b', 'a']])], [(30, [3, False, 4], {})], [(1, 1, 'gnamereen', 1, 1, 1, 1, 1)], [({'1': 'one', '2': 'two', '3': 'tbhree', '25': 'c'}, {'1': 'one', '2': 'two', '3': 'tbhree', '25': 'c'}, [], [1, 2, '3'], {'1': 'one', '2': 'two', '3': 'tbhree', '25': 'c'})], [([[1, 2, 3], [4, 5, 6], [8, 9, 7]], {'10': [10, 20, 30], '11': [40, 50, 60]}, [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])], [([{'3': True}, {'3': True}], [{'3': True}, {'3': True}], [{'3': True}, {'3': True}], [{'3': True}, {'3': True}])], [(1, 'green', 1, 1, 1)], [(1.5, 'banana', [1, 2, 3], {'b': 2}, ['apple', 'banana'], {'b': 2})], [([[3.14, 'banana'], ['c', 'b', 'a']], [[3.14, 'banana'], ['c', 'b', 'a']])], [(2, 'green', 1, 'Aliredce', 1, 'Aliredce')], [('chercry', 'dattwo', 'apple', 'banana', 'cherry', 'cherry', 'dattwo')], [([1, 1, 3], {'a': 'apple', 'b': 'banana', 'c': 'cherry'}, [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']])], [(1, 'apple', False, True, [17, 1, 2, 3], [17, 1, 2, 3], {'a': 1, 'b': 2})], [([{}], [{}], [{}], [{}], [{}], [{}])], [([{'1': True, '2': False}, {'3': True, '4': True}], [{'1': True, '2': False}, {'3': True, '4': True}], [{'7': False, '8': False}], [{'1': True, '2': False}, {'3': True, '4': True}])], [([True, 26, 8.278263346367723, 'Jane', 'XRuBLHNn', False, -80], [])], [(['tbhree', 'vDRltNQ', 'pplJanee', 'cherry'], {})], [([{'1': False}, {'1': False}, {'1': False}, {'3': True, '4': True}], [{'5': False, '6': False}, {'7': False}], [{'5': False, '6': False}, {'7': False}], [{'1': False}, {'1': False}, {'1': False}, {'3': True, '4': True}], [{'1': False}, {'1': False}, {'1': False}, {'3': True, '4': True}])], [([['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []], [['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []], [[3.1, 93.91696605104102, -9.674549136974946, 9.2, 4.0, 1.5, -41.18839790246442, 11.974815865245986], [], [], []], [['d', 'TdZQiyPXDo', 'c', 'two', 'LYbdegAC', 'm', 'one', 'Jane', 'lOgg'], [], [], []])], [(['green', 'blue'], ['purple', 'orange', 'yellow'])], [([[1, 2], [3]], [[1, 2], [3]], [[4, 5], [6]], [[7, 8], [9], [9]], [[7, 8], [9]], [[1, 2], [3]])], [(19, 'green', 1, 1, 1)], [([[], [], []], [[], []])], [({'name': 'Bob'}, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob'})], [('dattwo', 'apple', 'baapplenana', 'cherry', 'date')], [([[], [], [-74.25370956493562, -12.399945640410806, 8.278263346367723, -9.674549136974946, -89.51696270839595, 4.0, 6.4, -98.76694370423638, 5.0], []], [[], [], [-74.25370956493562, -12.399945640410806, 8.278263346367723, -9.674549136974946, -89.51696270839595, 4.0, 6.4, -98.76694370423638, 5.0], []], [[], [], [-74.25370956493562, -12.399945640410806, 8.278263346367723, -9.674549136974946, -89.51696270839595, 4.0, 6.4, -98.76694370423638, 5.0], []])], [([[], [], [], []], [[], []])], [([[4, 5, 6]], {'1': 'apple', '2': 'banana', '3': 'cherry', '11': 'pplJanee'}, {'4': [10, 20, 30], '5': [40, '50', 60]}, [[4, 5, 6]])], [({'1': 'apple', '2': 'banana', '3': 'cherry', '11': 'pple'}, [[1, 2, 3], [1, 2, 3], [1, 2, 3]], {'4': [10, 20, 30], '5': [40, '50', 60]}, [[1, 2, 3], [1, 2, 3], [1, 2, 3]])], [('dattwo', 'apple', 'banana', 'd', 'cherry', 'date')], [('apple', 'apple')], [([['b', 'a'], ['c', 'd']], [4, 5, 6], [[[1], [2], [3]], [[4], [5], [6]]])], [([1, 2, '3'],)], [([2, 3, 4, 4, 2], [2, 3, 4, 4, 2], [2, 3, 4, 4, 2], [2, 3, 4, 4, 2])], [('chercry', 'dattwo', 'applae', 'banana', 'cherry', 'cherry', 'dattwo')], [({'1': 'one'}, {'2': 'two'}, {'3': 'three', '20': 'Alice'})], [([[1, 2], [3]], [[1, 2], [3]], [[4, 5], [6]], [[7, 8], [9], [9]], [[7, 8], [9]], [[4, 5], [6]])], [([[60, 1, 2]], [[60, 1, 2]], [['red', 'green', 'blue'], ['purple', 'yellow', 'orange']], [[60, 1, 2]], [[60, 1, 2]], [[60, 1, 2]])], [('apple', [3, 4], {'name': 'John'})], [([[1, 2], [3]], [[7, 8], [9], [9]], [[7, 8], [9]])], [(1.5, 'banana', [1, 2, 3], {'b': 2}, ['apple', 'banana'], {'b': 2}, 1.5)], [(0, 'apple')]]
results = [True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, False, False, False, True, True, True, True, False, True, True, True, True, False, True, False, False, True, True, True, True, True, True, False, False, False, True, True, True, False, False, False, False, True, False, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True, True, False, True, False, True, False, False, False, False, True, False, False, True, False, True, False, False, True, True, True, False, True, True, True, True, False, True, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, False, True, False, False]

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
        func_name = "check_type"
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
        for test_case in ['assert check_type((5, 6, 7, 3, 5, 6) ) == True', 'assert check_type((1, 2, "4") ) == False', 'assert check_type((3, 2, 1, 4, 5) ) == True']:
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
