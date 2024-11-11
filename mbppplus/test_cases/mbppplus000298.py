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
inputs = [[120, 35], [40, 20], [10, 8], [0, 0], [500, -50], [500, 0], [0, 500], [1, 0], [1, 1], [500, 500], [0, 501], [1, -1], [501, -50], [500, 1], [True, False], [501, 501], [False, True], [501, 0], [False, False], [501, 500], [0, 1], [500, 2], [502, 501], [1, 501], [1, 500], [1, -50], [2, 0], [1, -2], [2, 1], [502, -50], [2, -50], [503, 502], [73.15589926015126, 73.15589926015126], [503, 501], [73.15589926015126, 37.688172821388065], [2, -52], [504, 504], [501, 69], [503, 0], [69, 501], [504, 505], [0, 2], [502, 0], [2, 2], [502, 503], [500, 501], [73.99361665758236, 73.15589926015126], [504, 506], [37.688172821388065, 73.15589926015126], [3, -1], [504, 501], [502, 504], [506, 506], [502, 2], [38.526128276032885, 37.688172821388065], [54.35980990509703, 54.35980990509703], [503, 2], [503, -2], [506, 505], [2, 3], [3, -2], [503, 503], [502, 1], [1, 2], [69, 3], [0, 504], [504, 503], [502, 502], [501, -52], [504, 0], [73.99361665758236, 54.35980990509703], [4, -52], [507, 503], [507, 502], [505, 0], [5, -52], [507, 507], [507, 506], [505, 500], [1, 4], [0, 3], [69, -1], [501, 5], [69, 69], [38.526128276032885, 38.526128276032885], [4, -51], [54.35980990509703, 37.688172821388065], [0, -1], [507, 501], [506, 504], [True, True], [504, 2], [74.55187136846823, 73.99361665758236], [500, 505], [507, -52], [3, 501], [499, 500], [500, 502], [3, 500], [501, 499], [503, 4], [5, 5], [504, 5], [73.99361665758236, 73.99361665758236], [499, 1]]
results = [40, 19, 6, 13, -102, -18, 324, 2, 3, 829, 324, 1, -102, -16, 2, 831, 14, -18, 13, 829, 14, -14, 831, 512, 511, -49, 0, 0, 1, -102, -53, 833, 94, 831, 44, -55, 836, 99, -18, 693, 838, 14, -18, 3, 834, 831, 94, 840, 90, -2, 831, 836, 840, -14, 43, 66, -14, -21, 838, 4, -3, 835, -16, 4, -5, 326, 835, 833, -106, -18, 67, -59, 835, 834, -18, -61, 842, 840, 830, 6, 15, -11, -9, 87, 44, -58, 43, 12, 832, 837, 3, -14, 95, 837, -106, 548, 829, 832, 547, 827, -11, 4, -9, 95, -16]

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
        func_name = "wind_chill"
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
        for test_case in ['assert wind_chill(120,35)==40', 'assert wind_chill(40,20)==19', 'assert wind_chill(10,8)==6']:
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
