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
inputs = [[12], [15], [24], [100], [0], [30], [29], [99], [101], [28], [98], [27], [26], [True], [False], [97], [25], [31], [32], [33], [23], [21], [34], [1], [35], [2], [22], [36], [3], [96], [95], [4], [102], [56], [5], [55], [54], [6], [20], [37], [39], [19], [38], [7], [53], [57], [8], [93], [43], [103], [104], [9], [18], [17], [52], [64], [16], [65], [94], [40], [66], [92], [41], [67], [58], [63], [68], [105], [60], [69], [59], [106], [51], [70], [42], [88], [89], [107], [50], [71], [91], [62], [49], [10], [48], [108], [44], [61], [87], [109], [90], [110], [111], [45], [11], [46], [47], [72], [112], [76], [86], [113], [114]]
results = [61, 73, 109, 413, 0.0, 133, 129, 409, 417, 125, 405, 121, 117, 10.5, 0.0, 401, 113, 137, 141, 145, 105, 97, 149, 10.5, 153, 21.0, 101, 157, 25, 397, 393, 29, 421, 237, 33, 233, 229, 37, 93, 161, 169, 89, 165, 41, 225, 241, 45, 385, 185, 425, 429, 49, 85, 81, 221, 269, 77, 273, 389, 173, 277, 381, 177, 281, 245, 265, 285, 433, 253, 289, 249, 437, 217, 293, 181, 365, 369, 441, 213, 297, 377, 261, 209, 53, 205, 445, 189, 257, 361, 449, 373, 453, 457, 193, 57, 197, 201, 301, 461, 317, 357, 465, 469]

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
        func_name = "dog_age"
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
        for test_case in ['assert dog_age(12)==61', 'assert dog_age(15)==73', 'assert dog_age(24)==109']:
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
