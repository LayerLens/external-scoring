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
inputs = [['hello people', '@'], ['python program language', '$'], ['blank space', '-'], ['pythonprogramlanguage', '$'], ['    ', '*'], ['a_A_b', '!'], ['Testing one, two, three!', ' '], ['pythonprogTesting one, two, three!ramlanguage', '$'], ['pythonprogramlanguage', ' '], ['pytho!nprogramlanguage', '$'], ['pythonprogTesting one, two, three!ramlanguage ', ' '], ['pythonprogTesting one, two, three!ramlanguage', ' '], ['$', '$'], ['pythonprogTest *   a_A_b', ' '], ['pythonprogTpythonprogTesting one, two, three!ramlanguageramlanguage', '!'], ['pythonprogramlanguage ', ' '], ['pythonprogTest *   a_A_b ', ' '], ['pytoho!nprogramlanguage', '$'], ['pythonprtwo,oggramlanguage', ' '], ['pythonprogTst *   a_A_b ', '$'], [' ', ' '], ['!!', '!'], ['a_A_b', '$'], ['pythonprtwo,oggramnguage', ' '], ['pythonprogTst *    a_A_b ', '$'], ['pythonprogTst *    a_A_b  ', ' '], ['     ', '*'], ['  ', ' '], [' pythonprogTest ', ' '], ['!', '!'], ['pythonprtwo,oggramngupytho!nprogramlanguageage', ' '], ['pypythonprtwo,oggramngupytho!nprogramlanguageagethonprogTest *   a_A_b', ' '], ['pytho!nprogramlanguagpe', '$'], ['three!', '$'], ['ppythonprtwo,oggramlanguagee', ' '], ['p ytho!nprogramlanguage', '*'], ['Testing one, two, three!', 'p'], ['pytho!nprogramlanguag  ', '!'], ['!  !', '!'], ['pythonprogTpythonprogTesting one, two, three!ramlanguageramlanguage', ' '], ['p!', '!'], ['   ', ' '], ['!!', ' '], ['pytho!nprogramlangnuage', '$'], ['pythonprogTest *   a_A', ' '], ['pythonprogTsto *    a_A_b  ', ' '], ['a_A_a_A', '$'], ['*', '*'], ['pythonprogramlanguag$e', ' '], ['pytho!nprogramlanguag  !', '!'], ['pythor!nprogramlanguage', '*'], ['pytho!nprogramlanguage', '!'], ['pythonprogTst *  h  a_A_b  ', ' '], ['pytho!nprpythonprogTstoogramlanguage', '$'], ['pytho!nprogramlanguag', ' '], ['h$$', '$'], ['   ', '!'], ['p', ' '], ['pngupytho!nprogramlanguageage', ' '], ['ppythonprtwo,oggramlanguagee', 'p'], ['pythonprogramlanguag$e', '$'], ['h$', '$'], [' pythonprogTest ', '!'], ['pythonprogmlanguag$e', ' '], ['$', ' '], ['pythonprogTsto *    a_A_b  ', '!'], ['!!pythonprogramlanguag$e', ' '], ['pythonprogramlanguagee ', ' '], ['pytoho!nprogramlanguage', '!'], ['Testing one, two, three!pythonprogTst *    a_A_b  !', '!'], ['pythonprogTesting one, two, three!ramlapytho!nprogramlangnuagenguage ', ' '], ['pytoho!nprogramlangua ge', '!'], ['pythonprogmlpythonprogTstuag$e', ' '], ['pythonprogramlanguagee $', '$'], ['ppythonprpytho!nprogramlanguag  two,oggramlanguagee', ' '], ['!pythonprogTst *    a_A_b  !pythonprogramlanguag$e', '!'], ['pythonprogTpythonprogTesting one, two, three!ramlanguageramlangpythonprogTest *   a_A_b ge', ' '], ['p ytho!nprogramlanguae', '*'], ['pytho!nprogramlaanguag  ', '!'], ['!pythonprogramlanguag$e*', '*'], ['two,', '*'], ['h$', ' '], ['ttwo,', '*'], ['pythonprtwo,oggramngupypytho!nprogramlangnuagetho!nprogramlanguageage', ' '], ['ppythonprtwo,oggramlanguagee$$', ' '], ['pythothree!ramlapytho!nprogramlangnuagenguage!nprogramlanguage', '$'], ['', ' '], ['*', ' '], ['pythonprtwo,oggramlanguage!', '!'], ['pythonprogTesting one, twoe, three!ramlapytho!nprogramlangnuagenguage ', ' '], ['pytho!nprogramlangp ytho!nprogramlanguaenuage', '$'], ['pytho!nprogramlanguaggpe', ' '], ['pytthor!nprogramlanguage', '*'], ['pypythonprtwo,oggramngupytho!nprogramlanguageagethonprogTest *   a_A_b', '$'], ['pypythonprtwo,oggramngupytho!nprogramlangguageagethonprogTest', ' '], ['$$', '$'], ['pytho!nprogramlanguag  !', ' '], ['p', '$'], ['pythothree!ramlapytho!nprogramlangnuagenguage!nprogramlanguaage', '$'], ['hh$', '$'], ['pytoho!nprogramlangpythonprogTstua ge', '!'], [' pythonprogramlanguage ', ' '], ['p', 'p'], ['pythonprogTesting one$$, two, three!ramlanguage', '$'], ['pythothreae!ramlapytho!nprogramlangnuagenguage!nprogramlanguaage', '$'], ['pytho!nprogramlaanguag  ', ' '], ['pythonprogramlanguagee ', 'p']]
results = ['hello@people', 'python$program$language', 'blank-space', 'pythonprogramlanguage', '****', 'a_A_b', 'Testing one, two, three!', 'pythonprogTesting$one,$two,$three!ramlanguage', 'pythonprogramlanguage', 'pytho!nprogramlanguage', 'pythonprogTesting one, two, three!ramlanguage ', 'pythonprogTesting one, two, three!ramlanguage', '$', 'pythonprogTest *   a_A_b', 'pythonprogTpythonprogTesting!one,!two,!three!ramlanguageramlanguage', 'pythonprogramlanguage ', 'pythonprogTest *   a_A_b ', 'pytoho!nprogramlanguage', 'pythonprtwo,oggramlanguage', 'pythonprogTst$*$$$a_A_b$', ' ', '!!', 'a_A_b', 'pythonprtwo,oggramnguage', 'pythonprogTst$*$$$$a_A_b$', 'pythonprogTst *    a_A_b  ', '*****', '  ', ' pythonprogTest ', '!', 'pythonprtwo,oggramngupytho!nprogramlanguageage', 'pypythonprtwo,oggramngupytho!nprogramlanguageagethonprogTest *   a_A_b', 'pytho!nprogramlanguagpe', 'three!', 'ppythonprtwo,oggramlanguagee', 'p*ytho!nprogramlanguage', 'Testingpone,ptwo,pthree!', 'pytho!nprogramlanguag!!', '!!!!', 'pythonprogTpythonprogTesting one, two, three!ramlanguageramlanguage', 'p!', '   ', '!!', 'pytho!nprogramlangnuage', 'pythonprogTest *   a_A', 'pythonprogTsto *    a_A_b  ', 'a_A_a_A', '*', 'pythonprogramlanguag$e', 'pytho!nprogramlanguag!!!', 'pythor!nprogramlanguage', 'pytho!nprogramlanguage', 'pythonprogTst *  h  a_A_b  ', 'pytho!nprpythonprogTstoogramlanguage', 'pytho!nprogramlanguag', 'h$$', '!!!', 'p', 'pngupytho!nprogramlanguageage', 'ppythonprtwo,oggramlanguagee', 'pythonprogramlanguag$e', 'h$', '!pythonprogTest!', 'pythonprogmlanguag$e', '$', 'pythonprogTsto!*!!!!a_A_b!!', '!!pythonprogramlanguag$e', 'pythonprogramlanguagee ', 'pytoho!nprogramlanguage', 'Testing!one,!two,!three!pythonprogTst!*!!!!a_A_b!!!', 'pythonprogTesting one, two, three!ramlapytho!nprogramlangnuagenguage ', 'pytoho!nprogramlangua!ge', 'pythonprogmlpythonprogTstuag$e', 'pythonprogramlanguagee$$', 'ppythonprpytho!nprogramlanguag  two,oggramlanguagee', '!pythonprogTst!*!!!!a_A_b!!!pythonprogramlanguag$e', 'pythonprogTpythonprogTesting one, two, three!ramlanguageramlangpythonprogTest *   a_A_b ge', 'p*ytho!nprogramlanguae', 'pytho!nprogramlaanguag!!', '!pythonprogramlanguag$e*', 'two,', 'h$', 'ttwo,', 'pythonprtwo,oggramngupypytho!nprogramlangnuagetho!nprogramlanguageage', 'ppythonprtwo,oggramlanguagee$$', 'pythothree!ramlapytho!nprogramlangnuagenguage!nprogramlanguage', '', '*', 'pythonprtwo,oggramlanguage!', 'pythonprogTesting one, twoe, three!ramlapytho!nprogramlangnuagenguage ', 'pytho!nprogramlangp$ytho!nprogramlanguaenuage', 'pytho!nprogramlanguaggpe', 'pytthor!nprogramlanguage', 'pypythonprtwo,oggramngupytho!nprogramlanguageagethonprogTest$*$$$a_A_b', 'pypythonprtwo,oggramngupytho!nprogramlangguageagethonprogTest', '$$', 'pytho!nprogramlanguag  !', 'p', 'pythothree!ramlapytho!nprogramlangnuagenguage!nprogramlanguaage', 'hh$', 'pytoho!nprogramlangpythonprogTstua!ge', ' pythonprogramlanguage ', 'p', 'pythonprogTesting$one$$,$two,$three!ramlanguage', 'pythothreae!ramlapytho!nprogramlangnuagenguage!nprogramlanguaage', 'pytho!nprogramlaanguag  ', 'pythonprogramlanguageep']

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
        func_name = "replace_blank"
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
        for test_case in ['assert replace_blank("hello people",\'@\')==("hello@people")', 'assert replace_blank("python program language",\'$\')==("python$program$language")', 'assert replace_blank("blank space","-")==("blank-space")']:
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
