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
inputs = [['The quick brown fox jumps over the lazy dog.', 'fox'], ['Its been a very crazy procedure right', 'crazy'], ['Hardest choices required strongest will', 'will'], ['', ''], ['rfvPtELLC', ''], ['', 'rfvPtELLC'], ['LC', 'rfvPtELLC'], ['rfvPLCtELLC', 'rfvPtELLC'], ['rfvPtELLC', 'rfvPLCtELLC'], ['LC', ''], ['rfvPLtELLC', 'rfvPtELLC'], ['rfvPtELLC', 'rfvPtELLC'], ['rfvPLCtELLC', 'rfvPLtE'], ['rfvrfvPLtELLCPtELLC', 'rfvPtELLC'], ['', 'rfvPLtELLC'], ['rfvPLCtELLC', 'rfvPLCtEC'], ['rfvPLtE', 'rfvPLttELLC'], ['rfvPLCtELC', 'rfvPLCtELLC'], ['rfvPLttELLC', 'rfvvPtELLC'], ['rfvPrfvPtELLCLtE', 'rfvPLttELLC'], ['rfvrfvPLtELLCPtELLC', 'rfvvPtELLC'], ['rfLCELLC', 'rfvPLCtELLC'], ['rfvPrfvPtELLCLtE', 'rfvPLtELLCLC'], ['rfvPLCtELC', ''], ['rfvvPtELLC', ''], ['rfvPLttELLC', 'rfvPLttELLC'], ['rfvPtELLC', 'rfvvPtELLC'], ['rfvPtELLCLC', 'rfvPtELLC'], ['rfvPLtE', 'rfvPLtE'], ['rfvrfvPLtELLCPtELLC', 'rfrfvPLttELLCPtELLC'], ['rfvPLttELLC', 'rfvPLtELLC'], ['rfvvPEtELLC', 'rfvvPtELLrfvPrfvPtELLCLtEC'], ['rfvPtELLC', 'rfvvPtELLrfvPrfvPtELLCLtEC'], ['rfvvPtELLC', 'rfvvPtELLC'], ['rfvPLtELLCLC', 'rfvPtELLC'], ['rfvvPtELLrfvPrfvPtELLCLtEC', 'LC'], ['rfvrfvPLtELLCPtELLC', ''], ['rfv', 'rfvPLtELLCLC'], ['rfvPLttELLC', 'rfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC'], ['rfvvPtCELLC', 'rfvvPtELLC'], ['rfvPLttELLC', 'rfvPLCtELEC'], ['', 'rfvPLtELLCLC'], ['rfvPLttELLC', 'rfvrfrfvPLCtELLCCLCLC'], ['rfvPLCtELEC', 'rfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC'], ['rfvPLtELLtC', 'rfvtELLC'], ['rfvPLCtELLC', 'rfvPLCtELLC'], ['rfvrPrLtE', 'rfvPLtE'], ['LCrfvPLtE', 'rfvPtELLC'], ['rfvPLtrfvtELLCC', 'rfvPLtrfvtELLCC'], ['rfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC', 'rfvPLCtELLC'], ['rfvPLttELrfvtELLCC', 'rfvPLttELLC'], ['rfvPLtE', 'rfvPLtrfvPrfvPtELLCLtEE'], ['rfvvPtELLC', 'rfvvPtfELLC'], ['rfvPLtrfvtELLCC', 'rfvvPtrfvPLCtELCELLC'], ['rfvPLttrfvvPEtELLC', 'rfvPLCtELEC'], ['rfv', 'rfv'], ['LCrfvPLtE', 'rfvvPtELLrfvPrfvPtELLCLtEC'], ['rfvvPtELLrfvPrfvvPEtELLCrfvrPtELLCLtEC', 'rfvvPtELLrfvPrfvvPEtELLCrfvPtELLCLtEC'], ['rfvPLtC', 'rfvPLttELLC'], ['rfvPLttELLC', 'rfvvrfvvPtELLrfvPrfvPtvELLCLrfvvPtELLCtECPtELLrvPrfvPtELELCLtEC'], ['rfvPLCtrfvPLttELrfvtELLCCELEC', 'rfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC'], ['rfv', 'rffv'], ['rfvPLCtELLC', 'CrfvPLtC'], ['rfvvPtELLrfvPrfvPtELLCLtEC', 'rfvPtELLC'], ['rfvvPtELLrfvPrfvvPEtELLCrfvrPtELLCLtEC', 'rfvPLtELLtC'], ['rfvPLttELLC', 'rfvvPtELLrfvPrfvPtELLCLtEC'], ['rfvPLtttELLC', 'rfvvrfvvPtELLrfvPrfvPtvELLCLrfvvPtELLCtECPtELLrvPrfvPtELELCLtEC'], ['rfvvPtELLC', 'rfvvPtfELCLLC'], ['rfvPLtC', 'rfvPLtrfvvPtELLrfvPrfvvPEtELLCrfvPtELLCLtECtELLC'], ['rfvrfvrfrfvPLttELLCPtELLCtELLC', 'rfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC'], ['rfvrfvPLtELLCPtELLC', 'rfvrfvPLtELLCPtELLC'], ['rfvvPtELLrfvPrfvvPEtELLCrfvrPtELLCLtEC', 'rfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC'], ['rfvPrfvPtELLCLtE', 'rfrfvvrfvvPtELLrfvPrfvPtvELLCLrfvvPtELLCtECPtELLrvPrfvPtELELCLtECLtELLCLC'], ['rfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtECrfvvPtELLC', 'rfvPLttELLC'], ['rfvPLtC', 'rfCLtEC'], ['rfCLtECLLC', 'rfvPLtELLC'], ['rfvPLtELLC', 'rfvvPtfELLC'], ['rfvPLtELLC', 'rfvtELLC'], ['rfvvPEtELLC', 'rfCLtEC'], ['rfvPLtC', 'rfvPLtrfvvPtEPLLrfvPrfvvPEtELLCrfvPtELLCLtECtELLC'], ['rfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPrfvrfrfvPLCtELLCCLCLCtELLrvPrfvPtELLCLtEC', 'rfCLtECLLC'], ['rrfvvPEtELLCfvPLttELLC', 'rfvvrfvvPtELLrfvPrfvPtvELLCLrfvvPtELLCtECPtELLrvPrfvPtELELCLtEC'], ['rfrfvPLCtELLCvvPtELLrfvPrfvPtELLCLtEC', 'rfvvPtELLrfvPrfvPtELLCLtEC'], ['rfrfvPLttELLCPtELLCrfvPLtELLtC', 'rfrfvPLttELLCPtELLC'], ['rfvPLtELLrfvPLCtECC', 'rfvtELLC'], ['rrfvvPEtELLCfvPLttELLC', 'rfvPLtE'], ['rfrfvPLttELLCPtELLCrfvPLtELLtC', 'rfrfvPLttECLLCPtELLC'], ['rfvPLttELLLC', 'rfvvPtELLrfvPrfvPtELLCrfvPLCtECLtEC'], ['frffv', 'frffv'], ['rfv', 'rfvPLCtELC'], ['rfvrfvPLtELLCPtELLC', 'rfrLCrfvPLtEfvPLttELLCPtELLC'], ['rfvvPtELLC', 'rfvPLCtECrfvvEPtfELLC'], ['rfvvPtfELLC', 'rfvPLtELLC'], ['rfvvPtELLrfvPrfvvPEtELLCrfvrPtELLCLtEC', 'rfvPLCtELEC'], ['rfvrrfvPLCtECrfvrfvvPtELLrfvPrfvvPEtELLCrfvrPtELLCLtECvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPrfvrfrfvPLCtELLCCLCLCtELLrvPrfvPtELLCLtECfrfvPLCtELLCCLCtLC', 'rfvrrfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPrfvrfrfvPLCtELLCCLCLCtELLrvPrfvPtELLCLtECfrfvPLCtELLCCLCtLC'], ['rLfrfrfvPLttELLCPtELLCvPLttELLC', 'rLfvPLttELLC'], ['rfvPLtrfvvPtELLrfvPrfvvPEtELLCrfvPtELLCLtECtELLC', 'rfvPtELLC'], ['rfvPLtE', 'rfvvPLtE'], ['rfvrPrLtE', 'rfvPLCtECrfvvrfvvPtELLrfvPrfvPtELLCLrfvvPtELLCtECPtELLrvPrfvPtELLCLtEC'], ['rfvvPvEtELLC', 'rfvvPtELLrfPrfvPtELLCLtEC'], ['rfvPrfvPtELLCLtE', 'rfvPrfvvPLtELtELLCLC'], ['rLrfvrPrLtEfrfrfvPLttELtELLCvPLttELLC', 'rLfvPLttELLC'], ['rfrfvPLCtELLCvvPtELLrfvPrfvPtELLCLtEC', 'rfvPLrfrLCrfvPLtEfvPLttELLCPtELLC'], ['rfvPrfvPtELLCLtE', 'rfCLtECLLC']]
results = [('fox', 16, 19), ('crazy', 16, 21), ('will', 35, 39), ('', 0, 0), ('', 0, 0), None, None, None, None, ('', 0, 0), None, ('rfvPtELLC', 0, 9), None, None, None, None, None, None, None, None, None, None, None, ('', 0, 0), ('', 0, 0), ('rfvPLttELLC', 0, 11), None, ('rfvPtELLC', 0, 9), ('rfvPLtE', 0, 7), None, None, None, None, ('rfvvPtELLC', 0, 10), None, ('LC', 20, 22), ('', 0, 0), None, None, None, None, None, None, None, None, ('rfvPLCtELLC', 0, 11), None, None, ('rfvPLtrfvtELLCC', 0, 15), None, None, None, None, None, None, ('rfv', 0, 3), None, None, None, None, None, None, None, ('rfvPtELLC', 13, 22), None, None, None, None, None, None, ('rfvrfvPLtELLCPtELLC', 0, 19), None, None, None, None, None, None, None, None, None, None, None, None, ('rfrfvPLttELLCPtELLC', 0, 19), None, None, None, None, ('frffv', 0, 5), None, None, None, None, None, None, None, ('rfvPtELLC', 30, 39), None, None, None, None, None, None, None]

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
        func_name = "find_literals"
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
        for test_case in ["assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)", "assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)", "assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)"]:
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
