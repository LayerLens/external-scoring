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
inputs = [[1234], [51241], [321], [9], [9876543210], [112233445566], [111111], [112233445565], [111110], [112233445567], [10], [9876543211], [111112], [111109], [112233445568], [8], [9876543209], [11], [111113], [9876543208], [111108], [7], [6], [9876543206], [111114], [9876543207], [12], [111107], [5], [4], [3], [2], [112233445564], [9876543212], [1], [9876543213], [9876543205], [74], [9876543214], [0], [75], [111115], [76], [9876543204], [112233445569], [111106], [112233445570], [77], [111105], [72], [13], [9876543215], [112233445563], [112233445571], [73], [78], [112233445562], [9876543217], [79], [71], [111104], [111103], [70], [14], [9876543203], [69], [29], [30], [111102], [28], [68], [65], [111101], [52], [112233445572], [9876543216], [27], [15], [26], [91], [16], [31], [112233445573], [67], [32], [80], [17], [25], [111100], [53], [112233445574], [111099], [112233445561], [33], [92], [81], [9876543219], [112233445575], [112233445560], [66], [9876543218], [64], [54], [51], [111117], [63], [9876543202]]
results = [True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, True, False, True, True, True, True, False, True, True, True, False, True, True, False, True, False, True, False, False, False, False, True, False, True, True, True, False, False, True, True, False, True, True, True, False, False, False, True, False, True, True, False, False, True, True, True, False, True, False, True, True, True, True, True, True, True, False, True, True, False, True, True, False, True, False, False, False, True, True, True, True, False, False, True, True, True, True, True, False, True, False]

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
        func_name = "validate"
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
        for test_case in ['assert validate(1234) == True', 'assert validate(51241) == False', 'assert validate(321) == True']:
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
