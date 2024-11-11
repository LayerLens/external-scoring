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
inputs = [['A'], ['R'], ['S'], ['@'], ['®'], ['!'], [' '], ['ص'], ['&'], ['\n'], ['€'], ['^'], ['ä'], ['π'], ['~'], ['\t'], ['©'], ['๑'], ['$'], ['7'], ['%'], ['['], ['{'], ['é'], ['\x00'], ['\x1d'], ['♥'], ['\uffff'], ['\x7f'], ['\x80'], ['™'], ['文'], ['→'], ['F'], ['q'], ['E'], ['o'], ['W'], ['U'], ['O'], ['K'], ['v'], ['Z'], ['N'], ['P'], ['b'], ['y'], ['l'], ['V'], ['D'], ['u'], ['s'], ['I'], ['h'], ['H'], ['B'], ['k'], ['X'], ['L'], ['p'], ['Y'], ['c'], ['J'], ['T'], ['a'], ['e'], ['r'], ['G'], ['j'], ['m'], ['z'], ['n'], ['g'], ['t'], ['i'], ['d'], ['M'], ['x'], ['f'], ['C'], ['Q'], ['w']]
results = [65, 82, 83, 64, 174, 33, 32, 1589, 38, 10, 8364, 94, 228, 960, 126, 9, 169, 3665, 36, 55, 37, 91, 123, 233, 0, 29, 9829, 65535, 127, 128, 8482, 25991, 8594, 70, 113, 69, 111, 87, 85, 79, 75, 118, 90, 78, 80, 98, 121, 108, 86, 68, 117, 115, 73, 104, 72, 66, 107, 88, 76, 112, 89, 99, 74, 84, 97, 101, 114, 71, 106, 109, 122, 110, 103, 116, 105, 100, 77, 120, 102, 67, 81, 119]

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
        func_name = "ascii_value"
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
        for test_case in ["assert ascii_value('A')==65", "assert ascii_value('R')==82", "assert ascii_value('S')==83"]:
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
