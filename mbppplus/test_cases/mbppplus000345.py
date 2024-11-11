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
inputs = [[2], [3], [4], [1], [5], [69], [70], [6], [True], [71], [68], [7], [72], [67], [66], [8], [65], [64], [73], [9], [10], [63], [62], [60], [11], [61], [74], [75], [76], [18], [77], [59], [30], [17], [58], [78], [16], [39], [29], [15], [91], [28], [79], [31], [90], [12], [89], [13], [14], [40], [19], [41], [42], [32], [100], [43], [57], [20], [27], [80], [21], [56], [99], [81], [98], [97], [93], [33], [101], [92], [37], [35], [44], [82], [38], [83], [55], [94], [45], [84], [26], [53], [88], [52], [54], [87], [36], [50], [85], [95], [96], [102], [34], [51], [86], [22], [49], [103], [23], [25], [24]]
results = [82, 707, 3108, 1, 9669, 5004024325, 5377325366, 24310, 1, 5772579527, 4651748964, 52871, 6190741128, 4319598339, 4006697618, 103496, 3712197697, 3435274816, 6632791753, 187017, 317338, 3175130175, 2930989550, 2487744028, 511819, 2702102909, 7099740634, 7592625035, 8112510636, 6031074, 8660491917, 2287210107, 77688014, 4530449, 2099821386, 9237692542, 3344528, 288559271, 65570653, 2421007, 19967019163, 55014652, 9845265743, 91533855, 18893736042, 791660, 17867110361, 1182285, 1713726, 327509352, 7905235, 370556073, 418014394, 107286816, 31997333380, 470215019, 1924920761, 10218676, 45864027, 10484394704, 13044437, 1761873400, 30429094179, 11156292945, 28922955698, 27477055073, 22259882909, 125137441, 33629574181, 21088532284, 221765605, 167955683, 527504780, 11862204706, 253406230, 12603405331, 1610066359, 23482713870, 590247021, 13381201652, 37973546, 1337828597, 16885604120, 1216277972, 1468908198, 15947713495, 193367364, 999666690, 14196932373, 24758703711, 26089567072, 35327755862, 145288562, 1103727091, 15051968454, 16463238, 903607089, 37093856487, 20563863, 31208345, 25443544]

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
        func_name = "odd_num_sum"
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
        for test_case in ['assert odd_num_sum(2) == 82', 'assert odd_num_sum(3) == 707', 'assert odd_num_sum(4) == 3108']:
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
