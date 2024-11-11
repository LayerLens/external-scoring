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
inputs = [[[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]], [[2, 3, 8, 4, 7, 9, 8, 7, 9, 15, 14, 10, 12, 13, 16, 18]], [[10, 20, 20, 30, 40, 90, 80, 50, 30, 20, 50, 10]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 72, 542, 542, 347, 347, 72, 687, 542]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 5]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 542, 347, 347, 72, 687, 542]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 542]], [[72, 1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 14]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541]], [[542, 347, 687, 789, 72, 235, 348, 542, 542, 687, 789, 789, 542, 72, 542, 542, 347, 347, 72, 687, 542]], [[542, 347, 687, 789, 3, 72, 348, 235, 542, 542, 687, 789, 789, 542, 72, 542, 542, 347, 347, 71, 687, 542]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 4]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [[1, 2, 3, 4, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]], [[1, 2, 3, 4, 5, 7, 8, 9, 11, 11, 12, 13, 14, 15]], [[1, 2, 3, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 6]], [[1, 2, 3, 4, 347, 6, 7, 8, 9, 10, 11, 12, 13, 14, 4]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10]], [[542, 347, 687, 789, 72, 235, 348, 542, 542, 687, 789, 542, 72, 542, 542, 347, 347, 72, 687, 542]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 14]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 72, 542, 542, 347, 347, 72, 687, 1, 542]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 12, 10, 11, 12, 13, 14, 15]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347]], [[72, 1, 2, 3, 4, 347, 5, 6, 3, 8, 9, 10, 11, 12, 13, 12, 14]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 12, 3]], [[1, 2, 3, 4, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]], [[72, 1, 2, 3, 4, 347, 5, 6, 3, 8, 9, 10, 11, 12, 13, 235, 14]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 3]], [[1, 2, 3, 4, 5, 7, 8, 9, 11, 11, 12, 72, 14, 15]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10, 9, 2]], [[72, 1, 2, 3, 4, 347, 5, 6, 3, 8, 9, 10, 11, 12, 13, 235, 14, 8]], [[1, 2, 3, 4, 5, 7, 8, 9, 11, 11, 12, 687, 72, 14, 15, 1]], [[1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 72, 14, 15]], [[542, 5, 687, 72, 235, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 2, 10, 11, 12, 14]], [[72, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 14]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 541, 347, 347, 687, 542]], [[72, 1, 2, 3, 4, 15, 347, 5, 6, 3, 8, 9, 10, 11, 12, 13, 235, 14, 8]], [[542, 6, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 541, 347, 347, 687, 542]], [[1, 2, 3, 4, 5, 7, 8, 9, 11, 11, 12, 13, 14, 15, 1, 1]], [[542, 5, 687, 72, 236, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347]], [[72, 1, 2, 3, 4, 347, 5, 6, 3, 8, 9, 10, 11, 12, 13, 3, 14]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 542, 347, 347, 72, 687, 542, 542]], [[542, 347, 687, 72, 235, 348, 542, 542, 687, 789, 542, 72, 542, 542, 347, 347, 72, 687, 542, 347]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 12, 13, 542, 14, 15, 3]], [[1, 2, 3, 4, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 9]], [[1, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10, 9, 13, 2]], [[542, 71, 347, 687, 789, 72, 235, 348, 542, 542, 687, 789, 789, 542, 72, 542, 543, 347, 347, 72, 687, 542]], [[1, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10, 9, 13, 2, 7]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 7, 14, 15]], [[1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 72, 14, 15, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10, 11, 12, 13, 14, 15, 10]], [[1, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10, 9, 13, 2, 7, 14]], [[542, 347, 687, 789, 72, 235, 542, 789, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347]], [[542, 5, 687, 72, 72, 236, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347]], [[1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 72, 14, 15, 11]], [[1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 13, 14, 15, 1, 1]], [[542, 5, 687, 72, 236, 542, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347, 542, 542, 789]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 14, 8]], [[72, 8, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 14]], [[542, 347, 687, 789, 3, 72, 348, 235, 542, 542, 687, 789, 789, 542, 72, 542, 347, 347, 71, 687, 542]], [[1, 2, 3, 4, 6, 7, 8, 8, 9, 10, 11, 11, 13, 3, 15]], [[1, 2, 3, 347, 5, 6, 71, 8, 9, 10, 11, 12, 13, 14]], [[1, 2, 3, 4, 4, 5, 6, 8, 9, 10, 11, 3, 235, 13, 14, 15]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 12, 13, 542, 14, 15, 3, 542]], [[542, 347, 687, 789, 72, 235, 542, 789, 542, 687, 789, 789, 542, 542, 2, 347, 347, 72, 687, 541, 347]], [[72, 8, 2, 3, 4, 347, 6, 7, 8, 9, 10, 11, 12, 13, 13, 14, 8]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [[1, 2, 3, 4, 5, 7, 8, 11, 11, 12, 72, 14, 15, 8]], [[1, 543, 2, 3, 0, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [[72, 1, 2, 3, 3, 4, 347, 15, 6, 3, 8, 9, 10, 11, 12, 13, 14]], [[1, 2, 3, 347, 5, 6, 71, 8, 9, 10, 11, 12, 13, 14, 12]], [[1, 2, 3, 4, 15, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10, 11, 12, 13, 14, 15, 10, 10, 10]], [[542, 347, 687, 789, 72, 235, 542, 542, 687, 789, 789, 542, 72, 542, 542, 347, 347, 72, 542]], [[1, 2, 3, 4, 71, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]], [[542, 347, 687, 789, 3, 72, 348, 235, 542, 542, 687, 789, 789, 542, 72, 542, 347, 347, 71, 687, 4, 542, 347]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10, 9, 2, 12]], [[1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 7, 14, 15]], [[72, 1, 2, 3, 4, 347, 5, 6, 3, 8, 9, 10, 11, 12, 13, 3, 14, 3]], [[1, 2, 3, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 12, 3]], [[1, 2, 3, 4, 5, 7, 9, 11, 11, 12, 13, 14, 235, 15]], [[1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 12, 3, 12, 14]], [[1, 2, 3, 4, 14, 5, 7, 8, 9, 11, 11, 12, 13, 14, 15, 1, 1, 1]], [[542, 347, 687, 789, 235, 542, 542, 687, 789, 789, 542, 72, 542, 542, 347, 347, 72, 687, 542]], [[1, 2, 3, 4, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 5, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 10]], [[3, 347, 687, 789, 72, 235, 542, 542, 687, 789, 542, 542, 541, 347, 347, 687, 542, 789]], [[2, 3, 347, 5, 6, 71, 8, 9, 11, 12, 13, 14]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 10, 9, 5]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 542, 14, 15, 3]], [[1, 2, 3, 4, 347, 6, 7, 9, 10, 11, 12, 13, 14, 4, 13, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 10, 10, 11, 12, 13, 14, 15, 5, 9, 1]], [[3, 347, 687, 789, 72, 235, 542, 687, 789, 542, 542, 541, 347, 348, 687, 542, 789]], [[542, 347, 5, 687, 72, 72, 236, 542, 687, 789, 789, 542, 542, 347, 347, 72, 687, 541, 347]], [[0, 1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 72, 14, 15, 9]], [[1, 2, 4, 5, 7, 8, 9, 1, 11, 11, 12, 13, 14, 15, 1, 1, 13]], [[1, 2, 4, 5, 7, 8, 9, 11, 11, 12, 72, 15, 9]], [[542, 71, 789, 72, 235, 542, 542, 687, 789, 789, 542, 542, 542, 347, 72, 687, 542]], [[14, 1, 2, 3, 4, 347, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 12, 3]], [[542, 347, 687, 789, 73, 235, 348, 542, 542, 687, 789, 542, 72, 542, 542, 347, 347, 72, 687, 542]]]
results = [2, 8, 20, 1, 542, 5, 542, 8, 1, 542, 12, 542, 542, 542, 4, 4, 4, 11, 6, 4, 8, 542, 1, 542, 4, 542, 3, 3, 8, 3, 3, 11, 2, 3, 1, 11, 542, 2, 12, 542, 3, 542, 1, 542, 3, 542, 542, 3, 8, 3, 542, 3, 4, 9, 8, 3, 542, 542, 11, 1, 542, 8, 8, 542, 3, 1, 3, 3, 542, 8, 1, 8, 1, 3, 12, 15, 10, 542, 8, 542, 2, 7, 3, 3, 11, 12, 1, 542, 4, 5, 9, 542, 2, 5, 3, 4, 1, 542, 542, 9, 1, 9, 542, 14, 542]

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
        func_name = "max_occurrences"
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
        for test_case in ['assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2', 'assert max_occurrences([2,3,8,4,7,9,8,7,9,15,14,10,12,13,16,18])==8', 'assert max_occurrences([10,20,20,30,40,90,80,50,30,20,50,10])==20']:
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
