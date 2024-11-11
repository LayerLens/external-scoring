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
inputs = [[2], [3], [1], [10], [100], [1000], [9], [7], [8], [998], [102], [101], [6], [99], [5], [997], [1001], [11], [999], [994], [993], [12], [True], [992], [13], [991], [990], [4], [995], [39], [1002], [996], [97], [16], [40], [1004], [41], [1005], [15], [103], [1006], [94], [989], [38], [17], [96], [95], [93], [14], [1003], [92], [1007], [98], [1008], [1009], [42], [35], [36], [37], [988], [43], [34], [104], [33], [65], [105], [44], [54], [106], [55], [32], [53], [56], [91], [31], [90], [52], [28], [30], [57], [29], [89], [18], [59], [66], [64], [63], [62], [60], [61], [27], [26], [88], [87], [107], [1010], [67], [85], [25], [1011], [51], [68], [50]]
results = [4.5, 12.0, 1.0, 302.5, 255025.0, 250500250.0, 225.0, 112.0, 162.0, 249001249.5, 270529.5, 262701.0, 73.5, 247500.0, 45.0, 248253997.0, 251252001.0, 396.0, 249750000.0, 246021212.5, 245279937.0, 507.0, 1.0, 244540152.0, 637.0, 243801856.0, 243065047.5, 25.0, 246763980.0, 15600.0, 252005254.5, 247508241.0, 232897.0, 1156.0, 16810.0, 253516275.0, 18081.0, 254274045.0, 960.0, 278512.0, 255033323.5, 212087.5, 242329725.0, 14449.5, 1377.0, 225816.0, 218880.0, 205437.0, 787.5, 252760012.0, 198927.0, 255794112.0, 240124.5, 256556412.0, 257320225.0, 19414.5, 11340.0, 12321.0, 13357.0, 241595887.0, 20812.0, 10412.5, 286650.0, 9537.0, 70785.0, 294945.0, 22275.0, 40837.5, 303398.5, 43120.0, 8712.0, 38637.0, 45486.0, 192556.0, 7936.0, 186322.5, 36517.0, 5887.0, 7207.5, 47937.0, 6525.0, 180225.0, 1624.5, 53100.0, 74068.5, 67600.0, 64512.0, 61519.5, 55815.0, 58621.0, 5292.0, 4738.5, 174262.0, 168432.0, 312012.0, 258085552.5, 77452.0, 157165.0, 4225.0, 258852396.0, 34476.0, 80937.0, 32512.5]

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
        func_name = "find_Average_Of_Cube"
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
        for test_case in ['assert find_Average_Of_Cube(2) == 4.5', 'assert find_Average_Of_Cube(3) == 12', 'assert find_Average_Of_Cube(1) == 1']:
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
