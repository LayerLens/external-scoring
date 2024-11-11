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
inputs = [['probasscurve', 'pros'], ['digitalindia', 'talent'], ['exoticmiles', 'toxic'], ['The quick brown fox jumps over the lazy dog', 'fox'], ['This is a sample string', 'i a'], ['1234567890', '01234'], ['abcd efgh', 'ab cd'], ['This is a sampile string', 'i a'], ['abcd efgh', 'This is a sampile string'], ['a', '01234'], ['This is a sample string', 'a'], ['abcabgh', 'ab'], ['i a', 'This is a sampile string'], ['dog', 'This is a sampile string'], ['01234', '01234'], ['abcabgh', 'a'], ['The quick brown fox jumps otver the lazy dog', 'fox'], ['do', 'This is a sampile string'], ['abcabggh', 'a'], ['This is a sample string', 'This'], ['ia', 'This is a sampile string'], ['ia', 'This is a sample stringsample'], ['This is a sasmple string', 'This is a sample strin1234567890g'], ['sis', 'dog'], ['abcd efgh', 'bab cd'], ['bab cd', 'bab cd'], ['bab cd', 'This is a sample stringsample'], ['This is a sampile string', 'This is a sampile string'], ['do', 'do'], ['This is a sample stringsample', 'Thish is a sampile string'], ['a', '1234567890'], ['dog', 'dog'], ['Thiss is a sampring', 'This is a sampring'], ['The quick brown fox jumps over the lazy dog', 'This is a sampile string'], ['brownabcd', 'iaquick'], ['This is a sasmple string', 'This is a sample strin1234567g'], ['This is a sample stringsamplae', 'This is a sample stringsample'], ['Thish is a sampile string', 'Thish is a sampile string'], ['1234567890', '1234567890'], ['a', '0123'], ['This is a sample stringsam', 'This is a sample stringsample'], ['This is a sample stringsample', 'stringsam'], ['bab cd', 'bdab cd'], ['This is a sampThis is a sample stringsamplele stringsample', 'Thish is a sampile string'], ['i a', 'i a'], ['aa', 'a'], ['1234567890', 'This is a sampThis is a sample stringsamplele stringsample'], ['a', 'dog'], ['i a', 'ia'], ['The quickfox jumps otver the lazy dog', 'fox'], ['bdab', 'The quick brown fox jumps over the lazy dog'], ['This is a sample stringsample', 'bab cd'], ['This is a sasmple string', 'Thiss is a sampring'], ['The quickfox jumpsg otver the latzy dog', 'The quickfox jumpsg otver the latzy dog'], ['This is a sample stringsam', 'stringsam'], ['The quick brown fox jumps otver the lazy dog', 'The quickfox jumpsg otver the latzy dog'], ['Tthis is a sampile sstring', 'This is a sampile string'], ['The quick brown fox jumps otver the lazy dog', 'sampile'], ['Thish is a sampile string', 'This is a sampile string'], ['0123', '01234'], ['012strin1234567g34', '01234'], ['aab', 'ab'], ['abdog', 'ab'], ['stringsamplea', 'a'], ['stringsamplea', 'stringsamplea'], ['1234567890', 'This is asampThis sampThis is a sample stringsamplele stringsample'], ['The quick brown fox jumps otver the lazy dog', 'foox'], ['Thiss is a sampring', 'The quickfox jumpsg otver the latzy dog'], ['dThis is a sampile stri', 'dThis is a sampile stri'], ['ab cd', 'ab cd'], ['jumpsg', 'jumpsg'], ['fstringsampleaox', 'fox'], ['the', '01234'], ['bdab cd', '1234567890'], ['This is a sample stringsample', 'This is a sample stringsample'], ['stri', 'stringsam'], ['brownabcd', 'brownabcd'], ['This issasmple a sampile string', 'This is a sampile string'], ['0123', '0123'], ['bdabb cd', '1234567890'], ['over', 'The quickfox jumpsg otver the latzy dog'], ['01234', '0134'], ['This is a sasmring', 'This is a sasmple string'], ['bdab cd', 'bdab cd'], ['ia', 'ia'], ['fstrix', 'The quickfox jumps otver the lazy dog'], ['aasampThisb', 'ab'], ['Thiss', 'bab cd'], ['stri', 'sampile'], ['This is a sample strimplae', 'This is a sample stringsample'], ['a', 'a'], ['bab cd', 'babstringsamplea cd'], ['abrownabcd', 'The quickfox jumps otver the lazy dog'], ['bdabcdab', 'This is a sample strin1234567g'], ['i aThis is a sasmple string', 'This is a sample strin1234567g'], ['Thish is a sampile string', 'stringsam'], ['bdabb cd', '0123'], ['This is a sampring', 'This is a sample strin1234567g'], ['The quick brown fox jumg', 'The quickfox jumpsg otver the latzy dog'], ['This is a sasmple string', 'This is a sample stringsample'], ['1234567890', 'fox'], ['foox', 'This is a sample strimplae'], ['This is a sasmple sstringstring', 'This is a sasmple sstringstring'], ['03134', '0134'], ['0123', 'llae'], ['bdabb cd', '01223'], ['aquickfox', 'dog']]
results = ['bacuve', 'digiidi', 'emles', 'The quick brwn  jumps ver the lazy dg', 'Thsssmplestrng', '56789', 'efgh', 'Thsssmplestrng', 'bcdf', 'a', 'This is  smple string', 'cgh', '', 'do', '', 'bcbgh', 'The quick brwn  jumps tver the lazy dg', 'do', 'bcbggh', '  a ample trng', '', '', '', 'sis', 'efgh', '', 'bbcd', '', '', '', 'a', '', '', 'quckbowfoxjuovzydo', 'brownbd', '', '', '', '', 'a', '', 'Th   ple ple', '', '', '', '', '1234567890', 'a', ' ', 'The quick jumps tver the lazy dg', '', 'Thisissmplestringsmple', 'let', '', 'Th   ple ', 'bwn', '', 'Th quck brown fox ju otvr th zy dog', '', '', 'strin567g', '', 'dog', 'stringsmple', '', '1234567890', 'The quick brwn  jumps tver the lazy dg', 'n', '', '', '', 'stringsamplea', 'the', 'bdab cd', '', '', '', '', '', 'bdabb cd', '', '2', '', '', '', '', 'smpThis', 'Thiss', 'tr', '', '', '', 'bwnb', 'bdbcdb', '', 'Thh   ple ', 'bdabb cd', '', 'bwn', '', '1234567890', 'foox', '', '', '0123', 'bdabb cd', 'aquickfx']

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
        func_name = "remove_dirty_chars"
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
        for test_case in ['assert remove_dirty_chars("probasscurve", "pros") == \'bacuve\'', 'assert remove_dirty_chars("digitalindia", "talent") == \'digiidi\'', 'assert remove_dirty_chars("exoticmiles", "toxic") == \'emles\'']:
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
