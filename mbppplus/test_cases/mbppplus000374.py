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
inputs = [['GeMKSForGERksISBESt'], ['PrECIOusMOVemENTSYT'], ['GooGLEFluTTER'], ['A'], ['a'], ['aa'], ['aA'], ['Aaa'], ['aaaAaA'], ['aaaAaAA'], ['aaaA'], ['aaA'], ['aAaa'], ['aaaaA'], ['AaaA'], ['aaaAaaaAaAA'], ['aAaaa'], ['aaaAAaA'], ['AaaaAA'], ['aaaaAaAA'], ['AaaaAAA'], ['aaaaAaA'], ['AaaaaAA'], ['Aa'], ['aaaAaaaaaAAA'], ['aaaAAaaaaaAAaaaAAaAA'], ['aaaaAAaA'], ['aAaaaaAAaaaaAAA'], ['aaaaaAAaA'], ['aaaaaAaAAaaAAaA'], ['aaaaAAaAA'], ['xTzcVWVVy'], ['aaaaAAaAAAaaA'], ['aaAaaaAAaA'], ['aaaaaAaAAaaAaAaA'], ['aaaaAaaaAaAA'], ['AaaaAAaA'], ['AAa'], ['aaaaaAaAAaaAAaAA'], ['AaAa'], ['AaaaaAAA'], ['aaaaaAAaAAAaa'], ['aaAaaaAAAaaAAaAA'], ['xTzcVWVaaaAAaaaaaAAaaaAAaAAy'], ['aaaaAaAaAaa'], ['aaaaAaaaaaAaAaAaaA'], ['AaaaaAAaaaaaAAaaaAAaAAaaAAA'], ['aaaaaAaAAaaaAAaA'], ['aaaaAaaAAaA'], ['aaAaaaAaaAAaAA'], ['aaaAA'], ['aAaAaaA'], ['aaaAAaaaaaAAaaAaAAaAA'], ['AaaaaA'], ['AAAa'], ['aaaAAAaaaAaaAAaA'], ['aaAaaaaAAAaaAAaAA'], ['aaaaAaAAaa'], ['aaa'], ['aaaAAaaaaaAAaAaAaAAaaAaaaAAAaaAAaAAaAA'], ['aaaaAaaaaAAAaaAAaA'], ['aaAaaaAAAaaAAaAAaaAaaaAaA'], ['AaaaaAAaaaaaAAaAaAaAAaaAaaaAAAaaAAaAAaAAaA'], ['aaaAaaaAaaaaaAAAaAA'], ['aaaaaAaaaaaAAAAaaaaAAAaaAAaAA'], ['aaaaaaaaAaAAaaAaAaAaaAaAAaaAAaA'], ['aaaaAaaaaaAaAAaaAAaA'], ['aaaaaAaAAaa'], ['aaaaaAaaaaAaAAaaaAAaaaAAaA'], ['aaaAAaaaaaAAAaAaAaAAaaAaaaAAAaaAAaAAaAA'], ['aaAaaaAAAaaAAAaAA'], ['aaaaaaaaAaAAaaAaAaAaaAaaaaAAaAAaAAaaAAaaaaAAaAaaaaA'], ['aaaaaAaaaAaAA'], ['aaaaAaaaaaAaaaaaAAAAaaaaAAAAaAA'], ['aaaaAAaaaaaAAaaAaAAaAA'], ['AAaaaAAaA'], ['AAaaaaAAaA'], ['AAaaaA'], ['aAaaaaAAaAaaA'], ['aaaaAaAAaaaAAa'], ['aaaaaaaaaaAaaaAAAaaAAaAAAaAAaaAaAaaaaAAaaaaA'], ['aaaaaAaaaaAAAaaAAaA'], ['aaaAAaaaaAAA'], ['aAaaaAAaAAAaaA'], ['AaAaaaaAA'], ['aaaaaaaAaaaaAaAAaaaAAaaaAAaAaAA'], ['AaAaaaaAAAaA'], ['xzcVWVVy'], ['AaAaAaaaAAAaA'], ['aaaaAaaa'], ['aaaaaA'], ['aaaaaaaaAaAAaaAaAaAaaAaaaaAAaAAaAAaaAAaaaaAAaAAAaaAaaaaAAaAaaaaA'], ['aaaaAaaaaaAaAaAaaAaaaAAaaaaaAAaAaAaAAaaAaaaAAAaaAAaAAaAA'], ['aaaAaaaaAAAaaAAaAA'], ['aaaaaaaAaAaAaaAAaaaaAAA'], ['aAaaaaAAaaaaAA'], ['aaaAAaaaaaAAaaaAAaAAaaaaaAaaaAaAA'], ['AaaaA'], ['AaAaA'], ['AaaaaAAAa'], ['aAaAaaaAA'], ['AaA'], ['aaaAaaaAaaaaaAAAaAAA'], ['aAAaaaAA'], ['aaaAAaaaaaaaaAAaaaaaAAAaAaAaAAaaAaaaAAAaaAAaAAaAAAAaaaAAaAAaaaaaAaaaAaAA']]
results = [5, 6, 4, 1, 0, 0, 1, 0, 1, 2, 1, 1, 0, 1, 1, 2, 0, 1, 2, 2, 3, 1, 2, 1, 3, 2, 1, 3, 1, 1, 2, 4, 1, 1, 1, 2, 1, 2, 2, 1, 3, 0, 2, 2, 0, 1, 3, 1, 1, 2, 2, 1, 2, 1, 3, 1, 2, 0, 0, 2, 1, 1, 1, 2, 2, 1, 1, 0, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 3, 1, 2, 2, 1, 4, 1, 0, 1, 1, 2, 2, 3, 2, 2, 1, 1, 3, 2, 1, 3, 2, 2]

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
        func_name = "max_run_uppercase"
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
        for test_case in ["assert max_run_uppercase('GeMKSForGERksISBESt') == 5", "assert max_run_uppercase('PrECIOusMOVemENTSYT') == 6", "assert max_run_uppercase('GooGLEFluTTER') == 4"]:
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
