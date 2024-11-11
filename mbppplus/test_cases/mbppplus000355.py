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
inputs = [[[1, 3, 5, 7, 4, 1, 6, 8]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[1, 5, 7, 9, 10]], [[-10, -5, 0, 5, 10]], [[0, 1, -1, 2, -2, 3, -3]], [[-10, -5, 0, 5, 10, 0]], [[0, 0, 1, -1, 2, -2, 3, -3]], [[-10, -5, 0, 5, 10, -2, 0]], [[0, 0, 1, -1, 2, -2, 3, -3, -3]], [[0, 1, 1, -1, 2, -2, 3, -3]], [[-10, -1, 0, 5, 10, 0]], [[0, 1, -1, 2, 3, -3, -3]], [[0, 0, 1, -1, 2, -2, 3, -3, 3]], [[0, 0, 1, 2, -2, 3, -3, -3]], [[-10, -1, 0, 5, 10, 0, 5]], [[0, 1, 2, -2, 3, -3, -3]], [[0, 0, 1, -1, 2, -2, 3, -3, -3, 2]], [[0, 1, 2, -2, -3, -3]], [[-10, -1, 0, 5, 10, 0, 5, -10]], [[-10, -5, 0, -10, -1, 10, -2, 0]], [[1, 2, -2, 3, -3, -3]], [[-10, -5, 0, 1, 10]], [[0, 0, 1, -1, -2, 3, -3, -3, 2]], [[0, 0, 1, -1, 2, -2, 3, -3, -3, 2, -3]], [[-10, -1, 0, 5, -2, 10, 0, 5, -10, -1]], [[-10, -5, 10, 0, -10, -1, 10, -2]], [[0, 1, 1, -1, -10, 3, -3, 3, 3]], [[-5, 0, 10, 1, 10]], [[-10, 3, 0, 1, 10]], [[-2, -10, -5, 0, 5, 10]], [[1, 2, -2, 3, -3]], [[-10, -5, -1, 5, 11, 10, 1]], [[0, 3, 1, -1, 2, -2, 3, -3, 3, -1]], [[-10, -1, 0, 5, 10, 0, 5, -10, -10]], [[-10, -1, 0, 5, 10, 0, 5, -10, -1]], [[-10, -5, -2, 5, 10, 0]], [[-10, -5, -1, 5, 11, 10, 1, 1]], [[-10, -5, -1, 11, 10, 1, -1]], [[-10, 0, 5, 10, 0, 0]], [[0, 1, -1, 2, 3, -4, -3]], [[-5, 0, 10, 1, -2, 10]], [[0, 0, 0, -1, 2, -2, 3, -3]], [[0, 0, 1, 2, -2, 3, -3, -3, 2]], [[0, 1, -1, 2, 3, 5, -3]], [[-10, 2, 0, 5, -2, 10, 0, 5, -10, -1]], [[0, 0, -10, -1, 2, -2, 3, -3, 3]], [[0, 0, 1, -1, 2, -2, 3, -3, -1, -3, 2, -3]], [[-10, -5, 0, 10, 5, 10, 10, 10]], [[0, 1, 2, -1, -3, -3]], [[-10, -5, 0, -10, -1, 10, 11, -2, 0]], [[0, 1, -1, 2, -2, 3, -3, 0]], [[0, 1, 2, -1, -3]], [[0, 1, -1, 2, 3, 11, 5, -3]], [[-10, -5, -1, 11, 1, 10, 1]], [[-10, -5, -10, -1, 10, -2, 0, -10]], [[0, 0, -1, 2, -2, 3, -4]], [[0, 1, -1, 2, -2, -4, -3, -4]], [[-5, 10, 0, -10, -1, 10, -2]], [[-2, -10, -5, 0, 5, 10, -2]], [[-5, 0, 5, -2, 0]], [[1, 2, -2, -3, -3]], [[0, -1, 2, 3, 11, 5, -3]], [[0, 1, 2, -2, 3, -3, -3, 2, 2]], [[0, 0, 2, -1, 5, -3, -3, 2, 3]], [[0, 0, 0, -1, 2, -2, -3]], [[-10, -5, -1, 5, 11, 10]], [[-4, -10, 0, 1, 1, -1, -10, 3, -3, 3, 3]], [[-10, -5, 0, 5, 2]], [[-1, 1, -1, 2, 3, -4, -3]], [[-10, -5, 0, 5, -5, 0]], [[0, 0, -1, 2, -2, 3, -4, 0]], [[-10, 0, 5, 10, 0, 0, 10]], [[-2, -10, -5, 0, 5, 10, -5]], [[-10, -1, 0, 5, 10, 0, 1, -10, -10]], [[-10, 0, 5, 10]], [[-10, 10, 0, -10, -1, 10, -2]], [[0, 2, -1, 1, -3]], [[0, 2, -1, 2, -1, 3, 11, 5, -3]], [[-5, 0, 1, -2, 10]], [[0, 0, -1, 2, -2, 3, -4, -2]], [[-4, -10, -5, 0, 5, 10, -10]], [[0, 1, -1, 2, 3, 5, -3, 0, -3]], [[-10, -5, -1, 5, 11, 0, 1, 1, 11]], [[-1, 0, 2, -1, 5, -3, -3, 2, 3]], [[0, 1, 2, -2, 3, -3, -3, 3]], [[-10, 1, -5, 0, 10, 5, 10, 10, 10]], [[0, 1, 1, -1, 2, -2, 3, -3, -3]], [[-5, 0, -10, -1, 10, -2]], [[-4, 0, 1, 2, -2, -3, -3]], [[-10, -5, 0, -1, 10, 11, 3, 0]], [[-11, -5, -1, 5, 6, 9, 11, 10, 1, 1, 1]], [[-4, -5, 0, 5, 10, -10]], [[-10, 3, -1, 5, 11, 10]], [[-5, -1, 5, 11, 10, -11, 1, 1]], [[-10, -5, 4, -2, 5, 10, 0]], [[-2, -10, -5, 0, 5, 10, -5, 10]], [[0, 1, 1, 2, -2, 3, -3, -3]], [[-10, -5, -1, 5, 11, -1, 1, 1, 11]], [[-10, 1, 0, 10, 5, 10, 10, 10]], [[-10, -5, -1, 5, 11, -1, 1, 1, 1, 11]], [[0, 1, -1, 2, 3, -4, -3, 3]], [[0, 0, 2, -1, 5, -3, -3, 3]], [[-4, -10, -5, 0, 5, 10, -10, -5]], [[-1, 1, -1, 3, -4, -3]], [[-2, -10, -5, 0, 5, 10, -2, -2]]]
results = [4, 2, 10, 50, 0, 50, 0, 50, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 10, 50, 2, 50, 0, 0, 10, 50, 0, 0, -30, 10, 2, 50, 0, 10, 10, 50, 50, 50, -50, 0, 0, 0, 0, 0, -50, 0, 0, 50, 0, 50, 0, 0, 0, 50, 50, 0, 0, -50, 10, 0, 2, 0, 0, 0, 0, 50, -4, 50, -2, 50, 0, -50, 10, 10, -50, 10, 0, 0, 0, 0, 20, 0, 50, 0, 0, -10, 0, 0, -4, 50, -66, 20, -30, -50, 50, 10, 0, 50, -10, 50, 0, 0, 20, 4, 10]

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
        func_name = "mul_even_odd"
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
        for test_case in ['assert mul_even_odd([1,3,5,7,4,1,6,8])==4', 'assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2', 'assert mul_even_odd([1,5,7,9,10])==10']:
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
