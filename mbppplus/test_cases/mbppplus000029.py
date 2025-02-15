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
inputs = [[[5, 15, 37, 25, 79]], [[41, 32, 15, 19, 22]], [[99, 15, 13, 47]], [[500, 1000, 1500, 2000, 3000]], [[444444444, 555555555, 777777777, 888888888, 999999999]], [[1000000000, 2000000000, 5000000000, 10000000000]], [[1, 2, 2, 3, 4, 7, 8, 8]], [[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[11, 22, 33, 44, 55, 66, 77, 88, 99]], [[99, 444444444, 777777777, 888888888, 999999999]], [[11, 22, 31, 32, 33, 55, 66, 77, 88]], [[500, 999, 1500, 3000]], [[11, 22, 33, 55, 66, 77, 88, 99, 10000000000]], [[11, 22, 31, 32, 33, 55, 66, 66, 77, 77]], [[1, 2, 3, 4, 4, 5, 7, 8, 9, 10]], [[11, 22, 33, 44, 44, 55, 66, 77, 88, 99]], [[11, 22, 33, 33, 55, 66, 77, 88, 99, 9999999999]], [[11, 22, 32, 33, 33, 55, 66, 66, 77, 77]], [[11, 22, 22, 31, 32, 32, 33, 55, 66, 77, 88]], [[1, 2, 3, 4, 5, 6, 6, 7, 9, 9, 10]], [[11, 11, 22, 33, 44, 55, 66, 66, 88, 99]], [[11, 11, 22, 44, 55, 66, 66, 89, 99]], [[2, 3, 4, 5, 6, 6, 7, 9, 9, 10, 6999]], [[11, 11, 44, 55, 66, 66, 89, 99]], [[11, 11, 22, 22, 22, 33, 55, 66, 77, 99, 10000000000]], [[1000000000, 2000000000, 2000000000, 10000000000]], [[1, 2, 3, 4, 4, 7, 8, 8]], [[1, 2, 3, 4, 7, 8, 8, 77]], [[500, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 9000, 10000]], [[11, 22, 33, 44, 55, 66, 66, 77, 88, 99]], [[1, 2, 3, 4, 4, 5, 7, 8, 9, 9, 10]], [[1, 2, 2, 3, 4, 7, 8, 8, 1000000000]], [[1999999999, 2000000000, 5000000000, 10000000000]], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]], [[11, 33, 44, 44, 55, 66, 77, 88, 88, 99]], [[11, 22, 31, 32, 33, 55, 66, 67, 77, 77]], [[11, 22, 33, 33, 44, 55, 66, 66, 77, 88, 99]], [[8, 11, 22, 33, 44, 66, 77, 88, 99]], [[500, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 8000, 9000, 10000]], [[1, 2, 3, 4, 4, 5, 7, 8, 9, 9, 10, 99]], [[11, 33, 44, 44, 55, 66, 77, 88, 88, 99, 99]], [[99, 6999, 444444444, 777777777, 888888888, 888888889, 999999999]], [[1999999999, 2000000000, 9999999999, 10000000000]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5, 6, 6, 8, 9, 9, 10]], [[11, 22, 33, 33, 44, 55, 65, 66, 77, 88, 99]], [[1, 2, 3, 5, 6, 7, 9, 9, 10, 888888888, 888888888]], [[11, 22, 33, 33, 44, 55, 65, 66, 77, 88, 99, 4000]], [[11, 22, 33, 33, 44, 55, 65, 66, 77, 88, 99, 4000, 444444444]], [[1999999999, 2000000000, 5000000000, 5000000000, 10000000000]], [[11, 22, 31, 32, 33, 55, 66, 66, 66, 77, 77]], [[22, 33, 1999999999, 2000000000, 10000000000]], [[11, 22, 33, 33, 44, 55, 65, 66, 77, 99]], [[500, 500, 1000, 3000, 3001, 4000, 5000, 6000, 7000, 7001, 8000, 8000, 9000, 10000]], [[1, 23, 33, 1999999999, 2000000000, 9999999999, 10000000000]], [[11, 33, 43, 44, 54, 55, 66, 77, 77, 88, 88, 99, 99]], [[10, 22, 33, 33, 44, 55, 65, 65, 66, 77, 99]], [[55, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]], [[1, 2, 3, 4, 4, 4, 7, 7, 8]], [[11, 22, 33, 44, 44, 55, 66, 66, 77, 88, 99]], [[11, 22, 32, 33, 34, 66, 66, 77, 77]], [[1, 2, 3, 4, 4, 7, 7, 8, 8]], [[1, 2, 3, 4, 4, 5, 7, 8, 9, 10, 100]], [[99, 6999, 444444444, 777777777, 888888888, 888888888, 888888889, 999999999]], [[11, 11, 44, 55, 66, 89, 99]], [[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10]], [[11, 22, 33, 33, 65, 66, 77, 88, 99, 4000, 444444444]], [[11, 22, 23, 31, 32, 32, 33, 55, 66, 77, 88]], [[99, 6999, 444444444, 888888888, 888888889, 999999999, 9999999999]], [[11, 11, 44, 44, 55, 66, 66, 89, 89, 99]], [[1, 2, 3, 4, 4, 5, 6, 8, 9, 10, 888888889]], [[11, 22, 32, 33, 33, 55, 66, 77, 88, 9999999999]], [[11, 22, 32, 33, 33, 66, 66, 88, 9999999999]], [[4000, 444444444, 1000000000, 2000000000, 2000000000, 5000000000, 10000000000]], [[11, 22, 33, 44, 55, 66, 77, 88, 99, 10000000000]], [[11, 22, 32, 33, 33, 33, 55, 66, 77, 77]], [[11, 22, 33, 33, 44, 55, 65, 77, 99]], [[11, 22, 33, 33, 65, 66, 77, 88, 99, 500, 501, 4000, 444444444]], [[55, 777777777, 888888888, 999999999]], [[11, 33, 33, 44, 55, 65, 66, 77, 77, 99, 4000, 444444444]], [[1, 2, 3, 4, 4, 4, 5, 7, 8, 9, 9, 9, 10, 99]], [[11, 23, 33, 44, 55, 66, 77, 88, 99, 10000000000]], [[44, 500, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 9000, 10000]], [[11, 22, 31, 32, 33, 33, 55, 66, 66, 77, 77]], [[1, 2, 3, 4, 5, 5, 6, 6, 8, 9, 9, 10]], [[11, 22, 31, 32, 32, 33, 55, 66, 77, 88]], [[1999999999, 2000000000, 2000000000, 9999999999, 10000000000]], [[444444444, 777777777, 888888888, 999999999, 1000000000]], [[65, 4000, 444444444, 1000000000, 2000000000, 2000000000, 5000000000, 10000000000]], [[33, 33, 44, 55, 65, 66, 77, 99, 4000, 444444444]], [[500, 500, 1000, 3000, 3001, 4000, 5000, 6000, 7000, 7001, 8000, 9000, 10000]], [[500, 999, 1500, 1500, 3000]], [[5, 11, 33, 33, 44, 55, 66, 77, 77, 99, 4000, 444444444]], [[44, 100, 500, 500, 1000, 3001, 5000, 6000, 7000, 8000, 9000, 10000]], [[1, 2, 3, 4, 4, 4, 4, 5, 7, 8, 8, 9, 9, 9, 10, 99]], [[3, 11, 22, 31, 32, 33, 55, 66, 66, 77, 77]], [[11, 11, 22, 33, 44, 66, 66, 88, 99]], [[1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10]], [[100, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 8000, 9000, 10000]], [[8, 11, 22, 31, 32, 33, 33, 55, 66, 66, 77, 77, 77]], [[1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10]], [[4, 99, 6999, 444444444, 777777777, 888888888, 888888888, 888888889, 999999999]], [[11, 22, 30, 32, 32, 33, 55, 66, 77, 88, 5000000000]], [[1, 2, 5, 6, 7, 8, 9, 9, 10, 888888888, 888888888]], [[11, 33, 44, 44, 55, 66, 77, 88, 88, 99, 100]], [[11, 32, 33, 33, 44, 55, 65, 66, 77, 77, 99, 4000, 444444444]], [[64, 65, 4000, 444444444, 1000000000, 2000000000, 2000000000, 5000000000, 10000000000]]]
results = [[5, 15, 25, 37, 79], [15, 19, 22, 32, 41], [13, 15, 47, 99], [500, 1000, 1500, 2000, 3000], [444444444, 555555555, 777777777, 888888888, 999999999], [1000000000, 2000000000, 5000000000, 10000000000], [1, 2, 2, 3, 4, 7, 8, 8], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 22, 33, 44, 55, 66, 77, 88, 99], [99, 444444444, 777777777, 888888888, 999999999], [11, 22, 31, 32, 33, 55, 66, 77, 88], [500, 999, 1500, 3000], [11, 22, 33, 55, 66, 77, 88, 99, 10000000000], [11, 22, 31, 32, 33, 55, 66, 66, 77, 77], [1, 2, 3, 4, 4, 5, 7, 8, 9, 10], [11, 22, 33, 44, 44, 55, 66, 77, 88, 99], [11, 22, 33, 33, 55, 66, 77, 88, 99, 9999999999], [11, 22, 32, 33, 33, 55, 66, 66, 77, 77], [11, 22, 22, 31, 32, 32, 33, 55, 66, 77, 88], [1, 2, 3, 4, 5, 6, 6, 7, 9, 9, 10], [11, 11, 22, 33, 44, 55, 66, 66, 88, 99], [11, 11, 22, 44, 55, 66, 66, 89, 99], [2, 3, 4, 5, 6, 6, 7, 9, 9, 10, 6999], [11, 11, 44, 55, 66, 66, 89, 99], [11, 11, 22, 22, 22, 33, 55, 66, 77, 99, 10000000000], [1000000000, 2000000000, 2000000000, 10000000000], [1, 2, 3, 4, 4, 7, 8, 8], [1, 2, 3, 4, 7, 8, 8, 77], [500, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 9000, 10000], [11, 22, 33, 44, 55, 66, 66, 77, 88, 99], [1, 2, 3, 4, 4, 5, 7, 8, 9, 9, 10], [1, 2, 2, 3, 4, 7, 8, 8, 1000000000], [1999999999, 2000000000, 5000000000, 10000000000], [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10], [11, 33, 44, 44, 55, 66, 77, 88, 88, 99], [11, 22, 31, 32, 33, 55, 66, 67, 77, 77], [11, 22, 33, 33, 44, 55, 66, 66, 77, 88, 99], [8, 11, 22, 33, 44, 66, 77, 88, 99], [500, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 8000, 9000, 10000], [1, 2, 3, 4, 4, 5, 7, 8, 9, 9, 10, 99], [11, 33, 44, 44, 55, 66, 77, 88, 88, 99, 99], [99, 6999, 444444444, 777777777, 888888888, 888888889, 999999999], [1999999999, 2000000000, 9999999999, 10000000000], [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 6, 8, 9, 9, 10], [11, 22, 33, 33, 44, 55, 65, 66, 77, 88, 99], [1, 2, 3, 5, 6, 7, 9, 9, 10, 888888888, 888888888], [11, 22, 33, 33, 44, 55, 65, 66, 77, 88, 99, 4000], [11, 22, 33, 33, 44, 55, 65, 66, 77, 88, 99, 4000, 444444444], [1999999999, 2000000000, 5000000000, 5000000000, 10000000000], [11, 22, 31, 32, 33, 55, 66, 66, 66, 77, 77], [22, 33, 1999999999, 2000000000, 10000000000], [11, 22, 33, 33, 44, 55, 65, 66, 77, 99], [500, 500, 1000, 3000, 3001, 4000, 5000, 6000, 7000, 7001, 8000, 8000, 9000, 10000], [1, 23, 33, 1999999999, 2000000000, 9999999999, 10000000000], [11, 33, 43, 44, 54, 55, 66, 77, 77, 88, 88, 99, 99], [10, 22, 33, 33, 44, 55, 65, 65, 66, 77, 99], [55, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], [1, 2, 3, 4, 4, 4, 7, 7, 8], [11, 22, 33, 44, 44, 55, 66, 66, 77, 88, 99], [11, 22, 32, 33, 34, 66, 66, 77, 77], [1, 2, 3, 4, 4, 7, 7, 8, 8], [1, 2, 3, 4, 4, 5, 7, 8, 9, 10, 100], [99, 6999, 444444444, 777777777, 888888888, 888888888, 888888889, 999999999], [11, 11, 44, 55, 66, 89, 99], [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10], [11, 22, 33, 33, 65, 66, 77, 88, 99, 4000, 444444444], [11, 22, 23, 31, 32, 32, 33, 55, 66, 77, 88], [99, 6999, 444444444, 888888888, 888888889, 999999999, 9999999999], [11, 11, 44, 44, 55, 66, 66, 89, 89, 99], [1, 2, 3, 4, 4, 5, 6, 8, 9, 10, 888888889], [11, 22, 32, 33, 33, 55, 66, 77, 88, 9999999999], [11, 22, 32, 33, 33, 66, 66, 88, 9999999999], [4000, 444444444, 1000000000, 2000000000, 2000000000, 5000000000, 10000000000], [11, 22, 33, 44, 55, 66, 77, 88, 99, 10000000000], [11, 22, 32, 33, 33, 33, 55, 66, 77, 77], [11, 22, 33, 33, 44, 55, 65, 77, 99], [11, 22, 33, 33, 65, 66, 77, 88, 99, 500, 501, 4000, 444444444], [55, 777777777, 888888888, 999999999], [11, 33, 33, 44, 55, 65, 66, 77, 77, 99, 4000, 444444444], [1, 2, 3, 4, 4, 4, 5, 7, 8, 9, 9, 9, 10, 99], [11, 23, 33, 44, 55, 66, 77, 88, 99, 10000000000], [44, 500, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 9000, 10000], [11, 22, 31, 32, 33, 33, 55, 66, 66, 77, 77], [1, 2, 3, 4, 5, 5, 6, 6, 8, 9, 9, 10], [11, 22, 31, 32, 32, 33, 55, 66, 77, 88], [1999999999, 2000000000, 2000000000, 9999999999, 10000000000], [444444444, 777777777, 888888888, 999999999, 1000000000], [65, 4000, 444444444, 1000000000, 2000000000, 2000000000, 5000000000, 10000000000], [33, 33, 44, 55, 65, 66, 77, 99, 4000, 444444444], [500, 500, 1000, 3000, 3001, 4000, 5000, 6000, 7000, 7001, 8000, 9000, 10000], [500, 999, 1500, 1500, 3000], [5, 11, 33, 33, 44, 55, 66, 77, 77, 99, 4000, 444444444], [44, 100, 500, 500, 1000, 3001, 5000, 6000, 7000, 8000, 9000, 10000], [1, 2, 3, 4, 4, 4, 4, 5, 7, 8, 8, 9, 9, 9, 10, 99], [3, 11, 22, 31, 32, 33, 55, 66, 66, 77, 77], [11, 11, 22, 33, 44, 66, 66, 88, 99], [1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10], [100, 500, 1000, 3001, 4000, 5000, 6000, 7000, 8000, 8000, 9000, 10000], [8, 11, 22, 31, 32, 33, 33, 55, 66, 66, 77, 77, 77], [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10], [4, 99, 6999, 444444444, 777777777, 888888888, 888888888, 888888889, 999999999], [11, 22, 30, 32, 32, 33, 55, 66, 77, 88, 5000000000], [1, 2, 5, 6, 7, 8, 9, 9, 10, 888888888, 888888888], [11, 33, 44, 44, 55, 66, 77, 88, 88, 99, 100], [11, 32, 33, 33, 44, 55, 65, 66, 77, 77, 99, 4000, 444444444], [64, 65, 4000, 444444444, 1000000000, 2000000000, 2000000000, 5000000000, 10000000000]]

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
        func_name = "comb_sort"
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
        for test_case in ['assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]', 'assert comb_sort([41, 32, 15, 19, 22]) == [15, 19, 22, 32, 41]', 'assert comb_sort([99, 15, 13, 47]) == [13, 15, 47, 99]']:
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
