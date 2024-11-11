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
inputs = [[3, 4], [2, 3], [5, 5], [4, -2], [-2, 3], [0, 5], [-3, -4], [0, 10], [10, -1], [0, 0], [2, -3], [1, 100], [-1, 100], [5, 10], [5, 0], [-3, 2], [0, 9], [-1, 10], [0, 4], [5, -2], [4, 9], [-2, -2], [1, 99], [100, 5], [99, 2], [100, 100], [-4, -2], [100, 3], [0, 3], [5, 11], [4, 1], [-2, 0], [4, 4], [100, 6], [100, 4], [11, 5], [-4, -4], [5, 9], [11, 99], [100, -1], [6, 6], [-1, -1], [3, 0], [2, 2], [9, -1], [-4, 2], [-2, 5], [6, 0], [5, 4], [-1, 0], [99, 4], [-1, 9], [5, 2], [99, 1], [11, -1], [-4, 7], [7, 0], [98, 3], [100, -2], [99, -1], [3, 7], [-3, -3], [1, 6], [3, 1], [3, 8], [99, 99], [100, 9], [-1, 98], [7, -1], [9, 99], [5, 8], [11, 3], [3, -3], [2, 5], [99, -4], [5, 101], [9, 9], [8, 3], [99, -3], [1, 10], [7, 1], [101, 100], [8, 0], [100, 101], [4, 8], [2, 4], [3, 3], [8, 4], [101, -2], [98, 102], [8, 8], [2, -4], [-2, 101], [-1, -2], [100, 7], [-3, -2], [1, 2], [9, 3], [7, 7], [4, 3], [2, -2], [11, 10], [1, 0], [5, -3], [99, 3], [98, 2], [8, 7], [3, 6], [1, -1], [-1, 8], [101, 6]]
results = [81, 8, 3125, 0.0625, -8, 0, 0.012345679012345678, 0, 0.1, 1, 0.125, 1, 1, 9765625, 1, 9, 0, 1, 0, 0.04, 262144, 0.25, 1, 10000000000, 9801, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 0.0625, 1000000, 0, 48828125, 4, 1, 256, 1000000000000, 100000000, 161051, 0.00390625, 1953125, 12527829399838427440107579247354215251149392000034969484678615956504532008683916069945559954314411495091, 0.01, 46656, -1.0, 1, 4, 0.1111111111111111, 16, -32, 1, 625, 1, 96059601, -1, 25, 99, 0.09090909090909091, -16384, 1, 941192, 0.0001, 0.010101010101010102, 2187, -0.037037037037037035, 1, 3, 6561, 369729637649726772657187905628805440595668764281741102430259972423552570455277523421410650010128232727940978889548326540119429996769494359451621570193644014418071060667659301384999779999159200499899, 1000000000000000000, 1, 0.14285714285714285, 29512665430652752148753480226197736314359272517043832886063884637676943433478020332709411004889, 390625, 1331, 0.037037037037037035, 32, 1.0410203556852167e-08, 39443045261050590270586428264139311483660321755451150238513946533203125, 387420489, 512, 1.0306101521283646e-06, 1, 7, 270481382942152609326719471080753083367793838278100277689020104911710151430673927943945601434674459097335651375483564268312519281766832427980496322329650055217977882315938008175933291885667484249510001, 1, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 65536, 16, 27, 4096, 9.802960494069208e-05, 127367821481320961306779453124811493852927587601071435268660949497933336539304230215165634203675222190265666055792155413670466901678107154499490273199816067233222775795686789175668564014387134300740911104, 16777216, 0.0625, -2535301200456458802993406410752, 1.0, 100000000000000, 0.1111111111111111, 1, 729, 823543, 64, 0.25, 25937424601, 1, 0.008, 970299, 9604, 2097152, 729, 1.0, 1, 1061520150601]

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
        func_name = "power"
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
        for test_case in ['assert power(3,4) == 81', 'assert power(2,3) == 8', 'assert power(5,5) == 3125']:
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
