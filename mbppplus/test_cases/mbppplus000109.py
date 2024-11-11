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
inputs = [[10, 4], [5, 2], [16, 3], [100, 10], [50, 5], [20, 8], [200, 6], [20, 20], [199, 6], [49, 6], [5, 6], [200, 100], [5, 5], [49, 49], [49, 50], [199, 20], [50, 6], [50, 49], [199, 8], [10, 8], [49, 5], [20, 5], [49, 20], [7, 6], [20, 10], [8, 200], [8, 5], [11, 10], [200, 200], [6, 6], [50, 50], [49, 199], [199, 199], [5, 20], [11, 7], [11, 12], [200, 20], [50, 201], [9, 8], [100, 100], [8, 10], [100, 6], [200, 50], [198, 100], [10, 10], [8, 9], [9, 9], [12, 11], [51, 6], [20, 6], [8, 8], [201, 50], [9, 10], [10, 9], [9, 6], [49, 200], [201, 201], [20, 21], [6, 201], [202, 202], [21, 21], [20, 200], [200, 202], [198, 20], [5, 100], [21, 12], [7, 8], [198, 101], [8, 6], [198, 198], [9, 50], [198, 199], [8, 51], [10, 5], [51, 21], [199, 101], [4, 50], [50, 198], [13, 13], [52, 51], [8, 7], [5, 9], [7, 101], [202, 7], [6, 7], [49, 7], [201, 52], [12, 7], [12, 8], [51, 202], [12, 12], [7, 7], [100, 101], [13, 12], [201, 200], [6, 200], [202, 9], [202, 12], [12, 9], [199, 50], [9, 201], [101, 100], [9, 51], [13, 100], [202, 52], [5, 50], [20, 51]]
results = [4, 6, 84, 0, 2264, 0, 2598596, 0, 2519482, 238, 0, 0, 0, 0, 0, 0, 284, 0, 42774, 0, 2028, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35484, 0, 0, 0, 0, 0, 0, 330, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1015208, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        func_name = "get_total_number_of_sequences"
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
        for test_case in ['assert get_total_number_of_sequences(10, 4) == 4', 'assert get_total_number_of_sequences(5, 2) == 6', 'assert get_total_number_of_sequences(16, 3) == 84']:
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
