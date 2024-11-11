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
inputs = [[[1, 2, 3, 4, 5, 6], 4], [[4, 5, 6, 7], 2], [[9, 8, 7, 6, 5], 3], [[6, 9, 2, 1, 5, 3], 4], [['apple', 'banana', 'cherry', 'date'], 3], [[6, 9, 2, 1, 5, 3], 5], [['apple', 'cherry', 'date'], 3], [['apple', 'banana', 'cherry', 'date'], 4], [['apple', 'banana', 'cherry', 'cherry', 'date'], 4], [[6, 9, 2, 1, 5, 3, 2], 4], [[9, 2, 1, 5, 3], 4], [[6, 9, 2, 5, 3], 5], [[9, 2, 9, 1, 5, 3], 4], [['apple', 'banana', 'cherry', 'date'], 1], [[9, 2, 9, 1, 5, 3], 1], [['apple', 'cherry', 'deate'], 3], [[6, 9, 2, 1, 5, 3], 3], [['apple', 'cherrry', 'banana', 'cherry', 'date'], 4], [[6, 9, 2, 1, 5, 3], 2], [[6, 9, 2, 5, 1, 5, 3, 2], 4], [[9, 2, 9, 1, 5, 3, 9], 1], [[6, 9, 2, 1, 5, 3], 1], [[9, 2, 1, 5, 3], 1], [['apple', 'cherry', 'deate'], 2], [['apple', 'cherry', 'date'], 1], [['applpe', 'apple', 'cherrry', 'banana', 'cherry', 'date', 'applpe'], 4], [['apple', 'cherry', 'cherry'], 3], [['apple', 'cherry', 'cherry', 'cherry'], 3], [['apple', 'cherrry', 'banana', 'date'], 4], [[9, 2, 9, 1, 5, 3, 9, 5], 1], [[9, 2, 9, 1, 1, 3, 9, 5], 1], [['apple', 'cherry', 'cherry', 'date'], 1], [['apple', 'cherry', 'cherry', 'cherry'], 4], [[9, 2, 10, 3, 9, 1, 5, 3, 9], 1], [['cherry', 'cherry', 'cherry'], 3], [[6, 2, 1, 5, 3], 4], [['apple', 'banana', 'cherrry', 'cherry', 'date'], 4], [[6, 9, 2, 5, 3], 2], [[9, 2, 9, 1, 1, 3, 9], 1], [[9, 2, 1, 5, 3, 2], 1], [[6, 9, 2, 5, 4, 1, 5, 3, 2], 4], [[6, 2, 1, 6, 5, 3], 4], [[9, 2, 9, 1, 5, 3, 9, 5], 3], [[9, 2, 9, 1, 1, 3, 9], 2], [[9, 2, 10, 3, 9, 1, 5, 3, 9], 2], [[6, 9, 2, 1, 3, 5, 3], 5], [[4, 6, 9, 2, 1, 3, 5, 3], 5], [['apple', 'banana', 'cherry', 'date'], 2], [[5, 2, 1, 6, 5, 3], 5], [[6, 9, 2, 1, 5, 3, 2], 3], [[9, 2, 10, 3, 9, 1, 5, 4, 9], 2], [['apple', 'banana', 'cherry', 'date', 'date'], 3], [[9, 2, 9, 1, 1, 4, 9], 1], [[9, 2, 9, 1, 5, 3], 3], [['apple', 'banana', 'cherry', 'date', 'date'], 4], [[9, 2, 2, 9, 1, 5, 3], 1], [[5, 2, 1, 5, 3], 5], [[9, 2, 1, 5, 3], 3], [[6, 2, 1, 5, 3, 2], 4], [[9, 2, 9, 1, 1, 1, 4, 9], 1], [[9, 3, 2, 9, 1, 1, 3, 9], 2], [['apple', 'banana', 'cherrry', 'cherry', 'date'], 1], [['cdatey', 'apple', 'cherry', 'deate'], 3], [['apple', 'cherrry', 'banana', 'cherry', 'date'], 1], [[9, 2, 10, 3, 9, 1, 5, 4, 9], 3], [[9, 2, 2, 9, 3, 1, 5, 3], 1], [[6, 2, 1, 5, 9, 3], 5], [[6, 9, 2, 1, 5, 3, 2], 6], [['apple', 'cherrry', 'banana', 'ccdateyherry', 'date'], 4], [['applpe', 'apple', 'cherrry', 'banana', 'cherry', 'date', 'applpe', 'applpe'], 4], [['cdatey', 'banana', 'cherry', 'date'], 4], [[6, 2, 5, 3, 2], 4], [[6, 9, 2, 5, 3], 1], [[6, 9, 7, 2, 1, 5, 3, 7], 4], [['apple', 'cherry', 'cherry', 'aepple', 'date'], 1], [[6, 5, 3, 2], 4], [[9, 4, 2, 6, 1, 5, 3, 2], 3], [[9, 2, 1, 5, 3, 9], 4], [['apple', 'banana', 'cherry', 'date', 'banana'], 1], [['cdatey', 'apple', 'cherry', 'deate'], 4], [[1, 2, 9, 1, 1, 4, 9], 1], [[6, 9, 2, 1, 5, 3], 6], [[1, 2, 5, 9, 1, 1, 4, 9], 1], [['aepple', 'apple', 'banana', 'cherrry', 'cherry', 'date'], 1], [[9, 2, 9, 1, 5, 3], 5], [[10, 2, 9, 1, 5, 3, 9], 1], [[9, 2, 5, 3], 3], [[1, 2, 5, 9, 1, 1, 4, 9, 9, 1], 1], [[3, 6, 9, 2, 1, 5, 3], 4], [[2, 9, 1, 5, 3, 9, 5], 3], [[3, 9, 2, 10, 3, 9, 1, 5, 3, 9], 2], [['appple', 'cdatey', 'apple', 'cherry', 'deate'], 3], [[2, 1, 9, 1, 1, 4, 9], 1], [[2, 9, 1, 5, 3, 9, 2], 3], [['apple', 'banana', 'cherry', 'ddate'], 1], [[9, 2, 10, 3, 9, 1, 5, 4, 9], 4], [[2, 1, 9, 1, 1, 4, 9], 5], [[4, 6, 9, 2, 1, 3, 5, 3, 2], 5], [['cherry', 'cherry', 'y', 'cherrry'], 3], [[2, 1, 9, 10, 1, 1, 4, 9], 1], [[6, 9, 1, 5, 3, 2], 3], [['apple', 'banana', 'cherry', 'date', 'date'], 1], [[6, 1, 6, 5, 3], 4], [[6, 2, 1, 5, 9, 3, 3], 5], [[9, 2, 1, 5, 3], 2]]
results = [[4, 3, 2, 1, 5, 6], [5, 4, 6, 7], [7, 8, 9, 6, 5], [1, 2, 9, 6, 5, 3], ['cherry', 'banana', 'apple', 'date'], [5, 1, 2, 9, 6, 3], ['date', 'cherry', 'apple'], ['date', 'cherry', 'banana', 'apple'], ['cherry', 'cherry', 'banana', 'apple', 'date'], [1, 2, 9, 6, 5, 3, 2], [5, 1, 2, 9, 3], [3, 5, 2, 9, 6], [1, 9, 2, 9, 5, 3], ['apple', 'banana', 'cherry', 'date'], [9, 2, 9, 1, 5, 3], ['deate', 'cherry', 'apple'], [2, 9, 6, 1, 5, 3], ['cherry', 'banana', 'cherrry', 'apple', 'date'], [9, 6, 2, 1, 5, 3], [5, 2, 9, 6, 1, 5, 3, 2], [9, 2, 9, 1, 5, 3, 9], [6, 9, 2, 1, 5, 3], [9, 2, 1, 5, 3], ['cherry', 'apple', 'deate'], ['apple', 'cherry', 'date'], ['banana', 'cherrry', 'apple', 'applpe', 'cherry', 'date', 'applpe'], ['cherry', 'cherry', 'apple'], ['cherry', 'cherry', 'apple', 'cherry'], ['date', 'banana', 'cherrry', 'apple'], [9, 2, 9, 1, 5, 3, 9, 5], [9, 2, 9, 1, 1, 3, 9, 5], ['apple', 'cherry', 'cherry', 'date'], ['cherry', 'cherry', 'cherry', 'apple'], [9, 2, 10, 3, 9, 1, 5, 3, 9], ['cherry', 'cherry', 'cherry'], [5, 1, 2, 6, 3], ['cherry', 'cherrry', 'banana', 'apple', 'date'], [9, 6, 2, 5, 3], [9, 2, 9, 1, 1, 3, 9], [9, 2, 1, 5, 3, 2], [5, 2, 9, 6, 4, 1, 5, 3, 2], [6, 1, 2, 6, 5, 3], [9, 2, 9, 1, 5, 3, 9, 5], [2, 9, 9, 1, 1, 3, 9], [2, 9, 10, 3, 9, 1, 5, 3, 9], [3, 1, 2, 9, 6, 5, 3], [1, 2, 9, 6, 4, 3, 5, 3], ['banana', 'apple', 'cherry', 'date'], [5, 6, 1, 2, 5, 3], [2, 9, 6, 1, 5, 3, 2], [2, 9, 10, 3, 9, 1, 5, 4, 9], ['cherry', 'banana', 'apple', 'date', 'date'], [9, 2, 9, 1, 1, 4, 9], [9, 2, 9, 1, 5, 3], ['date', 'cherry', 'banana', 'apple', 'date'], [9, 2, 2, 9, 1, 5, 3], [3, 5, 1, 2, 5], [1, 2, 9, 5, 3], [5, 1, 2, 6, 3, 2], [9, 2, 9, 1, 1, 1, 4, 9], [3, 9, 2, 9, 1, 1, 3, 9], ['apple', 'banana', 'cherrry', 'cherry', 'date'], ['cherry', 'apple', 'cdatey', 'deate'], ['apple', 'cherrry', 'banana', 'cherry', 'date'], [10, 2, 9, 3, 9, 1, 5, 4, 9], [9, 2, 2, 9, 3, 1, 5, 3], [9, 5, 1, 2, 6, 3], [3, 5, 1, 2, 9, 6, 2], ['ccdateyherry', 'banana', 'cherrry', 'apple', 'date'], ['banana', 'cherrry', 'apple', 'applpe', 'cherry', 'date', 'applpe', 'applpe'], ['date', 'cherry', 'banana', 'cdatey'], [3, 5, 2, 6, 2], [6, 9, 2, 5, 3], [2, 7, 9, 6, 1, 5, 3, 7], ['apple', 'cherry', 'cherry', 'aepple', 'date'], [2, 3, 5, 6], [2, 4, 9, 6, 1, 5, 3, 2], [5, 1, 2, 9, 3, 9], ['apple', 'banana', 'cherry', 'date', 'banana'], ['deate', 'cherry', 'apple', 'cdatey'], [1, 2, 9, 1, 1, 4, 9], [3, 5, 1, 2, 9, 6], [1, 2, 5, 9, 1, 1, 4, 9], ['aepple', 'apple', 'banana', 'cherrry', 'cherry', 'date'], [5, 1, 9, 2, 9, 3], [10, 2, 9, 1, 5, 3, 9], [5, 2, 9, 3], [1, 2, 5, 9, 1, 1, 4, 9, 9, 1], [2, 9, 6, 3, 1, 5, 3], [1, 9, 2, 5, 3, 9, 5], [9, 3, 2, 10, 3, 9, 1, 5, 3, 9], ['apple', 'cdatey', 'appple', 'cherry', 'deate'], [2, 1, 9, 1, 1, 4, 9], [1, 9, 2, 5, 3, 9, 2], ['apple', 'banana', 'cherry', 'ddate'], [3, 10, 2, 9, 9, 1, 5, 4, 9], [1, 1, 9, 1, 2, 4, 9], [1, 2, 9, 6, 4, 3, 5, 3, 2], ['y', 'cherry', 'cherry', 'cherrry'], [2, 1, 9, 10, 1, 1, 4, 9], [1, 9, 6, 5, 3, 2], ['apple', 'banana', 'cherry', 'date', 'date'], [5, 6, 1, 6, 3], [9, 5, 1, 2, 6, 3, 3], [2, 9, 1, 5, 3]]

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
        func_name = "reverse_Array_Upto_K"
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
        for test_case in ['assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]', 'assert reverse_Array_Upto_K([4, 5, 6, 7], 2) == [5, 4, 6, 7]', 'assert reverse_Array_Upto_K([9, 8, 7, 6, 5],3) == [7, 8, 9, 6, 5]']:
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
