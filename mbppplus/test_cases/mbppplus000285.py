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
inputs = [[[1, 3, 6, 13, 17, 18]], [[10, 5, 3, 15, 20]], [[18, 1, 3, 6, 13, 17]], [[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]], [[11, 22, 33, 44, 55, 66, 77, 88, 99, 110]], [[9, 4, 12, 7, 16, 3, 11, 8, 5, 13]], [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]], [[2, 99, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 79, 83, 89, 97]], [[11, 22, 44, 33, 44, 55, 66, 77, 88, 99, 110, 22, 44]], [[2, 31, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 30, 79, 83, 89, 97]], [[2, 99, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 5, 79, 83, 89, 97]], [[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 987]], [[2, 3, 4, 5, 6, 7, 8, 29, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], [[2, 3, 4, 5, 6, 8, 29, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 23]], [[2, 99, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97]], [[2, 31, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 30, 79, 83, 89, 16]], [[2, 3, 5, 7, 11, 13, 18, 19, 16, 23, 29, 31, 22, 37, 23, 7]], [[9, 4, 12, 9, 7, 16, 3, 10, 8, 5, 13]], [[2, 5, 7, 11, 13, 17, 19, 29, 31, 37]], [[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2583]], [[11, 22, 33, 44, 55, 66, 77, 15, 99, 110]], [[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 987, 2584]], [[2, 99, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 7]], [[9, 3, 12, 7, 16, 3, 11, 8, 4, 13, 13]], [[2, 99, 19, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97]], [[11, 21, 33, 44, 55, 66, 77, 88, 99, 110]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 7, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 2]], [[47, 4, 12, 9, 7, 16, 3, 10, 8, 5, 13]], [[34, 55, 35, 89, 144, 233, 377, 610, 987, 1597, 2584, 987, 987]], [[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 987, 2584, 2584]], [[9, 3, 12, 3, 7, 16, 3, 11, 8, 8, 4, 13, 13]], [[2, 3, 4, 5, 6, 8, 29, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 21]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 7, 43, 47, 53, 59, 61, 67, 71, 73, 83, 89, 97, 2]], [[2583, 9, 4, 12, 9, 7, 16, 3, 10, 8, 5, 13]], [[2, 5, 7, 11, 13, 17, 3, 19, 29, 31, 37]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]], [[83, 34, 55, 89, 144, 377, 610, 987, 1597, 2584, 987]], [[2, 5, 7, 11, 13, 17, 19, 18, 29, 31, 37]], [[2, 3, 2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 23]], [[9, 3, 12, 7, 16, 3, 11, 8, 4, 13, 13, 7]], [[2, 3, 5, 7, 11, 13, 17, 12, 19, 23, 29, 31, 37, 23]], [[9, 4, 12, 9, 7, 16, 3, 10, 8, 8, 5, 13, 9, 16]], [[11, 21, 44, 55, 66, 77, 88, 99, 110]], [[2, 3, 5, 7, 11, 13, 18, 19, 16, 23, 29, 31, 22, 37, 23, 7, 7]], [[2, 3, 4, 5, 6, 8, 29, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 21]], [[11, 21, 44, 55, 66, 77, 88, 99, 110, 66]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 47, 61, 67, 71, 73, 79, 83, 89, 97, 5]], [[2, 5, 7, 11, 13, 18, 19, 18, 29, 31, 37]], [[2, 99, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 79]], [[9, 3, 12, 3, 7, 16, 3, 3, 11, 8, 8, 4, 13, 13]], [[83, 34, 55, 89, 144, 377, 610, 987, 1597, 2584, 89, 34, 987]], [[2583, 9, 4, 33, 12, 9, 7, 16, 3, 10, 8, 5, 13]], [[2, 3, 5, 7, 11, 13, 18, 19, 16, 23, 29, 31, 22, 35, 37, 23, 7]], [[47, 4, 6, 12, 9, 7, 16, 3, 10, 8, 5, 13]], [[2, 3, 4, 5, 6, 8, 29, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 20, 26, 27, 28, 29, 30, 21]], [[9, 4, 12, 8, 7, 16, 3, 10, 8, 8, 5, 13, 9, 16]], [[2, 99, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 79, 59]], [[11, 21, 33, 44, 55, 66, 77, 99, 110]], [[9, 4, 12, 7, 7, 16, 3, 11, 8, 5, 13, 3, 5, 9]], [[2, 3, 4, 5, 6, 8, 29, 20, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 20, 26, 27, 28, 29, 30, 21]], [[2, 99, 5, 7, 11, 17, 19, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97]], [[2, 99, 19, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 47]], [[7, 21, 33, 44, 55, 66, 77, 99]], [[2, 31, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 74, 30, 83, 89, 16]], [[11, 21, 33, 28, 44, 55, 66, 77, 99, 110]], [[9, 10, 8, 7, 16, 3, 10, 8, 8, 5, 13, 9, 16, 3]], [[2, 99, 19, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 18, 67, 71, 5, 79, 83, 89, 97]], [[2583, 9, 4, 9, 33, 12, 9, 7, 16, 3, 10, 8, 5, 13]], [[2, 31, 3, 89, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 30, 79, 83, 89, 97]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 7, 43, 47, 53, 59, 61, 67, 71, 73, 83, 89, 97, 2]], [[2583, 9, 4, 33, 12, 9, 7, 66, 3, 10, 8, 5, 13]], [[2, 3, 4, 5, 6, 7, 8, 29, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 19]], [[3, 12, 3, 7, 16, 3, 3, 11, 8, 8, 4, 13, 13]], [[2, 99, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 79, 83, 89, 97, 61]], [[2, 31, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 30, 79, 83, 89, 16, 3]], [[83, 34, 55, 89, 89, 144, 377, 610, 987, 1597, 2584, 89, 34, 987]], [[13, 11, 21, 44, 55, 66, 77, 88, 99, 56, 110]], [[2, 3, 5, 7, 11, 17, 19, 23, 29, 31, 37]], [[9, 3, 12, 3, 7, 16, 3, 11, 8, 8, 4, 13, 13, 7, 3]], [[34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 233]], [[2, 3, 4, 5, 6, 8, 29, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 21]], [[2, 3, 4, 5, 6, 7, 8, 29, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 19, 20]], [[2, 99, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 5, 79, 83, 89, 97, 53]], [[2, 99, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 79, 6, 59]], [[3, 12, 7, 16, 3, 3, 11, 8, 8, 4, 13, 13]], [[2, 99, 5, 7, 11, 17, 19, 23, 42, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 5]], [[2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 7, 43, 47, 53, 59, 61, 67, 71, 73, 83, 89, 97, 2]], [[16, 11, 21, 33, 44, 13, 66, 77, 99, 110]], [[11, 22, 44, 33, 44, 55, 66, 77, 88, 99, 110, 22, 44, 44]], [[2, 3, 4, 5, 6, 8, 29, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 27, 28, 29, 30, 21]], [[2, 99, 19, 5, 7, 11, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 67, 71, 5, 79, 83, 89, 97, 47, 31]], [[2, 3, 5, 7, 11, 17, 34, 23, 29, 31, 37, 5, 5]], [[11, 21, 33, 44, 55, 77, 88, 99, 110]], [[11, 21, 44, 55, 66, 77, 42, 88, 99, 110, 66]], [[2583, 9, 4, 33, 12, 9, 7, 66, 3, 10, 8, 5, 13, 9]], [[2, 31, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 30, 79, 83, 89, 96]], [[11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 22, 44]], [[2583, 9, 4, 33, 12, 9, 7, 16, 3, 8, 10, 8, 5, 13]], [[11, 21, 33, 44, 55, 77, 88, 99, 110, 110]], [[2, 3, 5, 7, 11, 13, 17, 19, 22, 29, 31, 37, 7, 43, 47, 54, 59, 67, 71, 73, 79, 83, 89, 97, 2]], [[2, 3, 5, 7, 11, 17, 19, 23, 29, 31, 37, 37]], [[47, 4, 12, 9, 9, 16, 3, 10, 8, 5, 13]], [[11, 21, 44, 55, 41, 66, 77, 88, 99, 66, 110, 66, 66]], [[2, 99, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 79, 24, 83, 89, 97]], [[7, 21, 33, 44, 66, 55, 66, 77, 99]], [[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 7, 43, 47, 53, 59, 61, 67, 13, 73, 83, 89, 97, 2]]]
results = [4, 3, 4, 2, 4, 3, 4, 1, 1, 2, 7, 2, 2, 2, 4, 4, 2, 2, 2, 2, 3, 1, 1, 3, 3, 2, 4, 2, 3, 2, 3, 3, 4, 5, 4, 2, 4, 1, 1, 2, 2, 2, 4, 2, 5, 3, 3, 4, 3, 2, 3, 2, 6, 3, 4, 3, 3, 4, 6, 2, 3, 5, 6, 2, 2, 2, 2, 3, 5, 2, 5, 2, 2, 4, 4, 5, 2, 3, 3, 3, 1, 6, 2, 4, 4, 2, 2, 4, 3, 2, 3, 8, 4, 2, 3, 3, 3, 5, 2, 6, 4, 4, 3, 2, 3, 5, 2, 3, 2]

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
        func_name = "largest_subset"
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
        for test_case in ['assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4', 'assert largest_subset([10, 5, 3, 15, 20]) == 3', 'assert largest_subset([18, 1, 3, 6, 13, 17]) == 4']:
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
