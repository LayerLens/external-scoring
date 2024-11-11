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
inputs = [['python'], ['1'], ['12345'], [''], ['-5'], ['10'], ['-100'], ['100000'], ['   15'], ['25    '], ['  -200   '], ['123a'], ['-b456'], ['!7890@'], ['12ab34'], ['5@678'], ['123.45'], ['1,000'], ['1,0'], ['+123'], ['-987'], ['   1   2   3   '], ['  1  2  '], ['  '], ['-b45b6'], ['   '], ['-9+1237'], ['6-b456'], ['5  1  2  @678'], ['    1  2   '], ['123.4  -200   '], ['12ab324'], ['5  1  2   @678'], ['125,000'], ['123.4.5'], ['12ab341'], ['5'], ['--5'], ['1235'], ['6-b    1  2   456'], ['456'], ['12ab1235341'], ['-97'], ['6-b    1  2 1235  456'], ['   1   2    3   '], ['123.4  -200  4 '], ['1423.45'], ['4'], ['1423.5'], ['123.4  -212ab34100   '], ['12ab1235123.4  -200  4 341'], ['-212ab34100'], ['12ab13235123.4  -200  4 341'], ['-2132ab341012ab3240'], ['@@678'], ['  12ab324  1 1 2   '], ['@678'], ['44'], ['-9+14422371,000'], ['12ab21235341'], ['6-b    1  -2002 12355  456'], ['-2005'], ['12ab1235123.4'], ['-2-9+123712ab34100'], ['  -2000   '], ['VuNmzvmS'], ['3'], ['12ab123512312ab1235123.4.4'], ['1,0456'], ['     '], ['12ab3-b45641'], ['142443.45'], ['9-97'], ['123.4123.4  -2120ab34100   '], ['123.46-b4565'], ['125,000-20004'], ['123.4'], ['  12ab324  1 1    '], ['!790@'], ['-b412ab123-53415b6'], ['123.5'], ['0  -2000   '], ['    12ab324  1 1    '], ['11,0'], ['444'], ['6-b 12ab13235123.4  -200  4 341   1  2   456'], ['12aab13235123.4'], ['123.4  -206-b    1  2 1235  4560   '], ['-2123.5132ab341012ab3240'], ['-200'], ['-212a123.4  -212ab34100   34100'], ['    15'], ['  12ab324 a123.45 1 1 2   '], ['@@7678'], ['6-b    1  2 1235  456!790@'], ['15'], ['0  -2000 0  '], ['--55'], ['  1  2   '], ['141,045623.5'], ['1123.4    1  2   5'], ['12ab123512312a2b1235123.4.4'], ['0  -2000 0  -100'], ['  12ab324 a123.4    12ab324  1 1    2   '], ['12a1123.4    1  2   5b123.4..54'], ['6-b    VuNmzvmS1  2 1235  456'], ['456!790@'], ['12ab212351,000341'], ['b-b45b6'], ['1123.4  VuNmzvmS  1  2   5'], ['12ab133235123.4'], ['12ab3-b  12ab324 a123.45 1 1 2   4564'], ['12a1123.4'], ['2ab34 1  2   5'], ['2 5    '], ['DJm'], ['3VuNmzvmS1'], ['12136-b    1  -2002 12355  456a'], ['b-b456'], ['6-b    VuNmzNvmS1  2 1235  456'], ['125,00    150004'], ['12136-b    1-2000  -2002 12355  456a'], ['0   -2000   '], ['115']]
results = [False, True, True, None, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, True, False, False, None, False, None, False, False, False, False, False, False, False, False, False, False, True, False, True, False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, True, False, True, False, False, None, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]

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
        func_name = "check_integer"
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
        for test_case in ['assert check_integer("python")==False', 'assert check_integer("1")==True', 'assert check_integer("12345")==True']:
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
