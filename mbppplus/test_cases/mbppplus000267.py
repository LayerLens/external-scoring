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
inputs = [[153], [259], [4458], [12345678901234567890], [12345678901234567889], [12345678901234567891], [12345678901234567892], [12345678901234567888], [12345678901234567893], [12345678901234567887], [12345678901234567886], [12345678901234567894], [12345678901234567885], [3], [12345678901234567895], [72], [71], [2], [1], [12345678901234567896], [73], [12345678901234567884], [4], [74], [70], [68], [12345678901234567883], [21], [22], [12345678901234567882], [75], [67], [20], [12345678901234567881], [12345678901234567897], [44], [69], [12345678901234567880], [12345678901234567879], [64], [76], [12345678901234567878], [12345678901234567898], [66], [5], [12345678901234567899], [19], [65], [12345678901234567901], [45], [43], [83], [63], [42], [18], [23], [41], [12345678901234567900], [12345678901234567902], [62], [53], [17], [82], [84], [12345678901234567905], [52], [51], [46], [24], [50], [16], [6], [61], [12345678901234567903], [49], [85], [86], [7], [25], [87], [60], [54], [40], [47], [12345678901234567906], [8], [48], [89], [26], [9], [12345678901234567907], [77], [59], [55], [10], [78], [15], [88], [90], [12345678901234567904], [14], [56], [12345678901234567908], [11]]
results = [True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "armstrong_number"
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
        for test_case in ['assert armstrong_number(153)==True', 'assert armstrong_number(259)==False', 'assert armstrong_number(4458)==False']:
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
