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
inputs = [['python'], ['aaa'], ['data'], [''], ['ms'], ['mms'], ['msms'], ['mmms'], ['yQNKBeQ'], ['msmyQNKBeQs'], ['mmss'], ['m'], ['msmss'], ['msmyQNyQNKBeQKBeQs'], ['mmsss'], ['mmsmyQNKBeQsmsss'], ['smssms'], ['mmsmss'], ['yKQNKBeQ'], ['mmmmmsmsssmmsss'], ['msmms'], ['msmyQNyQNKBeQKBeQsmmsmss'], ['msmyQNyQNBKBeQKBeQsmmsmss'], ['mmmsms'], ['mmsms'], ['msmmsms'], ['mmmss'], ['smssm'], ['mss'], ['msmmmss'], ['mmmms'], ['mssmsmyQNKBeQs'], ['mmsmyQNKBeQsmmsss'], ['msmyQNKBeQNs'], ['zWgdk'], ['mmsmsmmssss'], ['mQsmyQNKBeQs'], ['smssmsmyQNKBeQsmssms'], ['mmmmsms'], ['RfuIu'], ['mmssms'], ['RufuIu'], ['mmsmyQNyQNKBeQKBeQsmmmsms'], ['mssmsmysQNKBeQs'], ['mssmsNKBeQs'], ['mmmsmsmss'], ['mmmmsmyQNKBeQsmmsssssms'], ['msmmss'], ['smss'], ['smszWgdksm'], ['smssmms'], ['msmyQNyQNKBeQKBseQsmmsmss'], ['mmsmyQNyQNKBmmmsmseQKBeQsmmmsms'], ['msmmmmsmyQNKBeQNsss'], ['mmmsmss'], ['mmmmmmsmsssmmsss'], ['mmmsmyQNKBeQNsssms'], ['smssmsmymmsmsmmssssQNKBeQsmssms'], ['mmsmyQNKBmeQs'], ['mmmsmyQNyQNKBmmmsmseQKBeQsmmmsmsmsms'], ['mmmmsmsmsmmmmmmsmsssmmsss'], ['mmmssyQNKBeQmss'], ['msmyQNyQKNKBeQKBeQsmmsmss'], ['msmyQNyQKNKBmsmyQNKBeQNseQKBeQsmmsmss'], ['msmyQNyQNKBeQKBseQsmmQsmss'], ['msmyQNKBesQNs'], ['yKQNKBemssmsmysQNKBeQsQ'], ['mmsmyQNKBeQssmmsss'], ['msmmsmmsms'], ['mmyKQNKBeQmssyQNKBeQmss'], ['mmmmsmssmsNKBeQsmsmmms'], ['mmmsmmmsmsssmmsss'], ['smssmmmmmsmsssmmsssm'], ['mmmsmyQNKBeQsmssss'], ['msmyQNyQNBKyBeQKBeQsmmsmss'], ['msmmsmmmsms'], ['mmmsmsmyQNyQNKBeQKBseQsmmsmssms'], ['mmmmmsmyQNKBeQNsssmsmms'], ['mmmmsmsmsmmmmmmsmsssmmmmsmyQNKBeQsmmssssss'], ['mmmmsmyQNKBeQNsssmsmsmmsmmssss'], ['mmmmmmmsmyQNKBeQNsssmsmsmmsmmssssmmsmyQNKBeQNsssmsmms'], ['mssmQsmyQNKBeQs'], ['smmsssmsmymmsmsmmssssQNKBeQsmssms'], ['yKQN'], ['smssmmmmmmmmmsmyQNKBeQNsssmsmsmmsmmssssmmsmyQNKBeQNsssmsmmss'], ['smssmsmyQNKBmmsmyQNKBeQssmmssseQsmssms'], ['Rf'], ['mmRufuIus'], ['smssmBmmsmyQNKBeQssmmssseQsmssms'], ['BmmmsmyQNyQNKBmmmsmseQKBeQsmmmsmsmsmsRfuIu'], ['smsmsmssmsmyQNKBmmsmyssseQsmssms'], ['yKQNKmssmQsmyQNKBeQsBeQ'], ['mssmmmmsmyQNKBeQsmmsssssms'], ['zWgdWk'], ['mssmmms'], ['zWgdW'], ['smmsmyQNKBeQssmmsssmssm'], ['mssmsmysQNKBeQss'], ['mszWgWdWkms'], ['msmssmsmysQNKBeQss'], ['mmsmyQNyQNKBmmmsmseQKBmeQsmmmsms'], ['smszkWgdksm'], ['msmyQNyQNKBeQKBesQsmmsmss'], ['smssmBmmsmyQNKBeQsssmmssseQssmssms']]
results = [False, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "all_Characters_Same"
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
        for test_case in ['assert all_Characters_Same("python") == False', 'assert all_Characters_Same("aaa") == True', 'assert all_Characters_Same("data") == False']:
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
