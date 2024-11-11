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
inputs = [[[1, 2, 3, 4]], [[4, 5, 12]], [[9, 2, 3]], [[9, 5, 3, 8, 1, 2, 4, 7, 6]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 8]], [[9, 5, 3, 8, 1, 2, 7, 6]], [[9, 5, 3, 8, 1, 2, 7, 9, 6, 8, 7, 6]], [[9, 5, 3, 8, 5, 1, 2, 4, 7, 6]], [[9, 5, 2, 3, 8, 1, 2, 7, 6, 1]], [[9, 5, 3, 8, 1, 2, 4, 6]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 8]], [[9, 5, 3, 8, 0, 2, 7, 7, 6, 8]], [[9, 5, 3, 8, 1, 4, 4, 7, 6]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 8, 2]], [[9, 5, 3, 8, 0, 7, 7, 6, 8]], [[9, 3, 5, 2, 3, 8, 1, 2, 7, 6, 1]], [[9, 5, 3, 8, 1, 2, 7, 5]], [[9, 3, 5, 8, 2, 3, 7, 8, 1, 2, 7, 6, 1]], [[9, 3, 8, 1, 2, 4, 7, 6, 8]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 8, 1]], [[9, 3, 8, 0, 7, 7, 6, 8]], [[9, 5, 3, 8, 1, 4, 4, 7, 6, 8]], [[9, 5, 1, 3, 8, 1, 2, 7, 6]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 8, 8]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 8, 5]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 9, 2]], [[9, 10, 5, 3, 8, 1, 2, 4, 6]], [[9, 5, 3, 8, 1, 6, 4, 5, 6, 8]], [[9, 5, 3, 8, 2, 2, 4, 6]], [[9, 5, 3, 8, 4, 4, 7, 6]], [[9, 5, 3, 8, 4, 4, 7, 6, 5]], [[9, 5, 2, 3, 8, 1, 2, 7, 6, 1, 2]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 9]], [[9, 5, 2, 3, 8, 1, 4, 4, 8, 6]], [[9, 3, 5, 8, 2, 3, 7, 8, 1, 2, 7, 5, 1]], [[9, 5, 3, 8, 0, 7, 7, 6, 8, 6]], [[9, 5, 3, 1, 8, 1, 2, 4, 2]], [[9, 3, 8, 10, 2, 4, 7, 6, 9, 8]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 8, 2]], [[9, 3, 3, 8, 2, 2, 4, 6]], [[9, 1, 5, 3, 8, 1, 2, 2, 7, 6, 8, 2]], [[9, 5, 1, 3, 8, 1, 2, 7, 6, 3]], [[9, 5, 3, 8, 1, 6, 4, 5, 6, 8, 3]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 8, 9, 1]], [[9, 3, 8, 8, 1, 2, 4, 7, 8, 8]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 8, 8, 9]], [[9, 5, 4, 8, 1, 2, 4, 7, 6, 8, 1]], [[2, 9, 5, 3, 8, 6, 4, 5, 6, 8]], [[9, 5, 2, 8, 1, 4, 4, 8]], [[8, 1, 3, 8, 1, 2, 7, 6]], [[9, 6, 3, 9, 8, 1, 2, 2, 7, 6, 8, 5]], [[9, 5, 2, 8, 4, 4, 8]], [[9, 10, 5, 3, 8, 1, 4, 6, 6]], [[9, 5, 3, 3, 8, 1, 4, 4, 7, 6, 8, 5]], [[9, 5, 3, 9, 8, 1, 2, 2, 7, 6, 8, 9, 1]], [[10, 7, 3, 8, 2, 4, 6]], [[9, 3, 4, 8, 2, 2, 4, 7, 6, 8, 1]], [[9, 6, 3, 9, 8, 1, 2, 2, 8, 7, 6, 8, 5]], [[9, 5, 3, 8, 1, 3, 4, 4, 6, 8, 1]], [[9, 3, 3, 8, 2, 2, 6]], [[9, 3, 3, 8, 2, 2, 3, 6]], [[9, 2, 5, 2, 3, 8, 1, 2, 7, 6, 1, 2]], [[9, 5, 1, 8, 3, 8, 1, 2, 7, 6]], [[1, 9, 5, 3, 8, 1, 2, 4, 6]], [[9, 5, 1, 3, 8, 1, 2, 7, 6, 1, 2]], [[9, 8, 8, 1, 2, 4, 2, 7, 8, 8, 7]], [[9, 1, 5, 4, 8, 1, 2, 2, 7, 6, 8, 2]], [[9, 5, 3, 8, 1, 2, 7, 9, 6, 6, 8, 7, 6]], [[9, 5, 2, 3, 8, 1, 4, 4, 8, 6, 8]], [[9, 5, 8, 2, 7, 9, 6, 8, 7, 6, 6]], [[10, 5, 3, 8, 5, 1, 2, 4, 7, 6]], [[9, 5, 3, 8, 1, 2, 4, 7, 6, 6, 9]], [[9, 5, 1, 8, 1, 5, 2, 4, 2]], [[9, 3, 8, 10, 2, 8, 7, 6, 8]], [[9, 9, 5, 3, 8, 4, 4, 7, 6]], [[9, 3, 5, 0, 8, 1, 2, 7, 5]], [[9, 5, 3, 8, 1, 4, 4, 7, 6, 8, 6]], [[9, 5, 3, 8, 1, 4, 4, 7, 6, 4]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 9, 2, 9]], [[9, 3, 4, 2, 2, 2, 4, 7, 6, 8, 1, 9]], [[9, 5, 3, 2, 1, 2, 2, 7, 8, 9, 1]], [[9, 5, 8, 2, 3, 7, 8, 1, 2, 7, 6, 1]], [[9, 5, 8, 1, 2, 4, 6]], [[7, 3, 8, 2, 4, 6]], [[9, 5, 2, 4, 8, 1, 3, 2, 7, 6, 1]], [[9, 5, 3, 8, 2, 1, 2, 2, 7, 6, 8, 5]], [[7, 3, 7, 2, 4]], [[9, 5, 3, 8, 1, 2, 2, 7, 6, 8, 9, 1, 1]], [[9, 5, 3, 8, 2, 2, 7, 6, 8, 10, 1, 1]], [[9, 5, 3, 8, 4, 4, 7, 6, 7]], [[9, 3, 5, 7, 8, 2, 3, 7, 8, 1, 2, 7, 5, 1]], [[9, 5, 3, 8, 1, 2, 1, 7, 8, 1]], [[9, 5, 3, 8, 2, 2, 4, 6, 2]], [[9, 3, 8, 1, 2, 5, 7, 6, 8]], [[9, 5, 2, 4, 1, 8, 10, 2, 4, 2]], [[9, 5, 3, 8, 0, 7, 7, 6, 8, 8]], [[9, 3, 5, 0, 8, 2, 3, 7, 8, 1, 2, 7, 6, 1]], [[9, 5, 3, 8, 1, 4, 7, 6, 8, 6]], [[10, 7, 3, 8, 2, 4, 5]], [[9, 5, 3, 8, 1, 2, 2, 6, 8, 9, 1, 1]], [[9, 5, 3, 8, 1, 2, 2, 6, 0, 9, 1, 1]], [[9, 5, 2, 8, 1, 9, 4, 4, 8]], [[9, 3, 8, 0, 7, 7, 6]], [[10, 9, 5, 3, 9, 8, 1, 2, 2, 7, 6, 8, 9, 1]]]
results = [3, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 8, 8, 9, 8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 9, 8, 7, 6, 6, 8, 8, 8, 8, 9, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 7, 8, 7, 8, 7, 9, 8, 8, 8, 8, 8, 8, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 9, 8, 8, 8, 6, 9, 8, 8, 8, 8, 8, 8, 8, 6, 8, 8, 5, 8, 9, 6, 8, 8, 7, 8, 9, 9, 9, 8, 8, 8, 9, 8, 9, 9]

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
        func_name = "big_diff"
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
        for test_case in ['assert big_diff([1,2,3,4]) == 3', 'assert big_diff([4,5,12]) == 8', 'assert big_diff([9,2,3]) == 7']:
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
