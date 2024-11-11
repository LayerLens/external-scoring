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
inputs = [[[1, -2, 3, -4]], [[3, 4, 5, -1]], [[1, 2, 3, 4]], [[0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10]], [[]], [[1]], [[-1, -2, -3, 0, 1, 2, 3, 3, 2, 1, 0, -1]], [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5]], [[10, 20, 30, 40]], [[0, 1]], [[-5, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]], [[-1, -2, -3, 0, 1, 2, 1, 3, 2, 1, 0, -1]], [[10, 20, 10, 30, 40]], [[-5, -4, -3, -2, -1, -1, 1, 2, 4, 5]], [[-2, -3, 0, 1, 2, 1, 3, 2, 1, 0, -1]], [[0, -1, 2, -3, 4, -5, 6, 8, -9, 10]], [[10, 20, -9, 40]], [[-5, -4, 3, -2, -1, 0, 1, 2, 3, 4, 5]], [[-1, -2, -3, 0, 1, 2, 1, 3, -1, 2, 1, 0, -1]], [[0, 1, 1]], [[0, -1, 2, -3, 4, -5, 6, 6, -7, 8, -9, 10]], [[2, 3, 4, 5]], [[-5, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 4, 5]], [[-5, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 0]], [[-2, -3, 0, 1, 2, 1, 3, 2, 1, -4, 0, -1]], [[10, -9, 40]], [[-5, -4, -3, -2, -1, 1, 2, 4, 5, 5]], [[10, 19, 30]], [[-1, -2, -3, 0, 1, 2, 1, 3, 1, 0, -1]], [[10, 30, 40, 10]], [[0, -1, 2, -3, 4, -5, 6, 8, -9, 10, 4]], [[0, -1, 2, -2, -3, 4, -5, 6, 8, -9, 10, 4]], [[0, -1, 2, 4, -5, 6, 8, -9, 10, 4]], [[10, -2, -9, 40]], [[0, -1, -1, 2, -3, 4, -5, 6, 8, -9, 10, 4, 4]], [[2, 3, 4, 2, 4]], [[3, 2, 3, 4, 2, 4, 2]], [[0, -1, 2, -3, 4, -5, 6, -7, 8, 10]], [[0, -1, 2, -3, 4, -5, 6, 8, -10, -9, 10, 4]], [[3, 2, 3, 4, 2, 5, 2]], [[-4, -2, -1, 1, 2, 4, 5, 5]], [[-1, -2, -3, 0, 1, 2, 10, 3, 3, 2, 1, 0, -1, 2]], [[-5, 3, -4, 3, -2, -1, 0, 1, 2, 3, -9, 4, 5]], [[-2, -2, 0, 1, 2, 1, 3, 1, -4, 0, -1, -1]], [[10, 20, -9]], [[0, -1, 2, -3, 4, -5, 6, 8, 2, 10]], [[30, 3, 4, 5, 3]], [[0, -1, -1, 2, -3, 4, -5, 6, 8, -9, 10, 4, 4, 6]], [[-9, -4, -2, -1, -1, 1, 2, 4, 5]], [[-1, -2, -3, 0, 1, 2, 1, 3, 2, 1, 0, -1, 2]], [[-5, 3, -4, 3, -2, -1, 0, 1, 3, -9, 4, 5]], [[0, -1, -1, 1, -3, 4, -5, 6, 8, -9, 10, 4, 4]], [[-97.00921686941055, -62.31826514441987, -47.8901822007769, 27.86472361019527, 59.008009822655055]], [[9, 10, 10, 30]], [[10, 21, 20, -9]], [[10, 20, -9, 39]], [[0, -1, 2, -3, 4, -5, 6, -7, 8, 10, -7]], [[-1, -2, -3, 0, 1, 2, 10, 3, 3, 2, 1, 0, -1, 2, 2]], [[10, -9, 40, 40]], [[0, -1, 2, 4, -5, 6, -7, 8, 10]], [[-5, 3, -4, 3, -2, -1, -3, 0, 1, 2, 3, -9, 4, 5, 0]], [[3, 3, 2, 4, 2, 4, 2]], [[-5, -4, -3, -2, -1, -1, 1, 2, 3, 4, 5]], [[0, -1, 2, 4, 1, -5, 6, -7, 8, 10]], [[-5, -4, 3, -2, -1, 0, 1, 2, 3, 4, 5, 5]], [[-1, -2, -3, 3, 0, 1, 2, 3, 3, 2, 1, 0, -1, -3]], [[0, -1, 2, 4, -5, 6, 8, -9, 10, 4, -1]], [[-5, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -4]], [[0, -1, -1, 2, 4, -3, 4, -5, 8, -9, 10, 4, 4]], [[0, -1, 2, 4, -5, 6, -7, 8, 10, 2]], [[9, 10, 11, 30]], [[9, 30, 5, 40, 10]], [[0, -1, -1, 2, -3, 4, -5, 6, 8, -9, 10, 4, 4, 2]], [[0, -1, 2, 4, 6, 8, -9, 10, 4]], [[-1, -2, -3, 0, 1, 2, 1, 3, -2, 2, 1, 0, -1, 3]], [[-2, -5, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -4]], [[-1, -2, -3, 0, 1, 10, 3, 3, 2, 1, 3, 0, -1, 2]], [[-5, -4, -3, -2, -1, -1, 1, 2, 39, 4, 5, 5]], [[-5, -3, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -4, -1]], [[-1, -2, -3, 0, 1, 3, 3, 2, 1, 3, 0, -1, 2]], [[10, 20, 10, 9, 30, 5]], [[0, -1, -2, -1, 2, -3, 4, -5, 6, 8, -9, 10, 4, 4, 2]], [[-2, -3, 0, 1, 2, 1, 3, 1, -4, -1, -1]], [[10, 20, 11, 39]], [[0, -1, 2, 4, 1, -5, 6, -7, 8, 10, 10]], [[10, 19, -9, 40, 40, 40]], [[-5, -3, -4, -3, -2, -1, 0, -2, 1, 2, 3, 4, 5, -4]], [[10, 20, -9, 39, 20]], [[0, -1, 20, -3, 4, -5, 6, 6, -7, 8, -9, 10]], [[-5, -3, -4, -3, -2, -1, 1, 2, 3, 4, 5]], [[0, -1, -1, 2, -3, 4, -5, 6, 8, -9, 10, 4, 4, -9]], [[-2, -3, 0, 1, 2, 1, 3, 2, 1, -4, 0, -1, 0]], [[10, -9, 40, 40, 40]], [[10, 0, -2, -9, 40, -2]], [[-5, -4, -3, -2, -1, -1, 3, 1, 2, 4, 5, 1]], [[-1, -3, -3, 0, 1, 2, 3, 11, 3, 2, 1, 0, -1, 3]], [[-9, -4, -2, -1, 1, 2, 4, 5]], [[0, -1, 2, 3, -3, 4, -5, 6, 8, -10, -9, 10, 4]], [[0, -1, 2, -3, -1, 4, -5, 6, 8, -10, -9, 10, 4]], [[10, 21, 20, -4, -9]], [[10, 20, -9, 40, -9]], [[-5, -3, -3, -3, -2, -1, 0, 1, 3, 4, 5, 0]], [[-11.074239280905289, 59.008009822655055, -62.31826514441987, 27.86472361019527, 59.008009822655055, -97.00921686941055]], [[10, 20, 19, -9, 40, -9]], [[-5, -3, -3, -2, -1, 0, 1, 2, 3, 4, 5, -4, -1]], [[0, -1, 2, -2, -3, 4, -5, 6, 8, -9, 10, 4, -3]], [[-9, -4, -2, -1, 1, 5, 2, 2, 4, 5, -1]], [[0, -1, 2, 4, -5, 6, -7, 8, 10, 2, 6]], [[10, 20, 10, 30, 5]]]
results = [2, 3, 4, 5, 0, 1, 6, 5, 5, 4, 1, 5, 6, 5, 4, 6, 5, 3, 6, 6, 2, 6, 4, 6, 5, 6, 2, 5, 3, 5, 4, 6, 6, 6, 2, 7, 5, 7, 5, 6, 7, 5, 8, 7, 5, 2, 6, 5, 8, 4, 7, 6, 7, 2, 4, 3, 3, 5, 9, 3, 5, 7, 7, 5, 6, 7, 7, 6, 5, 7, 6, 4, 5, 8, 6, 7, 5, 8, 6, 5, 7, 6, 8, 5, 4, 7, 5, 5, 4, 6, 5, 7, 6, 4, 2, 6, 8, 4, 7, 6, 3, 3, 4, 3, 4, 5, 6, 6, 7, 5]

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
        func_name = "pos_count"
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
        for test_case in ['assert pos_count([1,-2,3,-4]) == 2', 'assert pos_count([3,4,5,-1]) == 3', 'assert pos_count([1,2,3,4]) == 4']:
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
