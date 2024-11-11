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
inputs = [[5], [10], [15], [991], [567], [13], [24], [568], [992], [569], [990], [566], [True], [989], [25], [14], [565], [23], [988], [12], [11], [16], [17], [993], [564], [563], [22], [994], [9], [21], [995], [996], [20], [18], [997], [8], [987], [45], [562], [570], [26], [561], [998], [19], [77], [7], [76], [560], [986], [27], [44], [571], [28], [75], [46], [78], [74], [985], [29], [572], [984], [73], [983], [79], [573], [47], [50], [982], [981], [71], [49], [80], [51], [999], [30], [81], [6], [1000], [980], [1001], [1002], [82], [1003], [52], [574], [53], [1004], [70], [575], [69], [576], [979], [83], [72], [68], [43], [89], [42], [977], [33], [4], [36], [978], [3]]
results = [True, False, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, False, False, True, True, True, True, True, True, False, True, False, True, True, True, False, False, True, True, False, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True]

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
        func_name = "dif_Square"
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
        for test_case in ['assert dif_Square(5) == True', 'assert dif_Square(10) == False', 'assert dif_Square(15) == True']:
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
