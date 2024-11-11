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
inputs = [[[1, 2, 3, 3, 3, 3, 10], 7, 3], [[1, 1, 2, 4, 4, 4, 6, 6], 8, 4], [[1, 1, 1, 2, 2], 5, 1], [[], 0, 1], [[], 1, 0], [[], 1, 1], [[], 0, 0], [[], 0, -1], [[True], 1, 2], [[], 2, 0], [[], 2, -1], [[], 2, 2], [[], 1, 2], [[], 2, 1], [[], 0, 2], [[52], 2, 0], [[], 1, -1], [[52], 2, 2], [[], 3, 2], [[], 52, 2], [[], 53, 2], [[], 52, 1], [[], 52, 53], [[True], 2, 2], [[52], 3, 2], [[], 52, 52], [[], 53, 53], [[], 52, -1], [[], 3, 0], [[], 53, 3], [[], 52, 0], [[], 2, 53], [[52, 52], 3, 2], [[52, 52], 4, 2], [[52], 3, 0], [[], 4, 1], [[52, 52, 52], 52, 2], [[52, 52], 53, 53], [[52, 52, 52, 52], 52, 2], [[52, 52, 52], 53, 53], [[52], 2, 1], [[52, 52], 2, -1], [[], 52, 4], [[], 3, -1], [[52, 52], 52, 52], [[52], 53, 53], [[28.804254987535558], 3, 3], [[], 4, -1], [[], 3, 3], [[52, 52, 52], 52, 3], [[], 4, 4], [[53], 3, 3], [[], 4, 53], [[28.804254987535558], 53, 2], [[28.804254987535558], 4, 2], [[True], 52, 2], [[True], 53, 2], [[28.804254987535558], 4, 3], [[], 54, 53], [[25.39355163010451], 54, 3], [[True], 2, 1], [[], 2, 3], [[True], 2, 0], [[True], 54, 0], [[52, 52], 52, 53], [[52], 1, 4], [[], 54, -1], [[52, 52], 53, 2], [[53], 3, 2], [[], 54, 2], [[], 4, 2], [[25.39355163010451], 3, 3], [[], 3, 53], [[53], 4, 3], [[True], 2, 3], [[28.804254987535558, 28.804254987535558], 4, 3], [[True, True], 53, 52], [[], 53, 52], [[True, True], 4, 4], [[True, True], 3, 4], [[52], 1, 2], [[False, False, True], 52, 52], [[28.804254987535558, 28.804254987535558], 2, 4], [[52, 52, 52, 52], 52, 1], [[51, 52, 52], 52, 53], [[28.804254987535558], 5, 2], [[52, 52, 52, 52], 52, 0], [[], 3, 4], [[True], 52, 53], [[True, True, True], 53, 2], [[True, True, True], 4, 4], [[True, True], 54, 0], [[52, 52, 52], 51, 51], [[28.804254987535558, 28.804254987535558], 53, 2], [[True], 2, 4], [[23.860250214479723], 52, 2], [[28.804254987535558], 5, 1], [[True], 54, 4], [[52], 3, 3], [[28.804254987535558], 5, 3], [[28.804254987535558, 28.804254987535558], 53, 53], [[52, 52], 53, 54], [[52, 52], 52, 54], [[52], 4, 3]]
results = [True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "is_majority"
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
        for test_case in ['assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True', 'assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False', 'assert is_majority([1, 1, 1, 2, 2], 5, 1) == True', 'assert is_majority([1, 1, 2, 2], 5, 1) == False']:
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
