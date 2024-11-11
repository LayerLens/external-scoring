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
inputs = [[[1, 2, 3, 4, 5], [6, 7, 8, 9]], [[1, 2, 3], [4, 5, 6]], [[1, 4, 5], [1, 4, 5]], [[], [1, 2, 3]], [[1, 2, 3], []], [[], []], [[1000000, 2000000, 3000000], [1000000, 2000000, 3000000]], [[3000000], []], [[], [1, 2]], [[63.43122042559975, -31.187672074988427, 63.43122042559975], [1]], [[False, False, True, False, True, False], [3, 2, 63, 2000000, 2, -93, 51, 3000000, -61, 3]], [[63.43122042559975, -31.187672074988427, 63.43122042559975], [1, 1]], [[63.43122042559975, -31.187672074988427, 63.43122042559975, -31.187672074988427], [63.43122042559975, -31.187672074988427, 63.43122042559975, -31.187672074988427]], [[1, 3], [True]], [[63.07613966106393, -31.187672074988427, 63.43122042559975], [1]], [[], [2, 3]], [[2, 2, 3], [2, 2, 3]], [[63.07613966106393, 63.07613966106393, 63.43122042559975], [1]], [[False, False, True, False, True, True], [False, False, True, False, True, True]], [[2, 3], [2, 3]], [[63, 3000000, 3000000], [63, 3000000, 3000000]], [[], [1, 2, 2]], [[2, 3, 3], [2, 3, 3]], [[3, 3000000, 2, 4, 3], [3, 3000000, 2, 4, 3]], [[1, 2], [1, 2]], [[1], [1]], [[False, False, False, True, False, True, False], [False, False, False, True, False, True, False]], [[1, 2, 3], [-64]], [[], [False, True, False]], [[-93], []], [[], [2, 2]], [[63.07613966106393, 63.07613966106393, 63.43122042559975, 63.43122042559975], [63.07613966106393, 63.07613966106393, 63.43122042559975, 63.43122042559975]], [[33.96565948782273, 63.07613966106393, 63.43122042559975, 63.43122042559975], [33.96565948782273, 63.07613966106393, 63.43122042559975, 63.43122042559975]], [[3, 3000000, 1, 2, 4, 3, 3], [3, 3000000, 1, 2, 4, 3, 3]], [[3, 3000000, 4, 3], [3, 3000000, 4, 3]], [[33.17607444762987, 63.07613966106393, 44.99937757260167, 63.43122042559975], [33.17607444762987, 63.07613966106393, 44.99937757260167, 63.43122042559975]], [[2, 3, 3000000], [2, 3, 3000000]], [[1, 2, 2, 2], [1, 2, 2, 2]], [[3, 2999999, 1, 3, 4, 3, 3, 3], [3, 2999999, 1, 3, 4, 3, 3, 3]], [[-76.59859490046561, 33.96565948782273, 0.21095117898697424, -99.50475342484972, 33.96565948782273, 63.43122042559975, 33.17607444762987], [2]], [[-61, 3000000, 4, 3], [-61, 3000000, 4, 3]], [[3], [3]], [[1000000, 2000000, 3000000], [2000000, 1000000, 2000000, 3000000]], [[2, 5, 3, 2], [2, 5, 3, 2]], [[3, 3000000, 1, 2, 4, 3, 3, 3000000], [3, 3000000, 1, 2, 4, 3, 3, 3000000]], [[3, 3000000, 1, 4, 3], [3, 3000000, 1, 4, 3]], [[], [2, 2, 3]], [[], [3, 3]], [[63.07613966106393, 63.07613966106393, 63.43122042559975, 63.43122042559975, 63.07613966106393], [63.07613966106393, 63.07613966106393, 63.43122042559975, 63.43122042559975, 63.07613966106393]], [[3, 3000000, 1, 2, 4, 3, -93, 3, 3000000], [3, 3000000, 1, 2, 4, 3, -93, 3, 3000000]], [[2, False, 3000000], [2, False, 3000000]], [[2, 3, 2], [2, 3, 2]], [[63.07613966106393, 63.07613966106393, 63.43122042559975, 63.43122042559975, 63.07613966106393, 63.07613966106393], [63.07613966106393, 63.07613966106393, 63.43122042559975, 63.43122042559975, 63.07613966106393, 63.07613966106393]], [[False, True, False, True], []], [[3, 3, 3, 3], [3, 3, 3, 3]], [[-64, -81, 3, 31, 18, 51], [3, 3]], [[], [2, 2999999, 2, 3]], [[33.96565948782273, 63.07613966106393, 63.43122042559975], [33.96565948782273, 63.07613966106393, 63.43122042559975]], [[3, 3000000, 4], [3, 3000000, 4]], [[1, 1], [1, 1]], [[1, 1, 1], [63.07613966106393, 63.07613966106393, 63.43122042559975]], [[3, 2999999, 1, 3, 4, 3, 3, False], [3, 2999999, 1, 3, 4, 3, 3, False]], [[False, True, False], [-93, -57, -51, 38, -57]], [[1, 3, 2, 1, 2, 2], [1, 3, 2, 1, 2, 2]], [[3000000, -64], [3000000, -64]], [[3, 2999999, 3000000, 38], [3, 2999999, 3000000, 38]], [[3, 3, 3], [3, 3, 3]], [[63.07613966106393, 63.07613966106393, 63.43122042559975, 71.94678677068327, 63.43122042559975, 63.07613966106393, 63.07613966106393], [63.07613966106393, 63.07613966106393, 63.43122042559975, 71.94678677068327, 63.43122042559975, 63.07613966106393, 63.07613966106393]], [[False, False, True, False, False, False], []], [[0, -64, -13, 2000000, -97, -34, 78, 2000000, 1000000, -64], []], [[92.17179846001889, 63.43122042559975], [92.17179846001889, 63.43122042559975]], [[2, 51], [2, 51]], [[], [2, 3000000, 60, 38, 33, 78, -13, -93, -34, -81]], [[1, 1, 1], [1, 1, 1]], [[3, 4], [3, 4]], [[], [5, 3, 3]], [[-93, -57, -57, -51, 18, -57], [-93, -57, -57, -51, 18, -57]], [[3, 3000000, 3000000, 3], [3, 3000000, 3000000, 3]], [[3000000, 3000000, 3, 3], [3000000, 3000000, 3, 3]], [[3000000, 4], [3000000, 4]], [[-64, -81, 3, 31, 51], [3, 3]], [[0, 3, 2, 1, 2, 2, 3, 3, 2], [0, 3, 2, 1, 2, 2, 3, 3, 2]], [[False, False, True, False, True, False, True], [3, 2, 63, 2000000, 2, -93, 51, 3000000, -61, 3]], [[2, 2, 2], [2, 2, 2]], [[33.31988234449095, 63.07613966106393, 63.43122042559975], [33.31988234449095, 63.07613966106393, 63.43122042559975]], [[31], [31]], [[3, 3000000, 1, 2, 4, 38, 3, 3, 3], [3, 3000000, 1, 2, 4, 38, 3, 3, 3]], [[1, 63, 1, 1], [1, 63, 1, 1]], [[1, -34], [1, -34]], [[3, 3000000, 1, 4, -34], [3, 3000000, 1, 4, -34]], [[3000000, 3000000, 3, 3, 3], [3000000, 3000000, 3, 3, 3]], [[True, True, False, True], [False, True, False, False]], [[-70, -57, -93, 2999999, -48, False, False, 81], []], [[True, False], [True, False]], [[3, 3], [3, 3]], [[2, 2, -34, 3], [2, 2, -34, 3]], [[2, 5, 2, 2], [2, 5, 2, 2]], [[63.43122042559975, 63.43122042559975, -31.187672074988427, 63.43122042559975], [63.43122042559975, 63.43122042559975, -31.187672074988427, 63.43122042559975]], [[33.96565948782273, 44.99937757260167, 63.07613966106393, 63.43122042559975], [33.96565948782273, 44.99937757260167, 63.07613966106393, 63.43122042559975]], [[-57, -57, -51, 18, -57], [-57, -57, -51, 18, -57]], [[63.07613966106393, 63.07613966106393, 63.43122042559975, 46.05166169810378, 63.43122042559975, 63.07613966106393], [63.07613966106393, 63.07613966106393, 63.43122042559975, 46.05166169810378, 63.43122042559975, 63.07613966106393]], [[-57, -51, 18, -57], [-57, -51, 18, -57]], [[3, 2, 2], [3, 2, 2]], [[3, 3, 3, -81], [3, 3, 3, -81]], [[-64], [18, 2, 3]], [[2999999, 3000000, 38, 38], [2999999, 3000000, 38, 38]], [[31, 3, 3, 3], [31, 3, 3, 3]]]
results = [False, False, True, False, False, False, True, False, False, False, False, False, True, True, False, False, True, False, True, True, True, False, True, True, True, True, True, False, False, False, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, False, True, True, True, False, True, False, True, True, True, True, True, False, False, True, True, False, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, False, True, True]

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
        func_name = "overlapping"
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
        for test_case in ['assert overlapping([1,2,3,4,5],[6,7,8,9]) == False', 'assert overlapping([1,2,3],[4,5,6]) == False', 'assert overlapping([1,4,5],[1,4,5]) == True']:
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
