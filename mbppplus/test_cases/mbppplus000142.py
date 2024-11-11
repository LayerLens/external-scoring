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
inputs = [[[1, 2, 3]], [[1, 2, 1, 2]], [[1, 2, 3, 4, 5]], [[1, 2, 3, 4, 1]], [[1, 'a', 2.5, 'b', 1, 2.5, 'c']], [[]], [[1]], [[1, 'a', 2.5, 'b', 2.5, 'c']], [[1, 'a', 2.5, 'b', 'b', 2.5, 'c', 'c']], [['', 1, 'a', 2.5, 'b', 1, 2.5, 'c']], [[1, 'a', 2.5, 'b', 2.5, 'c', 2.5]], [[1, 'a', 2.5, 'b', 1, 2.5, 'c', 'b']], [[1, 'a', 2.5, 2.4132043402592354, 2.5, 'c']], [[1, 'a', 2.5, '', 'b', 1, 2.5, 'c', 'b']], [[1, 'a', 'b', 1, 2.5, 'c']], [[1, 'a', 2.5, 'b', 2.5, 'c', 2.5, 'b']], [[2]], [[1, 2, 3, 4, 1, 4]], [[1, 'a', 2.5, 'b', 1, 2.5, 'c', 'b', 2.5]], [[2, 2]], [[1, 'c', 'b', 1, 2.5, 'c']], [[1, 'a', 2.5, 2.5, 'c']], [[1, 1]], [[1, 'a', 2.5, 'b', 2.5, 'c', 'c']], [[1, 'a', 'b', 2.5, 'c', 'cc']], [[1, 'a', 2.5, 'b', 'b', 2.5, 'ac', 'c', 'c']], [[1, 'a', 2.5, 'b', 'b', 'ac', 'c', 'c']], [[1, 'a', 2.5, '', 'b', 1, 2.5, 'b']], [[1, 2, 3, 4, 1, 1]], [[2, 'a', 2.5, '', 'b', 1, 2.5, 'b']], [['', 1, 'a', 2.5, 'b', 1, 2.5, 'c', '']], [[1, 2]], [[1, 2, 5, 3, 4, 1, 4, 5, 2]], [[1, 'c', 'cb', 1, 2.4132043402592354, 'c']], [[1, 'a', 2.5, 'b', 1, 2.5, 'c', 'b', 'a']], [[1, 2, 3, 2, 1, 4, 2]], [['', 1, 'a', 2.5, 'cb', 1, 2.5, 'c', '']], [[1, 'a', 2.5, '', 'b', 1, 2.5, 2.5, 'b', 2.5]], [[1, 'a', 2.4132043402592354, 2.5, 'c']], [[3, 5, 3, 4, 1, 4, 5, 2]], [[1, 2, 3, 3, 2, 2, 4, 2]], [[-97.72133553330038, -22.07383795649666, 2.5, -29.118774451154366, -56.59753538486449, 12.066693167589861, 44.74013652952752, 2.5, -21.841980273620436, 2.4132043402592354]], [[1, 'a', 2.5, 'b', 'b', 'c', 'c']], [[2, 2, 2]], [[1, 2, 3, 3, 2, 2, 4, 2, 2]], [[1, 'a', 2.0407928337162407, 'b', 2.5, 'c']], [[3]], [[5, 4, 5, 5]], [[1, 'a', 2.5, 1, 2.5, 'c', 'b', 1]], [[1, 'a', 2.5, 'b', 2.5, 'c', 'b', 2.5, 'b']], [[1, 'a', 'cc', 'b', 'ac', 'c', 'c']], [['a', 2.5, 'b', 1, 'bb', 2.5, 'c', '']], [[1, 'a', 2.0407928337162407, 'b', 'c']], [[1, 'a', 2.5, 2.311342558914553, 'c', 2.5]], [[-13, 1]], [[1, 'a', 2.5, 'b', 2.5, 'c', 'c', 'c', 1]], [[2, 3]], [[1, 2, 2, 2]], [[1, 'a', 2.5, 'b', 'b', 'c', 'c', 'a']], [[1, 'c', 'b', 1, 2.5, 'c', 'b']], [[1, 'a', 2.5, 'b', 'b', 'b', 2.5, 'ac', 'c', 'c']], [[1, 'cc', 'cb', 1, 2.5, 'c']], [[2, 'a', 'c', 2.5, '', 'b', 1, 2.5, 'b']], [[1, 'c', 'cb', 2.4132043402592354, 'c']], [[1, 2, 3, 3, 2, 2, 2, 4, 2, 2]], [[-14, 1]], [[1, 'a', 2.5, 2.5, 'c', 2.5]], [[1, 'a', 'b', 1, 2.5]], [[4, 4]], [[2, 2, -14, 2]], [[1, 2, 5, 3, 4, 1, 4, 5, 3, 2]], [[1, 2, 3, 3, 2, 2, 3, 2, 4, 5, 2, 2]], [['a', 2.5, 'b', 2.5, 'cc', 'c']], [[1, 'a', 2.5, '', 'b', 1, 2.5, 2.5, 'b', 2.5, '']], [[1, 'a', 2.5, 'b', 1, 2.5, 1]], [[1, 'a', 2.5, 'b', 'c', 'bc', 2.5, 'b']], [[-13, -37, -14, -37]], [[1, 'bb', 'a', 2.5, 'b', 2.9537947452443776, 'c', 2.5]], [[1, 'a', 2.4132043402592354, 2.5, 3, 'c']], [[1, 2, 3, 3, 2, -14, 3, 2, 4, 5, 2, 2]], [[2, 5, 3]], [['a', 'b', 1, 2.5, 'c']], [[1, 'a', 2.5, '', 'b', 1, 3.2945116598503565, 'c', 'b']], [[1, 'a', 2.5, '', 'b', 1, 2.5, 2.311342558914553, 'b', 2.5]], [[1, 2, 5, 3, 4, 1, 4, 3, 2]], [[-97.72133553330038, -22.07383795649666, 2.5, -29.78635935943484, -56.59753538486449, 12.066693167589861, -56.59753538486449, 2.5, -21.841980273620436, 2.4132043402592354]], [['a', 'b', 1, 2.5, 'c', 'b']], [[1, 'a', 2.5, 'cb', 'b', 'b', 2.5, 'c', 'c']], [[-21.841980273620436, 1, 'a', 2.5, 2.5, 'c', 2.5]], [[1, 'a', 2.5, 2.589643424113979, 2.5, 'c']], [[1, 'a', 2.5, '', 'ac', 1, 2.5, 2.311342558914553, 'b', 2.5]], [[1, 2, 2]], [['', 1, 'a', 2.5, 'cb', 1, 2.5, 'c', -14, '']], [[2, 3, 4, 1, 4]], [[1, 'a', 2.5, 5, '', 'b', 1, 2.5, 2.5, 'b', 2.5, '']], [[1, 'a', 2.5, 'cc', 'b', 'b', 2.5, 'c', 'c']], [[1, 'a', 2.5, '', 'b', 1, 2.5, 'b', 2.5]], [[1, -37, -14, -37]], [[1, 'aa', 'a', 2.5, 'b', 1, 2.5, 'c', 'b']], [[1, 'bbb', 'a', 2.5, 'b', 3.3482302076342627, 1, 2.5, 'c', 'b', 'a', 3]], [[1, 2.5, 'b', 'b', 'c', 'c', 'a']], [['', 1, 'a', 2.5, 'b', 1, 'a', 2.5, 'c']], [[1, 'a', 2.5, 'cb', 'b', 'b', 2.5, 'c', 'c', 'b']], [['cc', '', 1, 'a', 2.5, 'cb', 1, 2.5, 1, 'c', '']], [[1, 'ac', 'bbb', 2.5, '', 'b', 1, -22.07383795649666, 'c', 'b']], [[1, 2, 3, 4, 1, 4, 5, 3, 2]]]
results = [True, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "all_unique"
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
        for test_case in ['assert all_unique([1,2,3]) == True', 'assert all_unique([1,2,1,2]) == False', 'assert all_unique([1,2,3,4,5]) == True']:
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
