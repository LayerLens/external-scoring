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
inputs = [[1500, 1200], [100, 100], [2000, 5000], [-2000, -5000], [-1500, -1200], [-100, -100], [-5000, -1501], [-1501, -5000], [-5000, -5000], [-1501, -1501], [-2001, -2001], [-1501, -4999], [-2001, -4999], [-2000, -2001], [-2000, -4999], [-101, -100], [-1499, -1501], [-5000, -1500], [-2000, -2000], [-2001, -1501], [-1499, -100], [-100, -2000], [-5000, -4999], [-1501, -100], [-5000, -1499], [-1499, -1499], [-5000, -2001], [-100, -5000], [-1502, -1501], [-1500, -2002], [-2002, -1499], [-5000, -100], [-1200, -1200], [-2002, -2003], [-1500, -2000], [-5001, -5000], [-2002, -1500], [-2001, -2000], [-2000, -102], [-1502, -5001], [-1500, -1501], [-2001, -102], [-2002, -1501], [-100, -1499], [-1502, -2002], [-101, -101], [-1500, -4999], [-2000, -100], [-5001, -5001], [-99, -2003], [-101, -1200], [-1200, -1502], [-98, -2003], [-1500, -2001], [-2001, -2002], [-99, -2004], [-4999, -1501], [-100, -99], [-98, -100], [-99, -2000], [-5000, -1502], [-1199, -1199], [-1200, -5000], [-1501, -1499], [-1499, -99], [-101, -1501], [-2002, -4999], [66.25586492562002, 36.64907257918932], [-1502, -2001], [-102, -2003], [-1502, -1502], [-100, -103], [-98, -98], [-4999, -5000], [-101, -1502], [-1500, -101], [False, True], [-1200, -1199], [-101, -2000], [-2003, -2003], [-1500, False], [-2000, -101], [-101, -1499], [-99, -100], [-101, -1500], [-1500, -1500], [-99, -4999], [-100, -101], [-1201, -5000], [-2001, -4998], [-4999, -2000], [True, -2003], [-1999, -4999], [-1503, -1502], [-4999, -4998], [-4999, -4999], [-99, -99], [-5000, -5001], [-1498, -1498], [-98, -99], [-5000, -2000], [-99, -101], [-1201, False], [34, 34], [-1999, -1999], [-1502, -5000]]
results = [False, True, False, False, False, True, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, True, True, False]

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
        func_name = "noprofit_noloss"
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
        for test_case in ['assert noprofit_noloss(1500,1200)==False', 'assert noprofit_noloss(100,100)==True', 'assert noprofit_noloss(2000,5000)==False']:
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
