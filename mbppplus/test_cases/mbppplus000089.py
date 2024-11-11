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
inputs = [[0], [6], [10], [9], [-5], [-100], [1000000], [462], [1], [463], [-99], [True], [-7], [-8], [-6], [1000001], [False], [77], [464], [465], [461], [78], [2], [3], [460], [4], [-102], [459], [999999], [466], [-103], [-104], [21], [-1], [-2], [999998], [22], [999997], [-3], [20], [18], [5], [-4], [-9], [467], [-65], [23], [19], [468], [999996], [999995], [469], [-98], [-33], [-64], [24], [458], [999994], [76], [1000002], [-66], [470], [-34], [-10], [88], [79], [1000003], [999993], [-105], [-63], [-97], [1000004], [87], [999992], [-35], [17], [457], [16], [-101], [-32], [25], [-40], [-39], [80], [-41], [-42], [15], [-106], [471], [75], [71], [-107], [472], [-96], [-31], [81], [50], [-62], [72], [82], [456], [51], [61], [-69], [86], [62], [26], [-43]]
results = [0, 12, 30, 25, 0, 0, 250000500000, 53592, 1, 53824, 0, 1, 0, 0, 0, 250001000001, 0, 1521, 54056, 54289, 53361, 1560, 2, 4, 53130, 6, 0, 52900, 250000000000, 54522, 0, 0, 121, 0, 0, 249999500000, 132, 249999000001, 0, 110, 90, 9, 0, 0, 54756, 0, 144, 100, 54990, 249998500002, 249998000004, 55225, 0, 0, 0, 156, 52670, 249997500006, 1482, 250001500002, 0, 55460, 0, 0, 1980, 1600, 250002000004, 249997000009, 0, 0, 0, 250002500006, 1936, 249996500012, 0, 81, 52441, 72, 0, 0, 169, 0, 0, 1640, 0, 0, 64, 0, 55696, 1444, 1296, 0, 55932, 0, 0, 1681, 650, 0, 1332, 1722, 52212, 676, 961, 0, 1892, 992, 182, 0]

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
        func_name = "sum_series"
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
        for test_case in ['assert sum_series(6) == 12', 'assert sum_series(10) == 30', 'assert sum_series(9) == 25']:
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
