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
inputs = [[3], [5], [2], [0], [10], [100], [101], [99], [1], [102], [8], [4], [True], [False], [11], [9], [42], [7], [43], [103], [51], [6], [81], [82], [50], [52], [98], [12], [49], [97], [37], [41], [22], [26], [80], [40], [44], [13], [21], [46], [20], [96], [48], [45], [47], [53], [38], [79], [23], [25], [104], [19], [24], [95], [91], [78], [14], [36], [94], [39], [63], [93], [30], [62], [29], [77], [35], [90], [92], [28], [83], [89], [57], [18], [105], [61], [16], [15], [58], [27], [72], [56], [85], [33], [76], [73], [75], [59], [60], [17], [84], [55], [31], [74], [32], [88], [54], [87], [106], [64], [107], [108], [34]]
results = [30, 210, 6, 0, 2970, 25497450, 26527650, 24497550, 0, 27588756, 1260, 90, 0, 0, 4290, 1980, 814506, 756, 893970, 28681380, 1756950, 420, 11025720, 11577006, 1624350, 1897506, 23527350, 6006, 1499400, 22586256, 493506, 740460, 63756, 122850, 10494360, 671580, 979110, 8190, 53130, 1167480, 43890, 21673680, 1381800, 1070190, 1271256, 2046330, 548340, 9982440, 75900, 105300, 29806140, 35910, 89700, 20789040, 17518410, 9489480, 10920, 442890, 19931760, 607620, 4062240, 19101270, 215760, 3812256, 188790, 9015006, 396270, 16764930, 18297006, 164430, 12148710, 16036020, 2730756, 29070, 30963660, 3573990, 18360, 14280, 2925810, 142506, 6903756, 2545620, 13355370, 314160, 8558550, 7292700, 8119650, 3131130, 3347070, 23256, 12741330, 2370060, 245520, 7697850, 278256, 15331140, 2203740, 14649756, 32154570, 4324320, 33379506, 34639110, 353430]

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
        func_name = "difference"
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
        for test_case in ['assert difference(3) == 30', 'assert difference(5) == 210', 'assert difference(2) == 6']:
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
