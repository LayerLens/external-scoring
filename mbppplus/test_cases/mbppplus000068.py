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
inputs = [[999], [9999], [99], [10000], [5000], [4999], [4998], [5001], [90], [92], [89], [91], [10001], [93], [5002], [4997], [True], [94], [4996], [4995], [10002], [88], [10003], [5003], [5004], [21], [87], [22], [4994], [95], [86], [96], [20], [9998], [4993], [23], [47], [97], [5005], [10004], [9], [9997], [10005], [85], [8], [46], [9996], [84], [7], [19], [9995], [98], [10006], [18], [100], [101], [24], [68], [61], [69], [44], [43], [17], [5006], [16], [6], [10], [45], [10007], [66], [15], [83], [48], [9994], [81], [60], [74], [5007], [67], [28], [80], [72], [79], [70], [29], [49], [9993], [65], [4992], [4991], [11], [10008], [73], [12], [62], [71], [4990], [5008], [78], [50], [59], [77], [10009]]
results = [504, 31626, 0, 31626, 8442, 8442, 8442, 8442, 0, 0, 0, 0, 31626, 0, 8442, 8442, 0, 0, 8442, 8442, 31626, 0, 31626, 8442, 8442, 0, 0, 0, 8442, 0, 0, 0, 0, 31626, 8442, 0, 0, 0, 8442, 31626, 0, 31626, 31626, 0, 0, 0, 31626, 0, 0, 0, 31626, 0, 31626, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8442, 0, 0, 0, 0, 31626, 0, 0, 0, 0, 31626, 0, 0, 0, 8442, 0, 0, 0, 0, 0, 0, 0, 0, 31626, 0, 8442, 8442, 0, 31626, 0, 0, 0, 0, 8442, 8442, 0, 0, 0, 0, 31626]

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
        func_name = "div_sum"
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
        for test_case in ['assert amicable_numbers_sum(999)==504', 'assert amicable_numbers_sum(9999)==31626', 'assert amicable_numbers_sum(99)==0']:
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
