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
inputs = [[[10, 20, 1, 45, 99]], [[1, 2, 3]], [[45, 46, 50, 60]], [[10]], [[10, 10, 10]], [[10, 9, 10]], [[10, 9, 10, 9]], [[10, 10, 10, 10]], [[10, 9, 10, 10]], [[10, 10]], [[10, 10, 10, 9]], [[10, 10, 10, 9, 10]], [[10, 9, 10, 10, 10]], [[9, 10]], [[10, 9, 9, 10]], [[10, 10, 10, 10, 9]], [[10, 10, 10, 9, 10, 10]], [[9, 10, 10, 10, 10]], [[10, 9, 9]], [[10, 10, 9, 10, 9]], [[9, 10, 10]], [[11, 10, 9, 10, 9, 10]], [[10, 9, 10, 9, 9]], [[11, 10, 10]], [[9, 9, 10, 10]], [[10, 11, 10, 9]], [[10, 9, 9, 10, 9]], [[11, 10, 9, 10, 10, 10, 10, 10]], [[9, 10, 10, 9, 10]], [[9, 10, 10, 10, 9, 10, 10]], [[10, 9, 9, 9]], [[9, 10, 10, 10]], [[11, 10, 10, 9]], [[10, 10, 9, 10]], [[9, 9, 10]], [[9, 10, 9, 9, 10]], [[11, 11, 10, 10, 9]], [[10, 10, 8, 10, 9, 10]], [[8, 9, 10, 10, 9]], [[8, 10, 10]], [[10, 9, 8, 9, 10, 9]], [[8, 10]], [[10, 9, 9, 10, 9, 10]], [[11, 10, 10, 8, 9]], [[11, 11, 10, 10, 10, 9]], [[11, 11, 10, 10, 9, 10]], [[10, 10, 10, 11, 10, 10]], [[11]], [[12, 8, 11, 10]], [[10, 9, 10, 8, 10]], [[10, 10, 8, 10, 9, 10, 10]], [[9, 10, 9, 9, 10, 9, 9]], [[10, 9, 8, 9, 10]], [[11, 11, 10, 10, 10, 10]], [[9, 10, 10, 9, 8, 10]], [[8, 10, 9]], [[7, 8, 10]], [[8]], [[10, 10, 10, 8, 10, 9, 10, 10]], [[11, 10, 10, 10, 8, 10, 9, 10, 10]], [[11, 10, 10, 8]], [[11, 11, 10, 10, 11, 10, 9]], [[11, 11, 10, 10, 11, 10, 8]], [[10, 9, 8, 10]], [[10, 7, 9, 10]], [[11, 10, 10, 11, 9]], [[10, 10, 10, 11, 9, 10]], [[9, 10, 9, 9, 9, 10, 8, 9]], [[9, 10, 9, 9]], [[9, 10, 10, 9]], [[11, 8, 10, 10]], [[9, 10, 9, 8, 9, 10, 9]], [[11, 9, 10, 9, 10, 10, 9, 10]], [[11, 10, 10, 10, 8, 10, 11, 9, 10, 10]], [[11, 9, 9]], [[9, 9, 9, 10, 10, 9]], [[11, 9, 10, 10, 10, 9]], [[11, 10, 10, 11, 9, 10]], [[10, 10, 11, 10, 10]], [[9, 12, 10]], [[10, 9, 10, 10, 9]], [[11, 8, 10, 11, 10]], [[11, 10, 8, 9, 10]], [[12, 12, 8, 11, 10]], [[11, 10, 10, 10, 8, 10, 11, 8, 9, 10, 10, 10]], [[10, 9, 10, 9, 10]], [[11, 10, 7, 8]], [[7, 9, 10, 9, 10, 9, 10]], [[9, 10, 10, 10, 9, 10]], [[10, 10, 10, 9, 10, 10, 10, 10]], [[9, 10, 9, 9, 10, 9, 9, 10]], [[11, 11, 10, 10, 9, 9]], [[11, 9, 10]], [[9, 11, 9, 9, 10, 9, 9]], [[11, 11, 10, 10, 11, 10, 10]], [[10, 9, 9, 8, 9]], [[10, 9, 10, 10, 10, 10, 10]], [[11, 10, 9]], [[12, 12, 8, 11, 10, 12]], [[10, 9, 8, 9, 11, 10]], [[10, 7, 9]], [[10, 12, 9, 10, 9]], [[-115.40386094393058, 13.801990543244983, -90.4732800288427, -75.81228356592653]], [[7, 7, 8, 10]]]
results = [1, 1, 45, 10, 10, 9, 9, 10, 9, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 9, 8, 9, 9, 10, 11, 8, 8, 8, 9, 8, 10, 8, 8, 7, 8, 8, 8, 8, 9, 8, 8, 7, 9, 9, 8, 9, 9, 8, 8, 9, 8, 9, 9, 9, 9, 10, 9, 9, 8, 8, 8, 8, 9, 7, 7, 9, 9, 9, 9, 9, 9, 10, 8, 9, 9, 8, 8, 7, 9, -115.40386094393058, 7]

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
        func_name = "smallest_num"
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
        for test_case in ['assert smallest_num([10, 20, 1, 45, 99]) == 1', 'assert smallest_num([1, 2, 3]) == 1', 'assert smallest_num([45, 46, 50, 60]) == 45']:
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
