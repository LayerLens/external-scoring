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
inputs = [[18], [30], [6], [101], [997], [9973], [99991], [1000003], [102], [998], [9974], [1000004], [999], [1000005], [1000006], [1000], [9972], [9975], [996], [99992], [103], [1000007], [99993], [995], [1000008], [True], [99989], [99988], [False], [1001], [1000010], [99990], [1002], [1003], [1000009], [994], [104], [993], [84], [992], [9971], [85], [23], [99994], [83], [9970], [86], [991], [87], [1004], [24], [25], [9], [105], [9976], [1000011], [82], [106], [26], [99995], [9977], [39], [27], [10], [107], [28], [8], [88], [22], [38], [1000002], [9969], [99996], [990], [21], [7], [108], [1005], [81], [1000001], [100], [40], [20], [19], [3], [1000012], [5], [55], [89], [1000000], [37], [9968], [41], [999998], [999997], [2], [9967], [9965], [109], [1000013], [90], [99997], [9966], [99998], [999999], [111], [1006]]
results = [26, 48, 8, 0, 0, 0, 0, 0, 144, 1000, 9976, 1546020, 0, 0, 1142880, 2184, 21684, 0, 2016, 181440, 0, 0, 0, 0, 2882880, 0, 0, 171456, 0, 0, 1309248, 190944, 1344, 0, 0, 1152, 196, 0, 192, 1984, 0, 0, 0, 106836, 0, 11976, 88, 0, 0, 1512, 56, 0, 0, 0, 18480, 0, 84, 108, 28, 0, 0, 0, 0, 12, 0, 48, 14, 168, 24, 40, 1333344, 0, 215712, 1872, 0, 0, 240, 0, 0, 0, 186, 84, 36, 0, 0, 1615488, 0, 0, 0, 2460906, 0, 21600, 0, 1040448, 0, 2, 0, 0, 0, 0, 156, 0, 14592, 100000, 0, 0, 1008]

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
        func_name = "sumofFactors"
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
        for test_case in ['assert sumofFactors(18) == 26', 'assert sumofFactors(30) == 48', 'assert sumofFactors(6) == 8']:
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
