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
inputs = [[['julia', 'best', 'tseb', 'for', 'ailuj']], [['geeks', 'best', 'for', 'skeeg']], [['makes', 'best', 'sekam', 'for', 'rof']], [[]], [['abc', 'defg', 'hijk', 'uvwxyz', 'ijklmnop', 'qrstuv']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed']], [['geeks']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk']], [['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji']], [['aba', 'cdc', 'efe', 'ghg', 'ijij', 'klm', 'mlk']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'mnoponm', 'aaa', 'bbb', 'ccc']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']], [['']], [['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ji']], [['abc', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed']], [['ef', 'defg', 'hijk', 'uvwxyz', 'ijklmnop', 'qrstuv']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk', 'def']], [['aba', 'cdc', 'efe', 'ij', 'kmlk', 'qrstuv', 'ghg', 'mmlk', 'ijij', 'klm', 'mlk']], [['app', '123', 'adef3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'xxx', 'yyy', 'zzz']], [['aba', 'cdc', 'effe', 'ij', 'kmlk', 'qrstuv', 'ghg', 'mmlk', 'ijij', 'klm', 'mlk']], [['aba', 'cdc', 'vvvefe', 'ghg', 'cd', 'ijij', 'klm', 'mlk']], [['app', '123', 'adef3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed', 'apple']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'mnoponm', 'aaa', 'bbb', 'ccc', 'defed']], [['', '']], [['abc', 'defg', 'hijk', 'uvwxyz']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'ijjiklkji', 'mnoponm', 'aaa', 'bbb', 'ccc', 'defed']], [['app', '123', 'adef3', 'apple', 'elppa', 'xyx', 'hhh', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed', 'apple']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']], [['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'fe']], [['cdc', 'efe', 'ij', 'kmlk', 'qrstuv', 'mmlk', 'ijij', 'mmelppak', 'klm', 'mlk']], [['lll']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'ssslll', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']], [['abc', 'ijklmnfedop', 'defg', 'hijk', 'uvwxyz', 'ijklmnop', 'qrstuv']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecr', 'abc', 'zyx', 'def', 'fed']], [['geeji', 'geeks']], [['ab', 'ba', 'dc', 'ef', 'fe', 'gh', 'hg', 'ji', 'fe']], [['ab', 'ba', 'dc', 'ef', 'fe', 'gh', 'hg', 'ji', 'fe', 'ef']], [['abc']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'yyy', 'zzz']], [['jjj', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'fe']], [['cdc', 'efe', 'ij', 'kmlk', 'qrstuv', 'mmlk', 'ijij', 'mmelppak', 'mlk']], [['abac']], [['aba', 'cdc', 'effe', 'ij', 'kmlk', 'qrstuv', 'ghg', 'mmlk', 'ijij', 'klm', 'ghg', 'mlk']], [['geeji', 'gedddeji', 'geeks']], [['geeks', 'geeks', 'geeks']], [['app', '123', 'adef3', 'apple', 'xyx', 'ssslll', 'hhh', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'def', 'fed', 'apple']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk', 'def', 'def', 'ijklmnop', 'gedddeji']], [['ji', 'adef3', 'geeks', 'geeji']], [['abcba', 'defed', 'ghighg', 'mnoponm', 'aaa', 'bbb', 'ccc']], [['ad3', 'ppp']], [['ab', 'ba', 'dc', 'mlk', 'ef', 'fe', 'gh', 'hg', 'ji', 'fe']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk', 'def', 'def', 'ijklmnop', 'gedddeji', 'ijklmnop']], [['abc', 'defg', 'uvwxyz']], [['aba', 'cdc', 'vvvefe', 'ghg', 'cd', 'ijij', 'klm', 'mlk', 'klm']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed', 'ddd']], [['hijbak', 'abc', 'ijklmnfedop', 'defg', 'hijk', 'uvwxyz', 'ijklmnop', 'qrstuv']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk', 'def', 'def', 'klm']], [['ijjiklkji']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'tab', 'racecar', 'abc', 'zyx', 'def']], [['geeks', 'geeks', 'geeks', 'geeks']], [['abcba', 'defezyxd', 'cccc', 'ghighg', 'mnoponm', 'aaa', 'bbb', 'ccc']], [['ad3']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'mnoponm', 'aa', 'bbb', 'ccc', 'defed']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'mnoponm', 'aaa', 'lll', 'ccc', 'defed']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'ijjiklkji', 'rrr', 'ssslll', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz', 'ssslll']], [['ab', 'ba', 'dc', 'mlk', 'ef', 'fe', 'gh', 'hg', 'ji']], [['aaa', 'pppp', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']], [['hijbak', 'abc', 'ijklmnfedop', 'defg', 'hijk', 'uvwxyz', 'ijkklmnop', 'qrstuv']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'ttacocat', 'abc', 'zyx', 'def', 'fed']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'tab', 'tacocat', 'racecar', 'abc', 'ssslll', 'zyx', 'def', 'ji', 'fed']], [['ab', 'ba', 'dc', 'ef', 'fe', 'gh', 'hg', 'ji', 'fe', 'fe']], [['abcba', 'cccc', 'ghighg', 'aaa', 'bbb', 'ccc', 'aaa']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'yyy', 'abc', 'zyx', 'def', 'fed']], [['mnoponm']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'tab', 'racecar', 'abc', 'zyx', 'def', 'racecar']], [['abc', 'ijklmnfedop', 'hijk', 'uvwxyz', 'ijklmnop', 'qrstuv']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'mlk', 'def', 'def', 'ijklmnop', 'gedddeji', 'def']], [['aba', 'cdc', 'vvvefe', 'ijijj', 'ghg', 'cd', 'ijij', 'klm', 'mlk']], [['abcba', 'defed', 'ijklkji', 'mnoponm', 'aaa', 'ijkli', 'lll', 'ccc', 'defed']], [['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'ij']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'mnoponm', 'aaa', 'bbb', 'zzz', 'ccc']], [['abc', 'cba', 'def', 'batfed', 'hij', 'jih', 'klm', 'mlk', 'def', 'def', 'klm']], [['ab', 'ba', 'cd', 'dc', 'ef', 'fe', 'gh', 'hg', 'ij', 'ji', 'fe', 'gh']], [['eji', 'ji', 'adef3', 'geeks', 'klm', 'geeji']], [['aba', 'cdc', 'efe', 'ij', 'kmlk', 'qrstuv', 'ghg', 'mmlk', 'iracecrjij', 'klm', 'mlk']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'xxx', 'yyy', 'zzz', 'ttt']], [['abcba', 'defed', 'ijklkji', 'mnoponm', 'aaa', 'ijkli', 'lll', 'ccc', 'defed', 'aaa']], [['aiiib', 'ba', 'dc', 'mlk', 'ef', 'fe', 'gh', 'hg', 'ji']], [['abcba', 'cccc', 'ghighg', 'aaa', 'bbb', 'ccc', 'aaa', 'aaa']], [['aba', 'cdc', 'efe', 'ij', 'kmlk', 'qrstuv', 'ghg', 'mmlk', 'ijij', 'mlk']], [['abcba', 'defezyxd', 'cccc', 'ghighg', 'mnoponm', 'aaa', 'bbb', 'cccfe']], [['app', '123', 'apple', 'elppa', 'xyx', 'bat', 'tab', 'racecar', 'abc', 'zyx', 'def', 'racecar']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'klm', 'ddd', 'tab', 'tacocat', 'racecar', 'yyy', 'abc', 'zyx', 'def', 'fed', 'ddd']], [['eji', 'ji', 'adef3', 'geeks', 'klm', 'geeji', 'klm']], [['ij', 'aiiibj', '']], [['geeji', 'gedddeji', 'geeks', 'geeks']], [['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'yyy', 'zzz', 'iii']], [['tab']], [['abc', 'defg']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'ml', 'def']], [['aba', 'cdc', 'vvvefe', 'ghg', 'cd', 'klm', 'mlk']], [['abcba', 'cccc', 'ghighg', 'mnoponm', 'aaa', 'bbb', 'cccfe']], [['abc', 'defg', 'hjk']], [['abcba', 'defezyxd', 'cccc', 'ghighg', 'mnoponm', 'aaa', 'bbb', 'ccc', 'bbb']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'ml', 'hij']], [['abc', 'cba', 'def', 'fed', 'hij', 'jih', 'klm', 'ml', 'hij', 'hij']], [['app', '123', 'ad3abac', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecr', 'abc', 'zyx', 'def', 'fed']], [['app', '123', 'apple', 'elppa', 'xyx', 'klm', 'ddd', 'tacocat', 'racecar', 'yyy', 'abc', 'zyx', 'def', 'fed', 'ddd', 'app']], [['abc', 'def', 'fed', 'hij', 'jih', 'klm', 'ml', 'def', 'cba']], [['abcba', 'defed', 'ghighg', 'ijklkji', 'mnoponm', 'aa', 'bbb', 'defed']], [['app', '123', 'ad3', 'apple', 'elppa', 'xyx', 'bat', 'ddd', 'tab', 'tacocat', 'racecar', 'abc', 'zyx', 'def', 'fed', 'elppa']]]
results = [2, 1, 2, 0, 0, 3, 0, 4, 5, 1, 0, 0, 0, 4, 3, 3, 0, 5, 1, 3, 0, 1, 1, 4, 1, 1, 0, 1, 4, 0, 6, 1, 0, 0, 0, 3, 0, 4, 6, 0, 0, 5, 0, 0, 2, 0, 0, 2, 6, 0, 0, 0, 4, 6, 0, 2, 4, 0, 7, 0, 2, 0, 0, 0, 1, 1, 0, 3, 0, 0, 3, 3, 5, 1, 3, 0, 3, 0, 7, 1, 1, 6, 0, 4, 7, 0, 1, 1, 2, 2, 3, 0, 0, 3, 3, 0, 0, 0, 1, 0, 0, 4, 1, 0, 0, 1, 4, 5, 3, 3, 4, 1, 4]

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
        func_name = "count_reverse_pairs"
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
        for test_case in ['assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2', 'assert count_reverse_pairs(["geeks", "best", "for", "skeeg"]) == 1', 'assert count_reverse_pairs(["makes", "best", "sekam", "for", "rof"]) == 2']:
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
