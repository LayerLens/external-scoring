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
inputs = [[9], [10], [11], [-5], [-4], [-6], [-7], [True], [False], [-8], [-3], [-9], [-10], [-11], [-12], [75], [74], [73], [72], [76], [71], [-13], [57], [-14], [77], [56], [-2], [-46], [-16], [-15], [70], [-17], [-1], [0], [-47], [-60], [55], [78], [-48], [54], [-61], [-49], [58], [59], [-18], [-19], [53], [-62], [-20], [-21], [-63], [79], [-45], [-87], [-88], [-89], [-22], [-44], [-59], [1], [-86], [-50], [-51], [-90], [2], [95], [-23], [60], [-85], [96], [-91], [-93], [-94], [-84], [-92], [-24], [52], [97], [94], [-52], [93], [92], [-83], [61], [62], [50], [-53], [8], [49], [-25], [69], [-66], [3], [4], [99], [-33], [51], [-32], [63], [100], [-82], [-95], [-54]]
results = [49, 66, 88, 5, 5, 5, 5, 3, 3, 5, 5, 5, 5, 5, 5, 5886726723, 4443758530, 3354494068, 2532232653, 7798252600, 1911525875, 5, 37295139, 5, 10330485255, 28153267, 5, 5, 5, 5, 1442968191, 5, 5, 3, 5, 5, 21252272, 13684979325, 5, 16042865, 5, 5, 49405541, 65448408, 5, 5, 12110400, 5, 5, 5, 5, 18128737857, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 1630580875000, 5, 86700682, 5, 2160059765853, 5, 5, 5, 5, 5, 5, 9141870, 2861469960548, 1230889085546, 5, 929170680305, 701410194693, 5, 114853951, 152149092, 5209405, 5, 37, 3932463, 5, 1089264460, 5, 8, 10, 5021529726403, 5, 6900993, 5, 201554635, 6652110601405, 5, 5, 5]

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
        func_name = "cal_sum"
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
        for test_case in ['assert cal_sum(9) == 49', 'assert cal_sum(10) == 66', 'assert cal_sum(11) == 88']:
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
