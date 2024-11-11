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
inputs = [[('a', 'a', 'c', 'b', 'd'), ['a', 'b']], [(1, 2, 3, 1, 4, 6, 7, 1, 4), [1, 4, 7]], [(1, 2, 3, 4, 5, 6), [1, 2]], [(), []], [(1, 1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [(), [1, 2, 3, 4, 5]], [(1, 2, 3, 4, 5, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], [(2, 3, 4, 5, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], [(4, -46, 64, 3, 3, 1, 67), [1, 2, 3, 4, 5]], [(1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [('OX', -48.873894802445946), []], [('OOXX', -48.873894802445946), []], [('OOXX', -48.873894802445946), [False, True, True, True, False, False, True, False, True, True]], [(4, -46, 64, 3, 9, 3, 1, 67), [1, 2, 3, 4, 5]], [('OOXX', -48.873894802445946), [8, 87, 1, 3, 34, 79, -32, 28, False]], [(), [1, 2, False, 3, 4, 5]], [(1, 1, 2, 2, 2, 0, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [(1, 1, 2, 2, 2, 0, 3, 3, 3), [1, 2, 2, 3, 3]], [('OOXX', -48.873894802445946, 'OOXX'), []], [('OOXX', -48.873894802445946), [False, True, True, True, False, False, True, False, True, True, True]], [(1, 1, 2, 2, 2, 3, 3, 3), [1, 2, 2, 3, 3]], [(5, 1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [(-48.873894802445946, 89.4498825238312, -48.873894802445946, -48.873894802445946, -63.30134785965016, -83.39947209096098, -48.873894802445946, -48.873894802445946, -28.62571567417322, -71.79928701608094), [72, -86, 79]], [(3, 1, 1, 2, 2, 2, 0, 3, 3, 3), [1, 2, 2, 3, 3]], [('OOXX', -48.873894802445946, -48.873894802445946), [8, 87, 1, 3, 34, 79, -32, 28, False]], [(1, 1, 2, 2, 2, 0, 3, 3, 3), [1, 2, 2, 3, 3, 2]], [(1, 1, 2, 2, 2, 0, 3, 3, 3), [7, 1, 2, 2, 3, 3]], [(4, -46, 64, 3, 9, 3, 1, 67, -46), [1, 2, 3, 4, 5]], [('OOXX', -48.873894802445946), [8, 87, 1, 3, 34, 79, -32, 29, 2, False]], [('OOXX', -48.873894802445946, 'OX', -48.873894802445946), [8, 87, 1, 4, 3, 34, 79, -32, 28, False, 0, -32]], [(3, 2, 1, 2, 2, 2, 0, 3, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [('OOXX', -28.62571567417322), [False, True, True, True, False, False, True, False, True, True]], [('OOXX', -48.873894802445946, 'OX', -48.873894802445946), [8, 87, 1, 4, 3, 34, 79, -32, 28, False, 0, 79, -32, 8]], [('OOXX', -48.873894802445946), [True, True, True, True, False, True, True, False]], [(1, 1, 2, 2, 2, 3, 3, 3), [2, 2, 3, 3]], [(1, 1, 2, 2, 7, 2, 0, 3, 3, 3), [1, 2, 2, 3, 3]], [('OOXX', -48.873894802445946), [False, True, True, True, False, False, True, True, False, True, True, True]], [(4, -46, 3, 9, 3, 1, 67), [1, 2, 3, 4, 5, 5]], [('OOXX',), ['OX', 'mYim', '', 'YdH', 'Qnm']], [(4, -46, 64, 3, 9, 3, 1, 67, 3), [1, 2, 3, 4, 5]], [(1, 1, 2, 2, 2, 0, 3, 3, 3), [1, 2, 2, 3, 3, 2, 3]], [('OOXX', -83.39947209096098, -48.873894802445946), [False, True, True, True, False, False, True, True, False, True, True, True]], [(1, 1, 2, 2, 2, 0, 3, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [(1, 1, 2, 2, 2, 3, 3, 3), [2, 3, 3]], [(1, 2, 3, 4, 5, 6), [1, 3, 3, 4, 5, 6, 7, 8, 9]], [(3, 1, 1, 2, 2, 0, 3, 3, 3), [1, 2, 2, 5, 3, 3]], [('OOXX', 'OOmYimXX', -48.873894802445946, 'OOXX'), []], [(4, -46, 64, 3, 9, 3, 1, 67), [1, 2, 3, 9, 4, 5]], [('OOXQnm', -122.20173217485707, -48.873894802445946), [False, True, True, False, False, True, True, False, True, True, True]], [(4, -46, 64, 3, 9, 3, 1, 67, -46, 64), [1, 2, 3, 4, 5]], [(4, -46, 64, 9, 3, 1, 67), [1, 2, 3, 4, 5]], [(2, 3, 4, 5, 6), [1, 3, 3, 4, 5, 6, 7, 8, 9]], [('OOXX', -48.873894802445946), [False, True, True, True, False, False, True, False, True, False, True]], [('OOXX', -48.873894802445946, 'OOXX'), ['OOXQnm', 'IUtxz', 'sEegPEBDio', 'OOXQnm', 'IUtxz']], [(1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 2, 3, 3, 2]], [('OOOXX', -48.873894802445946), []], [('OOXX', -48.873894802445946), [False, True, True, True, False, False, True, True, False, True, True, True, True]], [('', -48.873894802445946), [False, True, True, True, False, False, True, True, False, True, True, True]], [('sEegPEBDio', -122.20173217485707, -122.20173217485707), [False, -86, 70, 4, 34, -73, -35, 2, -46]], [(1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 3, 3, 2]], [('OOXX', -48.873894802445946, -48.76647231712022, 'OOXX'), []], [('OOXX', -48.873894802445946, -48.873894802445946), [8, 87, 1, 34, 79, -32, 28, False]], [(4, -46, 64, 3, 9, 3, 1, 67, 3, 1), [1, 2, 3, 4, 5]], [(1, 2, 3, 4, 5, 6), [87, 1, 3, 3, 4, 5, 6, 7, 8, 9]], [(1, 1, 2, 2, 2, 3, 3, 3, 1), [1, 1, 2, 2, 3, 3]], [(4, -46, 64, 4, 9, 3, 1, 67, -46), [1, 2, 3, 4, 5]], [('OOOXXX', 'OOXX', -48.873894802445946, 'OX'), [8, 87, 1, 4, 3, 34, 79, -32, 28, False, 0, -32, 0]], [(4, -46, 64, 3, 9, 3, 1, 67), [1, 2, 3, 9, 4, 5, 9]], [('OOXX', -28.62571567417322), [False, True, True, True, False, False, True, True, False, True, True, True, True]], [(1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 2, 3, 3, 2, 1]], [(1, 2, 3, 4, 5, 6), [87, 1, 3, 3, 4, 5, 8, 6, 7, 8, 9]], [(4, -46, 64, 3, 9, 3, 1, 67, 67), [1, 2, 3, 9, 4, 5, 9, 5]], [(1, 1, 2, 2, 3, 3, 3, 3), [1, 1, 2, 2, 3, 3]], [(-48.873894802445946, 'OOXX', -48.873894802445946, -48.873894802445946), [8, 87, 1, 34, 79, -32, 28, False]], [('OOXX', -48.873894802445946, 'OOXX'), ['OOXQnm', 'IUtxz', 'sEegPsEBDio', 'sEegPEBDio', 'OOXQnm', 'IUtxz', 'sEegPEBDio']], [('OOXX', -48.873894802445946), [True, True, True, True, False, True, True]], [(1, 1, 2, 2, 0, 3, 3, 3), [1, 2, 3, 2, 5, 3, 3]], [('OOXX', -48.873894802445946), [False, True, True, False, True, False, True, True]], [('OOXX', -48.873894802445946, -48.873894802445946), [False, True, True, True, False, False, True, False, True, True, True, False, True]], [('OOXX', -48.873894802445946), [False, True, True, False, False, True, False, True, False, True]], [(4, -46, 3, 9, 3, 1, 67, 9), [1, 2, 3, 4, 5, 5]], [('', -48.873894802445946), [False, True, True, True, False, False, True, True, False, True, True, True, True]], [('OOOXXX', 'OOXX', -48.873894802445946, 'OX'), [8, 5, 87, 1, 4, 3, 34, 79, -32, 28, False, 0, -32, 0, 1]], [(), [34.05391711465737, -2.906905516918812, 89.4498825238312, 65.92462636516228, 39.94639777324457]], [(-48.873894802445946, 'OOXX', 'mYim', -48.873894802445946, -48.873894802445946), [8, 87, 1, 34, 79, -32, 28, False]], [(1, 1, 2, 2, 2, 0, 3, 3, 3), [1, 2, 2, 3, 3, 2, 3, 3]], [('OOXX', -48.873894802445946, 'YdH', 'OOXX'), ['OOXQnm', 'IUtxz', 'sEegPEBDio', 'OOXQnm', 'IUtxz']], [('OX', -48.873894802445946, 'OX'), [72.37354833611045, 'TewyJp', False, 'sEegPsEBDio', None]], [('OOXX',), ['OX', 'mYim', 'YdHQnm', '', 'YdH', 'Qnm']], [(4, 3, 9, 3, 1, 67, 9), [1, 2, 3, 4, 5, 5]], [(4, -46, 64, 9, 3, 1, 67, 64), [1, 2, 3, 4, 5]], [('OOXX', 'sEegPsEBDio', -48.873894802445946, -48.873894802445946), [8, 87, 1, 34, 79, 28, False]], [(4, -46, 64, 3, 9, 3, 1, 67, -46, 64, 1), [1, 4, 3, 4, 5]], [(1, 1, 1, 2, 2, 2, 3, 3, 3), [1, 1, 2, 2, 3]], [('OOXX', -28.62571567417322), [False, True, True, True, False, False, True, True, False, True, True, True, True, False]], [('OOXX', -48.873894802445946), [8, 87, 1, 3, 34, 79, 29, 2, False]], [('OOXX', -28.62571567417322, -28.62571567417322), [False, True, True, True, False, False, True, True, False, True, True, True, True, False]], [(1, 1, 0, 2, 2, 2, 0, 3, 3, 3), [7, 2, 2, 3, 3, 3]], [('sEegPEBDio', -122.20173217485707, -122.20173217485707, -122.20173217485707), [False, -86, 70, 4, 34, -73, -35, 2, -46]], [(3, 1, 1, 2, 2, 2, 0, 3, 3, 3, 3), [1, 2, 2, 3, 3]], [('OOXX', -48.873894802445946, 'OOXX'), ['OOXQnm', 'IUtxz', 'sEegPsEBDio', 'sEegPEBDio', 'OOXQnm', 'IOOXXxz', 'sEegPEBDio']], [(-122.20173217485707, -48.873894802445946), [False, True, True, False, False, True, True, False, True, True, True]], [('OOX', 'OOmYimXX', -48.873894802445946, 'OOXX'), []], [('OOXX', -48.873894802445946, 'OOXX'), [2, -10, 87]], [(3, 1, 1, 2, 2, 0, 3, 3, 3), [1, 2, 3, 2, 5, 3, 3, 2]], [(1, 2, 3, 4, 5, 6), [87, 1, 3, 3, 4, 5, 8, 8, 6, 7, 8, 9]], [('OOXX', -122.20173217485707, -48.873894802445946), [True, True, True, True, False, True, True, False]]]
results = [3, 6, 2, 0, 18, 0, 6, 5, 4, 16, 0, 0, 0, 4, 0, 0, 16, 14, 0, 0, 14, 16, 0, 16, 0, 17, 14, 4, 0, 0, 20, 0, 0, 0, 12, 14, 0, 4, 0, 5, 20, 0, 18, 9, 6, 14, 0, 5, 0, 4, 3, 5, 0, 0, 16, 0, 0, 0, 0, 13, 0, 0, 6, 6, 18, 4, 0, 6, 0, 18, 6, 6, 16, 0, 0, 0, 15, 0, 0, 0, 4, 0, 0, 0, 0, 23, 0, 0, 0, 4, 3, 0, 6, 15, 0, 0, 0, 15, 0, 18, 0, 0, 0, 0, 20, 6, 0]

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
        func_name = "count_Occurrence"
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
        for test_case in ["assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3", 'assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6', 'assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2']:
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
