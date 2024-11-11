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
inputs = [['aabbbb'], ['aabAbbbc'], ['accddbbjjj'], [''], ['xyz123'], ['ab'], ['aabb'], ['xaabbyz123'], ['xaabbyz1323'], ['axyz123bb'], ['xaabbyz1323ababb'], ['xaabbyzxaababyz1323ababb123'], ['aabaabbb'], ['aBXGdUCk'], ['aaxyz123bbxyz123bb'], ['aBXbdUk'], ['xaabbyz1323ababbb'], ['xaabbyz1323ababbaaxyz123bbxyz123bb'], ['xaabbya1bxaabbyz1323ababbz123'], ['xaabxaabbyz1231323ababb123'], ['xaabbyz1z23'], ['aaxyaaxyz123bbxyz123bbz12ab3bbxyz123bb'], ['xaabbyzxaxaabbyz123ababyz1323ababb1323'], ['xaabxaabbyz1231323abab2b123'], ['aaxyaaxyz123bbxyz1223bbz12ab3bbxyz123bb'], ['abxaabbya1bxaabbyz1323ababbz123'], ['aaab'], ['xaabxaabbyz1231323ababbb123'], ['a'], ['xaabxaabbyz1231a323ababb123'], ['aab'], ['aaxyaaxyz123bbxyz123xyz123bbz12ab3bbxyz123bb'], ['aaaaabxyz123bbxyz123bba'], ['aaxyaaxyz123bbxyz1b223bbz12ab3bbxyz123bb'], ['xaabxaa3bbyz1231323ababb123'], ['aaxyaaxyz1aabyz123bb'], ['xaabxaa3bbyz1231aaxyaaxyz123bbxyz1223bbz12ab3bbxyz123bb323ababb123'], ['xaabbyz1323ababbaaxyz123bbxbyz123bb'], ['aBXbdk'], ['xaaabbyz1323ababbaaxyz123bbxbyz123bb'], ['aaxyaaxyz123bbxyz12xyz1233xyz123bbz12ab3bbxyz123bb'], ['ababaabbb'], ['aaxyaaxyz123bbxyz123bbz12ab3bbxyzxaabbyz1z23123bb'], ['xaaabbyz1323ababbbyz123bb'], ['xaabbyazxaababyz1323ababb123'], ['aabbabb'], ['aBXbdUxaabbya1bxaabbyz1323ababbz123k'], ['xaaxyz123bbbb'], ['xaabbayababb'], ['xaabbya1bxaabbxaabbyz1323ababbz1323ababbz123'], ['aabaaaxyaaxyz123bbxyz12xyz1233xyz123bbz12ab3bbxyz123bbabbb'], ['xaabbyzxaxaaxaabxaabbyz1231a323ababb123bbyz123ababyz1323ababb1323'], ['aaaxyaaxyz123bbxyz123bbz12ab3bbxyz123bbabbabb'], ['aSLQ'], ['xaaabbyz1323aaaxyaaxyz123bbxyz123bbz12ab3bbxyz123bbbabbaaxyz123bbxbyz123bb'], ['xaabbyzxaabbyazxaababyz1323ababb123xaxaabbyz123ababyz1323ababab1323'], ['xaabbya1bxaabbxaabbyz1323ababbz1323ababbxaabbyzxaabbyazxaababyz1323ababb123xaxaabbyz123ababyz1323ababab1323123'], ['aabaaaxyaaxyz123bbxyz12xyz1233xyz123bbz12ab3bbaabaaaxyaaxyz123bbxyz12xyz1233xyz123bbz12ab3bbxyz123bbabbb'], ['aaaaabxyz123bbxyz12aaxyaaxyz123bbxyz123bbz212ab3bbxyzxaabbyz1z23123bbbba'], ['aBXGdUCkaabbabb'], ['aBXGdUCkaabbbabb'], ['aaxyaaxyz123bbxyz1223bbz12ab3bbxyz1231bb'], ['aaxyaaxyz123bbxyz1xaaabbyz1323ababbaaxyz123bbxbyz123bbb223bbz12ab3bbxyz123bb'], ['xaabbyyzxaababyz1323ababb123'], ['b'], ['aaaaab'], ['aaxyaaxyz123bbxyz1xaaabbyz1323ababbaaxyz123bbxbyyz123bbb223bbz12ab3bbxyz123bb'], ['zAxZKNA'], ['aaaaabxyzxaabbyzxaabbyazxaababyz1323ababb123xaxaabbyz123ababyz1323ababab1323123bbxyz123bba'], ['xaabbxaabbya1bxaxaabbya1bxaabbyz1323ababbz123abbxaabbyz1323ababbz1323ababbxaabbyzxaabbyazxaababyz1323ababb123xaxaabbyz123ababyz1323ababab1323123yz1323'], ['xaabbya1bxaabbyz1323ababbz12xaabxaabbyz1231323ababb123'], ['xaabbbyyzxaababyz1323ababb123'], ['xaaabbyz1323ababbbyzaaabbbb'], ['xaabbyz1323ababbaaxyz123bybxyz123bb'], ['xaaxyz123bbb'], ['aaaaxyaaxyz123bbxyz1223bbz12ab3bbxyz1231bbbb'], ['xaabxaa3bbyz1231aaxyaaxyz123bbxyz1223bbz12ab3bbxyz12a3bb3x23ababb123'], ['aaxyaaxyz123bbxyz123bbz12ab3bbxyz12b3bb'], ['xaabbya1bxaabbyz1323ababbz12xaabxaabbyz1231323ababbaBXbdUk3'], ['xa2axyz123bbb'], ['aaxyaaxyz123bbxyz1223bbz12b3bbxyz12xaabbyyzxaababyz1323ababb1233bb'], ['LaSL'], ['aaaaxyaaxyz123bbxyz1223bbz12ab3bbxyz123bbb'], ['xaabbya1bxaabbxaabbyz1323ababbz1323ababbxaabbyzxaabbyazxaababyz1323ababb123xaxaabaaxyaaxyz123bbxyz1xaaabbyz1323ababbaaxyz123bbxbyz123bbb223bbz12ab3bbxyz123bbbyz123ababyz1323ababab1323123'], ['aabaaaxyaaxyz123bbxyz12xyzbbb'], ['xaaabbyzxaxaabbyz123ababyz1323ababb1323'], ['xaxaabbya1bxaabbyz1323ababbz123z123bbbb'], ['xaabbya1bxaabbyz1323ababbz12xaabxaabbyz1231323ababbaBXbdUk3ayababb'], ['axyxz123bb'], ['xaabbyzxaabbyazxaabaabyz1323ababb123xaxaabbaxyz123bbyz123ababyz1323ababab1323'], ['aabaaabbb'], ['axaabbyz1z23aaBXGdUGCkaabbbabbbb'], ['xaabbyzxaababyz1323abbabb123'], ['abxaabbybbyz132a3ababbz123'], ['aaxyaaxyz123bbxyz1223bbz12b3bbxyz12xaabbyyxaabxaabbyz1231323abab2b123zxaababyz1323ababb1233bb'], ['aabaaaxyaaxyz123bbxyz12xyz1233xyzaabbabb123bbz12ab3bbxyz123bbabbb'], ['aBXGdUCkaaabbabb'], ['xaaabbyz1323ababbaaxyz12bbb'], ['xaabbyzxaabbyazxaababyz132aabaaaxyaaxyz123bbxyz12xyz1233xyzaabbabb123bbz12ab3bbxyz123bbabbb3ababb123xaxaabbyz123ababyz1323ababab1323'], ['aaxyaaxyz123bbxyz123bbzxyz12b3bb'], ['aBxaabxaabbyz1231323ababbb123XGdUCk'], ['abaaxyaaxyz123bbxyz1b223bbz12ab3bbxyz123bbabaabbb'], ['aaaaabxyzxaabbyzxaabbyazxaababyz1323ababb123xaxaabbyz123ababyz1323ababab1323123bbxyz123bbaaSLQ'], ['xaabbyzxaxaaxaabxxaaabbyz1323ababbbyzaaabbbbaabbyz1231a323ababb123bbyz123ababyz1323ababb1323'], ['axaabbya1bxaabbyz1323ababbz12xaabxaabbyz1231323ababb123xaabbyz1z23aaBXGdUGCkaabbbabbbb'], ['xaaaxyaaxyz123bbxyz123bbz12ab3bbxyzxaabbyz1z23123bbabbyz123']]
results = [True, False, False, False, False, True, True, False, False, True, True, False, True, False, True, False, True, True, False, False, False, True, False, False, True, False, True, False, False, False, True, True, False, True, False, True, False, True, False, True, True, True, True, True, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, False, True, True, True, True, False, True, False, True, True, False, True, False, True, False, True, True, True, False, True, True, False, False, True, True, True, True, False, True, False, True, False, False, True, False]

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
        func_name = "text_starta_endb"
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
        for test_case in ['assert text_starta_endb("aabbbb")', 'assert not text_starta_endb("aabAbbbc")', 'assert not text_starta_endb("accddbbjjj")']:
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
