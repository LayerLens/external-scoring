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
inputs = [[[1, 2, 3]], [[4, 5, 6, 1]], [[1, 2, 3, 9]], [[9, 3, 2, 1]], [[9, 8, 7, 6, 5, 4, 3, 2, 1]], [[9, 9, 3, 2, 2, 1]], [[9, 9, 3, 2, 2, 1, 1]], [[9, 8, 7, 6, 5, 4, 3, 3, 2, 1]], [[9, 8, 8, 7, 7, 6, 6, 5, 3, 3, 2]], [[9, 3, 3, 2, 1]], [[9, 3, 3, 3, 2, 1]], [[9, 3, 3, 3, 2, 2, 1]], [[9, 8, 7, 6, 5, 4, 3, 2, 2, 1]], [[9, 3, 2, 2, 1]], [[9, 9, 9, 3, 2, 2, 1]], [[9, 4, 3, 2, 1]], [[9, 5, 3, 2, 1]], [[9, 3, 2, 2, 2, 1]], [[9, 9, 9, 3, 2, 2, 1, 1]], [[9, 5, 2, 1]], [[9, 3, 2, 2, 2, 2, 1]], [[9, 9, 3, 3, 3, 2, 2, 1]], [[9, 8, 7, 6, 5, 4, 4, 3, 2, 1]], [[9, 4, 3, 2, 2, 2, 1]], [[9, 9, 9, 3, 2, 2, 1, 1, 1, 1]], [[9, 8, 7, 6, 5, 4, 4, 4, 3, 2, 1]], [[9, 9, 3, 2, 1]], [[9, 9, 3, 2, 2, 2]], [[9, 9, 9, 3, 2, 2, 2]], [[9, 8, 7, 6, 5, 5, 4, 2, 1]], [[9, 5, 5, 2, 1]], [[9, 9, 3, 3, 3, 3, 2, 2, 1]], [[9, 4, 3, 2, 2, 1, 1]], [[9, 4, 3, 3, 2]], [[9, 9, 3, 2, 2, 1, 1, 1]], [[9, 9, 3, 2, 2]], [[9, 8, 7, 6, 5, 4, 3, 3, 1]], [[9, 9, 9, 3, 2, 2]], [[9, 9, 7, 2, 1]], [[9, 4, 4, 3, 2, 1]], [[9, 9, 7, 3, 2, 2]], [[9, 6, 3, 2, 1, 1]], [[9, 3, 3, 3, 2, 1, 1]], [[9, 4, 3, 2, 1, 1]], [[9, 6, 3, 2, 2, 1, 1]], [[8, 7, 7, 6, 5, 4, 3, 2, 2, 1]], [[6, 5, 3, 2, 1, 1]], [[9, 6, 3, 2, 2, 2, 1, 1]], [[9, 9, 3, 3, 3, 3, 2, 2, 1, 1]], [[9, 9, 9, 3, 2, 2, 2, 2]], [[9, 9, 3, 3, 2]], [[9, 5, 3, 2, 2, 1]], [[9, 9, 5, 2, 1]], [[9, 9, 3, 3, 2, 1]], [[9, 5, 2, 2]], [[9, 9, 4, 4, 2, 2, 1]], [[9, 9, 1]], [[9, 3, 3, 2, 2, 2, 1]], [[9, 4, 3, 3, 2, 0]], [[9, 8, 7, 6, 6, 5, 3, 3, 2]], [[9, 5, 5, 2, 1, 1, 1, 1]], [[9, 9, 2, 0]], [[9, 8, 6, 5, 4, 3, 2, 1]], [[6, 5, 3, 2, 2, 1, 1]], [[9, 9, 7, 7, 2, 1]], [[6, 5, 3, 3, 2, 2, 2, 1]], [[9, 3, 3, 2, 2, 1]], [[9, 3, 3, 2, 2, 2, 2, 1]], [[9, 3, 3, 2, 2, 2]], [[9, 9, 9, 3, 2, 2, 1, 1, 1]], [[9, 6, 5, 4, 3, 2, 1]], [[9, 6, 3, 2, 1, 1, 0]], [[9, 8, 7, 6, 5, 4, 4, 3, 3, 2, 1]], [[9, 9, 3, 3, 2, 2, 1, 1, 1]], [[9, 6, 3, 2, 2, 1, 1, 1]], [[9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 1]], [[9, 4, 3, 3, 1, 1]], [[6, 4, 3, 2, 2, 1, 1, 1]], [[9, 5, 4, 3, 2, 2, 1, 1]], [[9, 8, 7, 5, 5, 4, 2, 1]], [[8, 7, 7, 6, 5, 4, 2, 2, 1]], [[9, 9, 3, 3, 2, 2, 1]], [[9, 9, 7, 3, 2, 2, 1, 1]], [[9, 9, 3, 3, 3, 3, 3, 2, 2, 1, 1]], [[9, 6, 3, 1, 1, 0]], [[9, 8, 7, 7, 6, 5, 4, 3, 2, 2, 1]], [[9, 9, 9, 3, 3, 2, 2]], [[9, 5, 5, 2]], [[9, 9, 9, 9, 3, 3, 2, 2, 1, 1, 1]], [[9, 9, 9, 3, 2, 2, 2, 1, 1, 1]], [[9, 8, 7, 6, 5, 4, 3, 3, 3, 2, 1]], [[9, 9, 3, 3, 3, 3, 2, 1, 1]], [[8, 7, 7, 6, 5, 5, 4, 2, 2, 1]], [[9, 9, 3, 3, 2, 2, 1, 1, 1, 1]], [[9, 6, 5, 2, 1]]]
results = [321, 6541, 9321, 9321, 987654321, 993221, 9932211, 9876543321, 98877665332, 93321, 933321, 9333221, 9876543221, 93221, 9993221, 94321, 95321, 932221, 99932211, 9521, 9322221, 99333221, 9876544321, 9432221, 9993221111, 98765444321, 99321, 993222, 9993222, 987655421, 95521, 993333221, 9432211, 94332, 99322111, 99322, 987654331, 999322, 99721, 944321, 997322, 963211, 9333211, 943211, 9632211, 8776543221, 653211, 96322211, 9933332211, 99932222, 99332, 953221, 99521, 993321, 9522, 9944221, 991, 9332221, 943320, 987665332, 95521111, 9920, 98654321, 6532211, 997721, 65332221, 933221, 93322221, 933222, 999322111, 9654321, 9632110, 98765443321, 993322111, 96322111, 98765443211, 943311, 64322111, 95432211, 98755421, 877654221, 9933221, 99732211, 99333332211, 963110, 98776543221, 9993322, 9552, 99993322111, 9993222111, 98765433321, 993333211, 8776554221, 9933221111, 96521]

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
        func_name = "find_Max_Num"
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
        for test_case in ['assert find_Max_Num([1,2,3]) == 321', 'assert find_Max_Num([4,5,6,1]) == 6541', 'assert find_Max_Num([1,2,3,9]) == 9321']:
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
