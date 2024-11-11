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
inputs = [[12], [7], [10], [0], [-10], [2], [9], [9876543210], [100000000000000000000000000000000000000000], [99999999999999999999999999999999999999999999999999999999999998], [100000000000000000000000000000000000000001], [-9], [3], [True], [-42], [False], [99999999999999999999999999999999999999999999999999999999999997], [99999999999999999999999999999999999999999], [-8], [1], [99999999999999999999999999999999999999999999999999999999999996], [-1], [100000000000000000000000000000000000000002], [-48], [-2], [9876543211], [-11], [99999999999999999999999999999999999999999999999999999999999995], [100000000000000000000000000000000000000003], [11], [99999999999999999999999999999999999999999999999999999999999994], [13], [9876543212], [4], [-47], [8], [-7], [-41], [-61], [14], [-3], [-49], [100000000000000000000000000000000000000004], [-43], [99999999999999999999999999999999999999998], [15], [40], [-44], [99999999999999999999999999999999999999999999999999999999999999], [9876543213], [-60], [62], [100000000000000000000000000000000000000000000000000000000000000], [5], [17], [41], [63], [99999999999999999999999999999999999999997], [16], [42], [-59], [-46], [-45], [64], [-4], [-62], [6], [-58], [100000000000000000000000000000000000000005], [9876543214], [-12], [-63], [-40], [-50], [18], [-5], [-92], [-6], [-98], [-34], [-35], [61], [-14], [100000000000000000000000000000000000000006], [9876543215], [-38], [19], [-97], [-91], [100000000000000000000000000000000000000000000000000000000000001], [-93], [-15], [-64], [-36], [99999999999999999999999999999999999999996], [-33], [43], [20], [-95], [-30], [-37], [-13], [100000000000000000000000000000000000000007], [-16], [-99], [-32], [9876543216]]
results = [False, True, False, False, False, False, True, False, False, False, True, True, True, True, False, False, True, True, False, True, False, True, False, False, False, True, True, True, True, True, False, True, False, False, True, False, True, True, True, False, True, True, False, True, False, True, False, False, True, True, False, False, False, True, True, True, True, True, False, False, True, False, True, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, False, False, True, True, False, False, True, False, True, True, True, True, True, True, False, False, False, True, True, False, True, False, True, True, True, False, True, False, False]

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
        func_name = "find_Parity"
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
        for test_case in ['assert find_Parity(12) == False', 'assert find_Parity(7) == True', 'assert find_Parity(10) == False']:
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
