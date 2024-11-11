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
inputs = [[1, 2], [23, 56], [123, 256], [123456789, 987654321], [12345, 9], [9876543210, 123], [11111111, 99999999], [98765, 54321], [999999, 111111], [0, 987654321], [987654321, 23456789], [123456789123456789, 987654321987654321], [1000000, 999999], [9999, 8888], [123456789, 123], [1, 1234567890], [12345, 567891], [0, 256], [123, 0], [0, 0], [123, 456789], [12345, 5678], [1111, 2222], [1020304, 2030405], [1, 9], [10000000, 9999999], [200, 500], [3000, 30], [10, 256], [123, 5], [10, 10], [9999999999, 1111111111], [123, 256789], [23, 568], [0, 1], [1, 0], [1, 1], [3, 0], [24, 30], [9876543, 12], [8888, 9999], [5678, 1000000], [256, 256], [9999, 0], [123, 122], [30, 2], [123456788, 123456789], [1234567888, 1234567889], [1000000, 256], [12, 256], [256, 456789], [11, 256], [99999999, 99999999], [1234567889, 568], [1, 5], [23456788, 23456789], [123, 123], [54321, 0], [56, 9876543], [500, 500], [10000000, 10000000], [23456787, 23456789], [999999, 456789], [10001, 10000], [1111, 2223], [5, 568], [98765, 98765], [1111111111, 1111111111], [201, 500], [201, 123456788], [3, 2223], [456788, 456788], [23456788, 11111111], [567890, 567891], [54321, 123], [123456789, 123456789], [999999, 0], [2, 1], [10000, 123456788], [8889, 8888], [10, 8888], [1, 1111111111], [1111111111, 1111111110], [456787, 123], [98766, 54321], [256789, 1000000], [456789, 456789], [202, 201], [123456789123456789, 1234567890], [23456787, 23456788], [1111111110, 1111111110], [5678, 987654321987654320], [11111111, 123456789], [1000001, 256], [1111111112, 1], [1, 123], [456788, 123456789123456789], [2, 2], [1234567889, 202], [9, 56], [11, 11], [3, 2], [567, 568], [567890, 567890], [256, 3], [257, 257], [10, 499], [9, 256], [1000000, 1000000], [123456789, 123456790], [99999999, 3000], [98765, 987654321], [568, 8888], [0, 11111111], [8889, 8889], [1000003, 1000001], [456788, 456789], [1111111111, 9], [1111111111, 11], [5678, 9999], [8889, 56], [12346, 9], [9999, 2], [999998, 999999], [6, 5], [201, 200], [98765, 568], [8888, 8888], [99999999, 456789], [9999999999, 9999999999], [1000001, 1000001], [255, 256], [23456788, 8888], [123456788, 256], [501, 456789], [255, 1000001], [5678, 12], [1111111111, 2224], [987654321, 987654321], [9, 2030405]]
results = [1, 6, 7, 40, 8, 18, 64, 20, 48, 9, 32, 80, 53, 4, 0, 0, 20, 2, 1, 0, 9, 16, 4, 4, 8, 62, 3, 0, 6, 4, 0, 80, 7, 6, 1, 1, 0, 3, 5, 14, 4, 25, 0, 9, 1, 1, 1, 1, 12, 4, 2, 5, 0, 13, 4, 1, 0, 5, 6, 0, 0, 2, 15, 1, 5, 0, 0, 0, 4, 5, 1, 0, 35, 1, 6, 0, 9, 1, 14, 1, 15, 0, 1, 9, 21, 36, 0, 1, 1, 1, 0, 8, 28, 12, 0, 0, 17, 0, 4, 4, 0, 1, 1, 0, 1, 0, 12, 7, 0, 10, 33, 0, 5, 1, 0, 2, 1, 8, 0, 10, 5, 8, 7, 1, 1, 1, 7, 0, 15, 0, 0, 1, 18, 7, 11, 11, 8, 6, 0, 7]

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
        func_name = "digit_distance_nums"
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
        for test_case in ['assert digit_distance_nums(1,2) == 1', 'assert digit_distance_nums(23,56) == 6', 'assert digit_distance_nums(123,256) == 7']:
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
