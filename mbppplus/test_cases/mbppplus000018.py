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
inputs = [[5], [10], [15], [100], [99], [98], [96], [101], [97], [102], [22], [True], [23], [103], [104], [21], [95], [105], [20], [7], [9], [8], [6], [4], [106], [24], [19], [11], [94], [25], [3], [26], [93], [12], [108], [92], [42], [41], [43], [107], [2], [1], [13], [14], [38], [39], [53], [37], [52], [18], [54], [91], [55], [51], [50], [40], [90], [89], [56], [17], [76], [109], [110], [111], [27], [16], [44], [57], [88], [77], [58], [75], [28], [113], [112], [87], [59], [78], [70], [71], [69], [86], [72], [45], [47], [46], [49], [29], [60], [36], [30], [85], [48], [73], [84], [114], [31], [35], [34], [79], [83]]
results = [65, 280, 645, 29800, 29205, 28616, 27456, 30401, 28033, 31008, 1408, 1, 1541, 31621, 32240, 1281, 26885, 32865, 1160, 133, 225, 176, 96, 40, 33496, 1680, 1045, 341, 26320, 1825, 21, 1976, 25761, 408, 34776, 25208, 5208, 4961, 5461, 34133, 8, 1, 481, 560, 4256, 4485, 8321, 4033, 8008, 936, 8640, 24661, 8965, 7701, 7400, 4720, 24120, 23585, 9296, 833, 17176, 35425, 36080, 36741, 2133, 736, 5720, 9633, 23056, 17633, 9976, 16725, 2296, 38081, 37408, 22533, 10325, 18096, 14560, 14981, 14145, 22016, 15408, 5985, 6533, 6256, 7105, 2465, 10680, 3816, 2640, 21505, 6816, 15841, 21000, 38760, 2821, 3605, 3400, 18565, 20501]

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
        func_name = "is_octagonal"
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
        for test_case in ['assert is_octagonal(5) == 65', 'assert is_octagonal(10) == 280', 'assert is_octagonal(15) == 645']:
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
