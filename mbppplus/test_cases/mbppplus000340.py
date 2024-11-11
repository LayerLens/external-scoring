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
inputs = [['program2bedone'], ['3wonders'], ['123'], ['3wond-1ers2'], [''], ['hello world'], ['1234567890'], ['1 2 3'], ['      '], ['12 2 3'], ['hello 12 2 3world'], ['lhello world'], ['12 2  3'], ['lhello'], ['1 22 3'], ['22'], ['1 2 3lhello'], ['hello 12 2 olrld'], ['lhell3lhelloo world'], ['3'], ['1 22 322'], ['helhello 12 2 olrldlo world'], ['hello'], ['1lhell3lhelloo 22 3'], ['3world'], ['12 22 322'], ['2222'], ['1 22 3212'], ['hello 12 2 olrlld'], ['world'], ['1 22 13212'], ['112 2  3'], ['1lhell3lhell oo 22 3'], ['322'], ['helhello 12 2 olrldlo worldolrlld'], ['     olrldlo '], ['112'], ['olrlld'], ['12'], ['olrld'], ['1 2 2 3'], ['       '], ['oo'], ['122  3'], ['112 2  32233world'], ['1 2 3lheworldllo'], ['olrldlo'], ['olr'], ['hello 12 2 olrlld2222'], ['hello 12l 2 olrld'], ['old'], ['lhello worlolrlld222o2d'], ['1lhell3lhell'], ['wold'], ['22122  3'], ['ooo'], ['lhewll3lhelloo world'], ['1hello 12l 2 olrld 23 3'], ['olrlld2222'], ['1lhell3l13212hell'], ['13212lhell3lhellolo'], ['1 22 31 2 3212'], ['rw'], ['lhello122  3'], ['              '], ['ollrlld2222'], ['1 22 33'], ['1123'], ['3lhello1234567890'], ['31'], ['1lhell3lhelloo 222 3'], ['helhello'], ['bNEygn'], ['2lhell3lhelloo22'], ['        '], ['lhell3lhelloo weorld'], ['12 2 122  33'], ['1 22'], ['12 2 122  233'], ['        olrlld'], ['lhell3lhelloollo'], ['helhelllo'], ['233'], ['222'], ['12 2 122lhewll3lhelloo worldlhell3lhelloo  33'], ['3w12 2 122  33orld'], ['1l12 2  32 122lhewll3lhelloo worldlhell3lhelloo  33l oo 22 3'], ['1 32222 3212'], ['3lheworldllo'], ['lhdello worlolrlld222o2d'], ['122'], ['1l12 2  32 122lhewll3lhellloo worldlhell3lhelloo  33l oo 22 3'], ['31hello 12 2 olrlld2222'], ['1  22'], ['1l12'], ['worldolrlld'], ['hell3lhello1234567890o2222'], ['olrlld22d22'], ['3wold'], ['22122'], ['ollrll12 2 122  233d2222'], ['3123'], ['122 2 3'], ['1l12 2  3e2 122lhewll3lhellloo wohello 12l3lhelloo  33l oo 22 3'], ['hell3lhello1234567890o22223'], ['12 lhello1222 3'], ['hello 12 2 orld'], ['wworld']]
results = [1, 1, 3, 3, 0, 0, 10, 3, 0, 4, 4, 0, 4, 0, 4, 2, 3, 3, 1, 1, 6, 3, 0, 5, 1, 7, 4, 7, 3, 0, 8, 5, 5, 3, 3, 0, 3, 0, 2, 0, 4, 0, 0, 4, 9, 3, 0, 0, 7, 3, 0, 4, 2, 0, 6, 0, 1, 7, 4, 7, 6, 10, 0, 4, 0, 4, 5, 4, 11, 2, 6, 0, 0, 4, 0, 1, 8, 3, 9, 0, 1, 0, 3, 3, 10, 9, 16, 10, 1, 4, 3, 16, 9, 3, 3, 0, 15, 4, 1, 5, 13, 4, 5, 18, 16, 7, 3, 0]

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
        func_name = "number_ctr"
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
        for test_case in ["assert number_ctr('program2bedone') == 1", "assert number_ctr('3wonders') == 1", "assert number_ctr('123') == 3", "assert number_ctr('3wond-1ers2') == 3"]:
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
