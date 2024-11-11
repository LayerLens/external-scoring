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
inputs = [['011001', 6], ['11011', 5], ['1010', 4], ['1100110011', 5], ['0000', 3], ['10000100110011', 5], ['10000100110011', 3], ['11001100111100110011', 5], ['00011001100110', 4], ['1000110011100110', 4], ['11001100111100110011', 3], ['000110011000', 4], ['110011001111001100110001100111001101', 5], ['000110011000', 5], ['1000110011100110', 3], ['110011001111001100111100110011', 5], ['11001100111110011001111001100110001100111001101100110011', 5], ['00011001100110', 3], ['10001110011100110', 4], ['1000011001100111001100111100111001111001100110001100111001101', 5], ['10001100111001110001100111001100', 3], ['10001100111001110001100111001100', 5], ['110011001111001100111100110011', 4], ['11001100111110011001111001100110001100111001101100110011', 4], ['110011001111001100111100110011', 6], ['11001100111100110011', 6], ['1100110011110011001110100110011', 4], ['110011001111100110011110011001100001100110011', 4], ['1000000110011000110011100110', 4], ['110011001111100110011110011001100011001110101101100110011', 4], ['11001100111100110011', 7], ['110011001111001100110001100111001101', 7], ['1100110011110011001100110011110011001111', 7], ['1000111001111001100111100110011100110', 3], ['1000000110011000110011100110', 3], ['110011001111100110011110011001100011001110101101100110011', 7], ['1000011001100111001100111100111001111001100110001100111001101', 7], ['11001100111100110011110011001', 4], ['00011001100110', 5], ['1000011001100111001100111100111001111001100110001100111001101', 6], ['0001100110010', 5], ['1110011001111001100111100110011001100111110011001111001100110001100111001101100110011', 5], ['1100110011110011001100110011110011001111100110011110011001100011001110011011', 7], ['1100110011110011001111', 4], ['00110011001111001100111010011001100', 3], ['0001100110010', 7], ['11001100111100111100110011110011001100110011110011001111100110011110011001100011001110011011001111', 4], ['1000111001111001100111100110011100110', 4], ['1100110011110011001100110011110011001111', 4], ['11001100111100111000010011001100111100110011', 5], ['00110011001111001100111010011001100', 5], ['10001100111001110001100111001100', 2], ['1100110011110011100001001100110011110011001100110011001111001100111010011001100', 5], ['1000110011100110', 5], ['11001100111100110011110011001', 7], ['001100110011110011001110100110110011001111001100110011001111001100111110011001111001100110001100111001101101100', 5], ['00011110011001111100110011110011001100011001110011011001100110011000', 4], ['1100110011110011001111', 6], ['10001110011110011001111001100011100110', 4], ['11001100111110011001111001100110001100111001101100110011', 3], ['1000000110011000110011100110', 2], ['1100110011110011001100110011110011001111', 2], ['10000100110011', 7], ['1100110001111100110011110011001100011001110101101100110011', 7], ['110011001111001100110001100111001101', 6], ['110011001111001', 4], ['1110011001111001100111100110011001100111110011001111001100110001100111001101100110011', 7], ['11001100011111001100111100110001100011001110101101100110011', 7], ['11001100111100111000010011001100111100110011', 4], ['11001100111100110011101001010011', 3], ['1000110011100110', 6], ['000110011000110011001000110', 4], ['1000110011100111000110011100110011001111001100111100110011100', 7], ['11001100111100110011101001010011', 2], ['110011001111001100011101001010011', 2], ['000110011000110011001000110', 2], ['11001100111100110011101001010011', 1], ['110011001111001110000100110011001111100110011', 5], ['110011001111001100101000110011000111110011001111001100011000110011101011011001100111100111001101', 5], ['1100110011001100111100110011110011001001100101000110011000111001111001100011000110011101011011001100111100111001101', 5], ['111001100111100110011110010110011', 5], ['110011001111001100110011001111001110000100110011001111100110011011101001010011', 5], ['1000011001100111001100111100111001111001100110001100111001101', 4], ['110011001111001100110001100111001101', 8], ['110011001111001100110011001111001110000100110011001111100110011011101001010011', 1], ['1000110011100110', 7], ['110011001111100110011110011001100001100110011', 7], ['11001110011001111001100110001100111001101100111100111000010011001100111100110011', 6], ['1100110011110011000111001001010011', 5], ['110011001111001100111001001010011', 2], ['0001100011000110011001000110', 8], ['1100110011110011100001001100110011111100110011110011001110100110011100110011', 5], ['1000000110011000110011100110', 7], ['001100110011110011001110100110110011001111001100110011001111001100111110011001111001100110001100111001101101100', 4], ['11001100111100110011110011001', 8], ['000110011000110011001000110', 5], ['110011001111001100011101001100110011110011001110100110110011001111001100110011001111001100111110011001111001100110001100111001101101100001010011', 2], ['11001100111100111100110011110011001100110011110011001111100110011110011001100011001110011011001111', 7], ['1100110100110011', 6], ['111001100111100110011110010110011', 7], ['110011001111001100111001001010011', 6], ['11001100111100110011110011001', 5], ['11100110011110011001111001100110011001111100110011110011001100011001110011100110011110011001111001100110011001111100110011110011001100011001110011011001100111', 7], ['11001100111110011001111001100110001100111001101100110011', 6], ['0001110000001100110001100111001101001000110', 4]]
results = [3, 4, 2, 3, 0, 1, 1, 3, 1, 1, 2, 1, 3, 2, 1, 3, 3, 0, 1, 1, 1, 2, 2, 2, 4, 4, 2, 2, 1, 2, 4, 4, 4, 1, 1, 4, 3, 2, 2, 2, 2, 3, 4, 2, 1, 2, 2, 1, 2, 3, 2, 1, 3, 2, 4, 2, 1, 4, 1, 2, 1, 2, 2, 4, 4, 2, 5, 4, 2, 2, 3, 1, 3, 2, 2, 0, 1, 3, 3, 3, 3, 3, 1, 4, 1, 3, 4, 4, 3, 2, 2, 3, 1, 2, 4, 2, 2, 4, 4, 5, 4, 3, 5, 4, 1]

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
        func_name = "odd_Equivalent"
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
        for test_case in ['assert odd_Equivalent("011001",6) == 3', 'assert odd_Equivalent("11011",5) == 4', 'assert odd_Equivalent("1010",4) == 2']:
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
