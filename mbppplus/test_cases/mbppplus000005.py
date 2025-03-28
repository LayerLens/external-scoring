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
inputs = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[10, 20, 30]], [[12, 15]], [[]], [[-3, -2, -1, 0, 1, 2, 3]], [[9, 17, 5, 23, 10, 13, 19, 7, 2, 4]], [[-2, 17, 5, 23, 10, 13, 19, 7, 2, 4]], [[17, -3, -2, -1, 0, 1, 2, 3]], [[-2, 17, 5, 24, 10, 13, 19, 7, 2, 4]], [[-3, -2, -1, 0, 1, 2]], [[17, -3, -2, 1, 0, 1, 2, 3]], [[-3, -2, -1, 0, 1, 7, 2, 3]], [[-3, 1, -1, 0, 1, 2, 3]], [[17, -2, 1, -92, -36, 69, 18]], [[17, -2, 1, -92, -36, 69, 18, -36]], [[-3, 1, -1, 0, 1, 2, 3, 1]], [[False, True, False, True, False, True, True, True, False, False, False]], [[17, -3, -2, -1, 0, 1, 69, 3]], [[17, 4, -2, -1, 0, 1, 10, 3]], [[9, 17, 23, 10, 13, 19, 7, 7, 2, 4]], [[9, 17, 23, 10, 13, 19, 7, 7, 2, 9]], [[15, 17, -2, 1, -92, -36, 69, 18]], [[17, 1, 1, -92, -36, 69, 18, 17]], [[17, -3, -2, -1, 0, 1, 69, 17, 3]], [[-3, -2, -1, 0, 2, 1]], [[17, -2, 1, 1, -36, 69, 18]], [[-3, -2, -1, 0, 1, 69, 17, 3, -2]], [[-2, 17, 5, 24, 13, 19, 7, 2, 4]], [[False, True, False, True, False, True, True, True, False, False]], [[17, -2, 1, 1, -36, 18]], [[9, 17, 5, 12, 23, 10, 13, 19, 7, 2, 4]], [[17, -2, 1, -92, 18, -36, 17, -2]], [[17, -3, -2, -1, 0, 1, 2, 2, 3]], [[17, -2, 1, -92, -36, 69, 18, 17]], [[-2, 17, 24, 13, 19, 7, 2, 4]], [[24, 9, 17, 5, 12, 23, 10, 13, 19, 7, 2, 4]], [[17, -3, -2, 5, -1, 1, 2, 2, 3]], [[17, -2, 1, -92, -36, 69, 18, 17, 17]], [[17, -2, 1, -91, -92, -36, 69, 18]], [[17, -2, 1, -92, 18, -36, 17, 24, -2, -2]], [[17, -3, -2, 5, -1, 1, 2, 3, 3]], [[17, -3, -2, -1, 0, 1, 69, 3, -2]], [[-3, -2, -1, 2, 18, 1, 18, 7, 2, 3]], [[-3, -2, 15, 0, 2]], [[17, 4, -2, -1, 0, 3, 1, 3, 3]], [[17, 1, -1, 1, -92, -36, 69, 18, 1, 1]], [[-3, -2, -1, 0, 1, 69, 17, 3, -2, 17]], [[9, 17, 5, 12, 23, 10, 13, 19, 7, 4]], [[-3, -1, -2, -1, 0, 1, 2, 3, -1]], [[-3, -2, -1, 0, 1, 69, 3, -2, 17]], [[3, 17, 24, 13, 19, 7, 2, 4]], [[17, -2, 1, 18, -36, 17, -2]], [[4, -2, -1, 0, 3, 1, 3, 3]], [[-2, 17, 5, 23, 10, 13, 19, 7, 2, 4, 13]], [[17, -2, 1, -92, -36, 69, 18, 17, 18]], [[17, -1, -3, -2, -1, 0, 1, 2, 3, -1]], [[17, -3, -2, 4, 1, 0, 1, 2, 3]], [[17, -2, 1, 1, -35, 69, 18]], [[-2, 17, 5, 0, 23, 10, 13, 19, 7, 2, 4]], [[17, -3, -2, -1, 1, 69, 17, 3]], [[-2, 17, 5, 24, 13, 19, 7, 2, 3]], [[24, 9, 17, 6, 12, 23, 10, 13, 19, 7, 2, 4]], [[17, -2, 1, 18, -36, 17]], [[17, -2, -1, 0, 1, 7, 2, 3]], [[17, -2, 1, -36, 17, -2]], [[-2, 1, 18, -36, 16, -2]], [[24, 9, 17, 6, 12, 10, 13, 19, 7, 2, 4]], [[24, 10, 9, 17, 6, 12, 10, 13, 19, 7, 2, 4]], [[24, 9, 19, 6, 12, 10, 6, 13, 19, 7, 2, 4, 2, 6]], [[17, -3, 4, 1, 7, 1, 2, 3]], [[-3, 1, -1, 1, 2, 3, 1]], [[68, 17, -2, 1, -92, -36, 69, 1, 18]], [[6, 9, 17, 5, 12, 23, 10, 13, 19, 7, 4]], [[17, -3, -1, 0, 1, 69, 3, -2]], [[24, 9, -1, 19, 6, 12, 10, 6, 13, 19, 7, 2, 4, 2, 6, 2, -1]], [[24, 9, 17, 12, 10, 13, 19, 7, 2, 4, 68, 9]], [[17, -2, -91, -92, 18, -36, 17, 24, 7, -2, -2]], [[9, 17, 23, 10, 13, 19, 7, 7, 2, 9, 9]], [[17, -2, 4, 1, 0, 1, 2, 3]], [[17, -3, 4, 1, 7, 2, 3]], [[-2, 17, 5, 0, 10, 13, 19, 7, 2, 4]], [[-2, 10, -3, 18, -36, 16, -2]], [[17, -2, 4, 1, 18, -3, -36, 17, -2]], [[17, 17, 1, -92, -36, 69, 18, -36]], [[17, -2, -91, -92, 18, -36, 17, 24, 7, -2, -2, 24]], [[17, -3, -1, 0, 1, 69, 3, -2, 17]], [[-2, -91, 5, 0, 10, 14, 19, 7, 2, 4, -2]], [[17, -3, -2, -1, 0, 1, 69, -2]], [[17, 16, 6, 17, 1, -92, -36, 69, 18, -36]], [[24, 9, -2, 19, 6, 12, 10, 6, 13, 19, 7, 2, 4, 2, 6, 2, -1]], [[-3, -3, -2, -1, 0, 2, 3]], [[9, 17, 23, 10, 9, 13, 19, 7, 7, 2, 9]], [[17, -2, -91, -92, 18, -36, 17, -1, 24, 7, -2, -2, 24]], [[9, -3, -2, 5, -1, 1, 2, 2, 3]], [[-3, 1, -1, 0, 1, 2, 3, 1, 1]], [[24, 9, 17, 12, 23, 13, 19, 7, 2, 4]], [[16, 6, 17, 1, -92, -3, -36, 69, 18, -36]], [[-2, 1, 18, -36, 15, -2]], [[16, 17, 1, -92, -3, -36, 69, 18, -36, 1]], [[-2, 17, 3, 13, 23, 10, 13, 19, 7, 2, 4]], [[19, -3, -2, -1, 2, 1, 18, 7, 2, 3]], [[17, -2, 1, 68, 1, -35, 69, 18]], [[-2, 17, -2, 1, -92, -36, 69, 18, 17, 17]], [[-2, 1, 18, -3, -36, 15, -2, 18, -36]], [[-2, 17, 15, 5, 24, -2, 13, 7, 2, 3]], [[-3, -2, -1, 2, 18, -92, 18, 7, 2, 3]]]
results = [[1, 4, 9, 16, 25, 36, 49, 64, 81, 100], [100, 400, 900], [144, 225], [], [9, 4, 1, 0, 1, 4, 9], [81, 289, 25, 529, 100, 169, 361, 49, 4, 16], [4, 289, 25, 529, 100, 169, 361, 49, 4, 16], [289, 9, 4, 1, 0, 1, 4, 9], [4, 289, 25, 576, 100, 169, 361, 49, 4, 16], [9, 4, 1, 0, 1, 4], [289, 9, 4, 1, 0, 1, 4, 9], [9, 4, 1, 0, 1, 49, 4, 9], [9, 1, 1, 0, 1, 4, 9], [289, 4, 1, 8464, 1296, 4761, 324], [289, 4, 1, 8464, 1296, 4761, 324, 1296], [9, 1, 1, 0, 1, 4, 9, 1], [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [289, 9, 4, 1, 0, 1, 4761, 9], [289, 16, 4, 1, 0, 1, 100, 9], [81, 289, 529, 100, 169, 361, 49, 49, 4, 16], [81, 289, 529, 100, 169, 361, 49, 49, 4, 81], [225, 289, 4, 1, 8464, 1296, 4761, 324], [289, 1, 1, 8464, 1296, 4761, 324, 289], [289, 9, 4, 1, 0, 1, 4761, 289, 9], [9, 4, 1, 0, 4, 1], [289, 4, 1, 1, 1296, 4761, 324], [9, 4, 1, 0, 1, 4761, 289, 9, 4], [4, 289, 25, 576, 169, 361, 49, 4, 16], [0, 1, 0, 1, 0, 1, 1, 1, 0, 0], [289, 4, 1, 1, 1296, 324], [81, 289, 25, 144, 529, 100, 169, 361, 49, 4, 16], [289, 4, 1, 8464, 324, 1296, 289, 4], [289, 9, 4, 1, 0, 1, 4, 4, 9], [289, 4, 1, 8464, 1296, 4761, 324, 289], [4, 289, 576, 169, 361, 49, 4, 16], [576, 81, 289, 25, 144, 529, 100, 169, 361, 49, 4, 16], [289, 9, 4, 25, 1, 1, 4, 4, 9], [289, 4, 1, 8464, 1296, 4761, 324, 289, 289], [289, 4, 1, 8281, 8464, 1296, 4761, 324], [289, 4, 1, 8464, 324, 1296, 289, 576, 4, 4], [289, 9, 4, 25, 1, 1, 4, 9, 9], [289, 9, 4, 1, 0, 1, 4761, 9, 4], [9, 4, 1, 4, 324, 1, 324, 49, 4, 9], [9, 4, 225, 0, 4], [289, 16, 4, 1, 0, 9, 1, 9, 9], [289, 1, 1, 1, 8464, 1296, 4761, 324, 1, 1], [9, 4, 1, 0, 1, 4761, 289, 9, 4, 289], [81, 289, 25, 144, 529, 100, 169, 361, 49, 16], [9, 1, 4, 1, 0, 1, 4, 9, 1], [9, 4, 1, 0, 1, 4761, 9, 4, 289], [9, 289, 576, 169, 361, 49, 4, 16], [289, 4, 1, 324, 1296, 289, 4], [16, 4, 1, 0, 9, 1, 9, 9], [4, 289, 25, 529, 100, 169, 361, 49, 4, 16, 169], [289, 4, 1, 8464, 1296, 4761, 324, 289, 324], [289, 1, 9, 4, 1, 0, 1, 4, 9, 1], [289, 9, 4, 16, 1, 0, 1, 4, 9], [289, 4, 1, 1, 1225, 4761, 324], [4, 289, 25, 0, 529, 100, 169, 361, 49, 4, 16], [289, 9, 4, 1, 1, 4761, 289, 9], [4, 289, 25, 576, 169, 361, 49, 4, 9], [576, 81, 289, 36, 144, 529, 100, 169, 361, 49, 4, 16], [289, 4, 1, 324, 1296, 289], [289, 4, 1, 0, 1, 49, 4, 9], [289, 4, 1, 1296, 289, 4], [4, 1, 324, 1296, 256, 4], [576, 81, 289, 36, 144, 100, 169, 361, 49, 4, 16], [576, 100, 81, 289, 36, 144, 100, 169, 361, 49, 4, 16], [576, 81, 361, 36, 144, 100, 36, 169, 361, 49, 4, 16, 4, 36], [289, 9, 16, 1, 49, 1, 4, 9], [9, 1, 1, 1, 4, 9, 1], [4624, 289, 4, 1, 8464, 1296, 4761, 1, 324], [36, 81, 289, 25, 144, 529, 100, 169, 361, 49, 16], [289, 9, 1, 0, 1, 4761, 9, 4], [576, 81, 1, 361, 36, 144, 100, 36, 169, 361, 49, 4, 16, 4, 36, 4, 1], [576, 81, 289, 144, 100, 169, 361, 49, 4, 16, 4624, 81], [289, 4, 8281, 8464, 324, 1296, 289, 576, 49, 4, 4], [81, 289, 529, 100, 169, 361, 49, 49, 4, 81, 81], [289, 4, 16, 1, 0, 1, 4, 9], [289, 9, 16, 1, 49, 4, 9], [4, 289, 25, 0, 100, 169, 361, 49, 4, 16], [4, 100, 9, 324, 1296, 256, 4], [289, 4, 16, 1, 324, 9, 1296, 289, 4], [289, 289, 1, 8464, 1296, 4761, 324, 1296], [289, 4, 8281, 8464, 324, 1296, 289, 576, 49, 4, 4, 576], [289, 9, 1, 0, 1, 4761, 9, 4, 289], [4, 8281, 25, 0, 100, 196, 361, 49, 4, 16, 4], [289, 9, 4, 1, 0, 1, 4761, 4], [289, 256, 36, 289, 1, 8464, 1296, 4761, 324, 1296], [576, 81, 4, 361, 36, 144, 100, 36, 169, 361, 49, 4, 16, 4, 36, 4, 1], [9, 9, 4, 1, 0, 4, 9], [81, 289, 529, 100, 81, 169, 361, 49, 49, 4, 81], [289, 4, 8281, 8464, 324, 1296, 289, 1, 576, 49, 4, 4, 576], [81, 9, 4, 25, 1, 1, 4, 4, 9], [9, 1, 1, 0, 1, 4, 9, 1, 1], [576, 81, 289, 144, 529, 169, 361, 49, 4, 16], [256, 36, 289, 1, 8464, 9, 1296, 4761, 324, 1296], [4, 1, 324, 1296, 225, 4], [256, 289, 1, 8464, 9, 1296, 4761, 324, 1296, 1], [4, 289, 9, 169, 529, 100, 169, 361, 49, 4, 16], [361, 9, 4, 1, 4, 1, 324, 49, 4, 9], [289, 4, 1, 4624, 1, 1225, 4761, 324], [4, 289, 4, 1, 8464, 1296, 4761, 324, 289, 289], [4, 1, 324, 9, 1296, 225, 4, 324, 1296], [4, 289, 225, 25, 576, 4, 169, 49, 4, 9], [9, 4, 1, 4, 324, 8464, 324, 49, 4, 9]]

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
        func_name = "square_nums"
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
        for test_case in ['assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]', 'assert square_nums([10,20,30])==([100,400,900])', 'assert square_nums([12,15])==([144,225])']:
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
