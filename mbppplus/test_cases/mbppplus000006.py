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
inputs = [['aaaa'], ['ab'], ['abc'], ['aaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaab'], ['aaaaaaaaaaaaaaaaababab'], ['aaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaab'], ['aaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaabaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaab'], ['aaaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaaabaab'], ['aaaaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaabaaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabb'], ['aaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaababab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaababab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaaabaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaababaaaabaabaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaababab'], ['aaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaabaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaabaaababaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaabaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaababaaaabaabaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['pmUjgIomJ'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaabaaaaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaababaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabababaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaaaaaaaabaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaabababaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaababaaaabaaabaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabababaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaabababaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaabaaaaaaabbaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaabaaaaabaaab'], ['aaaaaaaaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabbabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaabababaaabaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaabaaaaaaaabaab'], ['pmUaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaabaaabjgmIomJ'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabababaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabababaaaaaaaaaaabaaaaaaababaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabababaaaaaaaaaaabaaaaaaababaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaababaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaabaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaabaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaaaaaaaaaaaaabababaaaaaaaaaaaaabaab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaabaaaaaaabb'], ['aaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaabaaaaaaabaabaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaabab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabab'], ['aaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaabababaaabaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaabaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaabababaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaababaaaaaaaaaaaaabababaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaaabaabaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaabaababaaaabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbabb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaababaaaabaabaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaabaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaab'], ['pmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaababaaaabaabaaaaaaaaaaaaaaaaabUjgIomJ'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaaaa'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaababaaabaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaababaaaabaabaaaaaaaaaaaaaaaaabUjgIomJb'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaababaaaabaaabaaaaaaaaaaaaaaaaab'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaabbaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaabaaaaabaaab']]
results = [1, 2, 3, 17, 18, 36, 22, 19, 56, 84, 103, 51, 142, 103, 16, 35, 89, 142, 37, 1, 90, 1, 109, 87, 20, 38, 82, 50, 21, 40, 100, 185, 160, 81, 57, 275, 181, 27, 182, 119, 153, 183, 17, 157, 146, 153, 57, 89, 175, 191, 28, 334, 116, 105, 159, 9, 88, 53, 43, 184, 231, 283, 246, 8, 327, 125, 233, 161, 70, 328, 106, 90, 18, 192, 120, 302, 126, 58, 214, 182, 99, 232, 385, 253, 386, 202, 135, 247, 40, 191, 9, 259, 41, 510, 28, 328, 49, 100, 353, 191, 51, 247, 126, 127]

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
        func_name = "find_Rotations"
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
        for test_case in ['assert find_Rotations("aaaa") == 1', 'assert find_Rotations("ab") == 2', 'assert find_Rotations("abc") == 3']:
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
