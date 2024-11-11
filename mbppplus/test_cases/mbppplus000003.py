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
inputs = [[13, 9], [15, 8], [2, 4], [2, 3], [5, 1], [1, 5], [0, 0], [-10, 10], [100, 100], [-50, -100], [123456789, -987654321], [-123456789, -987654321], [1000000000, 1000000001], [0, 1], [-100, -100], [-123456789, 0], [-10, -987654321], [1000000000, 100], [10, 0], [-101, -100], [1000000000, 1000000000], [10, 10], [-1, 0], [-101, 100], [-2, -2], [-123456789, -10], [-50, -50], [-50, -101], [-101, 1000000001], [1, -987654320], [-101, -101], [-11, -987654321], [-50, -102], [-3, 1], [-987654321, -987654320], [-987654321, -100], [0, 1000000001], [-50, -987654321], [-102, -987654321], [-102, 1], [1000000000, 10], [123456789, 1], [-10, -10], [10, -987654320], [-1, 1], [-101, -102], [-11, 0], [-1, -100], [-3, -987654320], [1, -50], [-123456789, -50], [-2, -1], [123456789, -2], [-2, -4], [-101, 10], [-2, 123456789], [-2, -987654321], [-1, -1], [1000000001, 1000000001], [-1, -2], [-50, 1000000000], [-3, -987654321], [-51, -50], [1, -1], [-100, -2], [1000000000, 101], [1000000000, -51], [-49, -102], [-102, -100], [-123456789, -123456789], [-51, -51], [-9, 10], [-4, -101], [-102, -101], [2, 2], [-50, -99], [-1, 101], [-2, -11], [-3, -2], [-987654321, -10], [-100, -49], [False, True], [True, True], [-987654321, -987654321], [123456789, -4], [123456789, 100], [9, 10], [-987654321, 1], [-3, -1], [-102, -102], [101, -101], [11, 10], [-50, -49], [False, False], [123456789, -50], [-10, 1], [-3, -51], [1, -10], [-10, 11], [-102, 2], [8, 8], [123456787, 1], [-987654321, 101], [9, -123456788], [8, -50], [-101, -3], [-123456788, 1000000000], [-12, 0], [-50, -1], [-987654320, 2], [-4, -123456789], [-2, -10], [-12, -101], [-9, -1]]
results = [True, False, False, True, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True]

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
        func_name = "is_Power_Of_Two"
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
        for test_case in ['assert differ_At_One_Bit_Pos(13,9) == True', 'assert differ_At_One_Bit_Pos(15,8) == False', 'assert differ_At_One_Bit_Pos(2,4) == False', 'assert differ_At_One_Bit_Pos(2, 3) == True', 'assert differ_At_One_Bit_Pos(5, 1) == True', 'assert differ_At_One_Bit_Pos(1, 5) == True']:
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
