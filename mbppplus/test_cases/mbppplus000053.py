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
inputs = [[99], [1221], [120], [0], [45678], [1], [45679], [2], [3], [45681], [4], [5], [45683], [45682], [45677], [6], [45676], [45675], [45680], [34], [45674], [33], [45673], [7], [32], [8], [58], [45672], [57], [55], [9], [31], [36], [56], [45684], [30], [29], [87], [45671], [40], [45685], [54], [35], [10], [45670], [96], [45669], [28], [11], [97], [59], [98], [27], [37], [45686], [41], [60], [53], [13], [26], [14], [52], [51], [25], [12], [50], [24], [85], [23], [45687], [39], [86], [88], [61], [38], [45668], [95], [84], [45667], [22], [45688], [42], [45666], [89], [15], [83], [45665], [90], [91], [49], [100], [45689], [94], [45664], [82], [62], [81], [16], [93], [101], [80], [102], [20], [48]]
results = [101, 1331, 121, 1, 45754, 2, 45754, 3, 4, 45754, 5, 6, 45754, 45754, 45754, 7, 45754, 45754, 45754, 44, 45754, 44, 45754, 8, 33, 9, 66, 45754, 66, 66, 11, 33, 44, 66, 45754, 33, 33, 88, 45754, 44, 45754, 55, 44, 11, 45754, 99, 45754, 33, 22, 99, 66, 99, 33, 44, 45754, 44, 66, 55, 22, 33, 22, 55, 55, 33, 22, 55, 33, 88, 33, 45754, 44, 88, 99, 66, 44, 45754, 99, 88, 45754, 33, 45754, 44, 45754, 99, 22, 88, 45754, 99, 99, 55, 101, 45754, 99, 45754, 88, 66, 88, 22, 99, 111, 88, 111, 22, 55]

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
        func_name = "next_smallest_palindrome"
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
        for test_case in ['assert next_smallest_palindrome(99)==101', 'assert next_smallest_palindrome(1221)==1331', 'assert next_smallest_palindrome(120)==121']:
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
