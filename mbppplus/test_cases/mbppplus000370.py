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
inputs = [[1, 1, 1], [-1, -2, -3], [1, 2, 2], [1, 2, 3], [10, 10, 20], [-5, 0, 5], [100, 99, 101], [7, 7, 7], [10000000000, 9999999999, 10000000000], [9999999999, 9999999999, 10000000000], [100, 100, 100], [9876543210, 1234567890, 9876543210], [9999999999, 9999999999, 9999999999], [9876543210, 9876543210, 9876543210], [8, 7, 7], [9999999999, 3, 9999999999], [99, 10000000000, 9999999999], [9876543210, 5, 9876543210], [100, 6, 9876543210], [99, 6, 9999999999], [8, 7, 100], [-5, -5, 5], [99, 0, 9999999999], [99, 10, 2], [9999999999, 101, 6], [100, 7, 100], [8, -5, 100], [1234567890, 1, 1234567890], [7, 10000000000, 9999999999], [1, 101, 6], [100, 8, 9999999999], [1, 2, 4], [8, 9999999999, 9999999999], [100, 5, 101], [101, 99, 101], [3, 10, 2], [-5, -5, 6], [1234567890, 7, 7], [100, 9999999999, 9999999999], [3, 3, 2], [-5, 6, -5], [5, 9876543210, 9876543210], [-4, -5, 6], [10000000000, 9999999998, 10000000000], [9999999999, 9999999999, 10000000001], [98, 10, 2], [10000000000, 9999999999, 10000000001], [8, 7, 6], [7, 7, 6], [5, 6, 5], [1, 3, 6], [4, 100, 99], [9876543209, 5, 9876543210], [100, 9876543210, 6], [1234567890, 1, 1], [0, 0, 5], [-5, 9876543210, 8], [100, 8, -4], [98, 9876543210, 6], [9999999999, 6, 10000000001], [100, 99, 6], [6, 100, 7], [100, 9999999999, 9999999998], [101, 6, 101], [9999999999, 100, 6], [6, 5, 5], [99, 100, 9999999999], [2, -5, 6], [98, 100, 100], [9876543210, 1, 1], [98, -5, 5], [7, 7, 9876543210], [10000000001, 100, 100], [-5, 100, 9999999997], [4, 9999999999, 9999999999], [97, -5, 97], [98, 3, 4], [8, 98, 6], [9876543209, 97, 1], [-1, 0, 5], [4, 10, 100], [101, 10000000000, 10000000001], [9876543209, 97, 9876543209], [2, 9876543210, 3], [6, 7, 7], [6, 7, 2], [98, -5, -5], [-6, 100, 9999999997], [9876543210, 0, 1], [6, -5, -5], [-4, 8, 6], [6, 5, 6], [9999999998, -76, 8], [100, 10000000000, 9999999999], [100, 9999999998, 100], [9876543209, 9876543210, 9876543210], [9999999998, 1, 9999999998], [10, 20, -1], [0, 5, 5], [8, 8, 6], [8, 7, 10000000000], [-4, -5, -5], [8, 97, 6], [-4, 100, 101], [5, 0, 0], [98, 5, 5], [8, 9876543209, 9876543210], [5, 6, 10], [1234567891, 1, 1], [100, -4, 100], [20, 9999999999, 9999999999], [100, 8, 100], [9999999998, 10000000000, 9999999998]]
results = [3, 0, 2, 0, 2, 0, 0, 3, 2, 2, 3, 2, 3, 3, 2, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 2, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 2, 2]

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
        func_name = "test_three_equal"
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
        for test_case in ['assert test_three_equal(1,1,1) == 3', 'assert test_three_equal(-1,-2,-3) == 0', 'assert test_three_equal(1,2,2) == 2']:
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
