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
inputs = [['polygon', 'y', 'l'], ['character', 'c', 'a'], ['python', 'l', 'a'], ['', 'a', 'b'], ['python', 'z', 'a'], ['python', 'o', 'o'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'm', 'n'], ['pythoon', 'a', 'b'], ['python', 'z', 'o'], ['z', 'a', 'a'], ['z', 'z', 'z'], ['', 'm', 'm'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'a', 'b'], ['python', 'z', 'z'], ['zzz', 'z', 'z'], ['zzz', 'a', 'a'], ['a', 'a', 'a'], ['a', 'b', 'o'], ['b', 'z', 'o'], ['', 'o', 'm'], ['', 'a', 'a'], ['AbCdEfGhIjKlMnOpQrStUvWYzz', 'a', 'a'], ['n', 'z', 'a'], ['', 'b', 'o'], ['pythona', 'z', 'a'], ['pythoonpythona', 'z', 'a'], ['zz', 'a', 'a'], ['mz', 'z', 'z'], ['', 'o', 'o'], ['a', 'm', 'o'], ['b', 'a', 'b'], ['b', 'o', 'o'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'm', 'n'], ['b', 'a', 'a'], ['mz', 'a', 'a'], ['zzz', 'z', 'a'], ['m', 'a', 'a'], ['zz', 'z', 'a'], ['mz', 'a', 'b'], ['aa', 'b', 'o'], ['m', 'n', 'm'], ['a', 'o', 'b'], ['z', 'a', 'z'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'a', 'a'], ['bb', 'a', 'a'], ['python', 'o', 'b'], ['n', 'n', 'n'], ['zzzzz', 'a', 'a'], ['zz', 'z', 'o'], ['zz', 'o', 'o'], ['a', 'z', 'a'], ['a', 'b', 'a'], ['n', 'z', 'z'], ['opythoon', 'a', 'o'], ['AbCdEfGhIjKlMnOpQrStUvWxYz', 'm', 'b'], ['zzzzza', 'b', 'b'], ['AbCdEfGhIjKlMnOpQrSthUvWYzz', 'a', 'a'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'b', 'b'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'z', 'z'], ['zz', 'z', 'z'], ['aa', 'b', 'b'], ['pythona', 'a', 'a'], ['AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'o', 'o'], ['mz', 'b', 'o'], ['mAbCdEfGhIjKlMnOpQrSthUvWYzz', 'm', 'm'], ['zz', 'n', 'a'], ['pythoonpynthona', 'z', 'a'], ['aa', 'o', 'o'], ['b', 'b', 'b'], ['a', 'a', 'z'], ['zpythoonpynthona', 'z', 'o'], ['zzzzz', 'm', 'm'], ['a', 'm', 'm'], ['oopythoon', 'a', 'o'], ['m', 'm', 'm'], ['zpythoonpynthona', 'o', 'b'], ['o', 'o', 'o'], ['pytoopythoonhona', 'z', 'a'], ['AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'z', 'a'], ['bb', 'a', 'o'], ['oo', 'o', 'o'], ['pytbboopythoonhona', 'z', 'z'], ['opythoon', 'z', 'z'], ['aa', 'z', 'b'], ['pythnn', 'o', 'b'], ['zzzzza', 'o', 'b'], ['AbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'o', 'o'], ['aaa', 'b', 'b'], ['AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'b', 'b'], ['a', 'o', 'a'], ['pythoAbCdEpythnnfGhIjKlMnOpQaaaxYzn', 'z', 'z'], ['AbCdEfGhIjKlMnOpQrStUvWxAbCdEfKGhIjKlMnOpQrStUvWxYzz', 'm', 'n'], ['opythoon', 'o', 'o'], ['pythooon', 'a', 'b'], ['pythooon', 'm', 'm'], ['', 'b', 'b'], ['zpythoonpynthona', 'b', 'o'], ['o', 'b', 'o'], ['b', 'b', 'o'], ['n', 'z', 'n'], ['zzzzza', 'b', 'a'], ['o', 'b', 'a'], ['ma', 'm', 'm'], ['mz', 'z', 'a'], ['AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'a', 'a'], ['zzzAbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzzzz', 'a', 'a'], ['pytohona', 'z', 'a']]
results = ['pollgon', 'aharaater', 'python', '', 'python', 'python', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'pythoon', 'python', 'z', 'z', '', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'python', 'zzz', 'zzz', 'a', 'a', 'b', '', '', 'AbCdEfGhIjKlMnOpQrStUvWYzz', 'n', '', 'pythona', 'pythoonpythona', 'zz', 'mz', '', 'a', 'b', 'b', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'b', 'mz', 'aaa', 'm', 'aa', 'mz', 'aa', 'm', 'a', 'z', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'bb', 'pythbn', 'n', 'zzzzz', 'oo', 'zz', 'a', 'a', 'n', 'opythoon', 'AbCdEfGhIjKlMnOpQrStUvWxYz', 'zzzzza', 'AbCdEfGhIjKlMnOpQrSthUvWYzz', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'zz', 'aa', 'pythona', 'AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'mz', 'mAbCdEfGhIjKlMnOpQrSthUvWYzz', 'zz', 'pythoonpynthona', 'aa', 'b', 'z', 'opythoonpynthona', 'zzzzz', 'a', 'oopythoon', 'm', 'zpythbbnpynthbna', 'o', 'pytoopythoonhona', 'AbCdEfGhIjKlaMnOpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYaa', 'bb', 'oo', 'pytbboopythoonhona', 'opythoon', 'aa', 'pythnn', 'zzzzza', 'AbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzz', 'aaa', 'AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'a', 'pythoAbCdEpythnnfGhIjKlMnOpQaaaxYzn', 'AbCdEfGhIjKlMnOpQrStUvWxAbCdEfKGhIjKlMnOpQrStUvWxYzz', 'opythoon', 'pythooon', 'pythooon', '', 'zpythoonpynthona', 'o', 'o', 'n', 'zzzzza', 'o', 'ma', 'ma', 'AbCdEfGhIjKlMnOpQrStUvWxAWbCdEfGhIjKlMnOpQrStUvWxYzz', 'zzzAbCdEfGhIjKlaMnOGpQrStUvWxAbCdEfGhIjKlMnOpQrStUvWxYzzzz', 'pytohona']

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
        func_name = "replace_char"
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
        for test_case in ['assert replace_char("polygon",\'y\',\'l\')==("pollgon")', 'assert replace_char("character",\'c\',\'a\')==("aharaater")', 'assert replace_char("python",\'l\',\'a\')==("python")']:
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
