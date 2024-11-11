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
inputs = [[[2, 1, 5, 3]], [[9, 3, 2, 5, 1]], [[3, 2, 1]], [[9, -3, 2, 0, -5, 1, 11, -7]], [[1]], [[3, 3, 3, 3]], [[-5, -3, -2, -1]], [[1, 2, 3, 4, 5]], [[-1, 0, 1, 2, -2]], [[-5, -3, 0, -2, -1]], [[-1, 4, 0, 1, 2, -2]], [[2]], [[-5, -3, 0, -3, -1]], [[-7, 2]], [[2, 2]], [[0, 3, 0, 1, 2, -2]], [[-6, -3, 0, -3, -1]], [[1, 1]], [[0, 9, 3, 0, -2]], [[-7, -7, 2]], [[5, -3, 0, -2, -1]], [[-1, -2, 0, 1, 2, -2, 2]], [[1, 2, 3, -3, 5]], [[9, -3, 2, -5, 1, 11, -7]], [[-6, -3, 0, -2, -1]], [[-5, -3, 0, -2, -3, -2]], [[-5, -3, 0, -3, -2, 11, -3, -7]], [[-5, -6, -2, 0, -3, -1]], [[-1, 2, 0, 1, 2, -2, 2]], [[-1, 1, 4, 0, 1, 2, -2]], [[-7, 2, -7]], [[0, 9, 3, 0, 10, -2]], [[2, 3, 3]], [[-5, -3, -2]], [[-5, -3, 0, 0]], [[-5, -3, -2, -1, -1]], [[3, 3, 3]], [[0, 9, 3, 9, 0, 10, -2]], [[-5, 0, 0]], [[0, 3, 0, 1, 2, -2, 0]], [[-7, -7, 3, 2]], [[-23.760842462159786, -91.16655074878469, -69.98937256313435, -23.593017846262015, 49.56089624759201]], [[-5, -3, 0, -2, -3, -3, -2, -5]], [[-5, -3, 0, -2, -3]], [[0, 9, 3, 0, -2, 9, 3]], [[0, 9, 0, -2, 0, 0]], [[3, 4, 3, 3]], [[-8, -2, 3, 2]], [[9, -3, 2, -5, 1, 11, -7, 1]], [[-1, 0, 9, 3, 0, -2, 0]], [[-5, -3, 0, -6, -3, -1]], [[0, 9, 3, 0, -2, 9, 3, 3]], [[-5, -3, -6, -2, 0, -2, -3]], [[2, -8, 1, 1]], [[-6, -3, 0, -3, -1, -3]], [[-6, -3, 0, -3, -1, -2, -3]], [[-5, -3, 0, -2, -3, -3, -2, -5, -5]], [[-6, -3, 0, -3, -1, -2, -3, -6]], [[-1, 4, 0, 1, -2]], [[0, 9, 0, -2, 0, 2]], [[-5, 0, -3, -1]], [[-1, -2, 0, 1, -2, 2]], [[-6, -3, 0, -2, -1, -3]], [[-5, -3, 0, -3, -1, -3]], [[-5, -2, -3, -2]], [[-7, 3, 3, 2]], [[-7, 0, 11, -7, 2]], [[0, 0, 3, 0, -2]], [[9, -6, -3, 5, -3, -1, -2, -3, -6]], [[0, 9, 3, 0, -2, 0]], [[-6, 0, -3, 0, -3, -1, -3]], [[3, 4, 3, 3, 4]], [[-2]], [[1, 2, 3, -3]], [[8, -4, 2, -5, 4, 1, 11, 8, -7, 1]], [[1, 2, 4, 3, -3, 1]], [[3, 3]], [[-1, -4, 4, 0, 1, -2]], [[-5, 0, -1]], [[-7, -7, 2, -7]], [[0, 3, 0, 1, 2, 0, -2, 3]], [[-5, -2, -3, -2, -2]], [[3]], [[1, 2, 2, 4, 5]], [[-4, 8, -4, 2, -5, 4, 1, 11, 8, -7, 8]], [[11, -7, 2]], [[-23.760842462159786, -91.16655074878469, -69.98937256313435, -23.593017846262015]], [[-2, 3, 2]], [[2, 0, 1, 2, -2, 2]], [[0, 3, 1, 2, 0, -2, 3, 3]], [[0, 9, 3, 9, 0, 10, 1, -2]], [[2, 0, 1, 2, 2]], [[-5, -2, -1, -1]], [[-1, -4, 5, 0, 1, -2, 1]], [[-5, -2, -1, 0]], [[-2, 3]], [[-5, 4, 0, -6, -3, -1, -1]], [[-5, -3, 0, -2, -3, -3, -2, -5, -5, -5]], [[2, 3, -6, 3, 3]], [[-6, -3, 0, -3, -1, -7, -2, -3, -6, -3, -1]], [[0, 9, -6, 3, 0, -2, 9, 3, 3]], [[1, 2, 4, 4, -3, 1]], [[2, -4, 4, 5, 4]], [[True, True, False]], [[78, 8, 0, 9, -42, 4, -29, 9, -3, -5]], [[-5, -3, -6, -2, 0, -2, -2]], [[-5, -3, -3, -2]], [[-42, 0, 9, 3, 0, 10, -2, 9, 3]], [[2, 0, 1, 2, -2, 2, 2, 2]]]
results = [4, 8, 2, 18, 0, 0, 4, 4, 4, 5, 6, 0, 5, 9, 0, 5, 6, 0, 11, 9, 8, 4, 8, 18, 6, 5, 18, 6, 4, 6, 9, 12, 1, 3, 5, 4, 0, 12, 5, 5, 10, 140.7274469963767, 5, 5, 11, 11, 1, 11, 18, 11, 6, 11, 6, 10, 6, 6, 5, 6, 6, 11, 5, 4, 6, 5, 3, 10, 18, 5, 15, 11, 6, 1, 0, 6, 18, 7, 0, 8, 5, 9, 5, 3, 0, 4, 18, 18, 67.57353290252267, 5, 4, 5, 12, 2, 4, 9, 5, 5, 10, 5, 9, 7, 15, 7, 9, 1, 120, 6, 3, 52, 4]

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
        func_name = "max_Abs_Diff"
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
        for test_case in ['assert max_Abs_Diff((2,1,5,3)) == 4', 'assert max_Abs_Diff((9,3,2,5,1)) == 8', 'assert max_Abs_Diff((3,2,1)) == 2']:
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
