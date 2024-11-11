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
inputs = [[2, 100], [8, 10], [8, 15], [3, 3], [1, 1000000], [0, 500], [11, 100], [7, 200], [5, 1000], [5, 1], [201, 200], [5, 0], [1, 500], [5, 8], [1, 11], [1, 0], [11, 1], [10, 1], [11, 8], [0, 11], [500, 200], [999, 5], [200, 0], [99, 999], [201, 201], [8, 8], [202, 201], [498, 200], [200, 999], [999, 999], [200, 200], [1, 1], [5, 202], [1001, 1000], [0, 998], [1000000, 1], [201, 202], [11, 201], [11, 202], [0, 0], [1002, 1], [5, 1001], [7, 7], [11, 200], [7, 1], [202, 498], [10, 10], [1002, 498], [201, 999], [10, 202], [202, 202], [11, 10], [10, 99], [0, 1], [1002, 1001], [12, 100], [202, 200], [11, 1000], [1000, 5], [11, 11], [1, 202], [998, 998], [499, 499], [1003, 1002], [0, 498], [12, 999], [8, 11], [1000, 10], [498, 499], [202, 1003], [1000, 100], [203, 202], [1002, 1002], [1002, 5], [200, 201], [199, 201], [204, 203], [0, 999], [500, 201], [998, 999], [11, 999], [1000, 1000], [99, 0], [8, 12], [499, 498], [1003, 5], [501, 201], [501, 1002], [9, 8], [5, 100], [1001, 204], [501, 501], [1000, 200], [199, 200], [1001, 12], [1, 998], [12, 12], [100, 203], [202, 1], [204, 1001], [1001, 1001], [204, 204], [998, 8], [1001, 200], [0, 202], [199, 1], [998, 12], [9, 9], [1003, 1003]]
results = [115, 37, 62, 9, 1, 0, 439, 697, 3172, 5, 2106, 1, 1, 25, 1, 1, 2, 1, 40, 0, 556, 81, 1, 9081, 1980, 37, 2062, 2421, 1367, 13536, 256, 1, 616, 13417, 0, 1, 2016, 917, 898, 1, 3, 3107, 25, 913, 7, 4978, 1, 6606, 10260, 1, 2155, 43, 1, 0, 13383, 459, 2005, 4588, 1, 41, 1, 13402, 5944, 13690, 0, 4815, 62, 1, 5967, 10174, 1, 2101, 13752, 27, 269, 2242, 2115, 0, 584, 13490, 4643, 1, 1, 64, 5968, 43, 2412, 12096, 27, 283, 2656, 6048, 1, 2044, 127, 1, 54, 1, 4, 10305, 13424, 2097, 109, 2578, 0, 19, 172, 45, 13855]

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
        func_name = "power_base_sum"
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
        for test_case in ['assert power_base_sum(2,100)==115', 'assert power_base_sum(8,10)==37', 'assert power_base_sum(8,15)==62', 'assert power_base_sum(3,3)==9']:
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
