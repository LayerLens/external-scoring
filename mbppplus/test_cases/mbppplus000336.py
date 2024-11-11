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
inputs = [['123.11'], ['e666.86'], ['3.124587'], ['1.11'], ['1.1.11'], ['1..2'], ['1.1$'], ['123.1111'], ['-123.11'], ['       123.11       '], [''], ['123'], ['.'], ['$123.11'], ['1.1.1'], ['1231.1111'], ['1..21..2'], ['13.1123$'], ['-1123.11'], ['TDH'], ['-1123.11123.11'], ['1..21.1.1'], ['123.       123.11       1'], ['11'], ['13.11$23$'], ['TD'], ['$12.11'], ['..'], ['$123.1..21.1.111'], ['$1123.       123.11       123.11'], ['123.'], ['1323.1.1.1'], ['KehoROOXec'], ['-123.113.11$23$1'], ['13.123$'], ['$.12.11'], ['-3.11'], ['$123.111..21.1.111'], ['123.1.1$11'], ['TTDH'], ['...'], ['13.11$1123.       123.11       123.113$'], ['-123.113.11$1'], ['$1123.'], ['1123.1123.1111'], ['1123.1123.11111231.1111'], ['1.11$'], ['1233.'], ['1231'], ['T..D'], ['1..      11 123.11       2'], ['1..'], ['1323.1TD.1.1'], ['$-123.113.11$11123.'], ['KehoROOXec1h.1.1'], ['-1123.11123.121'], ['TD$123.11'], ['-123.       123.11       1123.111'], ['1.1..'], ['KehoROOXe.c1h.1.1'], ['TD1231'], ['13123.1.1.1'], ['1123.1123.11111231.13.11$1123.       123.11       123.113$1111'], ['13.123-3.11$'], ['$1123. .      123.11       123.11'], ['123.       123.11  TD$123.11    2 1'], ['13123.13.1.1'], ['.....'], ['       123.-123.1111       '], ['123.       123.11  TD $123.11    2 1'], ['13.1123-3.11$'], ['131..3-3.11$'], ['131..3-3.113.123-3.11$1$'], ['o'], ['123.       123.11       1.'], ['1.'], ['12123.       123.11       13.1.1$11'], ['1231.1..      11 123.11       21111'], ['TD-1123.1112...3.11'], ['123-123.       123.11       1123.111'], ['1.111$'], ['1123.11123.11111231.13.11$1123.       123.11       123.113$1111'], ['13.1.1$11'], ['12311'], ['12123.  13123.1.1.1     123.11       13.1.1$11'], ['1231.1..      11 123.11  -123.113.11$23$1     21111'], ['$11233.121'], ['T'], ['1123.11123.11111231.13.113.'], ['1.1'], ['1'], ['VJ'], ['21111'], ['13.11$1123.       121123.11123.11111231.13.11$1123.3.11       123.113$'], ['-1123.111'], ['1123.111231.1111'], ['12-1123.11123.'], ['-123.          1123.111'], ['13.11$1123.       121123.11123.11111231.13.11$1123.3.11       123.1112313$'], ['T3D-1123.1112...3.11'], ['123.11123313$'], ['13.1.131..3-3.113.123-3.11$1$1$11'], ['1$123.11323.1.1.1'], ['1231.1..      11 123. 11       21111'], ['1123-123.      '], ['123.13111'], ['131..3-3.1TD$123.11$'], ['-1123.11123.11111231.13.11$1123.       123.11       123.113$1111.11'], ['1KehoROOXec'], ['12123.     1231.1..      11 123. 11       21111'], ['TD-1123.1131..3-3.1TD$123.11$112...3.11'], ['1231.11111'], ['1$123.113223.1.1.$12.11'], ['       1-123.113.11$23$123.11       ']]
results = [True, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "is_decimal"
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
        for test_case in ["assert is_decimal('123.11')==True", "assert is_decimal('e666.86')==False", "assert is_decimal('3.124587')==False", "assert is_decimal('1.11')==True", "assert is_decimal('1.1.11')==False"]:
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
