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
inputs = [[[12, 10, 5, 6, 52, 36], 2], [[1, 2, 3, 4], 1], [[0, 1, 2, 3, 4, 5, 6, 7], 3], [[], 0], [['apple', 'banana', 'cherry', 'date'], 2], [[1, 2, 3, 1, 2, 3], 3], [[2, 4, 6, 8, 10, 8, 6, 4, 2], 7], [['banana', 'cherry', 'date'], 2], [['banana', 'date'], 2], [[2, 4, 6, 8, 0, 8, 6, 4, 2, 0], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 6, 2], 4], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 2], [['apple', 'banana', 'date'], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 0], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 4], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0], 1], [[1, 2, 3, 1, 2, 8], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2], 4], [[2, 6, 8, 7, 8, 6, 8, 4, 2, 0, 2, 0], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0], 0], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 6], [[2, 6, 5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 1, 0, 2, 8], 3], [[4, 6, 8, 10, 8, 6, 4, 2, 8], 7], [[1, 2, 3, 1, 2, 3], 4], [[2, 5, 4, 6, 8, 0, 8, 6, 4, 2, 0], 4], [[7, 1, 2, 3, 1, 2, 3], 3], [[2, 6, 5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 8, 8], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8], 6], [[4, 6, 8, 10, 8, 6, 4, 2, 8], 4], [[2, 4, 6, 8, 10, 8, 6, 4, 2], 4], [[2, 5, 4, 6, 8, 0, 8, 6, 4, 2, 0, 2], 4], [[5, 6, 5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 1, 0, 2, 8], 4], [[2, 6, 8, 0, 8, 6, 8, 1, 4, 2, 0, 2], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 1, 0, 2, 8], 5], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 10], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8], 4], [['bbanana', 'banana', 'date'], 1], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 0, 2, 8], 6], [[4, 6, 8, 10, 8, 6, 4, 2, 8], 8], [['apple', 'cherry', 'date'], 2], [[5, 6, 5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 3], [[2, 8, 6, 8, 10, 8, 6, 4, 2], 7], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8], 7], [[6, 8, 0, 8, 6, 8, 4, 2, 0, 0, 2, 0, 0], 4], [[2, 4, 5, 6, 8, 10, 8, 6, 4, 2], 7], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 8], 1], [[5, 6, 5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 6], [[2, 6, 8, 0, 8, 6, 8, 2, 0, 2, 0, 8], 1], [[2, 6, 8, 0, 8, 6, 8, 4, 5, 0, 2, 0], 1], [[7, 1, 2, 3, 1, 2, 3, 3], 1], [[2, 6, 8, 0, 8, 6, 8, 2, 0, 0, 2, 0, 8], 1], [[4, 6, 8, 10, 8, 6, 4, 2, 8, 6], 7], [[2, 6, 8, 0, 8, 6, 8, 7, 1, 4, 2, 0, 2], 3], [[2, 5, 4, 6, 6, 8, 0, 8, 6, 3, 2, 0], 6], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8, 8], 7], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2], 2], [[4, 6, 10, 8, 6, 4, 2, 8], 4], [[2, 8, 7, 8, 6, 8, 4, 2, 0, 2, 0], 2], [[6, 8, 0, 8, 8, 4, 2, 0, 2], 0], [[7, 1, 2, 3, 1, 2, 3, 10, 3], 1], [[2, 6, 8, 0, 8, 6, 8, 0, 0, 2, 0, 8], 1], [['apple', 'cherry', 'date', 'date'], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8, 8, 0], 7], [[2, 4, 6, 8, 0, 8, 6, 4, 2, 0], 1], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8, 8, 0, 6], 7], [[1, 2, 4, 3, 1, 2, 3], 4], [[4, 6, 8, 10, 8, 6, 4, 2, 7, 8], 7], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 0, 2, 8, 2], 6], [[7, 1, 2, 3, 1, 2, 3, 10, 3], 0], [[2, 6, 8, 0, 7, 6, 8, 4, 2, 0, 2, 8, 8, 0, 6], 3], [[2, 6, 8, 4, 0, 8, 6, 8, 4, 2, 0, 2, 0, 8], 1], [[2, 8, 6, 8, 10, 6, 4, 2, 6], 8], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8, 0, 0, 0], 0], [[0, 0, 75, 4, 5, 3, 58, 8], 0], [[6, 8, 0, 8, 8, 4, 2, 0, 2, 8], 0], [[2, 6, 10, 8, 0, 8, 6, 8, 2, 0, 2, 0, 8], 2], [[2, 6, 8, 0, 8, 6, 8, 1, 4, 2, 0, 2, 8], 3], [[2, 6, 8, 0, 8, 6, 8, 7, 1, 4, 2, 0, 2], 2], [[True, False, True, True, False, True, False, False, False], 0], [[2, 4, 6, 8, 0, 8, 6, 4, 2, 0, 0], 3], [[4, 6, 8, 0, 8, 6, 4, 2, 0], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 5], [['apple', 'cherry', 'date', 'date'], 1], [[6, 8, 0, 8, 6, 8, 4, 2, 0], 3], [[2, 6, 8, 0, 8, 6, 8, 2, 0, 0, 2, 0, 8], 2], [['apple', 'cherry', 'date'], 1], [[1, 2, 3, 1, 2, 3], 5], [[2, 6, 8, 0, 8, 6, 8, 4, 5, 0, 2, 0], 2], [[2, 6, 5, 8, 0, 8, 6, 8, 4, 0, 2, 0, 0, 8, 8], 2], [[6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 4], [[2, 6, 8, 0, 8, 8, 2, 0, 0, 2, 2, 0, 8], 1], [[2, 6, 8, 0, 8, 6, 8, 4, 1, 0, 2, 8, 6], 10], [[2, 6, 8, 3, 0, 8, 6, 8, 5, 2, 0, 2, 0, 8], 1], [[2, 6, 8, 0, 8, 6, 8, 0, 0, 2, 6, 0, 8], 3], [['banana', 'cherry', 'cherry', 'date'], 2], [[2, 6, 8, 0, 8, 6, 8, 0, 0, 2, 0, 8, 0], 1], [['cherry', 'banana', 'cherry', 'cherry', 'date'], 2], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], 3], [[2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 8], 7], [[2, 6, 8, 0, 7, 6, 8, 0, 0, 2, 0, 8], 1], [[7, 1, 2, 3, 1, 2, 3], 6]]
results = [[5, 6, 52, 36, 12, 10], [2, 3, 4, 1], [3, 4, 5, 6, 7, 0, 1, 2], [], ['cherry', 'date', 'apple', 'banana'], [1, 2, 3, 1, 2, 3], [4, 2, 2, 4, 6, 8, 10, 8, 6], ['date', 'banana', 'cherry'], ['banana', 'date'], [8, 0, 8, 6, 4, 2, 0, 2, 4, 6], [0, 8, 6, 8, 4, 2, 0, 2, 6, 8], [0, 8, 6, 8, 4, 2, 0, 2, 2, 6, 8], [8, 6, 8, 4, 2, 0, 6, 2, 2, 6, 8, 0], [8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 2, 6], [8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 2, 6], ['date', 'apple', 'banana'], [2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0], [8, 6, 8, 4, 2, 0, 2, 0, 0, 2, 6, 8, 0], [6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 2], [1, 2, 8, 1, 2, 3], [8, 6, 8, 4, 2, 0, 2, 2, 6, 8, 0], [8, 7, 8, 6, 8, 4, 2, 0, 2, 0, 2, 6], [2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0], [8, 4, 2, 0, 2, 0, 0, 2, 6, 8, 0, 8, 6], [5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 2, 6], [0, 8, 6, 8, 4, 1, 0, 2, 8, 2, 6, 8], [2, 8, 4, 6, 8, 10, 8, 6, 4], [2, 3, 1, 2, 3, 1], [8, 0, 8, 6, 4, 2, 0, 2, 5, 4, 6], [3, 1, 2, 3, 7, 1, 2], [5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 8, 8, 2, 6], [0, 8, 6, 8, 4, 2, 0, 2, 8, 2, 6, 8], [8, 4, 2, 0, 2, 8, 2, 6, 8, 0, 8, 6], [8, 6, 4, 2, 8, 4, 6, 8, 10], [10, 8, 6, 4, 2, 2, 4, 6, 8], [8, 0, 8, 6, 4, 2, 0, 2, 2, 5, 4, 6], [5, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 5, 6], [8, 6, 8, 4, 1, 0, 2, 8, 2, 6, 8, 0], [0, 8, 6, 8, 1, 4, 2, 0, 2, 2, 6, 8], [6, 8, 4, 1, 0, 2, 8, 2, 6, 8, 0, 8], [2, 0, 0, 2, 6, 8, 0, 8, 6, 8, 4, 2, 0], [8, 6, 8, 4, 2, 0, 2, 8, 2, 6, 8, 0], ['banana', 'date', 'bbanana'], [8, 4, 2, 0, 0, 2, 8, 2, 6, 8, 0, 8, 6], [8, 4, 6, 8, 10, 8, 6, 4, 2], ['date', 'apple', 'cherry'], [8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 5, 6, 5], [4, 2, 2, 8, 6, 8, 10, 8, 6], [4, 2, 0, 2, 8, 2, 6, 8, 0, 8, 6, 8], [6, 8, 4, 2, 0, 0, 2, 0, 0, 6, 8, 0, 8], [6, 4, 2, 2, 4, 5, 6, 8, 10, 8], [6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 0, 8, 2], [6, 8, 4, 2, 0, 2, 0, 0, 5, 6, 5, 8, 0, 8], [6, 8, 0, 8, 6, 8, 2, 0, 2, 0, 8, 2], [6, 8, 0, 8, 6, 8, 4, 5, 0, 2, 0, 2], [1, 2, 3, 1, 2, 3, 3, 7], [6, 8, 0, 8, 6, 8, 2, 0, 0, 2, 0, 8, 2], [2, 8, 6, 4, 6, 8, 10, 8, 6, 4], [0, 8, 6, 8, 7, 1, 4, 2, 0, 2, 2, 6, 8], [0, 8, 6, 3, 2, 0, 2, 5, 4, 6, 6, 8], [4, 2, 0, 2, 8, 8, 2, 6, 8, 0, 8, 6, 8], [8, 0, 8, 6, 8, 4, 2, 0, 2, 2, 6], [6, 4, 2, 8, 4, 6, 10, 8], [7, 8, 6, 8, 4, 2, 0, 2, 0, 2, 8], [6, 8, 0, 8, 8, 4, 2, 0, 2], [1, 2, 3, 1, 2, 3, 10, 3, 7], [6, 8, 0, 8, 6, 8, 0, 0, 2, 0, 8, 2], ['date', 'date', 'apple', 'cherry'], [4, 2, 0, 2, 8, 8, 0, 2, 6, 8, 0, 8, 6, 8], [4, 6, 8, 0, 8, 6, 4, 2, 0, 2], [4, 2, 0, 2, 8, 8, 0, 6, 2, 6, 8, 0, 8, 6, 8], [1, 2, 3, 1, 2, 4, 3], [2, 7, 8, 4, 6, 8, 10, 8, 6, 4], [8, 4, 2, 0, 0, 2, 8, 2, 2, 6, 8, 0, 8, 6], [7, 1, 2, 3, 1, 2, 3, 10, 3], [0, 7, 6, 8, 4, 2, 0, 2, 8, 8, 0, 6, 2, 6, 8], [6, 8, 4, 0, 8, 6, 8, 4, 2, 0, 2, 0, 8, 2], [6, 2, 8, 6, 8, 10, 6, 4, 2], [2, 6, 8, 0, 8, 6, 8, 4, 2, 0, 2, 8, 0, 0, 0], [0, 0, 75, 4, 5, 3, 58, 8], [6, 8, 0, 8, 8, 4, 2, 0, 2, 8], [10, 8, 0, 8, 6, 8, 2, 0, 2, 0, 8, 2, 6], [0, 8, 6, 8, 1, 4, 2, 0, 2, 8, 2, 6, 8], [8, 0, 8, 6, 8, 7, 1, 4, 2, 0, 2, 2, 6], [True, False, True, True, False, True, False, False, False], [8, 0, 8, 6, 4, 2, 0, 0, 2, 4, 6], [0, 8, 6, 4, 2, 0, 4, 6, 8], [6, 8, 4, 2, 0, 2, 0, 0, 2, 6, 8, 0, 8], ['cherry', 'date', 'date', 'apple'], [8, 6, 8, 4, 2, 0, 6, 8, 0], [8, 0, 8, 6, 8, 2, 0, 0, 2, 0, 8, 2, 6], ['cherry', 'date', 'apple'], [3, 1, 2, 3, 1, 2], [8, 0, 8, 6, 8, 4, 5, 0, 2, 0, 2, 6], [5, 8, 0, 8, 6, 8, 4, 0, 2, 0, 0, 8, 8, 2, 6], [6, 8, 4, 2, 0, 2, 0, 0, 6, 8, 0, 8], [6, 8, 0, 8, 8, 2, 0, 0, 2, 2, 0, 8, 2], [2, 8, 6, 2, 6, 8, 0, 8, 6, 8, 4, 1, 0], [6, 8, 3, 0, 8, 6, 8, 5, 2, 0, 2, 0, 8, 2], [0, 8, 6, 8, 0, 0, 2, 6, 0, 8, 2, 6, 8], ['cherry', 'date', 'banana', 'cherry'], [6, 8, 0, 8, 6, 8, 0, 0, 2, 0, 8, 0, 2], ['cherry', 'cherry', 'date', 'cherry', 'banana'], [0, 8, 6, 8, 4, 2, 0, 2, 0, 0, 2, 6, 8], [4, 2, 0, 8, 2, 6, 8, 0, 8, 6, 8], [6, 8, 0, 7, 6, 8, 0, 0, 2, 0, 8, 2], [3, 7, 1, 2, 3, 1, 2]]

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
        func_name = "split_Arr"
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
        for test_case in ['assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]', 'assert split_Arr([1,2,3,4],1) == [2,3,4,1]', 'assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]']:
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
