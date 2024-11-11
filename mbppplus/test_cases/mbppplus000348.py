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
inputs = [['python programming, python language', 'python'], ['python programming,programming language', 'programming'], ['python programming,programming language', 'language'], ['c++ programming, c++ language', 'python'], ['', ''], ['UPmVaKepPO', 'UPmVaKepPO'], ['UPmVaKepPO', ''], ['', 'UPmVaKepPO'], ['UPmVepPO', 'UPmVepPO'], ['UPmVaKUPmVepPOepP', 'UPmVaKepPO'], ['UPmVaKepPO', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['UPmVaKepPO', 'UPmVepPO'], ['UUPmVaKepPOUPmVaKepPOaKPepPO', 'UPmVaKepPO'], ['UPPmVaKepPO', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['UPmVaKepPO', 'UPmVaKUPmVepPOepP'], ['UUPmVaKepPOUPmVaKepPOaKPepPOPO', 'UPmVaKepPO'], ['UPmVepPO', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['UPPmVaKepPO', 'UUPmVaKepPOUPmVaKep'], ['UPmVaKUPmVepPOepPUPmVepPO', 'UPmVepPO'], ['UPmVaKPepP', 'UPmVaKepP'], ['', 'UPmVaKepPPO'], ['UPmVaKUPmVepPOepPUUPmVaKepPpPO', 'UPPmVaKUPmVepPOepPUPmVepPO'], ['UPPmVaKUPmVepPOepPUPmVepPOO', 'UPPmVaKUPmVepPOepPUPmVepPOO'], ['UPPmVaKepPO', 'UPmVaKPepP'], ['UPmVaKPepPO', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['zsLntfBjA', 'ubw'], ['UPmVaKPepPO', 'UUPOaKPepPO'], ['UPmVaKepPO', 'UPmVaKUPmVepPOUPPmVaKUPmVepPOepPUPmVepPOOepP'], ['UPmVaKUPmVepPOepPUUPmVaKepPpPO', 'UPmVaKPepPO'], ['UPmVaKUPmVepPOepPUUPmVaKepPpPO', 'UPPmVaKmVepPOepPUPmVepPO'], ['UPmVaKepP', ''], ['UPmVaKPUPPmVaKUPmVepPOepPUPmVepPOepPO', 'UPPmVaKepPO'], ['zsLntfBjA', 'zsLntfBjA'], ['UPmVUUPmVaKepPOUPmVaKepaKUPmVepPOepP', 'UPmVaKepPO'], ['UPmVaeKepPO', 'UPmVaKepPO'], ['UPmVaKUPmVepPOUPPmVaPmVepPOepPUPmVepPOOepP', 'UPmVaKUPmVepPOUPPmVaKUPmVepPOepPUPmVepPOOepP'], ['UPmVaKUPmVepPOUPPmVaKUPmVepPOepPUPmVepPOOepP', 'UPmVepPO'], ['UUPmVaKepPOUPmVaKepPOaKPepPUPPmVaKepPOOPO', 'UUPmVaKepPOUPmVaKepPOaKPepPOPO'], ['UPPmVaKepPO', 'UUPmVaKepPOUPmVa'], ['UPPmVaKUPmVepPOepPUPmVepPO', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['UPO', 'UPmVaKepPO'], ['UPmVaKUPmVepPOepPUPmVepPO', 'UPmVaKUPmVepPOepPUPmVepPO'], ['UPmVUUPmVaKepPOUPmVaKepaKUPmVepPOepP', 'UPmVepPO'], ['UUPmVamKepPOUPmPVa', 'UUPmVaKepPOUPmVa'], ['zsLntfUPmVaKepPPOBjA', 'zsLntfUPmVaKepPPOBjA'], ['UPmVaKPUPPmVaKUPmVepPOepPUPmVepPOepPO', 'UPmVaKepP'], ['UPmVaKepPO', 'UPPmVaKUPmVepPOepPUPmVepPO'], ['UPmVUUPmVaKepPOUPmVaKepaKUPUPmVepPOepPOepP', 'UPmVepPO'], ['UPmVaKUPmVepPOepPUUPUUPmVaKepPOUPmVamVaKepPVpPO', 'UPmVaKUPmVepPOepPUUPmVaKepPpPO'], ['UPPmVaKepPO', 'PUUPmVaKepPOUPmVa'], ['UPmVaUPPmVaUPmVUUPmVaKepPOUPmVaKepaKUPmVepPOepPKUPmVepPOepPUPmVepPOpP', ''], ['UPmVepPO', 'UPmVepPUO'], ['UUPmVaKepPOUPmVaKepPOaKPepPUPPmVaKepPOOPO', 'UUPmVaKepPOUPmVaKepPOaKPepPUPPmVaKepPOOPO'], ['UPmVaeKepPO', 'UPmVaKepP'], ['UPmVaKUPmVepPOepPUPmVepPO', 'UPmVPUUPmVaKepPOUPmVaaKUPmVepPOepPUPmVepPO'], ['UPmVaKPUPPmVaKUPmVepPOepPUPmVepPOepPO', 'UPmVPUUPmVaKepPOUPmVaaKUPmVepPOepPUPmVepPO'], ['UPmVaKepP', 'UPmVaeKepPO'], ['PUUPmVazsLntfUPmVaKepPPOBjAKepPOUPmVa', 'PUUPmVaKepPOUPmVa'], ['UPmVaKUPmVepPOepPUUPUUPmVaKepPOUPmVamVaKepPVpPO', ''], ['UPmVaKPepP', 'UPmUUPmVaKepPOUPmVaKepP'], ['UPmVaKUPmVepPOUPmVUUPmVaKepPOUPmVaKepaKUPUPmVepPOepPOepPepPUPmpVepPO', 'UPmVaKUPmVepPOepPUPmpVepPO'], ['UPmVaKPepP', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['', 'PUUPmVazsLntfUPmVaKepPPOBjAKepPOUPmVa'], ['UUPmVaKepPOUPmVaKepPOaKPepPOPO', 'UPmVaKep'], ['UUPOaKPepPO', 'UPmVaKepPO'], ['UUPmVaKPepPOUPmVaKepPOPaKPepPUPPmVaKepPOOPO', 'UUPmVaKepPOUPmVaKepPOPaKPepPUPPmVaKepPOOPO'], ['UPmVa', 'UUPmVaKepPOUPmVaKepPOaKPepPO'], ['UPmVaeKepPO', 'UP'], ['UPmVaeKeUPmVPUUPmVaKepPOUPmVaaKUPmVepPOepPUPmVepPOpPO', 'UPmVaeKepPO'], ['UPmVaKeUPmVaKUPmVepPOepPUPmVepPOpP', 'UPmVaeKepPO'], ['UUPmVaKepPOUPmVaKep', 'UPmVaKP'], ['UPmVepPO', 'UPmVaKUPmVepPOepPUPmVepPO'], ['UPO', 'UUPmVaKepPOUPmVaKepPOaKPepPUPPmVaKepPOOPO'], ['UPPmVaKUPmVepPOepPUPmVepPO', 'zsLntfUPmVaKepPPOBjA'], ['UPmUVaKPepP', 'UPmUVaKPepP'], ['UPmVaKep', 'UPmVaKep'], ['UPmVUUPmVaKepPOUPmVaKepaKUPmVepPOepP', 'UPmVUUPVmVaKepPOUPmVaKepaKUPmVepPOepP'], ['UPmVaKUPmVepPOepP', 'UP'], ['UPPmVaKUUmVaKepPOUPmVaepPO', 'UPPmVaKUUPmVaKepPOUPmVaepPO'], ['UPPmVaKUPmVaKPUPPmVaKUPmVepPOepPUPmVepPOepPOepP', 'UPPmVaKepP'], ['UPmVzsLntfUPmVaKepPPOBjAVmVaKepPOUPmVaKOepaKUPmVepPOepPpPO', 'UPmVaKepPO'], ['UPPmVaKUPmVepPOepPUPmVepPO', 'UPPmVaKUPmVepPPOepPUPmVepPOO'], ['UPmVaKUPmVepPOepPUUPmVaKepPpPO', 'PUUPmVaKepPOUPmVa'], ['UPmVUUPmVaKepPOUPmVaKepaKUPUPmVepPOepPOepP', 'UPmVaKepP'], ['UPPmVaKepPmO', 'UPPmVaKepPO'], ['zsLntfBjA', 'UUPmVaKepPOUPmVa'], ['PUUPmVazsLntfUPmVaKepPPOBjAKepPOUPmVa', 'PUUPmVaKepPUPmVa'], ['UPPmVaKepP', 'UPmVepPO'], ['PUUPmVazsLntfUPmVaKepPPOBjAKepPaOUPmVa', 'PUUPmVazsLntfUPmVaKeUPPmVaKepPmOpPPOBjAKepPOUPmVa'], ['UPmVaKUPmVepPOepPUPmVPO', 'UPmVamKUPmVepPOepPUPmVepPO'], ['', 'UPmVaKepPP'], ['UPmVaKUPmVepPOUPPmVaKUPmVepPOepPUPmVepPOOepP', 'UPmVepPUO'], ['UPmUVaKPepP', 'UPmVepPO'], ['UPmVaKUPmVepPOepPUPmVepPO', 'UPmVaUKUPmVepPOepPUPO'], ['UPmPVaKP', 'UPmVaKP'], ['UPmVaKUPmVepPOepPUUPUUPmVaKepPOUPmVamVaKepPVpPO', 'UPmVaKeUPmVaKUPmVepPOepPUPmVepPOpP'], ['UPmVaKUPmVepPOepPUUPmVaKepPpPO', 'UPmVVaKP'], ['UUPmVaKepPOUPmVaKepPOaKPepPOPO', 'UPO'], ['UPmVaeKeUPmVPUUPmVaKepPOUPmVaaKUPmVepPOepPUPmVepPOpPO', 'UPmVaeKeUPmVPUUPmVaKepPOUPmVaaKUPmVepPOepPUPmVepPOpPO'], ['PUUPmVafUPmVaKepPPOBjAKepPOUPmVa', 'PUUPmVaKepPOUPmVa'], ['zfBjA', 'zsLntfBjA'], ['UUPmVaKepPOUPmVaKepPOaKPepPOUPmVUUPVmVaKepPOUPmVaKepaKUPmVepPOepP', 'UPPmVaKmVepPOepPUPmVepPUPOO'], ['PUUPmVazsLntfUPmVaKepPPOBjAKepPOUPmVa', 'UPPmVaKUPmVaKPUPPmVaKUPmVepPOepPUPmVepPOepPOepP'], ['PUUPmVazsLntfUPmVaKepPPOBjAKepPOUPmVa', 'PUUPmVaUKepPUPmVa'], ['UPmVUUPVmVaKepPOUPmVaKepaKUPmVepPOepP', 'UPmVaKepPO']]
results = [('python', 0, 6), ('programming', 7, 18), ('language', 31, 39), None, ('', 0, 0), ('UPmVaKepPO', 0, 10), ('', 0, 0), None, ('UPmVepPO', 0, 8), None, None, None, ('UPmVaKepPO', 1, 11), None, None, ('UPmVaKepPO', 1, 11), None, None, ('UPmVepPO', 6, 14), None, None, None, ('UPPmVaKUPmVepPOepPUPmVepPOO', 0, 27), None, None, None, None, None, None, None, ('', 0, 0), None, ('zsLntfBjA', 0, 9), ('UPmVaKepPO', 5, 15), None, None, ('UPmVepPO', 6, 14), None, None, None, None, ('UPmVaKUPmVepPOepPUPmVepPO', 0, 25), ('UPmVepPO', 25, 33), None, ('zsLntfUPmVaKepPPOBjA', 0, 20), None, None, ('UPmVepPO', 27, 35), None, None, ('', 0, 0), None, ('UUPmVaKepPOUPmVaKepPOaKPepPUPPmVaKepPOOPO', 0, 41), None, None, None, None, None, ('', 0, 0), None, None, None, None, ('UPmVaKep', 1, 9), None, None, None, ('UP', 0, 2), None, None, None, None, None, None, ('UPmUVaKPepP', 0, 11), ('UPmVaKep', 0, 8), None, ('UP', 0, 2), None, None, None, None, None, ('UPmVaKepP', 5, 14), None, None, None, None, None, None, None, None, None, None, None, None, None, None, ('UPmVaeKeUPmVPUUPmVaKepPOUPmVaaKUPmVepPOepPUPmVepPOpPO', 0, 53), None, None, None, None, None, None]

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
        func_name = "occurance_substring"
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
        for test_case in ["assert occurance_substring('python programming, python language','python')==('python', 0, 6)", "assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)", "assert occurance_substring('python programming,programming language','language')==('language', 31, 39)", "assert occurance_substring('c++ programming, c++ language','python')==None"]:
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
