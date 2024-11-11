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
inputs = [[[2, 3, 6, 7, 9], [1, 4, 8, 10], 5], [[100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7], [[3, 4, 7, 8, 10], [2, 5, 9, 11], 6], [[1, 2, 3], [], 1], [[], [1, 2, 3], 2], [[], [1], 1], [[1], [], 1], [[1, 2, 3], [], 3], [[1, 1, 1], [], 2], [[1, 2, 3], [True, True, False], 3], [[1, 2, 3, 1], [], 3], [[False, -64, 27, -83, 3, -39], [1], 1], [[False, -64, 27, -83, 3, -39], [1, 1], 1], [[96, False, 3, 50], [1, 2, 3, 3], 2], [[1, 2, 3, 2], [], 3], [[True, True, False, True], [True, True, False, True], 3], [[False, -64, 27, 3, -39], [False, -64, 27, 3, -39], 2], [[1, 2, 3, 1], [], 2], [[1, 50], [1, 50], 1], [[1, 1], [], 2], [[False, True, False, True], [False, True, False, True], 3], [[1, 2, 3, 2, 3], [], 3], [[1, 2, 3], [-39.319443006981004, -57.39432084514247, -76.34186082848302, -70.39547602882918, 5.979370667934944, -70.11319095554586, -77.67992498473315, -35.264606501444845, 53.4388130843717, -2.8800159179744185], 3], [[1, 2], [1, 2], 2], [[1, 2, 3, 1], [6.592840281996914, False], 3], [[False, 97, 96, 27, -83, 3, -39], [1, 1], 1], [[False, -64, 27, -83, 3], [False, -64, 27, -83, 3], 1], [[False, 28, -64, 27, 29, -83, 3], [False, 28, -64, 27, 29, -83, 3], 1], [[1, 2, 3, 2], [1, 2, 3, 2], 2], [[2], [2], 2], [[False, 4, -64, 27, -83, 3, -39], [1, 1], 1], [[False, 97, 96, 27, -83, 3, -39], [0, 1], 1], [[False, -64, 27, -83, 3, -39], [1, 1, 1], 1], [[1, 2, 28, 2], [], 3], [[1, 2, 3, 2], [1, 2, 3, 2], 4], [[1, 28, 2, 3, 2], [1, 28, 2, 3, 2], 2], [[96, False, 3], [1, 2, 3, 3], 2], [[False, 97, 96, 27, -83, 3, -39], [0, 1, 1], 1], [[False, -64, 27, -83, 3, -39], [3, 1], 1], [[False, 1, 1, 1], [], 2], [[1, 2, 29, 3, 2, 3], [], 3], [['r', 'zJBCERjzbi', 'dAeIcPYLJw'], [], 2], [[1, 28, 4, 3, 2], [1, 28, 4, 3, 2], 1], [[True, True, False, True, True], [True, True, False, True, True], 3], [[True, True, False], [True, True, False], 3], [[1, 1, 1], [False, False, False, True, False, True], 3], [[False, True, True, True], [False, True, True, True], 3], [[False, -64, 27, -83, 3, -39], [2], 1], [[False, -64, 27, -83, 3, False], [False, -64, 27, -83, 3, False], 1], [[1, 28, 2, 3, 3], [1, 28, 2, 3, 3], 2], [[1, 2, 3], [True, False], 3], [[96, -39, 3], [1, 2, 3, 3], 2], [[1, 1], [1, 1], 1], [[1, 2, 4, 3, 3], [96, -39, 3], 2], [[False, -64, 27, -83, 3, -39], [1, 1, 1], 2], [[96, False, 3, 50, False], [1, 2, 3, 3], 2], [[1, -39, 2, 3], [True, False, True], 3], [[-39, 2, 29, 4, -18, -31, 28, 3, -68, 43], [1, 2, 3], 2], [[False, 97, 96, 27, -83, 3, -39], [0, -31, 1], 1], [['r', 'zJBCERjzbi', 'dAeIcPYLrJw'], [], 3], [[1, 1, 1, 1], [1, 1, 1, 1], 1], [[False, 97, 96, 27, -83, 3, -39], [0, 1], 2], [[-64, 3, -83, 3, -39, 3], [3, 1], 1], [[2, 3], [2, 3], 1], [[1, 2, 3], [-39.319443006981004, -57.39432084514247, -76.34186082848302, -70.39547602882918, 5.979370667934944, -70.11319095554586, -77.67992498473315, -35.264606501444845, 53.4388130843717, -2.8800159179744185], 4], [[4, False, -64, 27, -83, 3, -39, -39, 3], [4, False, -64, 27, -83, 3, -39, -39, 3], 1], [[False, 28, -64, 27, 29, -83, -64, 3, 29], [False, 28, -64, 27, 29, -83, -64, 3, 29], 1], [[], [25.76844865917127, 5.979370667934944, 34.20953059107049, 73.57245412264768, 19.02562370256588, -57.39432084514247, 5.979370667934944, -39.319443006981004], 2], [[False, False, False], [False, False, False], 3], [[1, 1, 2, 3, 2], [1, 1, 2, 3, 2], 4], [[True, False, True, False, True, True], [True, False, True, False, True, True], 3], [[1, 28, 2, 3, 3, 2], [1, 28, 2, 3, 3, 2], 2], [[1, 2, 3, 2, 2], [1, 2, 3, 2, 2], 2], [[False, 96, 96, 27, -83, 3, -39], [False, 96, 96, 27, -83, 3, -39], 1], [['r', 'r', 'zJBCERjzbi', 'dAeIcPYLJw'], [], 2], [[False, 27, -83, 3, -39], [1, 1], 1], [[1, 2, 4, 3, 3, 3], [96, -39, 3], 2], [[1, 1, 1, 1], [1, 1, 1, 1], 3], [[1, 2, 2, 1], [6.592840281996914, False], 3], [[False, 27, -83, 3, -39], [1, 2, 1], 1], [[-64, 3, -83, 3, -39, 3], [3, -39, 1], 1], [[False, False, True], [False, False, True], 3], [[False, -64, 27, -83, 3, -38], [1, 1], 1], [[1, 2, 3], [True], 3], [[False, 27, -83, 3, -39], [1, 1, 1], 1], [[1, 2, 3, 43], [], 2], [[False, -64, False, 27, -83, 3, -83], [False, -64, False, 27, -83, 3, -83], 1], [[-64, 3, -83, 3, -39, 3], [4], 1], [[3, 1, 3], [3, 1, 3], 1], [[-39, 2, 29, -31, 4, -18, -31, 28, -68, 43], [-39, 2, 29, -31, 4, -18, -31, 28, -68, 43], 2], [[1, 2, 3, 3, 3, 3], [96, -31, 3], 2], [[3, False, 27, -83, 3, 3, -39], [3, False, 27, -83, 3, 3, -39], 1], [[4, 1, 2, 3, 1], [6.592840281996914, False], 4], [[False, -64, 27, -83, 3, -39], [3], 1], [[1, 3, 2, 3, 3, 2], [1, 3, 2, 3, 3, 2], 2], [[2, 1], [2, 1], 1], [[1, 2, 3, 2, 2], [1, 2, 3, 2, 2], 1], [[-68, 1, 1, 1, 1], [-68, 1, 1, 1, 1], 1], [[False, False], [False, False], 3], [[96, False, 3, 50], [1, 43, 2, 3, 3], 2], [[1, 2, 1], [], 3], [[50, 2, 3, 2, 2], [50, 2, 3, 2, 2], 1], [[False, True, True, False], [False, True, True, False], 4], [[43, -68, 1, 1, 1], [43, -68, 1, 1, 1], 1], [[False], [False], 1], [[1, 2, -83, 3], [-39.319443006981004, -57.39432084514247, -35.264606501444845, -76.34186082848302, -70.39547602882918, 5.979370667934944, -70.11319095554586, -77.67992498473315, -35.264606501444845, 53.4388130843717, -2.8800159179744185], 5], [[2, 1, 1], [2, 1, 1], 1]]
results = [6, 256, 8, 1, 2, 1, 1, 3, 1, True, 2, -83, -83, 1, 2, True, -64, 1, 1, 1, False, 2, -70.39547602882918, 1, 1, -83, -83, -83, 1, 2, -83, -83, -83, 2, 2, 1, 1, -83, -83, 1, 2, 'r', 1, True, True, False, True, -83, -83, 1, True, 1, 1, 1, -64, False, 1, -39, -83, 'zJBCERjzbi', 1, -39, -83, 2, -70.11319095554586, -83, -83, -39.319443006981004, False, 1, False, 1, 1, -83, 'r', -83, 1, 1, 1, -83, -83, False, -83, 2, -83, 2, -83, -83, 1, -68, 1, -83, 2, -83, 1, 1, 1, -68, False, 1, 2, 2, False, -68, False, -70.11319095554586, 1]

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
        func_name = "find_kth"
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
        for test_case in ['assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6', 'assert find_kth([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7) == 256', 'assert find_kth([3, 4, 7, 8, 10], [2, 5, 9, 11], 6) == 8']:
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
