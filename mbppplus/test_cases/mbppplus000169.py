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
inputs = [[60], [10], [2], [100], [1000], [10000], [100000], [500], [1000000], [99], [498], [499], [101], [False], [9999], [1001], [501], [True], [1002], [10001], [502], [999], [100001], [999999], [100002], [497], [9998], [1000001], [100003], [1003], [496], [1000002], [100004], [1004], [999998], [999997], [99999], [99998], [102], [1000003], [1005], [10002], [100005], [998], [999996], [503], [68], [10003], [103], [495], [69], [67], [1006], [100006], [98], [997], [104], [504], [996], [505], [1000004], [999995], [494], [1000005], [70], [1007], [1008], [493], [96], [97], [995], [1000006], [1000007], [99997], [38], [994], [506], [10004], [10005], [99996], [999994], [37], [95], [492], [993], [3], [4], [10006], [490], [66], [5], [73], [18], [100007], [39], [6], [507], [1009], [1010], [488], [491], [489], [19], [65], [27], [17], [487], [999993]]
results = [106, 12, 2, 200, 3300, 55358, 940774, 1404, 16326651, 192, 1391, 1391, 200, 0, 55188, 3300, 1404, 1, 3300, 55358, 1404, 3264, 940774, 16322563, 940774, 1391, 55188, 16326651, 940774, 3300, 1391, 16326651, 940774, 3300, 16322563, 16322563, 939948, 939948, 200, 16326651, 3300, 55358, 940774, 3264, 16322563, 1404, 114, 55358, 200, 1391, 114, 114, 3300, 940774, 192, 3264, 200, 1404, 3264, 1404, 16326651, 16322563, 1391, 16326651, 114, 3300, 3300, 1391, 192, 192, 3264, 16326651, 16326651, 939948, 57, 3264, 1404, 55358, 55358, 939948, 16322563, 57, 164, 1391, 3264, 3, 4, 55358, 1391, 114, 5, 133, 24, 940774, 57, 7, 1404, 3300, 3300, 1391, 1391, 1391, 24, 114, 38, 21, 1391, 16322563]

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
        func_name = "get_max_sum"
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
        for test_case in ['assert get_max_sum(60) == 106', 'assert get_max_sum(10) == 12', 'assert get_max_sum(2) == 2']:
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
