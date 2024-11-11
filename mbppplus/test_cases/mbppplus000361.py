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
inputs = [((1, 5, 7, (4, 6), 10),), ((2, 6, 8, (5, 7), 11),), ((3, 7, 9, (6, 8), 12),), ((3, 7, 9, (6, 8), (5, 12), 12),), ((2, 6, 8, (5, 7), 11, ((2, 9), (6, 3)), 4),), ((1, 2, 3, 4),), ((),), ((1, 5, 7, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12)),), (((), (), ((), ())),), (((1, 2, ((3, 4), 5)), ((6, 7, ()), 8)),), (((1, 2), (3, 4), (5, 6), ((7, 8), (9, 10), (11, 12)), (((13, 14), 15), 16), (17, 18, (19, 20))),), ((((1, (2, 3), 4), 5), (((6, 7), 8), 9), ((10, 11), 12, (13, (14, 15))), (16, 17), (18, (), 19, 20)),), (('BBeujUUS', '', 'cHImXR', 'BeujUUS'),), ((1, 5, 7, ((4, 6), 3), (10, 3), (10, 2), ((8, (14, 10)), 12), 1),), (((), ((), ())),), (((), (), ((), ()), ((), ())),), (((1, 2, ((3, 4), 5)),),), (('iaZtoqM', -15, 55),), ((2, 6, ((6, 3),), 8, (5, 7), 11, ((2, 9), (6, 3)), 4),), ((1, 5, 7, ((4, 6), 3), (10, 3), (10, 2), ((8, (14, 10)), 12), 1, (10, 3)),), ((2, 6, ((6, 3),), 8, (5, 7), 11, ((6, 4), (6, 3)), ((2, 9), (6, 3)), 4, ((6, 3),)),), (('BBeujUUS', '', 'cHImXR', 'BeujUUS', ''),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, (5, 7)),), (('iaZtoqM', 55, -15, 55),), (((), ((), (), ()), (), ((), ())),), ((((), ()),),), ((2, 6, 8, (5, 7), 11, ((2, 9), (6, 3)), 4, 6),), ((2, 20, ((6, 3),), 8, (5, 7), 11, 4),), ((2, 7, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, (5, 7)),), (((), (), ((), ()), ()),), ((14, 6, ((6, 3),), 8, (5, 7), 11, ((2, 9), (6, 3)), 4),), (((), ((), (), (), ()), ('iaZtoqM', 'pm', 'iaZtoqM', 'wOkCgN', 'oQjO', 'BBeujUUS', 'HjLKztlzPf', 'BeujUUS', '', ''), (), ((), ())),), ((1, 5, 7, ((15, 6), 3), ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), ((8, (14, 10)), (8, (14, 10), (14, 10)), 12), ((4, 6), 3)),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, (5, 7), (5, 7)),), (((), (), ((), ()), ((),)),), ((({'9': True, '1': True, '21': True, '32': False, '2': True, '-44': True}, 'BBeujUUS', -39.29936222397124, True, (81,), 'hTiPAxILj', -38.17279241711651, 15.51245915461675), ((), (), ()), (), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), ((), ())),), ((({'9': True, '1': True, '21': True, '32': False, '2': True, '-44': True}, 'BBeujUUS', -39.29936222397124, True, (81,), 'hTiPAxILj', -38.17279241711651, 15.51245915461675), ((), (), ()), (), ((), ())),), ((5, 7, 6, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12)),), ((2, 6, 20, 16, (5, 7), 11, ((2, 9), (6, 3)), 4, (5, 7)),), (((1, 2, 1, ((3, 4), 5)), ((6, 7, ()), 8)),), (('iaZtoqM', 55),), (((10, 10, 2), 5, 7, 6, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), ((4, 6), 3)),), (((1, 2), (3, 4), (5, 6, 5), (((13, 14), 15), 16), (17, 18, (19, 20))),), ((5, 7, 6, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), 6),), (((), ((), (), (), ()), ('iaZtoqM', 'pm', 'iaZtoqM', 'wOkCgN', 'oQjO', 'BBeujUUS', 'HjLKztlzPf', 'BeujUUS', '', ''), ((), ())),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, 6),), ((2, 10, 20, 16, (5, 7, 7), 11, ((2, 9), (6, 3)), 4, (5, 7)),), (((1, 2, ((3, 4),)), (1, 2, ((3, 4), 5))),), (((), (), ((),), ()),), (((1, 2), (3, 4), (5, 6, 5, 5), (5, 6, 5), (((13, 14), 15), 16), (17, 18, (19, 20))),), ((((), (), ()), (50, 80, -9, 12, 100, -66), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), ((), ())),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, 6, 20),), ((1, 5, 6, 7, ((4, 6), 3), (10, 3), (10, 2), ((8, (14, 10)), 12), 1, (10, 3), 5),), (((1, 2, 1, ((3, 4), 5)), ((6, 7, ()), 8, 8)),), ((1, 5, 7, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), ((4, 6), 3)),), ((((), (), ()), (50, 80, -9, 12, 100, -66), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), (50, 80, -9, 12, 100, -66, 12), ((), ())),), ((((), (), ()), (50, 80, -9, 12, 100, -66), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), (50, 80, -9, 12, 100, -66, 12), ((), (), ()), ((), ()), ((), (), ())),), ((9, 'iaZtoqM', -15, 55),), ((1, 5, 7, ((4, 6), 3), (10, 3), (10, 2), 8, 1),), ((1, 5, 7, ((15, 6), 3), ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), ((4, 6), 3, (4, 6)), ((8, (14, 10)), (8, (14, 10), (14, 10)), 12), ((4, 6), 3)),), (((45, 81, 83, 83, 24, 4, -32), ((), ())),), (((), (), (), ((), ()), ((),)),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, 6, 20, 11),), ((({'9': True, '1': True, '21': True, '32': False, '2': True, '-44': True}, 'BBeujUUS', -39.29936222397124, True, (81,), 'hTiPAxILj', -38.17279241711651), ((), (), (), ()), ('jGdwijsq', 'xbjajBrxs', 'iaZtoqM', 'gBXqaucn'), (), ((), ())),), ((1, 1, 7, ((4, 6), 3), (10, 3), (10, 2), 8, 1),), ((5, 7, 6, ((4, 6), 3), (10, 2), ((8, (14, 10)),)),), ((((), (), ()), (50, 80, -9, 12, 100, -66), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), ((), ())),), ((14, 6, ((6, 3),), 12, (5, 7), 11, ((2, 9), (6, 3)), 4),), ((5, 7, 7, 6, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12)),), (((1, 2), (5, 6), ((7, 8), (9, 10), (11, 12)), (((13, 14), 15), 16), (17, 18, (19, 20))),), ((8, 5, 6, 7, ((4, 6), 3), (10, 3), (10, 2), ((8, (14, 10)), 12), 1, (10, 3), 5),), ((14, 6, ((6, 3),), 10, 12, (5, 7), 11, ((2, 9), (6, 3)), 4),), (((1, 2, 1), ((6, 7, ()), 8)),), (((1, 2), (3, 4), (5, 6), (((13, 14), 15), 16), (17, 18, (19, 20))),), (((),),), (('', 'cHImXR', 'BeujUUS'),), (((17, 18, (19, 20)), (1, 2), (3, 4), (5, 6, 5), (((13, 14), 15), 16), (17, 18, (19, 20)), (5, 6, 5)),), (((10, 10, 2), 5, 6, 17, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), ((4, 6), 3)),), (((1, 2, 1, ((3, 4), 5)), ((6, 7, ()), 8), ((6, 7, ()), 8, 8)),), ((8, 5, 6, 7, (10, 3), (10, 2), ((8, (14, 10)), 12), 1, (10, 3), 5),), ((((), (), ()), (50, 80, -9, 12, 100, -66), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), (50, 80, -9, 12, 100, -66, 12), ((), ()), ((), ())),), ((2, 6, 20, (5, 7), 11, ((2, 9), (19, 2, 9), (6, 3)), 4, (5, 7), (5, 7)),), ((2, 6, (7,), 11, ((2, 9), (6, 3)), 4, 6),), ((False, True, True, False, False, False, False, False),), (((17, 18, (19, 20)), (1, 2), (3, 4), (5, 6, 5), (((13, 14), 15), 16), (17, 18, (19, 20)), (3, 4, 3), (5, 6, 5)),), ((14, 5, ((6, 3),), 8, (5, 7), 11, ((2, 9), (6, 3)), 4),), ((5, 7, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), 6),), ((2, (5, 7), 11, ((2, 9), (6, 3)), 4, 6, 4),), ((2, 6, 20, (5, 7), 11, ((2, 9), (6, 3)), 4, 6, (5, 7), (5, 7)),), (((), (), (), ((), (), ()), ((),)),), (((), ((), (), (), ()), ('iaZtoqM', 'pm', 'iaZtoqM', 'wOkCgN', 'oQjO', 'BBeujUUS', 'HjLKztlzPf', 'BeujUUS', '', ''), (), ((), ()), ()),), ((({'9': True, '1': True, '21': True, '32': False, '2': True, '-44': True}, 'BBeujUUS', -39.29936222397124, True, (81,), 'hTiPAxILj', -38.17279241711651, 15.51245915461675), ((), (), ()), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM', 'HjLKztlzPf'), (), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), ((), ())),), ((2, 6, 20, (5, 7), ((2, 9), (6, 3)), 4),), ((({'9': True, '1': True, '21': True, '32': False, '2': True, '-44': True}, 'BBeujUUS', -39.29936222397124, True, (81,), 'hTiPAxILj', -38.17279241711651, 15.51245915461675), ((), (), ()), ('KyvQyRlC', 'ggsHGhlSj', 'HjLKztlzPf', 'tdmtNqM', '', 'jGdwijsq', 'xbjajBrxs', 'oQjO', 'upscQa', 'iaZtoqM'), ((), ())),), (((), ((), (), (), ()), ('iaZtoqM', 'pm', 'iaZtoqM', 'wOkCgN', 'oQjO', 'BBeujUUS', 'HjLKztlzPf', 'BeujUUS', '', ''), (), ((), ()), ((), ())),), (((1, 2), (3, 4), (5, 83, 5), (5, 6, 5, 5), (5, 6, 5), (((13, 14), 15), 16), (17, 18, (19, 20)), (5, 83, 5)),), (('', 'cHImXR', 'BeujUUS', ''),), ((2, 20, ((6, 3),), 8, (5, 7), 11, 7, 4),), (((), ((), (), ()), (), ((), ()), ((), (), ())),), (((), ((), (), ()), (), ((), ()), ((), (), ()), ((), (), ())),), (((), (), (), ((), ())),), ((2, 6, 8, (5, 7), 11, ((2, 9), (6, 3), (2, 9)), 4, 6),), ((2, 6, ((6, 3),), 8, (5, 7), 11, ((6, 4), (6, 3)), ((2, 9), (6, 3)), 4, ((6, 3), (6, 3)), 4),), ((2, 6, 20, (5, 7), 11, ((2, 9), (19, 2, 9), (6, 3)), 4, (5, 7)),), ((1, 5, 7, ((4, 6), 3), (10, 3), (10, 2), 1, (10, 3, 3)),), (('gBXqaucn', 'BBeujUUS', '', 'cHImXR', 'BeujUUS', 'BeujUUS'),), ((8, 5, 6, 7, ((4, 6), 3), (10, 3), (10,), ((8, (14, 10)), 12), 1, (10, 3), 5),), ((6, (5, 7), ((2, 9), (6, 3)), 4),), ((14, 6, 10, 12, (5, 7), 11, ((2, 9), (6, 3)), 4),), ((5, 7, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12)),), ((5, 7, 7, 6, ((4, 6), 3), (10, 2), ((8, (14, 10)), 12), ((4, 6), 3)),)]
results = [(1, 5, 7, 10), (2, 6, 8, 11), (3, 7, 9, 12), (3, 7, 9, 12), (2, 6, 8, 11, 4), (1, 2, 3, 4), (), (1, 5, 7), (), (), (), (), ('BBeujUUS', '', 'cHImXR', 'BeujUUS'), (1, 5, 7, 1), (), (), (), ('iaZtoqM', -15, 55), (2, 6, 8, 11, 4), (1, 5, 7, 1), (2, 6, 8, 11, 4), ('BBeujUUS', '', 'cHImXR', 'BeujUUS', ''), (2, 6, 20, 11, 4), (2, 6, 20, 11, 4), ('iaZtoqM', 55, -15, 55), (), (), (2, 6, 8, 11, 4, 6), (2, 20, 8, 11, 4), (2, 7, 20, 11, 4), (), (14, 6, 8, 11, 4), (), (1, 5, 7), (2, 6, 20, 11, 4), (), (), (), (5, 7, 6), (2, 6, 20, 16, 11, 4), (), ('iaZtoqM', 55), (5, 7, 6), (), (5, 7, 6, 6), (), (2, 6, 20, 11, 4, 6), (2, 10, 20, 16, 11, 4), (), (), (), (), (2, 6, 20, 11, 4, 6, 20), (1, 5, 6, 7, 1, 5), (), (1, 5, 7), (), (), (9, 'iaZtoqM', -15, 55), (1, 5, 7, 8, 1), (1, 5, 7), (), (), (2, 6, 20, 11, 4, 6, 20, 11), (), (1, 1, 7, 8, 1), (5, 7, 6), (), (14, 6, 12, 11, 4), (5, 7, 7, 6), (), (8, 5, 6, 7, 1, 5), (14, 6, 10, 12, 11, 4), (), (), (), ('', 'cHImXR', 'BeujUUS'), (), (5, 6, 17), (), (8, 5, 6, 7, 1, 5), (), (2, 6, 20, 11, 4), (2, 6, 11, 4, 6), (False, True, True, False, False, False, False, False), (), (14, 5, 8, 11, 4), (5, 7, 6), (2, 11, 4, 6, 4), (2, 6, 20, 11, 4, 6), (), (), (), (2, 6, 20, 4), (), (), (), ('', 'cHImXR', 'BeujUUS', ''), (2, 20, 8, 11, 7, 4), (), (), (), (2, 6, 8, 11, 4, 6), (2, 6, 8, 11, 4, 4), (2, 6, 20, 11, 4), (1, 5, 7, 1), ('gBXqaucn', 'BBeujUUS', '', 'cHImXR', 'BeujUUS', 'BeujUUS'), (8, 5, 6, 7, 1, 5), (6, 4), (14, 6, 10, 12, 11, 4), (5, 7), (5, 7, 7, 6)]

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
        func_name = "remove_nested"
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
        for test_case in ['assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)', 'assert remove_nested((2, 6, 8, (5, 7), 11)) == (2, 6, 8, 11)', 'assert remove_nested((3, 7, 9, (6, 8), 12)) == (3, 7, 9, 12)', 'assert remove_nested((3, 7, 9, (6, 8), (5,12), 12)) == (3, 7, 9, 12)']:
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
