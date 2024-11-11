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
inputs = [[('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')], [('p', 'y', 't', 'h', 'o', 'n')], [('p', 'r', 'o', 'g', 'r', 'a', 'm')], [()], [('a',)], [('a', 'a')], [('Z', 'a', 'ZvCAMhN', 'a', 'a', 'a')], [('Z', 'a', 'ZvCAMhN', 'a', 'aa', 'a')], [('Z', 'a', 'ZvCAMhN', 'a', 'aa', 'a', 'aa')], [('ZZ', 'a', 'ZvCAMhN', 'a', 'a', 'a')], [('a', 'ZvCAMhN', 'aaZ', 'a', 'aa', 'a')], [('mKxDJT', 'VekfW', 'ZvCAMhN', 'aaZ', 'FiUaYFBklh', 'PBEOJoMiY', 'aFELUEp', 'aaZ', 'ZZ')], [('Z', 'a', 'ZvCAMhN', 'a', 'a', 'a', 'a')], [('ZZ', '', 'ZvCAMhN', 'aa', 'a', 'a')], [('aa', 'mKxDJTaa', 'a')], [('aa', 'ZvCAMhN', 'a')], [('aa', 'VekfW', 'a')], [('Z', 'ZvCAMhN', 'a', 'a', 'a', 'Z', 'a')], [('ZZZ', 'a', 'ZvCAMhN', 'a', 'a', 'a')], [('ZZZ', 'a', 'ZvCAMhN', 'a', 'a')], [('aFELUEpZ', 'a', 'ZvCAMhN', 'a', 'aa', 'a', 'aa')], [('aa', 'mKxDJTaa', 'aa')], [('a', '')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'tDuJm', 'IWSYg', 'Z')], [('aa', 'ZvCAMhN', 'a', 'aa')], [('ZZ', 'ZvCAMhN', 'aa', 'a', 'a')], [('Z', 'a', 'ZvCAMhN', 'a', 'aa', 'a', 'a')], [('mKxDJT', 'ZvCAMhN', 'aaZ', 'a', 'aa', 'a')], [('aa', 'aFELUEpZ')], [('mKxDJT', 'ZvCAMhN', 'aZ', 'ZZ', 'a', 'aa', 'a')], [('Z', 'aaZ', 'a', 'ZvCAMhN', 'a', 'a', 'a', 'a')], [('ZZZ', 'a', 'ZvCAMhN', 'a', 'aFELUEpa', 'a', 'a')], [('aFELUEp', 'ZvCAMhN', 'a', 'aa', 'a')], [('Z', 'aaZ', 'IWSYga', 'a', 'ZvCAMhN', 'a', 'a', 'a', 'a')], [('aZZ', 'aFELUEpZ')], [('ZZZ', 'tDuJma', 'a', 'ZvCAMhN', 'a', 'a', 'ZZ')], [('ZZ', 'ZvCAMhN', 'aa', 'a', 'a', 'ZvCAMhN')], [('aa', 'ZvCAMhN', 'aa')], [('Z', 'a', 'a', 'a', 'a')], [('aa', 'ZvCAMhN', 'aa', 'aa')], [('Z', 'aaZ', 'IWSYga', 'a', 'ZvCAMhN', 'PBEOJoMiYa', 'a', 'a', 'a')], [('', 'ZvCAMhN', 'aa', 'a', 'a', 'ZvCAMhN')], [('a', 'aa', 'a')], [('amKxDJTaa', 'Z', 'mKxDJTaaa', 'ZvCAMhN', 'a', 'aa', 'a')], [('Z', 'a', 'ZvCAMhN', 'a', 'a', 'FiUaYFBklh')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'tDuJm', 'IWSYg', 'Z', 'Z')], [('Z', 'a', 'a', 'a', 'Z', 'a')], [('ZZ', 'aaZa', 'ZvCAMhN', 'aa', 'a')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'SkSpnaC', 'aFELUEp', 'tDuJm', 'IWSYg', 'Z', 'Z')], [('ZvCAMhN', 'aaa', 'aa', 'aa', 'aa')], [('aa', 'a')], [('ZZ', 'aaZa', 'ZvCAMhN', 'aa', 'a', 'aa')], [('aFELUEpZ', 'a', 'ZvCAMhN', 'a', 'aa', 'a', 'aa', 'a')], [('a', 'IWSYga', 'ZvCAMhN', 'IWSYg', 'aVekfW', 'a', 'aa', 'a')], [('ZZ', 'a', 'ZvCAMhN', 'a', 'aa', 'a', 'ZvCAMhN')], [('', 'a', 'a', 'a', 'Z', 'a')], [('mKxDJT', 'ZvCAMhN', 'aZ', 'ZZ', 'mKxDJT', 'aa', 'aa', 'a')], [('ZZ', 'SkpnaC', 'FiUaYFBklh', 'a', 'a', 'a', 'a')], [('Z', 'a', 'ZvCAMhN', 'a', 'a', 'a', 'a', 'a')], [('a', '', '')], [('ZZ', 'a', 'ZvCAMhN', 'a', 'a')], [('ZZZ', 'a', 'a', 'aFELUEpa', 'a')], [('', 'a')], [('ZZ', 'ZvCAMhN', 'PBEOJoMiYa', 'aa', 'a', 'a', 'ZvCAMhN')], [('Z', 'aaZ', 'IWSYga', 'a', 'ZvCAMhN', 'IWSYga', 'a', 'a', 'a')], [('Z', 'aaZ', 'IWSYga', 'a', 'ZvCAMhN', 'IWSYga', 'a', 'a')], [('ZZZ', 'a', 'ZvCAMhN', 'a', 'aFFELUEpa', 'a')], [('ZZ', 'ZvCAMhN', 'a', 'aa', 'a')], [('SkpnaC', 'a', 'qHPQEqCm', 'PyvCTG', 'SkSpnaC', 'aFELUEp', 'tDuJm', 'IWSYg', 'Z', 'Z')], [('a', 'PBEOJoMiY', '')], [('Z', 'a', 'ZvCAMhN', 'a', 'a', 'a', 'a', 'a', 'a')], [('Z', 'ZvCAMhN', 'a', 'aa', 'a', 'a', 'Z', 'a')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'aZZ', 'tDuJm', 'IWSYg', 'Z')], [('Z', 'aaZ', 'IWSYga', 'a', 'ZvCAMhN', 'IWSYga', 'a', 'a', 'a', 'a')], [('aFELUEpZ', 'a', 'ZvCAMhN', 'a', 'a', 'aa', 'mKxDJTaa', 'a')], [('aa', 'VekfW', 'aa')], [('IWSYg', 'ZZZ', 'a', 'a', 'aFELUEpa', 'a')], [('ZZ', 'SkpnaC', 'FiUaYFBklh', 'a', 'a', 'a', 'a', 'a')], [('ZZ', 'aa', 'a', 'aa', 'aa')], [('aa', 'SkpVekfWnaC', 'aa')], [('mKxDJT', 'VekfW', 'ZvCAMhN', 'aaZ', 'FiUaYFBklh', 'PBEOJoMiY', 'aFELUEp', 'aaZamKxDJTaa', 'ZZ', 'VekfW', 'PBEOJoMiY')], [('SkpnaC', 'ZZ', 'aa', 'a', 'aa', 'aa', 'aa')], [('SkpnaC', 'ZZ', 'aa', 'aPBEOJoMiYaa', 'a', 'aa', 'aa', 'aa')], [('aa', 'SkfpVekfWnaC', 'aa')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'aZZ', 'tDuJm', 'IWSYg', 'aaZamKxDJTaa')], [('ZZ', 'SkpnaC', 'FiUaYFBklh', 'aaFELUEpa', 'a', 'a', 'a', 'a')], [('ZZ', 'ZvCAMhN', 'PBEOJoMiYa', 'aa', 'a', 'a', 'ZvCAMhN', 'a')], [('Z', 'ZvCAMhN', 'aPBEOJoMiYaa', 'a', 'aa', 'a', 'Z', 'a')], [('aFELUEpZ', 'a', 'ZvCAMhN', 'a', 'ZvCACMhN', 'aa', 'a', 'aaFELUEpZ', 'aa')], [('ZZ', 'a', 'ZvCAMhN', 'a', 'ZZZ', 'a', 'a')], [('ZZ', 'a', 'tDuJma', 'PBEOJoMiY', 'a', 'aa')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'aZZ', 'IWSYg', 'Z')], [('Z', 'aaZ', 'a', 'ZvCAMhN', 'a', 'a', 'a', 'a', 'a')], [('mKxDJT', 'ZvCAMhN', 'aZ', 'ZZ', 'mKxDJT', 'aa', 'SkfpVekfWnaC', 'aZtDuJm', 'aa', 'a')], [('ZvCAMhN', 'ZvCAaFELUEpMhN', 'aaa', 'aaa', 'aa', 'aa')], [('mKxDJT', 'VekfW', 'ZvCAMhN', 'aaZ', 'aZ', 'PBEOJoMiY', 'aFELUEp', 'aaZ', 'ZZ')], [('ZZZ', 'a', 'ZvCAMhN', 'a', 'aFELUEpa', 'a', 'ZmKxDJTaaavCAMhN', 'a')], [('ZvCNAMhN',)], [('SkpnaC', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'tDuJm', 'IWSYg', 'Z', 'Z')], [('Z', 'aaZ', 'IWSYga', 'a', 'ZvCAMhN', 'IWSYga', 'a', 'a', 'a', 'a', 'a')], [('ZvCAMhN', 'aaa', 'aa', 'aa', 'ZMvCAMhN', 'aa')], [('SkpnaC', 'Z', 'a', 'qHPQEqCm', 'PyvCTG', 'aFELUEp', 'aZZ', 'IWSYg', 'Z', 'Z')], [('ZvCAMhN', 'a', 'aa', 'aa')], [('Z', 'VekfW', 'ZvCAMhN', 'aaa', 'a', 'a', 'a')], [('ZZZ', 'a', 'aFELUEpa')]]
results = ['exercises', 'python', 'program', '', 'a', 'aa', 'ZaZvCAMhNaaa', 'ZaZvCAMhNaaaa', 'ZaZvCAMhNaaaaaa', 'ZZaZvCAMhNaaa', 'aZvCAMhNaaZaaaa', 'mKxDJTVekfWZvCAMhNaaZFiUaYFBklhPBEOJoMiYaFELUEpaaZZZ', 'ZaZvCAMhNaaaa', 'ZZZvCAMhNaaaa', 'aamKxDJTaaa', 'aaZvCAMhNa', 'aaVekfWa', 'ZZvCAMhNaaaZa', 'ZZZaZvCAMhNaaa', 'ZZZaZvCAMhNaa', 'aFELUEpZaZvCAMhNaaaaaa', 'aamKxDJTaaaa', 'a', 'SkpnaCZaqHPQEqCmPyvCTGaFELUEptDuJmIWSYgZ', 'aaZvCAMhNaaa', 'ZZZvCAMhNaaaa', 'ZaZvCAMhNaaaaa', 'mKxDJTZvCAMhNaaZaaaa', 'aaaFELUEpZ', 'mKxDJTZvCAMhNaZZZaaaa', 'ZaaZaZvCAMhNaaaa', 'ZZZaZvCAMhNaaFELUEpaaa', 'aFELUEpZvCAMhNaaaa', 'ZaaZIWSYgaaZvCAMhNaaaa', 'aZZaFELUEpZ', 'ZZZtDuJmaaZvCAMhNaaZZ', 'ZZZvCAMhNaaaaZvCAMhN', 'aaZvCAMhNaa', 'Zaaaa', 'aaZvCAMhNaaaa', 'ZaaZIWSYgaaZvCAMhNPBEOJoMiYaaaa', 'ZvCAMhNaaaaZvCAMhN', 'aaaa', 'amKxDJTaaZmKxDJTaaaZvCAMhNaaaa', 'ZaZvCAMhNaaFiUaYFBklh', 'SkpnaCZaqHPQEqCmPyvCTGaFELUEptDuJmIWSYgZZ', 'ZaaaZa', 'ZZaaZaZvCAMhNaaa', 'SkpnaCZaqHPQEqCmPyvCTGSkSpnaCaFELUEptDuJmIWSYgZZ', 'ZvCAMhNaaaaaaaaa', 'aaa', 'ZZaaZaZvCAMhNaaaaa', 'aFELUEpZaZvCAMhNaaaaaaa', 'aIWSYgaZvCAMhNIWSYgaVekfWaaaa', 'ZZaZvCAMhNaaaaZvCAMhN', 'aaaZa', 'mKxDJTZvCAMhNaZZZmKxDJTaaaaa', 'ZZSkpnaCFiUaYFBklhaaaa', 'ZaZvCAMhNaaaaa', 'a', 'ZZaZvCAMhNaa', 'ZZZaaaFELUEpaa', 'a', 'ZZZvCAMhNPBEOJoMiYaaaaaZvCAMhN', 'ZaaZIWSYgaaZvCAMhNIWSYgaaaa', 'ZaaZIWSYgaaZvCAMhNIWSYgaaa', 'ZZZaZvCAMhNaaFFELUEpaa', 'ZZZvCAMhNaaaa', 'SkpnaCaqHPQEqCmPyvCTGSkSpnaCaFELUEptDuJmIWSYgZZ', 'aPBEOJoMiY', 'ZaZvCAMhNaaaaaa', 'ZZvCAMhNaaaaaZa', 'SkpnaCZaqHPQEqCmPyvCTGaFELUEpaZZtDuJmIWSYgZ', 'ZaaZIWSYgaaZvCAMhNIWSYgaaaaa', 'aFELUEpZaZvCAMhNaaaamKxDJTaaa', 'aaVekfWaa', 'IWSYgZZZaaaFELUEpaa', 'ZZSkpnaCFiUaYFBklhaaaaa', 'ZZaaaaaaa', 'aaSkpVekfWnaCaa', 'mKxDJTVekfWZvCAMhNaaZFiUaYFBklhPBEOJoMiYaFELUEpaaZamKxDJTaaZZVekfWPBEOJoMiY', 'SkpnaCZZaaaaaaaaa', 'SkpnaCZZaaaPBEOJoMiYaaaaaaaaa', 'aaSkfpVekfWnaCaa', 'SkpnaCZaqHPQEqCmPyvCTGaFELUEpaZZtDuJmIWSYgaaZamKxDJTaa', 'ZZSkpnaCFiUaYFBklhaaFELUEpaaaaa', 'ZZZvCAMhNPBEOJoMiYaaaaaZvCAMhNa', 'ZZvCAMhNaPBEOJoMiYaaaaaaZa', 'aFELUEpZaZvCAMhNaZvCACMhNaaaaaFELUEpZaa', 'ZZaZvCAMhNaZZZaa', 'ZZatDuJmaPBEOJoMiYaaa', 'SkpnaCZaqHPQEqCmPyvCTGaFELUEpaZZIWSYgZ', 'ZaaZaZvCAMhNaaaaa', 'mKxDJTZvCAMhNaZZZmKxDJTaaSkfpVekfWnaCaZtDuJmaaa', 'ZvCAMhNZvCAaFELUEpMhNaaaaaaaaaa', 'mKxDJTVekfWZvCAMhNaaZaZPBEOJoMiYaFELUEpaaZZZ', 'ZZZaZvCAMhNaaFELUEpaaZmKxDJTaaavCAMhNa', 'ZvCNAMhN', 'SkpnaCaqHPQEqCmPyvCTGaFELUEptDuJmIWSYgZZ', 'ZaaZIWSYgaaZvCAMhNIWSYgaaaaaa', 'ZvCAMhNaaaaaaaZMvCAMhNaa', 'SkpnaCZaqHPQEqCmPyvCTGaFELUEpaZZIWSYgZZ', 'ZvCAMhNaaaaa', 'ZVekfWZvCAMhNaaaaaa', 'ZZZaaFELUEpa']

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
        func_name = "tup_string"
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
        for test_case in ['assert tup_string((\'e\', \'x\', \'e\', \'r\', \'c\', \'i\', \'s\', \'e\', \'s\'))==("exercises")', 'assert tup_string((\'p\',\'y\',\'t\',\'h\',\'o\',\'n\'))==("python")', 'assert tup_string((\'p\',\'r\',\'o\',\'g\',\'r\',\'a\',\'m\'))==("program")']:
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
