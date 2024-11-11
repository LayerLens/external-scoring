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
inputs = [[9], [10], [11], [65], [77], [2147483647], [123456], [0], [9223372036854775807], [34211], [2047], [31580], [123455], [31579], [34212], [2147483646], [False], [123453], [31578], [True], [2147483645], [31581], [1], [34213], [123454], [34210], [2046], [2], [2147483648], [53], [31577], [9223372036854775806], [34215], [9223372036854775805], [34208], [34214], [123457], [34209], [78], [3], [31582], [52], [9223372036854775804], [58], [9223372036854775803], [59], [60], [57], [34216], [9223372036854775802], [51], [2045], [9223372036854775808], [31576], [2044], [79], [123452], [2147483644], [123458], [123451], [31583], [54], [123459], [2147483649], [31575], [123460], [56], [95], [94], [123450], [123449], [55], [9223372036854775809], [9223372036854775801], [34217], [34207], [31584], [123448], [4], [123461], [2043], [93], [16], [80], [31574], [2147483643], [81], [50], [91], [47], [123464], [123465], [2147483650], [9223372036854775810], [123466], [9223372036854775800], [49], [34218], [92], [46], [34219], [83], [2048], [48], [15], [31585], [31586], [2147483651], [2147483642], [96], [17]]
results = [15, 12, 13, 127, 115, 1073741825, 73150, 0, 4611686018427387905, 64093, 1025, 17570, 73153, 17573, 64090, 1073741824, 0, 73155, 17572, 3, 1073741827, 17571, 3, 64091, 73152, 64092, 1024, 2, 4294967294, 43, 17575, 4611686018427387904, 64089, 4611686018427387907, 64094, 64088, 73151, 64095, 112, 3, 17568, 42, 4611686018427387906, 36, 4611686018427387909, 37, 34, 39, 64086, 4611686018427387908, 45, 1027, 18446744073709551614, 17574, 1026, 113, 73154, 1073741826, 73148, 73157, 17569, 40, 73149, 4294967295, 17577, 73146, 38, 97, 96, 73156, 73159, 41, 18446744073709551615, 4611686018427387911, 64087, 64097, 17566, 73158, 6, 73147, 1029, 99, 30, 110, 17576, 1073741829, 111, 44, 101, 49, 73142, 73143, 4294967292, 18446744073709551612, 73140, 4611686018427387910, 47, 64084, 98, 48, 64085, 109, 4094, 46, 9, 17567, 17564, 4294967293, 1073741828, 94, 31]

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
        func_name = "toggle_middle_bits"
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
        for test_case in ['assert toggle_middle_bits(9) == 15', 'assert toggle_middle_bits(10) == 12', 'assert toggle_middle_bits(11) == 13', 'assert toggle_middle_bits(0b1000001) == 0b1111111', 'assert toggle_middle_bits(0b1001101) == 0b1110011']:
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
