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
inputs = [[10, 3], [4, 2], [20, 5], [0, 5], [0, 1], [-1, 1], [1, 1], [0, 2], [5, 1], [6, 1], [-1, -1], [0, -1], [2, 1], [5, 5], [2, 2], [6, 6], [2, 5], [1, 6], [2, 4], [1, -1], [6, 5], [6, 2], [7, 7], [-1, 2], [5, 6], [-2, 2], [7, 4], [1, 2], [1, 7], [0, 4], [4, -1], [2, -2], [7, 6], [0, -2], [7, -1], [-2, 3], [3, 3], [5, -1], [-2, 6], [-2, -2], [7, 5], [6, -2], [-2, -1], [6, 4], [6, -1], [3, 5], [0, 7], [4, 5], [5, -2], [0, 6], [1, 4], [3, -1], [2, 3], [4, 4], [2, 6], [7, 1], [6, 7], [3, 4], [3, -2], [1, 5], [-1, 3], [3, 1], [-2, 1], [-2, 7], [2, -1], [5, 4], [0, 3], [-3, 1], [41, 41], [-2, 4], [5, 7], [5, 3], [-2, -3], [-1, 7], [-3, -3], [8, 4], [-3, -2], [4, 41], [-4, -2], [-4, 3], [4, -2], [8, -2], [-1, 6], [41, -1], [40, 41], [5, 41], [-4, 4], [-4, -4], [40, 5], [0, 8], [1, -2], [1, 41], [-3, 6], [8, 2], [8, 8], [-3, 7], [39, 8], [2, 8], [4, 6], [39, 3], [-3, -4], [41, 4], [41, -3]]
results = [3, 2, 4, 0, 0, -1, 1, 0, 5, 6, 1, 0, 2, 1, 1, 1, 0, 0, 0, -1, 1, 3, 1, -1, 0, -1, 1, 0, 0, 0, -4, -1, 1, 0, -7, -1, 1, -5, -1, 1, 1, -3, 2, 1, -6, 0, 0, 0, -3, 0, 0, -3, 0, 1, 0, 7, 0, 0, -2, 0, -1, 3, -2, -1, -2, 1, 0, -3, 1, -1, 0, 1, 0, -1, 1, 2, 1, 0, 2, -2, -2, -4, -1, -41, 0, 0, -1, 1, 8, 0, -1, 0, -1, 4, 1, -1, 4, 0, 0, 13, 0, 10, -14]

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
        func_name = "find"
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
        for test_case in ['assert find(10,3) == 3', 'assert find(4,2) == 2', 'assert find(20,5) == 4']:
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
