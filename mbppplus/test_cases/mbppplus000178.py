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
inputs = [[['Python', 3, 2, 4, 5, 'version']], [['Python', 15, 20, 25]], [['Python', 30, 20, 40, 50, 'version']], [['Python', 10, 5, 2.5, 2.5, 'version']], [['Python', 'version', 'is', '3.8.5', 1, 2, 3, 4, 5]], [['Python', [10, 5, 2.5, 2.5], 15, [20, 25]]], [['Python', [10, 5, 2.5, 2.5], 'version', 15, [20, 25]]], [['Python', 10, 3, 2.5, 2.5, 'version']], [['Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 5]], [['Python', 4, 10, 3, 2.5, 2.5, 'version']], [['Python', 10, 5, 2.5, 2.5, 'version', 'Python']], [['PythonPython', [10, 5, 2.5, 2.5], 25, [20, 25], 'PythonPython']], [['n', 'version', [10, 5, 2.5, 2.5], 'version', 15, [20, 25]]], [['PythonPython', [10, 5, 2.5, 2.5], 25, 'PythonPython']], [['Python', [10, 5, 2.5, 2.5], 'version', 15, [20, 25], [10, 5, 2.5, 2.5]]], [['PythonPython', [10, 5, 2.5, 2.5], 25, 'PythonPython', 'PythonPython']], [['Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 5, 3]], [['PythonPython', [10, 5, 2.5, 2.5], 25, [20, 25], 'PythhonPython', 'PythonPython', 25]], [['PythonPython', [10, 5, 2.5, 2.5], 25, 3, [20, 25], 'PythhonPython', 'PythonPython', 25]], [['PythonPython', [10, 5, 2.5, 2.5], 25, [20, 25], 'PythhonPython', 'PythonPython', 25, 'PythhonPython', 25]], [['PythonPython', [10, 5, 2.5, 2.5], 25, [20, 25], 'PythhonPython', 'PythonPython', 25, 'PythhonPython', 25, 'PythonPython']], [['Python', [10, 5, 2.5, 2.5], 'version', 15, [20, 25], 'Python']], [['PythonPython', [10, 5, 2.5, 2.5, 2.5], 25, [20, 25], 'PythhonPython', [10, 5, 2.5, 2.5, 2.5], 'PythonPython', 25, 'PythhonPython', 25, 'PythonPython']], [['Python', 10, 5, 2.5, 2.5, 'version', 10]], [[[10, 5, 2.5, 2.5, 2.5, 2.5], [10, 5, 2.5, 2.5, 2.5, 2.5], 'Python', [10, 5, 2.5, 2.5, 2.5, 2.5], 15, [20, 25], [10, 5, 2.5, 2.5, 2.5, 2.5]]], [['Python', 'version', 'is', '3.8.5', 1, 2, 'PythhonPython', 3, 4, 5]], [['n', 'version', [10, 5, 2.5, 2.5], 15, [20, 25]]], [['Python', 'Py', [10, 5, 2.5, 2.5], 15, [20, 25]]], [[[10, 5, 2.5, 2.5], 25, 'PythonPython', 'PythonPython']], [[[10, 5, 2.5, 2.5, 5], [10, 5, 2.5, 2.5, 5], 25, 'version']], [['PythonPython', [10, 5, 2.5], 25, [20, 25], 'PythonPython']], [['Python', 'Py', 15, [20, 25]]], [['PythonPython', 'PythonPytthon', [10, 5, 2.5, 2.5], 'Py', 3, [20, 25], 'Pythh3.8.5onPython', 'PythonPython', 25, 'PythhonPython', 25]], [['Python', 'versioen', 'is', '3.8.5', 1, 2, 'Python', 'PythhonPython', 3, 4, 5]], [['Python', [10, 5, 2.5, 2.5], 'version', 'veirsion', 15, [20, 25], 'Python']], [['Python', [10, 5, 2.5, 2.5], 'version', 15, [5, 20, 25], 15, 15]], [['PythonPython', 25, [20, 25], 'PythhonPython', 'PythonPython', 25, 25]], [['n', [10, 5, 2.5], 'version', [10, 5, 2.5], 'version', 15, [20, 25]]], [['PythonPython', [10, 5, 2.5, 2.5], 25, [20, 25], 'PythhonPython', 'tPythonPython', 25]], [['Python', 'version', 'is', '3.8.5', 1, 2, 'PythhonPython', 3, 4, 5, '3.8.5']], [['PythonPython', [10, 5, 2.5, 2.5], 25, 3, [20, 25], 'PythhonPython', 'PythonPython', 25, [10, 5, 2.5, 2.5]]], [['Python', [10, 5, 2.5, 2.5], [19, 25], 15, [19, 25], 'Python', 'Python']], [['PythonPython', 25, [20, 25], 'PythhonPython', 24, 25, 25]], [[20, 'Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 5, 3, 5]], [['Python', 'version', 'is', '3.8.5', 1, 2, 4, 5]], [['Python', 'version', 'is', '3.8.5', 1, 4, 2, 'PythhonPython', 3, 4, 5, 'Python']], [['n', [10, 5, 2.5], 'version', 'version', 25, [20, 25], [10, 5, 2.5]]], [['PythonPython', 25, [20, 25], 'PythhonPython', 'PythonPython', 25]], [['Python', 'version', 'is', '3.8.5', 1, 4, 2, 'PythhonPython', 3, 4, 5, 'Python', 2]], [[25, 'PythonPython', [10, 5, 2.5, 2.5], 25, 3, [20, 25], 'PythhonPython', 'PythonPython', 25]], [['n', [10, 5, 2.5], 'version', 'version', 25, [20, 25], 'PythonPytthon', [10, 5, 2.5]]], [['Python', 4, 'version', 'is', '3.8.5', 1, 2, 3, 4, 5, 3]], [['Python', [10, 5, 2.5, 2.5, 2.5], 3, [20, 25]]], [[[1, 20, 25], 'PythonPython', [10, 5, 2.5], 25, [1, 20, 25], 'PythonPython']], [['Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 5, 3, 5, 5]], [['Python', 'version', 5, 'is', '3.8.5', 4, 3, 2, 'PythhonPython', 3, 4, 5, 'Python', 2, 4]], [[25, 'PythonPython', 'PythonPython']], [['Python', [10, 5, 2.5, 2.5], [19, 25], 15, [19, 25], 'Python', 'Python', [19, 25]]], [['Python', [10, 5, 2.5, 2.5], [25], 15, [25], 'Python', 'Python']], [['Python', 'Py', 15, 16, [20, 25]]], [['n', [10, 5, 2.5], 'version', 'version', 25, [20, 25], [10, 5, 2.5], 25]], [['version', [10, 5, 2.5, 2.5], 'version', 14, [20, 25, 25]]], [['Python', 'Py', [10, 5, 2.5, 2.5], 15, [20, 25], 15]], [['Python', 'PyPythonPytthon', 15, [20, 25]]], [['PythonPython', [10, 5, 2.5, 2.5], 25, 3, [20, 25], 'PythhonPython', 'Pythhon', 'PythonPython']], [['n', [10, 5, 2.5], 'version', 'version', 25, [20, 25], 'PythonPytthon', [10, 5, 2.5], [10, 5, 2.5]]], [['Python', 5, 5, 2.5, 2.5, 'version', 'Python']], [['Python', 'version', 'is', '3.8.5', 2, 'version', 'PythhonPython', 3, 4, 5]], [['PythonPython', [10, 5, 2.5, 2.5], 25, 3, [20, 25], 'PythhonPython', 'PythonPython', 25, 24, [10, 5, 2.5, 2.5]]], [[5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 5, 3, 5, 5, 1]], [['Python', [10, 5, 2.5, 2.5, 2.5], 3, [20, 25], [20, 25], 'Python']], [['Python', 10, 5, 2.5, 2.5, 'version', 'Python', 2.5, 2.5]], [['Python', 'tPython', 10, 5, 2.5, 2.5, 'version', 'Python', 2.5]], [['PythonPython', 'PythonPytthon', [2.5, 10, 5, 2.5, 2.5], 'Py', 3, [2.5, 10, 5, 2.5, 2.5], [20, 25], 'Pythh3.8.5onPython', 'PythonPython', 25, 'PythhonPython', 25]], [['nn', [10, 5, 2.5], 'version', 'version', 25, [20, 25], [10, 5, 2.5], 25, 25]], [['versioen', [10, 5, 2.5, 2.5], 'n', 15, [20, 25], [10, 5, 2.5, 2.5]]], [['PythonPyothon', 'PythonPPythonPytthonython', [9, 5, 2.5, 2.5], 25, 'PythonPython']], [[[19, 25], 15, [19, 25], 'Python', 'Python', [19, 25], [19, 25]]], [['Python', 4, 'version', 'is', 1, 2, 3, 4, 5, 3, 5]], [['PythonPythoveirsionn', 'PythonPython', [10, 5, 2.5, 2.5, 2.5], 25, [20, 25], 'PythhonPython', [10, 5, 2.5, 2.5, 2.5], 'PythonPython', 25, 'PythhonPython', 25, 'PythonPython']], [['PythonPython', [10, 5, 2.5, 2.5], 25, [10, 5, 2.5, 2.5], [20, 25], 'PythhonPython', 'PythonPython', 25, 'PythhonPython', 25, 'PythonPython']], [['Python', 'versioen', 'is', '3.8.5', 'vertPythonPythonioen', 1, 2, 'Python', 'PythhonPythhonPythonPython', 3, 4, 5, '3.8.5']], [['Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 1, 4, 5, 3, 5, 5, 1]], [['version', 'versinon', [10, 5, 2.5, 2.5], 'version', 14, [20, 25, 25]]], [['Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 3, 5, 5]], [['Python', [10, 5, 2.5, 2.5], [25], 15, [25], 'Python']], [['Python', 5, 'version', 'is', '3.8.5', 2, 1, 2, 3, 4, 5]], [['n', [10, 5, 2.5], 'version', 'version', 25, [20, 25], 'tPythonPython', 26, [10, 5, 2.5]]], [['versioen', [2.5, 10, 5, 2.5, 2.5], 'n', [2.5, 10, 5, 2.5, 2.5], 15, [20, 25], [2.5, 10, 5, 2.5, 2.5]]], [['Python', 'version', 5, 'is', '3.8.5', 4, 3, 2, 'PythhonPython', 3, 4, 5, 'Python', 2, 3]], [[25, 'PythonPython', 'PythonPython', 25]], [['vversion', 'Python', 'version', 'is', '3.8.5', 1, 4, 9, 'PythhonPython', 3, 4, 5, 'Python']], [['PythonPPythonPytthonython', 25, [20, 25], 'PythonPython']], [['Python', [25], 15, [25], 'Python', [10, 5, 2.5, 2.5], 'Python', 15]], [['PythonPython', [10, 5, 2.5, 2.5], 25, [20, 25, 25], 'PythhonPython', [20, 25, 25], 'PythonPython', 25]], [['Python', 4, 'version', '3.vversion8.5', '3.8.5', 1, 4, 2, 'PythhonPython', 3, 5, 'Python', 2]], [['PythonPython', 24, [10, 5, 2.5, 2.5], 25, 'PythonPython']], [[16, 'Python', [10, 5, 2.5, 2.5], 'vsion', 15, [5, 20, 25], 15, 15]], [['Python', 'version', 5, 'is', '3.8.5', 1, 2, 'PythhonPython', 3, 4, 5, '3.8.5']], [[[20, 25, 25], 'Python', 'Py', [10, 5, 2.5, 2.5], 15, [20, 25, 25], [20, 25, 25]]], [[[10, 5, 2.5, 2.5], 25, [20, 25], 'PythonPython', 25, 'PythhonPython', 25]], [['Python', [9, 20, 25], 'Py', [10, 5, 2.5, 2.5], 15, [9, 20, 25], 15]], [['nn', [10, 5, 2.5], 'version', 'verission', 25, [20, 25], [10, 5, 2.5], 25, 25]], [['Python', 5, 'version', 'is', '3.8.5', 1, 2, 3, 4, 3, 5, 5, '3.8.5']], [['verission', 'Python', 'version', 'is', '3.8.5', 1, 2, 3, 4, 5]], [['version', [10, 9, 5, 2.5, 2.5], 'version', 14, [20, 25, 25]]], [['Python', 'Py', 15, 16, [21, 20, 25]]]]
results = [2, 15, 20, 5, 1, 15, 15, 3, 1, 3, 5, 25, 15, 25, 15, 25, 1, 25, 3, 25, 25, 15, 25, 5, 15, 1, 15, 15, 25, 25, 25, 15, 3, 1, 15, 15, 25, 15, 25, 1, 3, 15, 24, 1, 1, 1, 25, 25, 1, 3, 25, 1, 3, 25, 1, 2, 25, 15, 15, 15, 25, 14, 15, 15, 3, 25, 5, 2, 3, 1, 3, 5, 5, 3, 25, 15, 25, 15, 1, 25, 25, 1, 1, 14, 1, 15, 1, 25, 15, 2, 25, 1, 25, 15, 25, 1, 24, 15, 1, 15, 25, 15, 25, 1, 1, 14, 15]

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
        func_name = "min_val"
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
        for test_case in ["assert min_val(['Python', 3, 2, 4, 5, 'version'])==2", "assert min_val(['Python', 15, 20, 25])==15", "assert min_val(['Python', 30, 20, 40, 50, 'version'])==20"]:
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
