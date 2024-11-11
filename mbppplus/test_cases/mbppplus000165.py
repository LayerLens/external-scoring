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
inputs = [[10], [19], [32], [1], [1000000], [987654321], [987654320], [999999], [987654319], [2], [987654322], [999998], [1000001], [987654323], [4], [3], [1000002], [1000003], [987654324], [True], [987654318], [1000005], [1000004], [40], [987654325], [999997], [39], [1000006], [1000007], [999996], [999995], [42], [1000008], [987654326], [987654317], [987654327], [987654316], [38], [9], [11], [8], [12], [999994], [70], [7], [37], [5], [69], [36], [1000009], [987654315], [999993], [35], [34], [13], [41], [6], [43], [1000010], [33], [987654328], [44], [987654329], [45], [14], [71], [999992], [1000011], [1000012], [987654314], [1000013], [68], [72], [1000014], [77], [78], [67], [66], [73], [47], [48], [987654312], [91], [79], [15], [65], [987654330], [987654331], [987654332], [987654311], [49], [46], [987654313], [1000015], [64], [16], [90], [31], [80], [74], [987654333], [999991], [50], [63]]
results = [8, 16, 32, 1, 524288, 536870912, 536870912, 524288, 536870912, 2, 536870912, 524288, 524288, 536870912, 4, 2, 524288, 524288, 536870912, 1, 536870912, 524288, 524288, 32, 536870912, 524288, 32, 524288, 524288, 524288, 524288, 32, 524288, 536870912, 536870912, 536870912, 536870912, 32, 8, 8, 8, 8, 524288, 64, 4, 32, 4, 64, 32, 524288, 536870912, 524288, 32, 32, 8, 32, 4, 32, 524288, 32, 536870912, 32, 536870912, 32, 8, 64, 524288, 524288, 524288, 536870912, 524288, 64, 64, 524288, 64, 64, 64, 64, 64, 32, 32, 536870912, 64, 64, 8, 64, 536870912, 536870912, 536870912, 536870912, 32, 32, 536870912, 524288, 64, 16, 64, 16, 64, 64, 536870912, 524288, 32, 32]

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
        func_name = "highest_Power_of_2"
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
        for test_case in ['assert highest_Power_of_2(10) == 8', 'assert highest_Power_of_2(19) == 16', 'assert highest_Power_of_2(32) == 32']:
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
