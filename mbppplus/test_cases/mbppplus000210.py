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
inputs = [['pythonz.'], ['xyz.'], ['  lang  .'], ['*z@'], ['1234z5678'], ['z x z'], ['x'], [''], ['*z@*z@'], ['*z'], ['**z@'], ['**zz@'], ['*z x z*zz@'], ['*x*z@*z@z'], ['***z@'], ['z'], ['x****z@'], ['*z xz x z z*zz@'], ['z*zz@'], ['*@*z@'], ['***@'], ['***zz@@x****z@'], ['*x*z@*z@'], ['*z xzz x z z*zz@'], ['z*z@'], ['**z'], ['*@'], ['*@*z@@'], ['z*zz@z'], ['*@**z@'], ['****@'], ['****z@'], ['*zz'], ['***zz@@x*****z@'], ['z*zz@z*zz@z'], ['z*zz@z*zzz@z'], ['****z*z@z@@x****z@'], ['**zx*z@*z@'], ['*x@*z@'], ['z*****z@zz@z*zz@z'], ['*****@*z'], ['n'], ['**@*z@@'], ['z**z@'], ['*zzz*@z'], ['***@@'], ['z****z@'], ['*z@*z****z@z'], ['****z@*zzz*@z'], ['**z****z*z@z@@x****z@z@'], ['*zzz*z'], ['****z@*zzz*z****z@@z*z@**z@'], [' z  x z'], ['z**@*z@zz@z*zz@z'], ['*z@*z@**zz'], ['*zz xzz x z z*zz@'], ['*z *zz x zz x z z*zz@z*zz@'], ['z**z@*z@zz@z*zz@z'], ['**zx*z@*z*@'], ['z*zzz@'], ['*'], ['z*zz@zz'], ['z**zz@'], ['*z x*x@*z@zz  z*zz@'], ['1234z56n78'], ['z*zzzz@'], ['zzz'], ['**@@x*****z@'], ['**zx*z@*z*@x'], ['***z**z@@@*z@'], ['xz'], ['*zz xzz x z z*z'], ['1234z566n78'], ['z*zz@z*z*zz@z*zzz@zzzz@z'], ['z**@*z@ z  x zzz@z*zz@z'], ['1234z78'], ['zz'], ['*x*z@*zz@'], ['x*x@*z@zz'], ['**zz xzz x z z*z'], ['z**z**zz@'], ['z*zz@***z@'], ['z***zz@z@'], ['12334z78'], ['*z zzz'], ['*@@'], ['yVHKcHlY'], ['z*zz@***z@x*zz xzz x z z*z'], ['*z  x z*zz@'], ['z*zz@z*zz@*@*z@@'], ['*@***z'], ['JlGWYIid'], ['*****@'], ['zyVHKcHlY x z'], ['@*@*z@'], ['****z@*zzz*@zz'], ['*zzz***z x*x@*z@zz  z*zz@*z@z'], ['12314z566n78'], ['z*****z@'], ['12314z566n78*z x*x@*z@zz  z*zz@'], ['l'], ['*z@*z*z x*x@*z@zz  z*zz@****z@z'], ['*x@*zz@'], ['********z@*zzz*@zz'], ['****z@*zzz*z*@@z*z@**z@'], ['1234z566nl78']]
results = [True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, False, False, True, True, True, True, True, True, True, False, True, True, True, True, True]

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
        func_name = "text_match_wordz"
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
        for test_case in ['assert text_match_wordz("pythonz.")==True', 'assert text_match_wordz("xyz.")==True', 'assert text_match_wordz("  lang  .")==False']:
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
