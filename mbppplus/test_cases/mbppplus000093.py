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
inputs = [[[1, 2, 3], 4], [[1, 2, 2, 3, 3, 3, 4], 3], [[0, 1, 2, 3, 1, 2], 1], [[], 1], [[], 4], [[False], 4], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], 1], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], 1], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], False], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPshwex', 'ICMkS', '', ''], 1], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], 0], [[True, False, False, True, False, True, True, True, False], 2], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPVjygOQshwex', 'VjPshwex', 'ICMkS', '', ''], 1], [[], 2], [[4.779178548584724, 20.12336259087077], 1], [[4.779178548584724, 72.59056638104303, 92.53457117882732], True], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 20.12336259087077], False], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPVjygOQshwex', 'VjPshwex', 'ICMkS', '', '', 'CL', 'IV'], 1], [[True, False, False, True, False, True, True, False, True, False], 2], [[6.671642720053646, 72.59056638104303, 92.53457117882732, 20.12336259087077], 4], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPVjygOQshwex', 'VjPshwex', 'ICMkS', 'VjPVjygOQshwVjPshwexex', '', '', 'CL', 'IV'], 5], [[False, False], 4], [[5.159327309211834, 4.779178548584724], 1], [[4.779178548584724, 73.08137236933901, 92.53457117882732, 20.12336259087077], True], [[True, False], 4], [[23.020319535944452, [5, False, -74, -50, -9, 5, 4, -97], '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwVjPshwexex', 'q'], 2], [[4.779178548584724, 20.12336259087077, 4.779178548584724], False], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], 0], [[True, True], 4], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPVjygOQshwex', 'ICMkS', '', '', 'CL', 'IV'], -50], [[5], 2], [[23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwVjPshwexex', 'q', [5, False, -74, -50, -9, 5, 4, -97]], 2], [[5], False], [[23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwex', [5, False, -74, -50, -9, 5, 4, -97]], -50], [[5, 5], False], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], True], [[72.59056638104303, 92.53457117882732, 23.408003718694573, 20.12336259087077, 92.53457117882732], False], [[60, 4, 4, -43, 4, 81, -50, 5, 99, -97], 4], [[5.599696065924146], 4], [[23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], 'VIV', '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwex', [5, False, -74, -50, -9, 5, 4, -97]], -51], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPVjygOQshwex', 'ICMkS', '', '', 'CL', 'IV'], -74], [[], 3], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], -51], [[4.779178548584724, 20.12336259087077], False], [[20.12336259087077], False], [[23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwVjPshwexex', 'q'], 2], [[4.779178548584724, 20.12336259087077, 4.779178548584724], True], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], 2], [[5, 5], True], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 92.53457117882732], True], [[6.671642720053646, 73.08137236933901, 4.779178548584724, 20.12336259087077], 4], [[True], 4], [[True], 1], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], -9], [[72.59056638104303, 92.53457117882732, 23.408003718694573, 20.12336259087077, 92.53457117882732], True], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], -51], [[5.159327309211834, 4.779178548584724], -97], [[], 5], [[4.779178548584724, 23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], 'VIV', '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwex', [5, False, -74, -50, -9, 5, 4, -97]], -51], [[72.59056638104303, 92.53457117882732, 25.495320338145287, 23.408003718694573, 104.92811756855819, 20.12336259087077, 92.53457117882732], False], [[23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwVjPshwexex', 'q', [5, False, -74, -50, -9, 5, 4, -97]], 3], [[True, False, False, True, False, True, True, True, False], 81], [[72.59056638104303, 92.53457117882732, 20.12336259087077], 1], [[4.779178548584724, 73.08137236933901, 92.53457117882732], True], [[21.457739778830753, 4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], 0], [[5], 1], [[60, 4, 4, -43, 4, 82, -50, 5, 3, 99], 4], [[4.779178548584724, 72.59056638104303, 91.9284337556918, 92.53457117882732, 20.12336259087077], -51], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.95740817891545], -1], [[72.59056638104303, 92.53457117882732, 12.618578392571889, 20.12336259087077, 92.53457117882732], False], [['CL', 'vGL', 'VjygOQ', 'IV', 'VjPVjygOQshwex', 'ICMkS', '', '', 'CL', 'IV'], -43], [[], -9], [[], 82], [[72.59056638104303, 92.53457117882732, 23.408003718694573, 91.9284337556918, 92.53457117882732], True], [[5], -1], [[72.59056638104303, 92.53457117882732, 91.9284337556918, 92.53457117882732], False], [[False, True, False], 4], [[4.779178548584724, 23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], 'VIV', '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwex', [5, False, -74, -50, -9, 5, 4, -97], 'VIV'], -51], [[99, -31, 82, -60], 3], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732, 92.53457117882732], 4], [[None, 73.08137236933901, -72.0136627571263, -2.6946579959743957, 'grmqd', {}, 'VjPVjygOQshwex', {'-32': 12.618578392571889, '5': [66.8966114578121, -3.026526737101335, 4.779178548584724], '2': True, '-51': 81, '-77': 60}, 81], 5], [[4.779178548584724, 23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], 'VIV', '', [], False, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwex', [5, False, -74, -50, -9, 5, 4, -97], 'VVIV'], -51], [[72.59056638104303, 92.53457117882732, 20.12336259087077], 0], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], False], [[20.95740817891545, 5.599696065924146, 5.599696065924146], 4], [[5, 6], False], [['vGL', 'GEMQus', 'VjPVjygOQshwex', 'o', '', '', 'ICMkS', 'GHTx', 'grmqd', 'LvGL', 'vGL'], 5], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 20.12336259087077, 72.59056638104303], False], [[20.95740817891545, 5.599696065924146, 5.599696065924146, 5.599696065924146], 4], [[4.638246081712282, 4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732], 2], [[-3.026526737101335, -51.21354843845134, -50.84067158641727], 5], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077], 2], [[4.779178548584724, 72.59056638104303, 93.00370740734236, 20.12336259087077], 1], [[4.779178548584724, 72.59056638104303, 92.53457117882732], False], [[23.408003718694573, 93.00370740734236, 72.59056638104303, 25.495320338145287, 104.92811756855819, -72.0136627571263, 104.92811756855819, 59.68770177971405, -62.798823266707295, 5.159327309211834], 4], [[5], 5], [[60, 3, 4, 4, -43, 4, 81, -50, 5, 99, -97], 4], [[4.779178548584724, 20.12336259087077], True], [[20.95740817891545, 5.599696065924146, 4.638246081712282, 5.599696065924146, 5.599696065924146], 4], [[False, False], -43], [[4.779178548584724, 72.59056638104303, 92.53457117882732, 20.12336259087077, 92.53457117882732, 92.53457117882732], 3], [[], -77], [[4.000120888560737, 20.12336259087077], False], [[60, 4, -50, -43, 4, 81, -50, 5, 99, -97, 99], -60], [[23.020319535944452, 'IV', [5, False, -74, -50, -9, 5, 4, -97], '', [], True, 2, 'VjPVjygOQshwex', 'VjPVjygOQshwVjPshwexex', 'q'], 2]]
results = [0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 1]

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
        func_name = "frequency"
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
        for test_case in ['assert frequency([1,2,3], 4) == 0', 'assert frequency([1,2,2,3,3,3,4], 3) == 3', 'assert frequency([0,1,2,3,1,2], 1) == 2']:
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
