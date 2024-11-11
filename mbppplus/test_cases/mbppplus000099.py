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
inputs = [[2], [4], [6], [999999999], [1000000000], [True], [False], [1000000001], [999999998], [67], [999999997], [999999996], [1000000002], [1000000003], [66], [999999995], [65], [999999994], [68], [69], [71], [72], [999999993], [1000000004], [1], [73], [70], [64], [1000000005], [74], [98], [63], [0], [999999992], [1000000006], [3], [61], [62], [97], [999999991], [75], [11], [95], [1000000007], [94], [93], [96], [92], [76], [12], [77], [9], [44], [13], [10], [1000000008], [14], [91], [78], [79], [59], [99], [80], [90], [999999990], [85], [60], [57], [1000000009], [58], [84], [100], [43], [101], [48], [23], [1000000010], [56], [86], [55], [102], [5], [53], [46], [81], [47], [52], [49], [54], [83], [45], [16], [50], [30], [28], [82], [42], [33], [17], [31], [41], [51]]
results = [1, 1, 2, 21, 13, 1, 0, 14, 20, 3, 20, 19, 14, 15, 2, 20, 2, 19, 2, 3, 4, 2, 19, 14, 1, 3, 3, 1, 15, 3, 3, 6, 0, 18, 15, 2, 5, 5, 3, 20, 4, 3, 6, 16, 5, 5, 2, 4, 3, 2, 4, 2, 3, 3, 2, 14, 3, 5, 4, 5, 5, 4, 2, 4, 19, 4, 4, 4, 15, 4, 3, 3, 4, 4, 2, 4, 15, 3, 4, 5, 4, 2, 4, 4, 3, 5, 3, 3, 4, 4, 4, 1, 3, 4, 3, 3, 3, 2, 2, 5, 3, 4]

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
        func_name = "count_Set_Bits"
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
        for test_case in ['assert count_Set_Bits(2) == 1', 'assert count_Set_Bits(4) == 1', 'assert count_Set_Bits(6) == 2']:
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
