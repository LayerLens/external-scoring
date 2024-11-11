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
inputs = [[1], [2], [3], [-10], [-283], [-1000], [1000000000], [-999], [999999999], [-284], [-9], [False], [-282], [True], [999999998], [999999997], [-281], [-73], [-279], [-74], [94], [-280], [-72], [-278], [93], [-276], [999999995], [-285], [-277], [95], [-11], [-75], [-76], [1000000001], [-286], [-71], [92], [91], [-12], [-8], [1000000002], [90], [999999994], [89], [-1001], [1000000003], [-13], [-14], [-94], [999999996], [-95], [-98], [999999993], [-15], [76], [74], [40], [-96], [-70], [-97], [75], [41], [-99], [-19], [96], [88], [73], [39], [-16], [59], [16], [-69], [-77], [-43], [-44], [999999992], [77], [87], [-78], [18], [45], [8], [-100], [14], [-68], [-101], [13], [-79], [-287], [-102], [58], [-17], [38], [98], [-1002], [15], [1000000004], [57], [-288], [-1003], [60], [-20], [-998], [-7], [1000000005], [-18], [-1005]]
results = [False, True, False, True, False, True, True, False, False, True, False, True, True, False, True, False, False, False, False, True, True, True, True, True, False, True, False, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, False, False, False, True, True, True, False, True, False, False, True, True, True, True, True, False, False, False, False, False, True, True, False, False, True, False, True, False, False, False, True, True, False, False, True, True, False, True, True, True, True, False, False, False, False, True, True, False, True, True, True, False, True, False, True, False, True, True, True, False, False, True, False]

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
        func_name = "is_Even"
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
        for test_case in ['assert is_Even(1) == False', 'assert is_Even(2) == True', 'assert is_Even(3) == False']:
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
