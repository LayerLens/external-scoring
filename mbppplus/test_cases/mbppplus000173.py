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
inputs = [[[10, 2, 56]], [[[10, 20, 4, 5, 'b', 70, 'a']]], [[10, 20, -4, 5, -70]], [[]], [[7]], [[-10, 15, 0, -5, 2]], [[0]], [[10, -5, 'abc', 0, 3.14]], [[7, 10, 7]], [[15]], [[-10, 15, 0, 15, -5, 2, 15, 2]], [[-10, 15, -10, 0, 15, -5, 2, 15, 2]], [[-10, 0, -5, 2]], [[15, -10, 0, 1, 15, -5, 2, 15, 2]], [['TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'abc', 'abc', 'gTxGtFZLn', 'abc']], [[0, 15, 0, -5]], [[-10, 15, 0, 15, -5, 2]], [[-5, 7, 10, 7]], [[-10, 15, 0, 10, 2]], [[-10, 15, 0, 10, 2, 0]], [[-10, 15, 0, 15, 15, -5, 2]], [['TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'abc', 'abc', 'gTxGtLn', 'abc']], [[1, 0, 15, 0, -5]], [[-10, 0, 15, -5, 2]], [[15, 0, 2, 0]], [[-10, 15, 0, 1, 2, 0, 0]], [['TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc']], [[-10, 0, 10, 15, -5, 2]], [[-10, 10, 7]], [['TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc']], [[-10, -11, 15, -10, 0, 15, -5, 2, 15, 2]], [[2, -11, 15, -10, 0, 15, -5, 2, 15, 2]], [[-10, 15, 15, 0, -5, 2]], [['TTzXjVXDQt', 'ITwgTxGtLnVYEcw', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc']], [[-10, -11, 15, -10, 0, 15, -5, 2, 15, 2, 2]], [[-10, 0, 10, 15, -5, 2, 15]], [[10, -5, 'abc', 0, 15, 3.14]], [[15, 0, 10, 2, 0]], [[-11, 15, 0, -5, 2]], [[-10, 0, 1, 2, 0, 0]], [['TTzXjVXDQt', 'ITwgTxGtLnVYEcw', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc', 'abc']], [[-10, 15, 15, 15, -5, 2]], [[-10, 1, 2, 0, 0, 0]], [[11, -5, 7, 10, 7, 10]], [[-10, 15, 0, 15, -5, 2, 15, 2, -10]], [[-10, 0, 1, 15, -5, 2, 15, 2, 1, 2]], [[-10, 0, 15, 15, -5, 2]], [[-10, 15, 0, 15, -5, 15, 2]], [[-10, 0, 15, 15, -5, 2, 0]], [[0, 1, 0, 0]], [[7, 10, 7, 7]], [[-5, 1, 7, 10, 7]], [[-9, -10, 15, -10, 0, 15, -5, 2, 15, 2]], [[-10, 15, 0, 15, -5, 2, 15, 2, -9, -10, -10]], [['TTzXjVXDQt', 'TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc']], [[-10, 15, 1, 2, 0, 0]], [[2, 7, 10, -11, 7]], [[7, 10, 7, 15, 7]], [[0, 1, 0, 0, 0, 0]], [['TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'ITwgTxGtLnVYEcw', 'abc', 'gTxGtFZLn', 'abc']], [[-10, 15, 15, -5, 2, 15, 2, -9, -10, -10]], [[-5, 7, 10, 7, 10]], [[-10, -11, 15, -10, 0, -5, 2, 15, 2]], [[-10, 0, 1, 15, -11, 15, 2, 1, 2]], [[3.14, -17.036961582608342, 3.14, 3.14, 3.14]], [[0, -10, 0, 10, -5, 2]], [['TTzXjVXDQ', 'ITwgTxGtLnVYEcw', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'GgTxGtFZLn', 'abc']], [['TTzXjVXDQt', 'TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc', 'abc']], [[2, -11, 7, 15, -10, 0, 15, -5, 2, -11, 15, 2]], [[-9, -10, -4, 15, -10, 0, 15, -5, 2, 15, 7, 2]], [['TTzXjVXDQt', 'TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn']], [[15, 0, 10, 2, -5, 0]], [[-10, 15, -10, 0, 15, -5, 2, 15, 2, -9, -10, -10]], [[-10, 15, 15, 0, 2]], [[7, 10, 8]], [[-10, 1, -5, -10]], [[-10, -11, 15, -10, -5, 2, 15, 2]], [['TTzXjVXDQt', 'ucH', 'abc', 'ITwVYEcw', 'TTzXjVXDQt', 'abcTTzXjVXDQt', 'gTxGtFZLn', 'abc']], [['TTzXjVXDQt', 'ITwVYEcw', 'ucH', 'abc', 'ITwgTxGtLnVYEcw', 'abc', 'gTxGtFZLn', 'abc', 'ucH']], [[-10, 15, 15, 15, -5, 2, 2]], [[2, -10, 15, 0, 0, 10, 2]], [[14, -10, 15, 0, 2]], [[-10, 1, 2, 0, 0, 0, -10]], [[-10, 15, 14, 15, -5, 2]], [[-11, 0, 2]], [[-4, 7, 7]], [[15, 0, 1, 2, 0]], [['TTzXjVXDQt', 'ucH', 'abc', 'abc', 'ITwVYEcw', 'abc', 'gTxGtFZLn', 'abc', 'abc', 'abc']], [[-10, 0, 1, 15, -5, 2, 15, 2, 0, 1, 2]], [['TTzXjVXDQt', 'gTxGtFZLn', 'abc', 'ITwgTxGtLnVYEcw', 'abc', 'gTxGtFZLn', 'abc', 'ucH', 'gTxGtFZLn']], [[1, 0, -5, 2]], [[15, 15]], [[11, -5, 10, 7, 10]], [[-10, -11, 15, -9, -5, 2, 15, 2]], [[-10, 0, 15, -5, 2, 15]], [[15, 0, 2, 0, 0, 0]], [[-4, 10, 7, 7]], [[14, -10, 15, 0, -6, 2]], [[-1, 7, 10, 7]], [[-9, -10, 15, -10, 0, 15, -5, 2, 15, 2, 15, -10]], [[11, 7, 10, -5, 7, 10]], [[-9, -10, -4, 15, -10, 0, -4, -5, 2, 15, 7, 2]], [[-10, 1, 0, 0, 0, -10, 1]], [[0, -6, 0]], [[-10, 0, 1, 2, 15, -5, 2, 15, 2, 1, 2]], [[7, 10, 7, 7, 7]], [[0, 11, 0, -5]], [[11, 10, 7, 10]]]
results = [14, 19, 19, 0, 7, 14, 0, 14, 15, 6, 28, 29, 8, 29, 0, 11, 20, 20, 10, 10, 26, 0, 12, 14, 8, 10, 0, 15, 9, 0, 31, 32, 20, 0, 33, 21, 20, 9, 15, 4, 0, 26, 4, 23, 29, 26, 20, 26, 20, 1, 22, 21, 38, 39, 0, 10, 19, 28, 1, 0, 39, 21, 25, 21, 103, 9, 0, 0, 41, 49, 0, 14, 40, 15, 16, 8, 25, 0, 0, 28, 12, 14, 5, 25, 4, 18, 9, 0, 26, 0, 8, 12, 16, 33, 20, 8, 19, 20, 16, 45, 23, 47, 4, 6, 28, 29, 7, 11]

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
        func_name = "sum_of_digits"
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
        for test_case in ['assert sum_of_digits([10,2,56])==14', "assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19", 'assert sum_of_digits([10,20,-4,5,-70])==19']:
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
