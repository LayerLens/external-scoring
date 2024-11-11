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
inputs = [[['green', 'orange', 'black', 'white'], 'blue'], [[1, 2, 3, 4], 7], [['green', 'green', 'green', 'green'], 'green'], [[], 'red'], [['a', 'a', 'a', 'a', 'a'], 'a'], [[], 'green'], [[], []], [[], 'a'], [['a', 'a', 'a', 'a', 'a'], 'reda'], [[], 'reda'], [['a', '', 'a', 'a', 'a'], 'a'], [[], 'gren'], [['a', '', 'a', 'a', 'a'], 'ared'], [['a', '', 'a', 'green', 'a', 'a'], 'ared'], [[], 'ared'], [['a', '', 'a', 'redaa', 'green', 'a', 'a'], 'red'], [['a', '', 'a', 'a', 'a', 'a'], 'ared'], [['a', '', 'a', 'a', 'a'], 'aredd'], [['a', '', 'a', 'a', 'a'], 'gren'], [[], ['IMSzNXr']], [[], [False, True, True, False, True, False, True, True, False]], [[], ['red', 'HwtScMmS', 'jjtLKAcXm']], [['a', '', 'a', 'redaa', 'green', 'a', 'a'], 'aa'], [['a', 'a', 'areda', 'a', 'a', 'a'], 'a'], [['a', 'a', 'a', 'a', 'a'], 'gren'], [['a', 'a', 'a', 'a', 'a', 'a', 'a'], 'gren'], [['', 'a'], 'red'], [['a', 'a', 'a', 'a', 'a'], 'HwtScMmS'], [[], 'gaan'], [['a', 'a', ''], 'gren'], [['a', '', 'a', 'a', 'a'], 'reda'], [['a', 'a', ''], 'gregren'], [['a', 'aa', 'a', 'a', 'a'], 'reda'], [[], ['red', 'HwtScMmS', 'jjtLKaredaAcXm']], [['a', 'a', 'a', 'a', 'a', 'a'], 'a'], [['a', 'a', 'areda', 'a', 'a', 'a'], 'gregren'], [['red', '', 'CeR'], 'reda'], [['a', '', 'a', 'green', 'a', 'a'], 'areed'], [['a', 'a', 'a', 'jjtLKAcXm', 'a', 'a', 'a'], 'gren'], [['', 'a', 'a', 'a', 'a'], 'gaan'], [[], ''], [[], [[56.04013492061608, 22.809175570261317, -19.209978650818854], -9.19614909867073, ['CeR', 'aa', 'reda', 'cX', 'sqkDTbEWNY', 'gaan', 'aa', 'reda'], 'reda', -9.19614909867073]], [['red', '', 'CeR'], 'rda'], [['a', '', 'a', 'redaa', 'green', 'a', 'a'], 'rd'], [['red', 'gregren', '', 'CeR'], 'rda'], [[], [-8.3015872751577, -1.6872782556751815, -37.057532027723326, 56.04013492061608, 22.809175570261317]], [[], 'gregren'], [[], [-8.3015872751577, -1.6872782556751815, -37.057532027723326, 56.04013492061608, 22.809175570261317, -37.057532027723326]], [[], [-8.3015872751577, -1.6872782556751815, -37.057532027723326, 56.04013492061608, 22.809175570261317, 22.809175570261317]], [['red', 'IMSzNXr', 'gregren', 'CeRHwtScMmS'], 'red'], [['aredaa', '', 'a', 'a', 'a'], 'green'], [['red', 'gregren', 'CeRHwtScMmS'], 'red'], [['a', 'a', 'a', 'a', 'a', 'a', 'a'], 'sqkDTbEWNY'], [['a', '', 'a', 'redaa', 'a', 'a'], 'red'], [['Zwm', 'iAz', 'IEnmyrIGhY', 'EKrcuFaZ'], 'green'], [['a', '', 'a', 'redaa', 'areedgreen', 'a', 'a'], 'aa'], [['a', 'a', 'redaaa', 'a', 'a'], 'HwtScMmS'], [['a', '', 'a', 'a', 'a', 'a'], 'ard'], [['red', 'gregren', 'CEKrcuFaZwtScMmS'], 'red'], [['a', 'a', 'a', 'a'], 'a'], [[], ['rd', 'mlOBNlC', '', 'Zwm', 'gregren', 'Zwm']], [['a', 'a', 'a', 'iAz', 'a', 'a', 'aa', 'a'], 'sqkDTbEWNY'], [[], [-8.3015872751577, -1.6872782556751815, -37.057532027723326, 56.04013492061608, 22.809175570261317, -8.3015872751577]], [['a', 'a', 'redaaa', 'a', 'a'], 'areed'], [['Zwm', 'IEnmyrIGhY', 'EKrcuFaZ'], 'green'], [['a', 'a', 'a', 'a'], 'jjtLKaredaAcXm'], [['a', '', 'a', 'a', 'a', 'a', ''], 'ard'], [[], [-19.209978650818854, -37.057532027723326, 87.86645974977819, 32.00129666267674, -1.606104157903161, -82.74767724499756, -93.4885457411899, -19.209978650818854, 56.04013492061608]], [['a', 'a', 'areda', 'a', 'a', 'a'], 'rdegren'], [['a', 'a', 'HwtScMmS'], 'gregren'], [['a', 'a', 'areda', 'a', 'a'], 'gregren'], [['a', '', 'a', 'redaa', 'green', 'a', 'a', 'a'], 'rd'], [[], ['IMSzNXr', 'IMSzNXr']], [['areed', '', 'a', 'redaa', 'a'], 'jjtLKaredaAcXma'], [['aredaa', '', 'CeR', 'CeR'], 'rda'], [[], [-14, 78, False, True, False, -17, False, -99, True, -79]], [[], [[56.04013492061608, 22.809175570261317, -19.209978650818854, -19.209978650818854], [56.04013492061608, 22.809175570261317, -19.209978650818854, -19.209978650818854], -9.19614909867073, 'reda', -9.19614909867073]], [['red', '', 'CeR'], 'red'], [['', 'jjtLKAcXm', 'aa'], 'red'], [['red', '', 'CeR', ''], 'red'], [['a', '', 'a', 'redaa', 'a', 'a'], 'IMSzNXr'], [['a', '', 'aa', 'a', 'a', 'a'], 'ard'], [['Z', 'red', 'Utyz', 'cAvkmuMOrX', 'TaK'], 'green'], [['cX', '', 'a'], 'mlOBNlC'], [['a', '', 'a', 'redaa', 'green', 'a', 'a', 'a', 'a'], 'rd'], [[], 'ggreen'], [['a', 'a', 'a'], 'jjtLKaredaAcXm'], [['red', 'IMSzNXr', 'gregren', 'CeRHwtScMmS'], 'dred'], [['Zwm', 'iAz', 'IEnmyrIGhY', 'EKrcuFaZ'], 'gereen'], [['a', 'a', 'a', 'a'], 'jjtLKaredaAcXmIMSzNXr'], [['a', 'a', 'a', 'a', 'a', 'a', 'a'], 'areda'], [[], 'redea'], [[], ['rXziNV', 'gySc', 'gyScc']], [['a', 'a', 'a', 'a', 'a'], 'jjtLKaredaAcXmIMSzNXr'], [['red', 'gregren', 'CEKrcuFaZwtScMmS'], 'redggreena'], [['red', 'IMSzNXr', 'gregren', 'CeRHwtScMmS'], 'aa'], [['areed', '', 'a', 'redaa', 'a', 'a'], 'jjtLKaredaAcXma'], [['a', '', 'a', 'redaa', 'green', 'a', 'a'], 'iAz'], [['red', 'IMSzNXr', 'gereen', 'CeRHwtScMmS'], 'red'], [['a', '', 'aa', 'Z', 'a', 'a'], 'cX'], [['a', 'ajjtLKaredaAcXma', '', 'a', 'a', 'a'], 'gren'], [['IMSzNXr', 'gregren', 'CeRHwtScMmS'], 'dred'], [['a', '', 'a', 'a', 'a'], 'IEnmyrIGhY'], [['a', '', 'a', 'a', 'a'], 'areed'], [['a', 'a', 'areda', 'a', 'a'], 'grnegren'], [['a', 'a', 'a', 'redaaa', 'a', 'a'], 'areed']]
results = [False, False, True, True, True, True, True, True, False, True, False, True, False, False, True, False, False, False, False, True, True, True, False, False, False, False, False, False, True, False, False, False, False, True, True, False, False, False, False, False, True, True, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "check_element"
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
        for test_case in ['assert check_element(["green", "orange", "black", "white"],\'blue\')==False', 'assert check_element([1,2,3,4],7)==False', 'assert check_element(["green", "green", "green", "green"],\'green\')==True']:
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
