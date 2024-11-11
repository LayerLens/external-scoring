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
inputs = [[10], [2], [3], [100], [1000], [10000], [1000000], [49284], [76589], [92346], [109872], [92345], [76590], [1001], [10001], [109871], [True], [101], [99], [109873], [76588], [109870], [999999], [999998], [28], [9999], [109874], [49283], [102], [76591], [98], [92344], [29], [999], [109869], [109868], [97], [109867], [49285], [9998], [109866], [88], [49282], [30], [109876], [87], [31], [49280], [92343], [32], [92342], [49281], [103], [76592], [999997], [85], [95], [76587], [25], [86], [89], [104], [96], [27], [109875], [84], [1000001], [9997], [997], [49286], [1002], [105], [11], [9996], [1000002], [92341], [9], [8], [1000003], [76586], [109865], [12], [76585], [26], [996], [33], [49287], [92340], [76593], [92347], [76584], [7], [92348], [34], [92339], [106], [6], [76594], [109864], [92338], [998], [49288], [76595], [92337], [76583], [13], [83], [1004], [23], [82]]
results = [6, 1, 2, 57, 510, 5373, 510403, 26387, 40520, 49477, 58093, 49476, 40521, 510, 5374, 58093, 1, 57, 56, 58094, 40520, 58093, 510402, 510402, 16, 5372, 58094, 26386, 57, 40522, 56, 49476, 16, 509, 58093, 58093, 55, 58093, 26387, 5372, 58092, 50, 26385, 16, 58094, 49, 16, 26383, 49476, 16, 49475, 26384, 58, 40522, 510402, 48, 54, 40520, 15, 48, 51, 58, 54, 15, 58094, 48, 510403, 5371, 509, 26388, 510, 58, 7, 5370, 510403, 49475, 5, 4, 510403, 40519, 58092, 7, 40519, 15, 509, 17, 26389, 49474, 40523, 49477, 40518, 4, 49477, 18, 49473, 58, 4, 40523, 58092, 49473, 509, 26390, 40523, 49473, 40517, 8, 47, 510, 14, 47]

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
        func_name = "sequence"
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
        for test_case in ['assert sequence(10) == 6', 'assert sequence(2) == 1', 'assert sequence(3) == 2']:
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
