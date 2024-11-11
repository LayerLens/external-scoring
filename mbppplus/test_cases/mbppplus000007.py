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
inputs = [['hello', 'l'], ['abcda', 'a'], ['PHP', 'P'], ['a', 'a'], ['aaa', 'a'], ['hello world', 'x'], ['worlda', 'a'], ['x', 'x'], ['hello world', 'a'], ['world', 'x'], ['xx', 'x'], ['xworlaaada', 'x'], ['axworlaaada', 'x'], ['waaaorlda', 'a'], ['xhello world', 'a'], ['xxx', 'x'], ['worlda', 'x'], ['world', 'a'], ['hwllo world', 'a'], ['axx', 'a'], ['hwllo world', 'x'], ['hwllo', 'a'], ['hwl', 'a'], ['ahwllo world', 'a'], ['xxx', 'a'], ['hwll', 'a'], ['hhwl', 'a'], ['ahwllo', 'x'], ['whwlloorld', 'a'], ['wda', 'x'], ['hwl', 'x'], ['xrworlaaada', 'x'], ['aahwllo', 'a'], ['a', 'x'], ['xxwaaaorlda', 'x'], ['wda', 'a'], ['hxworlaaadawllo', 'a'], ['aaaa', 'a'], ['xrworworldalaaadax', 'x'], ['aaawda', 'x'], ['hello worldx', 'x'], ['xrworworldalaaadax', 'a'], ['xrworlaaadaworldx', 'x'], ['aahwllo', 'x'], ['xworlaaadaaaaa', 'a'], ['xxxx', 'a'], ['xhello worlda', 'a'], ['xrworworaldalaaadax', 'a'], ['xaaaa', 'x'], ['xxwaahello worldxaorlda', 'x'], ['axworlaaada', 'a'], ['worldxaorlda', 'x'], ['hellloa', 'a'], ['xaaa', 'x'], ['aa', 'a'], ['xhello', 'a'], ['xrworlaaaada', 'x'], ['axxxaawda', 'x'], ['hello worldxxhello worlda', 'a'], ['xhello', 'x'], ['hxworlaaadawlolo', 'a'], ['aa', 'x'], ['lo', 'x'], ['xaaaa', 'a'], ['waaaorllda', 'a'], ['ahwllao', 'x'], ['aaa', 'x'], ['xxhello', 'x'], ['wdaa', 'a'], ['xrworworaldalaaadaxa', 'a'], ['waaaorlxxwaaaorlda', 'a'], ['aahwllao', 'x'], ['hello worldx', 'a'], ['lo', 'a'], ['hellloa', 'x'], ['helwdalloa', 'x'], ['worldxxhellox', 'x'], ['hello', 'x'], ['l', 'x'], ['waaaorlldalo', 'x'], ['xrwax', 'x'], ['waaaorllda', 'x'], ['whwlloorld', 'x'], ['aahhwla', 'x'], ['waaaorlda', 'x'], ['llo', 'l'], ['axaahwllaoworlaaada', 'a'], ['hwllor world', 'a'], ['xworlaaadaaaaa', 'x'], ['waaaorlldal', 'a'], ['aahawllao', 'x'], ['lllo', 'l'], ['worlaaaadxaorlda', 'x'], ['hello worldxxhhelloworlda', 'a'], ['hwlll', 'a'], ['xrworwoxxxraldalaaadaxa', 'a'], ['ll', 'x'], ['aaahwllaoo', 'a'], ['worldx', 'a'], ['xrworworaldalaaadaxa', 'x'], ['hxworlaaadawlolo', 'x'], ['whello world', 'x'], ['ahwllo', 'a'], ['ahxworlaaadawlolo', 'a'], ['whello', 'x'], ['ax', 'a']]
results = ['heo', 'bcd', 'H', '', 'a', 'hello world', 'world', '', 'hello world', 'world', '', 'worlaaada', 'aworlaaada', 'waaorld', 'xhello world', 'x', 'worlda', 'world', 'hwllo world', 'xx', 'hwllo world', 'hwllo', 'hwl', 'hwllo world', 'xxx', 'hwll', 'hhwl', 'ahwllo', 'whwlloorld', 'wda', 'hwl', 'rworlaaada', 'hwllo', 'a', 'waaaorlda', 'wd', 'hxworlaadwllo', 'aa', 'rworworldalaaada', 'aaawda', 'hello world', 'xrworworldlaaadx', 'rworlaaadaworld', 'aahwllo', 'xworlaadaaaa', 'xxxx', 'xhello world', 'xrworworldalaaadx', 'aaaa', 'xwaahello worldaorlda', 'xworlaaad', 'worldaorlda', 'helllo', 'aaa', '', 'xhello', 'rworlaaaada', 'axaawda', 'hello worldxxhello world', 'hello', 'hxworlaadwlolo', 'aa', 'lo', 'xaa', 'waaorlld', 'ahwllao', 'aaa', 'hello', 'wd', 'xrworworldalaaadax', 'waaorlxxwaaaorld', 'aahwllao', 'hello worldx', 'lo', 'hellloa', 'helwdalloa', 'worldxhello', 'hello', 'l', 'waaaorlldalo', 'rwa', 'waaaorllda', 'whwlloorld', 'aahhwla', 'waaaorlda', 'o', 'xaahwllaoworlaaad', 'hwllor world', 'worlaaadaaaaa', 'waaorlldl', 'aahawllao', 'lo', 'worlaaaadaorlda', 'hello worldxxhhelloworld', 'hwlll', 'xrworwoxxxrldalaaadax', 'll', 'aahwlloo', 'worldx', 'rworworaldalaaadaa', 'hworlaaadawlolo', 'whello world', 'hwllo', 'hxworlaaadwlolo', 'whello', 'x']

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
        func_name = "remove_Occ"
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
        for test_case in ['assert remove_Occ("hello","l") == "heo"', 'assert remove_Occ("abcda","a") == "bcd"', 'assert remove_Occ("PHP","P") == "H"']:
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
