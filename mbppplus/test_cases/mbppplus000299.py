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
inputs = [[['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']], [['php', 'res', 'Python', 'abcd', 'Java', 'aaa']], [['abcd', 'Python', 'abba', 'aba']], [[]], [['AbCdE', 'fGH', 'IJKLMnOp', 'qrs', 'TUVW', 'xyz']], [['Python']], [['John', 'dylan', '!Rebecca', 'Diana!', '-', '_']], [['John', 'D@ve', 'MarY', 'Linda', 'Zach!', '@lex']], [['Elephant', 'l!ly', '&bbie', 'T@ger', 'D@lion', 'Rh!no']], [['%lice', '^ob', '&arl', '*andy', '$ugene', 'Oscar']], [['@my', 'B@ob', '$ara', 'Mike', 'S!mon', 'L!sa']], [['Oscar', '$ugene', 'D@ve!', '%lice', '^ob']], [['T@ger', 'Elephant', 'l!ly', '$ugene', 'Rh!no']], [['John', '!Rebecca', '@lex', 'Zach!', '&bbie']], [['John', 'dylan', 'L!sa', '!Rebecca', 'Diana!', '-', '_']], [['John', 'dylan', '*andy', '!Rebecca', 'Diana!', '-', '_']], [['John', 'dylan', '*andy', '!Rebecca', 'Diana!', '-', '__', 'Joh*andyn', '_']], [['John', 'dylan', 'L!sa', '!Rebecca', 'Diana!', '_', 'John']], [['&bbie', 'H', 'tTftc', 'IJKLMnOp', 'IJKLMnOp', 'HYAOjA']], [['!Rebecca', 'dylan', '!Rebecca', 'Diana!', '-', '_']], [['John', 'D@ve', 'Linda', 'Zach!', '@lex']], [['D@v@e!', 'Oscar', '$ug$ene', 'D@ve!', '%lice', '^ob', '%lice']], [['Oscar', '$ugene', 'D@ve!', '%lice', '^ob', 'Oscar']], [['John', 'D@ve', 'MarY', 'D@veZach!', 'Linda', 'Zach!', '@lex']], [['John', 'dylan', 'Diana!', '-', '_']], [['John', 'xyz', 'Diana!', '-', '_']], [['!Rebecca', 'dylan', 'Diana!', '-']], [['$ugene', 'D@ve!', '^ob']], [['John', 'dylan', '*andy', 'Joh*andJyn', '!Rebecca', 'Diana!', '-', '__', 'Joh*andyn', '_']], [['dylan', '!Rebecca', '&arl', 'DianaDiana!!', '-', '_']], [['John', 'dylan', '*anPythondy', 'Joh*andJyn', '!Rebecca', 'Diana!', '-', '__', 'DianaDiana!!', 'Joh*andyn', '_']], [['T@ger', 'Elephant', '$ugene', 'Rh!no', '_']], [['John', 'L!sa', '!Rebecca', 'Diana!', '__', 'John']], [['D@v@e!', 'Oscrar', '$ug$ene', 'D@ve!', '%lice', '^ob', '%lice']], [['D@veZach!', 'Python', 'jdps', 'Zach!']], [['John', 'dylan', '!RebeccJohna', 'L!sa', '!Rebecca', 'Diana!', '-', '_']], [['l!ly', '&bbie', 'T@ger', 'D@lion', 'Rh!no']], [['John', 'dylan', '!RebeccJohna', 'L!sa', '&arl', '!Rebecca', 'Diana!', '-', '_']], [['Oscar', '$ugene', 'D@ve!', '%lice', 'D@veZach!', '^ob', 'Oscar', 'D@veZach!']], [['!Rebecca', 'dylan', 'Diana!', '-', 'dylan']], [['fGH', 'IJKLMnOp', 'qrs', 'TUVW', 'xyz']], [['!Rebecca', 'dylan', 'Diana!', '$ugene', '-']], [['John', 'xyz', 'Diana!', '-', '_', 'Diana!']], [['&bbie', 'H', 'tTftc', 'IJKLMnOp', 'IJKLMnOp', 'HYAAOjA']], [['John', 'Johon', 'dylan', 'Diana!', '-', '_']], [['xyz', 'Diana!', '-', '_', 'Diana!', 'Diana!']], [['Elephant', 'l!ly', '&bbie', 'T@ger', 'D@lion', 'Oscrar', 'Rh!no']], [['dylan', 'L!sa', '!Rebecca', 'Diana!', '!!Rebecca', '-', '_', '-']], [['Oscar', 'D@ve!!', '$ugene', 'D@ve!', '%lice', '^ob']], [['!Rebecca', 'dylan', 'Diana!', '-', '-']], [['fGH', 'IJKLMnOp', 'qrs', 'TUVW', 'xyz', 'TUVW']], [['!!Rebe!cca', '!Rebecca', 'dylan', 'Diana!', '$ugene', '%lice']], [['S!mon', 'Diana!', '-', '_', 'Diana!', 'Diana!']], [['John', '@lex', 'Zach!', 'Linda']], [['Oscar', 'D@ve!', '%lice', 'D@veZach!', '^ob', '%liD@vevZach!ce', 'Oscar', '%liD@veZach!ce', 'D@veZach!']], [['%lice', '^ob', '&arl', 'OscD@veZach!ar', '*andy', '$ugene', 'Oscar']], [['John', 'L!sa', '!Rebecca', 'Zach!', '__', 'John']], [['%lice', '^ob', '&arl', 'OscD@veZach!ar', '*andy', '$ugHene', 'Oscar']], [['John', 'xyz', 'Diana!', '-', '_', 'xyz', 'John']], [['John', '@lex', 'MarY', 'Zach!', 'Linda']], [['John', 'D@ve', 'MarY', 'D@veZach!', '-', 'Linda', 'Zach!', '@lex']], [['dylan', '!Rebecca', '&arl', '-', '!!Rebecca', '_']], [['Oscar', 'D@ve!!', '$ugene', 'D@ve!', '%lice', '^ob', '$ugene']], [['^ob', '&arl', 'OscD@vtTftceZach!ar', '*andy', '$ugene', 'Oscar', 'Oscar']], [['$ugene', 'D@ve!', 'H^ob']], [['!Rebecca', 'Oscrar', 'dylan', 'Diana!', '-']], [['dylan', 'L!sa', '!Rebecca', 'S!mon', 'Diana!', '!!Rebecca', '-', '_', '-']], [['Oscar', 'D@ve!!', '$ugene', 'D@ve!', '%lice', '^ob', '^ob']], [['xyz', 'Diana!', '-', '_', 'Diana!', 'D@ve!', 'Diana!']], [['Elephant', 'l!ly', '&bbiMikee', 'T@ger', 'D@lion', 'Rh!no']], [['John', 'D@ve', 'MarY', 'Linda', 'Zach!', '@lex', 'D@ve']], [['John', 'D@ve', 'Linda', 'aZach!', '@lex', 'D@ve']], [['John', 'D@ve', 'MarY', 'Linda', 'Zach!', '@lex', 'D@ve', 'D@ve']], [['MarY', '!Rebecca', '&arl', '-', '!!Rebecca', '_', '&arl']], [['John', 'dylan', '*andy', 'Joh*andJyn', '!Rebecca', 'Diana!', '-', '__', 'Joh*andyn', 'Rh!no-', '_']], [['Oscar', '$ugene', '%lice', '^ob', 'Oscar']], [['John', 'L!sa', '!Rebecca', 'Diana!', '__', 'John', 'John']], [['dylan', '!Rebecca', '&arl', 'DianaDiana!!', 'TUVW-', '_']], [['D@v@e!', 'Oscar', '$ug$ene', 'D@ve!', '%lice', '^ob', '%lice', 'D@ve!']], [['D@v@e!', 'HYAAOjA', 'Oscar', '$ug$ene', 'D@ve!', '%lice', '^ob', '%lice', 'D@ve!']], [['!Rebecca', 'dylan', 'Diana!', 'dyla*andyn', '-', 'dylan']], [['T@ger', 'Elephant', '$ugene', 'Rh!no', '_', '$ugene']], [['$ugene', 'D@ve!', '%lice', '$$ugene', '^ob', '%lice']], [['John', 'D@ve', 'Linda', 'H', '@lex', 'D@ve']], [['AbCdE', 'fGH', 'IJKLMnOp', 'qrs', 'TUVW', 'xyz', 'qrs']], [['!Rebecca', '&arl', '-', '!!Rebecca', '_', '&arl']], [['OOscar', 'Oscar', '$uegene', 'D@ve!', '%lice', '^ob', 'Oscar']], [['John', 'D@ve', 'Linda', 'H', '@lex']], [['John', '!Rebecca', 'Zach!', '&bbie']], [['n$ugene', 'T@ger', 'Elephant', 'l!ly', '$ugene']], [['John', 'dylan', '!RebeccJohna', 'L!sa', '&arl', '!Rebecca', '-', '_']], [['xyz', 'Diana!', '-', '_', 'Diana!', 'H^ob', 'Diana!']], [['John', 'dylan', 'L!sa', '!Rebecca', 'Diana!', '__', 'John']], [['!Rebecca', 'dylan', 'Diana!', 'dylan']], [['$ara', 'Oscar', '$ugene', '%lice', '^ob', 'Oscar', '$ugene']], [['John', 'dylan', '*andy', '!Rebecca', 'Diana!', '-', '_', 'dylan']], [['John', 'Johon', 'dylan', 'Diana!', '-', '_', '_', '-']], [['^ob', '&arl', 'OscD@vtTftceZach!ar', '*andy', '$ugene', 'Oscar', 'D@lion']], [['John', 'dylan', '*andy', '!Rebecca', 'Diana!', '__', '-', '_', 'dylan']], [['John', 'dylan', '*andy', 'y*andy', '!Rebecca', 'Diana!', '-', '_', '__', 'dylan', '-']], [['fGH', 'IJKLMnOp', 'qrs', 'Pythonxyz', 'Mike', 'xyz', 'TUVW']], [['&bbie', '!Rebecca', '@lex', 'Zach!', '&bbie', '!Rebecca']], [['John', 'L!sa', '!Rebecca', 'L!s', 'Zach!', '__', 'John']], [['^ob', '&arl', 'OscD@veZach!ar', '*andy', '$ugene', 'Oscar']], [['John', 'dylan', '!RebeccJohna', 'LL!sa', '&arl', '!Rebecca', 'Diana!', '-', '_']], [['MarY', '!Rebecca', '&arl', '-', '!!Rebecca', '_', '&arl', '_']], [['AbCdE', 'fGH', 'IJKLMnOp', 'Zach!', 'qrs', 'TUVW', 'xyz']], [['John', 'Johon', 'dylan', 'Diana!', '-', '_', '_', '-', '_', 'Diana!']], [['John', 'dylan', '!Rebecca', '-', '_']], [['fGH', 'IJKLMnOp', 'Pythonxyz', 'Mike', 'dyla*andyn', 'TUVW']], [['Pythonxyz', 'John', 'D@ve', 'MarY', 'D@veZach!', 'Linda', 'Zach!', '@lex']], [['Elephant', 'l!ly', '&bbie', 'Elephalnt', 'T@ger', 'D@lion', 'D@Dlion', 'Rh!no']], [['fGH', 'IaZach!JKLMnOp', 'qrs', 'TUVW', 'xyz']], [['John', 'dylan', '!Rebecca', 'Diana!', '-', 'Pythonxyz', '!Rebecca']]]
results = [16, 10, 6, 0, 0, 6, 10, 18, 24, 5, 17, 10, 18, 9, 14, 10, 19, 18, 0, 6, 18, 16, 15, 18, 10, 10, 6, 5, 19, 0, 19, 18, 18, 17, 11, 14, 16, 14, 15, 6, 0, 6, 16, 0, 15, 18, 30, 10, 16, 6, 0, 6, 23, 14, 15, 5, 17, 5, 14, 14, 18, 0, 16, 10, 9, 12, 15, 16, 23, 24, 22, 17, 26, 0, 25, 10, 22, 0, 21, 21, 6, 18, 5, 17, 0, 0, 15, 13, 9, 13, 8, 22, 18, 6, 10, 10, 15, 11, 10, 10, 13, 5, 20, 5, 10, 0, 5, 21, 4, 13, 27, 33, 0, 19]

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
        func_name = "sample_nam"
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
        for test_case in ["assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16", 'assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10', 'assert sample_nam(["abcd", "Python", "abba", "aba"])==6']:
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
