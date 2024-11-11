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
inputs = [['The person is most value tet', 3], ['If you told me about this ok', 4], ['Forces of darkeness is come into the play', 4], ['', 3], ['', 5], ['', 10], ['This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestablishmentarianism.', 10], ['This is a Test of the Function', 4], ['This is a test sentence with all words having length of five.', 5], ['This is a very long and complex sentence that contains words of different lengthsa such as abracadabra, internationalization, and antidisestablishmentarianism.', 10], ['Test', 6], ['This is a test sentence with all words having length of five.', 10], ['Test', 10], ['T', 11], ['', 6], ['', 4], ['Tesallt', 6], ['abracadabra,Test', 10], ['This is a Test Thisof the Function', 4], ['five.', 4], ['This is a Test Thisof the Fuwith', 6], ['Fuwith', 10], ['contains', 5], ['iThis is a test sentence with all words having length of five.', 5], ['contais', 5], ['', 9], ['This is a test sentence with all words having length of five.t of the Function', 4], ['abracadabra,Test', 11], ['This is a Test Thisof the Fuwith', 7], ['This is a Test Thisof the Fuwith', 5], ['all', 6], ['contais', 3], ['abracadabra,Test', 5], ['This is a very long and complex sentence that contains words of different lengthsa such as abracadabra, internationalization, and antidisestablishmentarianism.', 9], ['TeT', 10], ['iThis is a test sentence with all words having length of five.', 10], ['very', 9], ['Test', 9], ['Fuwith', 5], ['This is a Test of the unction', 4], ['that', 11], ['This is a very long and complex sentence that contaThisins words of different lengths such as abracadabra, internationalization, and antidisestablishmentarianism.', 10], ['This is a Test of the unctionof', 4], ['This is a Test of the unction', 9], ['Tabracadabra,his is a Test Thisof the Function', 7], ['unctioncontais', 3], ['Test', 5], ['conThisoftais', 3], ['Tabracadabra,his is a Test Thisof the Function', 9], ['This is a test sen tence with all words having length of five.', 5], ['complex', 3], ['This is a Test of the unctionof', 5], ['aand', 6], ['aand', 9], ['tunctioncontais', 7], ['This is a Test of the unctionof', 7], ['having', 3], ['This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestatunctioncontaisblishmentarianism.', 10], ['different', 4], ['This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestablishmentarianism.', 11], ['This is a very long and complex sentence that contains words of different lengthsthationalization, and antidisestablishmentarianism.', 9], ['This is a test sentence with all words having length of five.', 7], ['', 7], ['This is a Test Thisof the FuwitThis is a Test of the Functionh', 7], ['This is a test sentence with all words having length of five.', 11], ['This is a very long and complex sentence that contains words of different lengthsthationalization, and antidisestablishmentarianism.', 6], ['TeunctionofT', 10], ['Thsenis is a Test of the Function', 4], ['This is a Tescontainst of the unctionof', 7], ['This isi a Test Thisof the Function', 7], ['aan', 9], ['This is a Tescontainst of the unctionof', 5], ['This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestatunctioncontaisblishmentarianism.', 11], ['tence', 9], ['lengthsa', 4], ['This is a very long and complex sentence that contains words of different lengthsa such as abracadabra, internationalization, and antidisestablishmentarianism.', 3], ['This i Test Thisof the FuwitThis is a Test of the Functionh', 11], ['a', 5], ['abracradabra,Test', 11], ['iThis is a test sentence with all words having length of five.', 11], ['FuwitThis', 6], ['thatunctioncontais', 11], ['This ise unction', 9], ['all', 5], ['iThis is a tiest sentence with all words having length of five.', 5], ['TeunctionofT', 5], ['This is a Test of the unctionof', 2], ['that', 5], ['FuwitThis', 5], ['Tabracadabra,his is a Test Thisof the Function', 11], ['test', 5], ['This', 2], ['abracadabra,Tebst', 10], ['This is a very long and complex sentence that contains words of differecontainsnt lengthsa such as abracadabra, internationalization, and antidisestablishmentarianism.', 3], ['Tesallt', 5], ['length', 3], ['thatt', 11], ['contais', 10], ['having', 11], ['Test', 8], ['lengths', 11], ['lengths', 5], ['thatunctioncontais', 10], ['This is a Test of abracadabra,Tebstthe unctionofwith', 2], ['lengthsTesallt', 5], ['TeT', 3], ['TieunctionofT', 5], ['', 8], ['FuwitThis', 7]]
results = ['person is most value', 'If you me about ok', 'Forces of darkeness is the', '', '', '', 'This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestablishmentarianism.', 'is a of the Function', 'This is a test sentence with all having length of', 'This is a very long and complex sentence that contains words of different lengthsa such as abracadabra, internationalization, and antidisestablishmentarianism.', 'Test', 'This is a test sentence with all words having length of five.', 'Test', 'T', '', '', 'Tesallt', 'abracadabra,Test', 'is a Thisof the Function', 'five.', 'This is a Test the', 'Fuwith', 'contains', 'is a test sentence with all having length of', 'contais', '', 'is a sentence all words having length of five.t of the Function', 'abracadabra,Test', 'This is a Test Thisof the Fuwith', 'This is a Test Thisof the Fuwith', 'all', 'contais', 'abracadabra,Test', 'This is a very long and complex sentence that contains words of lengthsa such as abracadabra, internationalization, and antidisestablishmentarianism.', 'TeT', 'iThis is a test sentence with all words having length of five.', 'very', 'Test', 'Fuwith', 'is a of the unction', 'that', 'This is a very long and complex sentence that contaThisins words of different lengths such as abracadabra, internationalization, and antidisestablishmentarianism.', 'is a of the unctionof', 'This is a Test of the unction', 'Tabracadabra,his is a Test Thisof the Function', 'unctioncontais', 'Test', 'conThisoftais', 'Tabracadabra,his is a Test Thisof the Function', 'This is a test sen with all having length of', 'complex', 'This is a Test of the unctionof', 'aand', 'aand', 'tunctioncontais', 'This is a Test of the unctionof', 'having', 'This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestatunctioncontaisblishmentarianism.', 'different', 'This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestablishmentarianism.', 'This is a very long and complex sentence that contains words of lengthsthationalization, and antidisestablishmentarianism.', 'This is a test sentence with all words having length of five.', '', 'This is a Test Thisof the FuwitThis is a Test of the Functionh', 'This is a test sentence with all words having length of five.', 'This is a very long and complex sentence that contains words of different lengthsthationalization, and antidisestablishmentarianism.', 'TeunctionofT', 'Thsenis is a of the Function', 'This is a Tescontainst of the unctionof', 'This isi a Test Thisof the Function', 'aan', 'This is a Tescontainst of the unctionof', 'This is a very long and complex sentence that contains words of different lengths such as abracadabra, internationalization, and antidisestatunctioncontaisblishmentarianism.', 'tence', 'lengthsa', 'This is a very long complex sentence that contains words of different lengthsa such as abracadabra, internationalization, antidisestablishmentarianism.', 'This i Test Thisof the FuwitThis is a Test of the Functionh', 'a', 'abracradabra,Test', 'iThis is a test sentence with all words having length of five.', 'FuwitThis', 'thatunctioncontais', 'This ise unction', 'all', 'is a sentence with all having length of', 'TeunctionofT', 'This a Test the unctionof', 'that', 'FuwitThis', 'Tabracadabra,his is a Test Thisof the Function', 'test', 'This', 'abracadabra,Tebst', 'This is a very long complex sentence that contains words of differecontainsnt lengthsa such as abracadabra, internationalization, antidisestablishmentarianism.', 'Tesallt', 'length', 'thatt', 'contais', 'having', 'Test', 'lengths', 'lengths', 'thatunctioncontais', 'This a Test abracadabra,Tebstthe unctionofwith', 'lengthsTesallt', '', 'TieunctionofT', '', 'FuwitThis']

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
        func_name = "remove_length"
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
        for test_case in ["assert remove_length('The person is most value tet', 3) == 'person is most value'", "assert remove_length('If you told me about this ok', 4) == 'If you me about ok'", "assert remove_length('Forces of darkeness is come into the play', 4) == 'Forces of darkeness is the'"]:
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
