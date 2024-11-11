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
inputs = [[3, 'python is a programming language'], [2, 'writing a program'], [5, 'sorting list'], [0, 'abc  def  ghi  jklm  nopqrs   tuvwxyz'], [0, ''], [10, 'thisisaverylongword testing wordlengths'], [100, 'hello python is a programming language'], [0, 'is'], [100, 'thisisaverylongwordw testing wordlengths'], [0, 'jklm'], [100, 'thisisaverylongwordw teseting wordlengths'], [0, 'thisisaverylongword testing wordlengths'], [10, 'is'], [10, 'hello python is a programming language'], [1, 'thisisaverylongword testing wordlengths'], [0, 'jklam'], [100, 'tuvwxyz'], [0, 'hello'], [0, 'jkjlam'], [100, ''], [1, 'jklam'], [100, 'thisisaverylongwordnopqrsw teseting wordlengths'], [10, 'heogramming language'], [10, ''], [100, 'i'], [11, 'thisisaverylongword testing wordlengths'], [100, 'thisisaverylongword'], [2, ''], [2, 'heogramming language'], [2, 'hello python is a programming language'], [100, 'ii'], [1, 'thisisaverylongwordw teseting wordlengths'], [100, 'thisisaveriylongwordw testing wordlengths'], [9, 'jklm'], [100, 'is'], [10, 'helloh python is a programming language'], [100, 'abc  def  ghi  jklm  nopqrs   tuvwxyz'], [2, 'heogramming laneguage'], [0, 'ajklamteseting'], [100, 'thisisaveriylongwordw'], [100, 'thisisaverylongwordw testheogramming languageing wordlengths'], [0, 'thisisaverylongwordnopqrsw teseting wordlengths'], [99, 'thisisaveriylongwordw'], [0, 'a'], [0, 'hello python is a programming language'], [0, 'aa'], [0, 'thisisaveriylongwordw'], [10, 'python'], [10, 'jkl'], [1, 'hello python is a programming language'], [1, 'jkllm'], [100, 'thisisaverylongwordnopqrsw teseting wordlengthsi'], [101, 'thisisaverylongwordw testing wordlengths'], [99, 'thisisaverylongwordw teseting wordlengths'], [99, 'heogramming langualaneguagege'], [0, 'ii'], [101, 'thisisaverylongwordw testheogramming languageing wordlengths'], [11, 'jkl'], [1, ''], [101, 'abc  def  ghi  jklm  nopqrs   tuvwx yz'], [0, 'thisisaveriylongwoordw'], [0, 'hlello'], [0, 'heogramming language'], [1, 'heogramming language'], [101, 'is'], [9, 'thisisaverylongwordnopqrsw teseting wordlengths'], [99, 'hello python is a programming language'], [1, 'thisisalanguageverylongwordw teseting wordleths'], [10, 'jkjlam'], [0, 'hlelllo'], [100, 'yz'], [0, 'ajheogramming languageklamteseting'], [9, 'helloh python is a programminlaneguageg language'], [11, 'thisisaveriylongwordw'], [2, 'thisisaverylongwordw teseting wordlengths'], [2, 'hlelllo'], [1, 'hello python is a prthisisaverylongwordnopqrsw teseting wordlengthsiogramming language'], [0, 'abc  def  ghi  jklm  thisisaveriylongwordwnopqrs   tuvwxyz'], [101, 'aaa'], [11, 'heogramming language'], [2, 'wordlengthsiogramming'], [1, 'thisisalanguageverylthisisaverylongwordnopqrsw teseting wordlengthsiongwordw teseting wordleths'], [11, 'wordlengthsiongwordw'], [1, 'heogramminghelloh python is a programming languagelanguage'], [11, 'thisisaverylongword'], [11, 'ljkl'], [99, 'thisisalanguageverylongwordw'], [1, 'ajheogramming languageklamteseting'], [0, 'wordlengthsi'], [100, 'thisisaveriylongwordwnopqrs'], [102, 'aaa'], [102, 'aaaa'], [10, 'thisisaveriylongwordw testing wordlengths'], [0, 'jkl'], [10, 'thisisaverylongwordnopqrsw teseting wordlengths'], [10, 'jk'], [100, 'thisisaverylongwordnopqrsw tegseting wordlengthsi'], [101, 'thisisajklmverylongwordw testing wordlengths'], [1, 'heogramming laneguage'], [1, 'ajklamteseting'], [100, 'thisisaverylongwordw testheogramming languagein wordlengths'], [102, 'thisisaveriylongwordw testing wordlengths'], [100, 'thisisavongwordw'], [100, 'hlello'], [0, 'hello python is heogramming laneguagea programming language'], [10, 'wlengthsiongwordw'], [99, 'hello pylanguage']]
results = [['python', 'programming', 'language'], ['writing', 'program'], ['sorting'], ['abc', 'def', 'ghi', 'jklm', 'nopqrs', 'tuvwxyz'], [], ['thisisaverylongword', 'wordlengths'], [], ['is'], [], ['jklm'], [], ['thisisaverylongword', 'testing', 'wordlengths'], [], ['programming'], ['thisisaverylongword', 'testing', 'wordlengths'], ['jklam'], [], ['hello'], ['jkjlam'], [], ['jklam'], [], ['heogramming'], [], [], ['thisisaverylongword'], [], [], ['heogramming', 'language'], ['hello', 'python', 'programming', 'language'], [], ['thisisaverylongwordw', 'teseting', 'wordlengths'], [], [], [], ['programming'], [], ['heogramming', 'laneguage'], ['ajklamteseting'], [], [], ['thisisaverylongwordnopqrsw', 'teseting', 'wordlengths'], [], ['a'], ['hello', 'python', 'is', 'a', 'programming', 'language'], ['aa'], ['thisisaveriylongwordw'], [], [], ['hello', 'python', 'is', 'programming', 'language'], ['jkllm'], [], [], [], [], ['ii'], [], [], [], [], ['thisisaveriylongwoordw'], ['hlello'], ['heogramming', 'language'], ['heogramming', 'language'], [], ['thisisaverylongwordnopqrsw', 'wordlengths'], [], ['thisisalanguageverylongwordw', 'teseting', 'wordleths'], [], ['hlelllo'], [], ['ajheogramming', 'languageklamteseting'], ['programminlaneguageg'], ['thisisaveriylongwordw'], ['thisisaverylongwordw', 'teseting', 'wordlengths'], ['hlelllo'], ['hello', 'python', 'is', 'prthisisaverylongwordnopqrsw', 'teseting', 'wordlengthsiogramming', 'language'], ['abc', 'def', 'ghi', 'jklm', 'thisisaveriylongwordwnopqrs', 'tuvwxyz'], [], [], ['wordlengthsiogramming'], ['thisisalanguageverylthisisaverylongwordnopqrsw', 'teseting', 'wordlengthsiongwordw', 'teseting', 'wordleths'], ['wordlengthsiongwordw'], ['heogramminghelloh', 'python', 'is', 'programming', 'languagelanguage'], ['thisisaverylongword'], [], [], ['ajheogramming', 'languageklamteseting'], ['wordlengthsi'], [], [], [], ['thisisaveriylongwordw', 'wordlengths'], ['jkl'], ['thisisaverylongwordnopqrsw', 'wordlengths'], [], [], [], ['heogramming', 'laneguage'], ['ajklamteseting'], [], [], [], [], ['hello', 'python', 'is', 'heogramming', 'laneguagea', 'programming', 'language'], ['wlengthsiongwordw'], []]

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
        func_name = "long_words"
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
        for test_case in ['assert long_words(3,"python is a programming language")==[\'python\',\'programming\',\'language\']', 'assert long_words(2,"writing a program")==[\'writing\',\'program\']', 'assert long_words(5,"sorting list")==[\'sorting\']']:
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
