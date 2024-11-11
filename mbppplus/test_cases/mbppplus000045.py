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
inputs = [[1212121], [1991], [121], [2121212121212121], [2121212121212122], [2121212121212119], [2121212121212123], [2121212121212124], [2121212121212125], [2121212121212120], [2121212121212118], [2121212121212126], [2121212121212117], [2121212121212127], [82], [40], [83], [39], [81], [2121212121212116], [2121212121212128], [2121212121212115], [41], [80], [19], [20], [42], [84], [18], [2121212121212129], [43], [21], [62], [17], [85], [2121212121212130], [79], [12], [2121212121212131], [86], [44], [52], [16], [11], [53], [63], [10], [78], [51], [61], [87], [50], [77], [54], [92], [55], [49], [22], [96], [38], [97], [56], [23], [91], [2121212121212114], [15], [93], [24], [48], [89], [60], [64], [65], [37], [76], [59], [35], [88], [2121212121212132], [58], [14], [94], [9], [47], [95], [66], [57], [36], [8], [13], [25], [45], [90], [2121212121212113], [67], [46], [7], [68], [75], [34], [2121212121212133], [2121212121212134], [26], [74]]
results = [True, False, True, True, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, False, False, False, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, False, True, True, False, True, True, True, True, True, True, True, True, False, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, True, True, False, True, True, False, True, True, False, True, True, True, True, False, True, True, False, True, True, True, False, False, True, True]

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
        func_name = "is_undulating"
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
        for test_case in ['assert is_undulating(1212121) == True', 'assert is_undulating(1991) == False', 'assert is_undulating(121) == True']:
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
