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
inputs = [[7], [4], [9], [10000000], [1000000000], [999999999], [1], [2], [123456789], [99999999], [1000000001], [10000001], [3], [19], [123456790], [100000000], [99999998], [True], [999999998], [9999999], [1000000002], [20], [10000002], [10000003], [18], [16], [999999997], [17], [10000004], [100000001], [100000002], [51], [10000005], [123456791], [21], [100000003], [9999997], [999999996], [22], [10000006], [52], [23], [123456788], [9999998], [123456792], [53], [99999997], [54], [61], [99999996], [62], [15], [123456787], [9999996], [14], [24], [50], [99999995], [5], [49], [123456793], [10000007], [9999995], [10000008], [100000004], [25], [99999994], [123456794], [123456786], [68], [67], [999999995], [69], [13], [10000009], [48], [66], [123456795], [10], [6], [123456785], [60], [123456796], [100000005], [59], [12], [58], [47], [123456784], [55], [74], [99999993], [1000000003], [11], [10000010], [123456797], [123456783], [9999994], [63], [8], [75], [26], [99999991], [999999993], [9999993], [99999992], [1000000004], [29], [99]]
results = [11, 7, 13, 10000024, 1000000030, 1000000029, 3, 5, 123456816, 100000026, 1000000031, 10000025, 6, 24, 123456817, 100000027, 100000025, 3, 1000000028, 10000023, 1000000032, 25, 10000026, 10000027, 23, 21, 1000000027, 22, 10000028, 100000028, 100000029, 57, 10000029, 123456818, 26, 100000030, 10000021, 1000000026, 27, 10000030, 58, 28, 123456815, 10000022, 123456819, 59, 100000024, 60, 68, 100000023, 69, 20, 123456814, 10000020, 19, 29, 56, 100000022, 9, 55, 123456820, 10000031, 10000019, 10000032, 100000031, 30, 100000021, 123456821, 123456813, 75, 74, 1000000025, 76, 18, 10000033, 54, 73, 123456822, 14, 10, 123456812, 67, 123456823, 100000032, 66, 17, 65, 53, 123456811, 61, 81, 100000020, 1000000033, 15, 10000034, 123456824, 123456810, 10000018, 70, 12, 82, 31, 100000018, 1000000023, 10000017, 100000019, 1000000034, 35, 106]

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
        func_name = "is_polite"
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
        for test_case in ['assert is_polite(7) == 11', 'assert is_polite(4) == 7', 'assert is_polite(9) == 13']:
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
