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
inputs = [[2, 3, 7], [4, 2, 7], [1, 13, 17], [100, 50, 4000], [25, 10, 500], [7, 11, 123], [25, 123, 500], [100, 4000, 4000], [4000, 4000, 4000], [4000, 50, 4000], [25, 123, 7], [500, 50, 4000], [50, 500, 50], [6, 122, 7], [7, 123, 7], [100, 4000, 50], [500, 50, 500], [4000, 50, 50], [6, 122, 122], [7, 123, 123], [50, 123, 7], [122, 7, 122], [122, 7, 11], [123, 25, 50], [4001, 50, 50], [4000, 50, 501], [122, 101, 100], [25, 10, 10], [25, 10, 501], [500, 6, 123], [7, 123, 500], [501, 123, 7], [50, 124, 7], [100, 122, 100], [123, 26, 25], [50, 50, 50], [4001, 26, 25], [499, 50, 4000], [4000, 50, 499], [103, 102, 102], [123, 7, 123], [50, 3999, 4000], [500, 50, 6], [4000, 499, 4000], [101, 103, 4001], [25, 500, 123], [25, 26, 123], [499, 4000, 499], [4000, 11, 4000], [25, 50, 4000], [49, 7, 7], [7, 7, 123], [499, 4000, 4000], [6, 500, 50], [500, 50, 501], [500, 51, 500], [4001, 4001, 499], [4001, 4001, 4001], [499, 4000, 6], [500, 51, 6], [100, 500, 500], [4000, 7, 124], [25, 500, 25], [4000, 49, 50], [499, 499, 4000], [50, 123, 123], [6, 4000, 50], [100, 103, 4001], [50, 121, 122], [501, 8, 7], [25, 499, 25], [10, 10, 500], [4000, 4001, 4000], [4000, 3999, 499], [101, 101, 4001], [500, 50, 7], [3999, 123, 7], [25, 25, 10], [11, 123, 11], [101, 101, 6], [50, 4000, 4000], [100, 51, 4000], [10, 500, 10], [101, 25, 50], [501, 7, 7], [50, 4000, 3999], [10, 500, 25], [25, 499, 123], [501, 49, 6], [102, 102, 102], [121, 4000, 51], [502, 123, 7], [50, 3998, 501], [25, 121, 121], [25, 9, 9], [501, 7, 502], [11, 25, 11], [3999, 101, 500], [7, 12, 500], [7, 122, 7], [499, 6, 499], [25, 11, 25], [499, 11, 4000], [121, 4000, 121], [50, 102, 50], [7, 8, 123]]
results = [(2, 1), None, (4, 1), (0, 80), (0, 50), (5, 8), (20, 0), (0, 1), (0, 1), (0, 80), None, (0, 80), (1, 0), None, (1, 0), None, (0, 10), (0, 1), (0, 1), (0, 1), None, (1, 0), None, (0, 2), (0, 1), None, None, (0, 1), None, None, None, None, None, (1, 0), None, (0, 1), None, (0, 80), None, (0, 1), (1, 0), (80, 0), None, (1, 0), (8, 31), None, None, (1, 0), (1, 0), (0, 80), (0, 1), None, (0, 1), None, None, (1, 0), None, (0, 1), None, None, (0, 1), None, (1, 0), None, None, (0, 1), None, None, None, None, (1, 0), (0, 50), (1, 0), None, None, None, None, None, (1, 0), None, (0, 1), (40, 0), (1, 0), (0, 2), (0, 1), None, None, None, None, (0, 1), None, None, None, (0, 1), (0, 1), None, (1, 0), None, (8, 37), (1, 0), (1, 0), (1, 0), None, (1, 0), (1, 0), (5, 11)]

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
        func_name = "find_solution"
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
        for test_case in ['assert find_solution(2, 3, 7) == (2, 1)', 'assert find_solution(4, 2, 7) == None', 'assert find_solution(1, 13, 17) == (4, 1)']:
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
