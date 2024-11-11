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
inputs = [[(1, 5, 7, 10, 13, 5)], [(1, 2, 3, 4, 5, 6)], [(7, 8, 9, 10, 11, 12)], [()], [(10, 20, 30, 40, 50, 60, 70, 80)], [(5, 'a', 10, 'b', 15, 'c', 20, 'd')], [('apple', 'red', 'banana', 'yellow', 'grape', 'purple')], [(1, 'a', 2, 'b', 3, 'c', 4, 'd')], [(1.5, 'a', 2.7, 'b', 3.2, 'c', 4.9, 'd')], [(1, 'a', 40, 'b', 3, 'c', 4, 'd')], [(3.2, 'a', 2.7, 'b', 3.2, 'c', 4.9, 'd')], [(10, 20, 30, 40, 60, 11, 70, 80)], [('apple', 'red', 'banapurplena', 'yellow', 'purple', 'grape')], [(1.5, 'a', 5.2, 'b', 3.2, 'c', 4.9, 'd')], [(10, 20, 30, 40, 50, 1, 70, 80)], [(1, 'a', 4, 'b', 3, 'c', 4, 'd')], [(1, 'a', 2, 'b', 3, 'c', 4, 'ec', 'd', 4)], [(1, 'a', 40, 'b', 'apple', 'dd', 3, 'c', 4, 'd')], [(10, 20, 1, 30, 40, 60, 11, 70, 80, 20)], [(1, 'a', 1, 'b', 3, 'c', 4, 'd')], [(1, 'a', 2, 'b', 'c', 4, 'ec', 4)], [(10, 20, 30, 40, 50, 1, 5, 80)], [(1, 'aa', 4, 'b', 3, 'c', 4, 'd')], [(1, 'a', 2, 3, 0, 'c', 4, 'd')], [(1.5, 'a', 2.7, 'bb', 3.2, 'c', 4.9, 'd')], [(1.5, 'a', 2.7, 'bb', 3.2, 'c', 4.9, 'dd')], [(1, 'a', 2, 3, 0, 'c', 4, 'd', 'c', 1)], [(1, 4, 3, 'c', 4, 'd')], [(1, 'a', 1, 'apple', 3, 'c', 4, 'd')], [(10, 20, 30, 11, 40, 1, 70, 80)], [(1, 'a', 2, 3, 5, 'c', 4, 'd')], [('apple', 'red', 'banapurplena', 'yellow', 'purple', 'graape')], [(4, 'e', 2, 3, 0, 'c', 4, 'd')], [(1.5, 'a', 5.2, 'b', 3.2, 'c', 'd', 'b')], [(1, 'purple', 40, 'b', 'apple', 'dd', 3, 'c', 4, 'd')], [(1, 'a', 2, 'b', 3, 'c', 4, 'ec', 'grape', 4)], [(1.5, '', 2.7, 'bb', 3.2, 'c', 4.9, 'd')], [(5, 'a', 10, 'b', 15, 'c', 20, 'd', 'a', 20)], [(1.5, 'a', 2.7, 'b', 'c', 4.9, 'd', 'd')], [(1.5, 'a', 'bb', 3.2, 'c', 5.618850405922002, 'd', 4.9)], [(1, 4, 50, 'c', 4, 'd')], [(1, 'grape', 2, 'b', 3, 'c', 4, 'd')], [(10, 20, 1, 30, 40, 60, 11, 70, 80, 20, 60, 20)], [(1.5, 'a', 2.7, 'bb', 3.2, 4.9, 'd', 'bb')], [(10, 20, 30, 50, 1, 5, 80, 20)], [('apple', 'red', 'banana', 'yellow', 'gprape', 'purple')], [('apple', 'red', 'banapurplena', 'yellow', 'purple', 'yellow', 'graape', 'yellow')], [(5, 'a', 10, 'b', 15, 'c', 20, 'd', 10, 'd')], [(0, 1, 'a', 2, 3, 0, 'c', 'd')], [(1, 'a', 40, 'b', 'dd', 'dd', 3, 'c', 4, 'd')], [(29, 10, 20, 30, 11, 1, 70, 80)], [(10, 20, 30, 40, 60, 11, 70, 80, 20, 70)], [(10, 30, 40, 11, 70, 80, 20, 70)], [(1.5, 'a', 2.7, 'bb', 3.2, 5.618850405922002, 'c', 4.9, 'dd', 3.2)], [(10, 20, 30, 40, 50, 1, 71, 79)], [(0, 'a', 1, 'apple', 3, 'c', 4, 'd')], [(10, 20, 30, 40, 50, 0, 71, 79)], [(10, 20, 30, 10, 50, 1, 4, 80)], [(1.5, 'a', 'bb', 3.2, 'c', 1.5, 5.618850405922002, 'd', 4.9, 4.9)], [(1, 'dgrape', 'a', 40, 'b', 'dd', 'dd', 3, 'c', 'dd', 4, 'd')], [(4, 3, 'c', 'd')], [(10, 20, 30, 50, 1, 5, 79, 20)], [(1, 29, 'a', 2, 'gprape', 'c', '', 4, 'ec', 4)], [(10, 0, 1, 30, 40, 60, 11, 70, 80, 20, 5, 10)], [(10, 70, 20, 30, 40, 50, 60, 70, 80, 80)], [(0, 'aa', 1, 'apple', 3, 'c', 4, 'd')], [(1.5, 'a', 2.7, 'bb', 3.2, 'a', 'd', 'a')], [(29, 10, 20, 30, 11, 20, 70, 80)], [(2.7, 1.5, 'a', 'bb', 3.2, 'c', 5.618850405922002, 'd', 4.9, 3.2)]]
results = [{1: 5, 7: 10, 13: 5}, {1: 2, 3: 4, 5: 6}, {7: 8, 9: 10, 11: 12}, {}, {10: 20, 30: 40, 50: 60, 70: 80}, {5: 'a', 10: 'b', 15: 'c', 20: 'd'}, {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}, {1: 'a', 2: 'b', 3: 'c', 4: 'd'}, {1.5: 'a', 2.7: 'b', 3.2: 'c', 4.9: 'd'}, {1: 'a', 40: 'b', 3: 'c', 4: 'd'}, {3.2: 'c', 2.7: 'b', 4.9: 'd'}, {10: 20, 30: 40, 60: 11, 70: 80}, {'apple': 'red', 'banapurplena': 'yellow', 'purple': 'grape'}, {1.5: 'a', 5.2: 'b', 3.2: 'c', 4.9: 'd'}, {10: 20, 30: 40, 50: 1, 70: 80}, {1: 'a', 4: 'd', 3: 'c'}, {1: 'a', 2: 'b', 3: 'c', 4: 'ec', 'd': 4}, {1: 'a', 40: 'b', 'apple': 'dd', 3: 'c', 4: 'd'}, {10: 20, 1: 30, 40: 60, 11: 70, 80: 20}, {1: 'b', 3: 'c', 4: 'd'}, {1: 'a', 2: 'b', 'c': 4, 'ec': 4}, {10: 20, 30: 40, 50: 1, 5: 80}, {1: 'aa', 4: 'd', 3: 'c'}, {1: 'a', 2: 3, 0: 'c', 4: 'd'}, {1.5: 'a', 2.7: 'bb', 3.2: 'c', 4.9: 'd'}, {1.5: 'a', 2.7: 'bb', 3.2: 'c', 4.9: 'dd'}, {1: 'a', 2: 3, 0: 'c', 4: 'd', 'c': 1}, {1: 4, 3: 'c', 4: 'd'}, {1: 'apple', 3: 'c', 4: 'd'}, {10: 20, 30: 11, 40: 1, 70: 80}, {1: 'a', 2: 3, 5: 'c', 4: 'd'}, {'apple': 'red', 'banapurplena': 'yellow', 'purple': 'graape'}, {4: 'd', 2: 3, 0: 'c'}, {1.5: 'a', 5.2: 'b', 3.2: 'c', 'd': 'b'}, {1: 'purple', 40: 'b', 'apple': 'dd', 3: 'c', 4: 'd'}, {1: 'a', 2: 'b', 3: 'c', 4: 'ec', 'grape': 4}, {1.5: '', 2.7: 'bb', 3.2: 'c', 4.9: 'd'}, {5: 'a', 10: 'b', 15: 'c', 20: 'd', 'a': 20}, {1.5: 'a', 2.7: 'b', 'c': 4.9, 'd': 'd'}, {1.5: 'a', 'bb': 3.2, 'c': 5.618850405922002, 'd': 4.9}, {1: 4, 50: 'c', 4: 'd'}, {1: 'grape', 2: 'b', 3: 'c', 4: 'd'}, {10: 20, 1: 30, 40: 60, 11: 70, 80: 20, 60: 20}, {1.5: 'a', 2.7: 'bb', 3.2: 4.9, 'd': 'bb'}, {10: 20, 30: 50, 1: 5, 80: 20}, {'apple': 'red', 'banana': 'yellow', 'gprape': 'purple'}, {'apple': 'red', 'banapurplena': 'yellow', 'purple': 'yellow', 'graape': 'yellow'}, {5: 'a', 10: 'd', 15: 'c', 20: 'd'}, {0: 1, 'a': 2, 3: 0, 'c': 'd'}, {1: 'a', 40: 'b', 'dd': 'dd', 3: 'c', 4: 'd'}, {29: 10, 20: 30, 11: 1, 70: 80}, {10: 20, 30: 40, 60: 11, 70: 80, 20: 70}, {10: 30, 40: 11, 70: 80, 20: 70}, {1.5: 'a', 2.7: 'bb', 3.2: 5.618850405922002, 'c': 4.9, 'dd': 3.2}, {10: 20, 30: 40, 50: 1, 71: 79}, {0: 'a', 1: 'apple', 3: 'c', 4: 'd'}, {10: 20, 30: 40, 50: 0, 71: 79}, {10: 20, 30: 10, 50: 1, 4: 80}, {1.5: 'a', 'bb': 3.2, 'c': 1.5, 5.618850405922002: 'd', 4.9: 4.9}, {1: 'dgrape', 'a': 40, 'b': 'dd', 'dd': 3, 'c': 'dd', 4: 'd'}, {4: 3, 'c': 'd'}, {10: 20, 30: 50, 1: 5, 79: 20}, {1: 29, 'a': 2, 'gprape': 'c', '': 4, 'ec': 4}, {10: 0, 1: 30, 40: 60, 11: 70, 80: 20, 5: 10}, {10: 70, 20: 30, 40: 50, 60: 70, 80: 80}, {0: 'aa', 1: 'apple', 3: 'c', 4: 'd'}, {1.5: 'a', 2.7: 'bb', 3.2: 'a', 'd': 'a'}, {29: 10, 20: 30, 11: 20, 70: 80}, {2.7: 1.5, 'a': 'bb', 3.2: 'c', 5.618850405922002: 'd', 4.9: 3.2}]

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
        func_name = "tuple_to_dict"
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
        for test_case in ['assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}', 'assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}', 'assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}']:
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
