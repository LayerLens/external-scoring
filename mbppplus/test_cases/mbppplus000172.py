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
inputs = [[25, 55, 65], [20, 10, 30], [15, 45, 75], [5, 5, 5], [-10, -20, -30], [-5, -10, -15], [-10, 20, 30], [-15, 0, 15], [-50, -20, 100], [-20, -19, 100], [5, 4, 4], [5, 0, 5], [-18, 99, 100], [-15, -15, 15], [-5, 99, 100], [-15, -14, 15], [-16, -18, 100], [-10, -30, -30], [18, -10, 57], [30, -30, -29], [4, 99, 100], [-11, 18, -10], [-20, 57, -16], [5, -9, 57], [-50, 100, -20], [4, -19, 4], [-16, -19, 100], [-31, 57, -20], [57, -18, 57], [-18, 99, 99], [-50, 15, -20], [4, 98, -5], [-20, -21, -30], [30, 31, -20], [-29, -50, 100], [-19, 4, 4], [-29, -30, -50], [20, 0, 15], [-19, -21, -30], [5, -15, 5], [-18, 99, 20], [-17, -18, -18], [5, 31, 4], [31, -29, -29], [3, 4, 3], [4, 100, 98], [4, 3, 4], [15, -30, -20], [-10, -10, -10], [5, -18, 4], [-30, 5, 5], [-20, -19, -19], [-10, -50, 15], [-31, 99, -5], [0, 20, 30], [-15, 98, -14], [5, 5, 57], [4, 57, -20], [3, 4, 4], [100, 99, 30], [-16, -18, 101], [5, -11, 57], [5, 5, 4], [3, 3, 3], [-15, -31, 15], [-5, -10, 5], [99, 30, 31], [57, -19, 4], [-20, -21, -31], [3, 3, 4], [20, 30, 30], [-20, -31, -31], [-20, -22, -31], [-29, -30, -30], [98, -18, -13], [100, -15, 98], [-66, 55, -22], [100, 99, 100], [101, -20, -50], [3, 101, 3], [57, 0, 15], [5, 4, 5], [-66, -20, 55], [-13, -11, 55], [100, 98, 100], [-21, -30, -30], [-29, -20, -31], [-17, 30, 30], [3, 101, -13], [4, 4, 4], [99, -9, -6], [-50, 15, -21], [100, -31, 100], [5, 57, -20], [-22, -18, -18], [-10, 5, -9], [-19, -20, 55], [4, 5, 4], [6, -11, 57], [57, 0, 14], [30, 14, 14], [0, 15, 20], [101, 18, -9], [16, -50, 15], [-18, -10, 100], [0, 3, -13], [4, 3, 3], [30, 31, -15], [6, 15, 57]]
results = [55, 20, 45, 5, -20, -10, 20, 0, -20, -19, 4, 5, 99, -15, 99, -14, -16, -30, 18, -29, 99, -10, -16, 5, -20, 4, -16, -20, 57, 99, -20, 4, -21, 30, -29, 4, -30, 15, -21, 5, 20, -18, 5, -29, 3, 98, 4, -20, -10, 4, 5, -19, -10, -5, 20, -14, 5, 4, 4, 99, -16, 5, 5, 3, -15, -5, 31, 4, -21, 3, 30, -31, -22, -30, -13, 98, -22, 100, -20, 3, 15, 5, -20, -11, 100, -30, -29, 30, 3, 4, -6, -21, 100, 5, -18, -9, -19, 4, 6, 14, 14, 15, 18, 15, -10, 0, 3, 30, 15]

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
        func_name = "median_numbers"
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
        for test_case in ['assert median_numbers(25,55,65)==55.0', 'assert median_numbers(20,10,30)==20.0', 'assert median_numbers(15,45,75)==45.0']:
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
