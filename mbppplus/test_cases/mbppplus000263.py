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
inputs = [['216.08.094.196'], ['12.01.024'], ['216.08.094.0196'], ['0.0.0.0'], ['0.0.00.0.0.0.0'], ['0.0.0.00'], ['0.00.0.00.0.0.0.0.0.00'], ['00.0.0.0.0.0.00'], ['0.00.0.00.0.00.00.0.00.0.0.0.0.0.00.0.0.0.00'], ['0.0.00.0.0.0'], ['ogsr'], ['0.00.0.00.0.0.0.0.0ogsr00'], ['0.0.0.0.0.00.0.0.0.000'], ['0.00.0.00.0.000.00'], ['0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0.0.0.000'], ['ogs0.00.0.00.0.000.00r'], ['0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.000'], ['0.0.00.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.000.00'], ['0.0.0.0.0.00.0.0.0.0.0.00.0.0.0000'], ['oggsr'], ['0.0.0.0.00.00.0.0.0.000'], ['0.0.00.0.0.0.00.0.00.0..00.000.0.00.0.0.0.0.0.00.0..0.0.000.00'], ['0.00.0.00.0.00.0.00.0.0.0.00.0.00.0..00.000.0.00.0.0.0.0.0.00.0..0.0.000.00.0.0.0.00'], ['0.0.00.0.0.0.00.0.00.0..00.000.0.00.0.0.0.0.0.00.0..0.00.000.00'], ['0.0.0.0.00.0.00.0.00.0000.0.00.0.0.0.0.0.00.0.0.0.000'], ['0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.000.0.00.0.0.0.0.0.00.0.0.0.000'], ['0.00.0.000.0.0.0.00.00.0.0.0.00000.00'], ['0.0.0.0.0.0.00.0.0.0.000'], ['0.0.00.0.0.0.00.0.000.0..00.000.0.00.0.0.0.0.0.00.0..0.0.000.00'], ['0.00.0.000.0.00.0.0.0.0.00.0.0.0.0.0.00.0.0.00000.00'], ['00.0.0.00'], ['0.0.0.0.00..00.0.0.0.000'], ['0.0.0.0.00.0.00.0.000'], ['0.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.000'], ['0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.00'], ['0.0.0.0..00..00.0.0.0.000'], ['00.0.0.0.00.0.0.0.00.0.00.0..00.000.0.00.0.0.0.0.0.00.0..0.00.000.000.00'], ['00.0.0..0.0.0.00'], ['0.0.0.0.0..0.0.0000'], ['0.00.0.000.00.0.000.0.00.0.0.0.0.00.0.0.0.0.0.00.0.0.00000.00.0.0.0.0.0.00'], ['0.0.00.0.0.0.00.0.000.0..00.000.0.00.0.0.0.0.0.00.0..0.0.000.000.0.0.0.0.00..0.0.0.000'], ['0.0.0.0.0.0.00.00.0.0.000'], ['0.00.0.00.0.0.00.0.0ogsr00'], ['0.00.0.000.0.00.0.0.0.0.0.0.0.0.0.00.0.0.00000.00'], ['00.0.0.000.0.0.0.0..0.0.0000'], ['ogs00.0.0..0.0.0.00r'], ['0.000.0.000'], ['0.0.000.0.0'], ['0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.00000.00.0000.00'], ['0..0.0.00.00.00.0.0.000'], ['oggosr'], ['0.00.0.00.0.00.00.0.00.0.0.0.00.0.00.0.00.0000.0.00.0.0.0.0.0.00.0.0.0.0000.0.0.0.0.0.00.0.0.0.00'], ['00.0.0.0.00.0.0.0.00.0.00.0..00.000.0.00.0.0.0.00.0.0.0.0..0.0.0000.000.000.00'], ['ogs0.00.0.00.0.000.00.0.000.0.00r0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.00'], ['0.0.00.0.0.0.00.00.0.0.000'], ['.0.0.0.0.00..00.0.0.0.000'], ['00.0.00.0.00.0.0.0.00.0.000.0..00.000.0.00.0.0.0.0.0.00.0..0.0.000.00..0.00'], ['0.00.0.00..0'], ['0.00.0.00.0.00.0.00.0.0.00.00.0.00.0..00.000.0.00.0.0.0.0.0.00.0..0.0.000.00.0.0.0.00'], ['0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.000.0.0.0.0.0.00.0..0.0.00000.00.0000.00'], ['0.00.0.0000.0.00.0.0.0.0.00.0.0.0.0.0.00.0.0.00000.00'], ['0.0.0.0.00.0.00.0.00.ogs0.00.0.00.0.000.00.0.000.0.00r0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.00000.0.00.0.0.0.0.0.00.0..0.0.000'], ['0.0.0.0.00.0.00.0.00.0000.0.0.0.0.0.0.0.0.00.0..0.0.000'], ['0.0.00.00'], ['0.0.0.0.00.000.0.0.0.000'], ['0.0.0.0.00..00.0..0.0.000'], ['0.0.00.0.0.0.000'], ['0.0.0.0.00.000.0.0ogs00.0.0..0.0.0.00r.0.000'], ['0.00.0.0.00.0.00.0.00.0000.0.00.0.0.0.0.0.00.0.0.0.000'], ['00.0.00.0.00.0.0.0.00.0.000.0..00.000.0.00.0.0.0.0.0.00.0..0.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.0.000.00..0.00'], ['0.0.00.0.0.0.000.00'], ['0.0.0.0.000.0.000'], ['00.0.0'], ['0.00.00.00.0.00.00.0.00.0.0.0.0.0.00.0.0.0.00'], ['0.0.0.0.0.00.0.0.0.0.0.00.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.000'], ['0.0.0.0.00.0.00.0.00.ogs0.00.0.00.0.000.00.0.000.0.00r0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.00000.0.00.0.0.0.0.0.00.0.0.0.00..00.0..0.0.0000.0..0.0.000'], ['0.00.0.00.0.00.00.0.00.0.0.0.00.0.00.0.00.0000.0.00.0.0.0.0.0.00.0.0.0.0000.0.0.0.0.00.000.0.000.00.0.0.0.00'], ['0.0.000.00.0.00.0.000.0.00.0.0.0.0.00.0.0.0.0.0.00.0.0.00000.00'], ['0.00.0.00.0.00.00.0.00.0.0.0.0.0.0.0.0.0.0.00'], ['0.000.0.000.000.0.00.0.0.0.0.0.00.0.0.00000.00.0.0.0.0.0.00'], ['0..0.0.00.00.00.0.0.00000.0.0.0.00.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.000.0.00'], ['0.0.0.0.000.00.0.0.00.0.00.0.00.0000.0.00.0.0.0.0.0.00.0.0.0.000.00.0.0.0.000'], ['0.0.00.0.0.0.00.00.0.0.0.000000.0.00.0.0.0.0.0.00.0..0.0.000.00'], ['00.00.0.00.0.0.0.0.0ogsr00.00.0.00.0.0.0.0.0.00'], ['Q'], ['00.0.'], ['0.00.0.00.0.00.00.0.00.0.0.0.00.0.00.0.00.0000.0.00.0..0.0.0.0.00.0.0.0.0000.0.0.0.0.0.00.0.0.0.00'], ['0.0.0.0.00.0.0.0.00.00.0.0.0.000000.0.00.0.0.0.0.0.00.0..0.0.000.000.000'], ['0.0.0.0.00.0.00.0.00.ogs0.00.0.00.0.000.00..0.000.0.00r0.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.00000.0.00.0.0.0.0.0.00.0.0.0.00..00.0..0.0.0000.0..0.0.000'], ['Q0.0000.0.000'], ['g00.00.0.00.0.0.0.0.0ogsr00.00.0.00.0.0.0.0.0.00'], ['0.000.0.0.0.00.0.00.0.00.000.0.00.0.0.0.000.0.00.0.0.0.0.0.00.0.0.0.000.0.00.0.00.00.0.00.0.0.0.00.0.00.0.00.0000.0.00.0..0.0.0.0.00.0.0.00.0.0.0.0000.0.0.0.0.0.00.0.0.0.00'], ['0.00.0.0.00.0.00.0.00.0000.00.00.0.0.0.0.0.00.0.0.0.000'], ['ogs0.ogsr0.0.000.00r'], ['0.00.0.0000.0.0.0.0..0.0.0000.0.0.0.00.00.0.0.0.00000.0.0'], ['0.0.0.0.00.000.0.0ogs00.0.0..0.000.0.000.000.0.00.0.0.0.0.0.00.0.0.00000.00.0.0.0.0.0.000.0.0.00r.0.000'], ['0.00.0.0.0..00'], ['.0.0.0.0.00.0.00.0.000'], ['0.00.0.0.00.0.00.0.00.0000.00.0.0.000.0.0.0.0..0.0.000000.00.0.0.0.0.0.00.0.0.0.000'], ['o0.00.0.00.0.00.00.0.00.0.0.0.0.0.00.0.0.0.00ggsr'], ['0.00.00.00.0.00.00.0.000.0.0.0.0.0.00.0.0.0.00'], ['0.0.00.0.00.0.0.0.000.00.0.00..00.0.0.0.000'], ['0..0.0.00.00.00.0.0.00000.0.0.0.00.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.00.00.0.00.00.0.00.0.0.0.000.0.0.0.0.00.0.0.0.0.0.00.0.00.0.00.000.0.00.0.0.0.0.0.00.0..0.0.0000.00.0000.00.000.0.00'], ['000.0.']]
results = ['216.8.94.196', '12.1.24', '216.8.94.196', '0...', '0......', '0...', '0.........', '00......', '0..................', '0.....', 'ogsr', '0........ogsr00', '0.........', '0......', '0.....................', 'ogs0......r', '0......................', '0.........................', '0..............', 'oggsr', '0.........', '0..........................', '0...................................', '0..........................', '0.....................', '0...........................', '0.............', '0..........', '0..........................', '0....................', '00...', '0..........', '0........', '0...............................', '0..........................................', '0...........', '00.............................', '00.......', '0........', '0.............................', '0....................................', '0..........', '0........ogsr00', '0...................', '00...........', 'ogs00.......r', '0...', '0....', '0..........................................', '0.........', 'oggosr', '0.......................................', '00...............................', 'ogs0..........r0..........................................', '0..........', '...........', '00...............................', '0.....', '0...................................', '0..........................................', '0....................', '0.........ogs0..........r0.......................................................', '0.......................', '0...', '0.........', '0...........', '0......', '0.......ogs00.......r..', '0.....................', '00..............................................................', '0.......', '0......', '00..', '0..................', '0..............................', '0.........ogs0..........r0..................................................................', '0..........................................', '0........................', '0...................', '0......................', '0.....................................', '0..............................', '0.........................', '00........ogsr00.........', 'Q', '00..', '0........................................', '0............................', '0.........ogs0...........r0..................................................................', 'Q0...', 'g00........ogsr00.........', '0......................................................................', '0.....................', 'ogs0.ogsr0...r', '0......................', '0.......ogs00.............................r..', '0......', '.........', '0................................', 'o0..................ggsr', '0..................', '0.................', '0...............................................................................', '000..']

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
        func_name = "removezero_ip"
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
        for test_case in ['assert removezero_ip("216.08.094.196")==(\'216.8.94.196\')', 'assert removezero_ip("12.01.024")==(\'12.1.24\')', 'assert removezero_ip("216.08.094.0196")==(\'216.8.94.196\')']:
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
