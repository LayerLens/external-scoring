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
inputs = [[5], [10], [100], [1000], [1001], [1002], [1003], [999], [True], [False], [998], [65], [66], [67], [997], [68], [64], [1004], [1005], [99], [996], [63], [995], [1006], [1007], [1008], [62], [994], [86], [1009], [85], [61], [87], [60], [44], [1010], [1011], [45], [59], [80], [69], [70], [71], [98], [97], [79], [1012], [2], [1013], [84], [56], [1], [0], [81], [78], [43], [1014], [72], [1015], [90], [42], [41], [46], [88], [3], [1016], [57], [4], [38], [993], [1017], [77], [101], [1018], [83], [82], [76], [58], [73], [39], [74], [89], [40], [75], [1019], [96], [47], [94], [95], [55], [48], [54], [1020], [102], [53], [91], [992], [1021], [991], [11], [92], [37]]
results = [2, 4, 25, 168, 168, 168, 168, 168, 0, 0, 168, 18, 18, 18, 167, 19, 18, 168, 168, 25, 167, 18, 167, 168, 168, 168, 18, 167, 23, 168, 23, 17, 23, 17, 14, 169, 169, 14, 16, 22, 19, 19, 19, 25, 24, 21, 169, 0, 169, 23, 16, 0, 0, 22, 21, 13, 170, 20, 170, 24, 13, 12, 14, 23, 1, 170, 16, 2, 12, 167, 170, 21, 25, 170, 22, 22, 21, 16, 20, 12, 21, 23, 12, 21, 170, 24, 14, 24, 24, 16, 15, 16, 171, 26, 15, 24, 167, 171, 166, 4, 24, 11]

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
        func_name = "count_Primes_nums"
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
        for test_case in ['assert count_Primes_nums(5) == 2', 'assert count_Primes_nums(10) == 4', 'assert count_Primes_nums(100) == 25']:
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
