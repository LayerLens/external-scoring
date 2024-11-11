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
inputs = [[[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2], [[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5], [[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3], [[1, 5, 3, 8, 7, 2, 6, 4, 9], 4], [[3, 2, 1], 2], [[], 0], [[5, 95, 81, -20, 8, 72, 0], 0], [[1, 5, 4, 3, 8, 7, 2, 6, 4, 9], 4], [[1, 5, 3, 8, 7, 2, 6, 4], 4], [[4, 5, 3, 8, 7, 2, 6, 4], 4], [[4, 5, 3, 8, 5, 2, 6, 4], 4], [[1, 5, 3, 8, 7, 2, 6, 4, 9], 5], [[1, 5, 5, 8, 7, 2, 6, 4, 9], 5], [[8, 1, 5, 3, 8, 7, 2, 6, 4], 3], [[1, 6, 3, 7, 8, 7, 2, 6, 6, 4, 9], 4], [[1, 4, 3, 8, 7, 2, 6, 4, 9], 4], [[8, 2, 1], 2], [[4, 5, 3, 8, 7, 2, 6, 4], 3], [[1, 5, 3, 8, 7, 2, 6, 4, 9], 1], [[2, 1], 2], [[1, 5, 3, 8, 7, 2, 6, 4, 9], 3], [[1, 4, 3, 8, 7, 2, 6, 4, 9], 3], [[7, 5, 3, 8, 7, 2, 6, 4, 9], 4], [[1, 5, 3, 8, 7, 2, 6, 4, 9, 1], 5], [[4, 5, 3, 8, 8, 2, 6, 4], 3], [[1, 5, 3, 8, 7, 2, 6, 9], 3], [[4, 5, 3, 8, 7, 2, 6, 4], 8], [[1, 6, 7, 8, 7, 2, 6, 6, 4, 9], 4], [[1, 5, 3, 8, 7, 2, 6, 9], 4], [[3, 5, 3, 8, 8, 2, 6, 4], 3], [[1, 5, 3, 8, 7, 2, 6, 4, 9, 1], 6], [[6, 3, 7, 8, 7, 2, 6, 6, 4, 9, 8], 3], [[6, 3, 7, 8, 7, 2, 6, 4, 9, 8], 3], [[1, 5, 3, 8, 7, 2, 6, 9], 2], [[8, 1, 5, 8, 7, 2, 6, 4], 3], [[4, 5, 3, 8, 8, 2, 6, 4], 4], [[1, 5, 3, 8, 7, 2, 6, 4, 9], 0], [[1, 5, 4, 3, 8, 7, 2, 6, 7, 9], 4], [[True, False, False, True, False, False, False, True, True], 0], [[1, 5, 5, 9, 8, 7, 2, 6, 4, 9], 5], [[1, 5, 3, 8, 7, 6, 4], 4], [[1, 6, 3, 7, 8, 7, 2, 6, 6, 4, 9], 7], [[1, 6, 3, 7, 8, 7, 2, 6, 6, 4, 9], 9], [[4, 5, 3, 8, 5, 2, 6, 4], 8], [[1, 5, 3, 8, 7, 2, 6, 4, 10], 5], [[1, 5, 3, 8, 7, 4, 6, 4], 4], [[1, 6, 3, 7, 8, 7, 2, 6, 4, 9], 7], [[1, 5, 3, 8, 7, 2, 6, 4, 9, 1], 0], [[1, 5, 3, 8, 1, 4, 6, 4], 4], [[8, 1, 5, 8, 7, 2, 4], 3], [[3, 5, 3, 8, 8, 2, 6, 4, 2], 9], [[1, 4, 3, 8, 7, 2, 6, 4, 9], 7], [[1, 5, 3, 8, 7, 2, 6, 9, 9], 4], [[1, 5, 3, 8, 7, 2, 6, 9, 9], 5], [[1, 6, 3, 7, 8, 7, 2, 6, 6, 4, 9], 3], [[1, 5, 8, 7, 2, 6, 4, 9], 3], [[1, 5, 3, 8, 2, 6, 4, 9], 0], [[6, 3, 7, 8, 7, 6, 4, 9, 8], 3], [[1, 6, 3, 7, 8, 7, 2, 95, 6, 4, 9], 5], [[1, 5, 3, 8, 7, 2, 6, 4, 9, 7], 5], [[1, 3, 8, 7, 2, 7, 4, 9], 4], [[7, 2, 1], 2], [[1, 1, 2, 3, 8, 7, 2, 6, 9, 7], 6], [[1, 5, 3, 8, 7, 2, 6, 4, 95, 9, 7], 5], [[3, 5, 3, 8, 8, 2, 6, 4], 2], [[1, 5, 3, 8, 7, 2, 6, 5, 95, 9, 7], 10], [[1, 4, 8, 7, 2, 6, 4, 9], 8], [[3, 1, 5, 3, 8, 7, 2, 6, 4, 9], 5], [[1, 5, 3, 8, 7, 2, 6, 9, 9], 3], [[1, 5, 3, 8, 2, 6, 9, 9], 4], [[1, 1, 3, 8, 7, 2, 6, 4, 9, 1], 5], [[1, 1, 3, 8, 7, 2, 4, 9, 1], 5], [[8, 1, 5, 8, 7, 2, 6, 4], 2], [[1, 6, 3, 7, 8, 7, 2, 6, 4, 9], 8], [[4, 5, 3, 8, 7, 2, -20, 7, 4], 8], [[3, 72, 2, 1], 2], [[7, 7, 1], 2], [[5, 96, 81, -20, 8, 6], 0], [[1, 1, 2, 3, 8, 7, 2, 6, 9, 7], 9], [[1, 3, 8, 7, 2, 6, 4, 95, 9, 7], 5], [[1, 3, 8, 7, 2, 6, 95, 9, 7], 5], [[1, 5, 4, 3, 8, 7, 10, 2, 6, 7, 9], 4], [[1, 5, 5, 9, 8, 7, 2, 6, 4, 9], 3], [[3, 1, 5, 3, 8, 7, 2, 6, 4, 9], 6], [[1, 5, 3, 8, 7, 2, 6, 5, 95, 9, 7], 5], [[4, 5, 3, 8, 8, 2, 6, 4], 1], [[1, 1, 2, 3, 8, 7, 2, 6, 9, 7, 3], 6], [[1, 5, 3, 8, 7, 4], 3], [[1, 5, 5, 9, 8, 8, 7, 2, 6, 4, 9], 4], [[1, 1, 6, 3, 7, 8, 7, 2, 6, 6, 4, 9], 9], [[True, False, False, True, False, False, False, True, True], 6], [[4, 5, 3, 8, 7, 2, 6, 4], 1], [[1, 8, 7, 2, 6, 4, 9], 4], [[1, 5, 4, 3, 8, 7, 10, 2, 6, 7, 9, 9], 4], [[3, 5, 3, 8, 8, 2, 6, 4], 6], [[3, 5, 3, 8, 8, 2, 6, 4], 7], [[1, 4, 0, 8, 7, 2, 6, 4, 9], 4], [[1, 5, 3, 8, 7, 2, 6, 4, 9, 7], 3], [[1, 5, 3, 8, 4, 7, 2, 6, 4, 9], 0], [[1, 1, 6, 3, 7, 8, 7, 2, 6, 6, 4, 9], 3], [[1, 5, 3, 8, 7, 4, 5], 6], [[1, 5, 3, 8, 7, 2, 6, 4, 9, 1, 6], 5], [[1, 5, 3, 8, 5, 7, 4], 3], [[1, 5, 3, 8, 7, 2, 6, 4, 95, 9, 1, 7], 5], [[1, 5, 5, 9, 8, 8, 7, 2, 6, 95, 9], 4], [[1, 5, 5, 9, 8, 8, 7, 2, 6, 4, 9], 3]]
results = [[100, 90], [100, 90, 80, 70, 60], [100, 90, 80], [9, 8, 7, 6], [3, 2], [], [], [9, 8, 7, 6], [8, 7, 6, 5], [8, 7, 6, 5], [8, 6, 5, 5], [9, 8, 7, 6, 5], [9, 8, 7, 6, 5], [8, 8, 7], [9, 8, 7, 7], [9, 8, 7, 6], [8, 2], [8, 7, 6], [9], [2, 1], [9, 8, 7], [9, 8, 7], [9, 8, 7, 7], [9, 8, 7, 6, 5], [8, 8, 6], [9, 8, 7], [8, 7, 6, 5, 4, 4, 3, 2], [9, 8, 7, 7], [9, 8, 7, 6], [8, 8, 6], [9, 8, 7, 6, 5, 4], [9, 8, 8], [9, 8, 8], [9, 8], [8, 8, 7], [8, 8, 6, 5], [], [9, 8, 7, 7], [], [9, 9, 8, 7, 6], [8, 7, 6, 5], [9, 8, 7, 7, 6, 6, 6], [9, 8, 7, 7, 6, 6, 6, 4, 3], [8, 6, 5, 5, 4, 4, 3, 2], [10, 8, 7, 6, 5], [8, 7, 6, 5], [9, 8, 7, 7, 6, 6, 4], [], [8, 6, 5, 4], [8, 8, 7], [8, 8, 6, 5, 4, 3, 3, 2, 2], [9, 8, 7, 6, 4, 4, 3], [9, 9, 8, 7], [9, 9, 8, 7, 6], [9, 8, 7], [9, 8, 7], [], [9, 8, 8], [95, 9, 8, 7, 7], [9, 8, 7, 7, 6], [9, 8, 7, 7], [7, 2], [9, 8, 7, 7, 6, 3], [95, 9, 8, 7, 7], [8, 8], [95, 9, 8, 7, 7, 6, 5, 5, 3, 2], [9, 8, 7, 6, 4, 4, 2, 1], [9, 8, 7, 6, 5], [9, 9, 8], [9, 9, 8, 6], [9, 8, 7, 6, 4], [9, 8, 7, 4, 3], [8, 8], [9, 8, 7, 7, 6, 6, 4, 3], [8, 7, 7, 5, 4, 4, 3, 2], [72, 3], [7, 7], [], [9, 8, 7, 7, 6, 3, 2, 2, 1], [95, 9, 8, 7, 7], [95, 9, 8, 7, 7], [10, 9, 8, 7], [9, 9, 8], [9, 8, 7, 6, 5, 4], [95, 9, 8, 7, 7], [8], [9, 8, 7, 7, 6, 3], [8, 7, 5], [9, 9, 8, 8], [9, 8, 7, 7, 6, 6, 6, 4, 3], [True, True, True, True, False, False], [8], [9, 8, 7, 6], [10, 9, 9, 8], [8, 8, 6, 5, 4, 3], [8, 8, 6, 5, 4, 3, 3], [9, 8, 7, 6], [9, 8, 7], [], [9, 8, 7], [8, 7, 5, 5, 4, 3], [9, 8, 7, 6, 6], [8, 7, 5], [95, 9, 8, 7, 7], [95, 9, 9, 8], [9, 9, 8]]

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
        func_name = "larg_nnum"
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
        for test_case in ['assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2))==set([100,90])', 'assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5))==set([100,90,80,70,60])', 'assert set(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3))==set([100,90,80])']:
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
