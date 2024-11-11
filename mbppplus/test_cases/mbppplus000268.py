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
inputs = [[10], [15], [20], [1000000], [100000000], [1000001], [53], [54], [True], [99999999], [999999], [52], [100000001], [55], [999998], [1000002], [100000002], [1000003], [100000003], [100000004], [56], [99999998], [100000005], [100000006], [99999997], [57], [99999996], [29], [28], [58], [999996], [999997], [59], [27], [51], [99999995], [60], [99999994], [999995], [50], [61], [999994], [99999993], [5], [4], [62], [85], [63], [64], [3], [30], [999993], [86], [100000007], [2], [83], [6], [31], [26], [32], [7], [1], [1000004], [25], [65], [66], [9], [33], [84], [68], [1000005], [87], [1000006], [99999992], [67], [82], [1000007], [35], [88], [49], [81], [93], [69], [48], [92], [34], [80], [8], [999992], [1000008]]
results = [(55, 5.5), (120, 8.0), (210, 10.5), (500000500000, 500000.5), (5000000050000000, 50000000.5), (500001500001, 500001.0), (1431, 27.0), (1485, 27.5), (1, 1.0), (4999999950000000, 50000000.0), (499999500000, 500000.0), (1378, 26.5), (5000000150000001, 50000001.0), (1540, 28.0), (499998500001, 499999.5), (500002500003, 500001.5), (5000000250000003, 50000001.5), (500003500006, 500002.0), (5000000350000006, 50000002.0), (5000000450000010, 50000002.5), (1596, 28.5), (4999999850000001, 49999999.5), (5000000550000015, 50000003.0), (5000000650000021, 50000003.5), (4999999750000003, 49999999.0), (1653, 29.0), (4999999650000006, 49999998.5), (435, 15.0), (406, 14.5), (1711, 29.5), (499996500006, 499998.5), (499997500003, 499999.0), (1770, 30.0), (378, 14.0), (1326, 26.0), (4999999550000010, 49999998.0), (1830, 30.5), (4999999450000015, 49999997.5), (499995500010, 499998.0), (1275, 25.5), (1891, 31.0), (499994500015, 499997.5), (4999999350000021, 49999997.0), (15, 3.0), (10, 2.5), (1953, 31.5), (3655, 43.0), (2016, 32.0), (2080, 32.5), (6, 2.0), (465, 15.5), (499993500021, 499997.0), (3741, 43.5), (5000000750000028, 50000004.0), (3, 1.5), (3486, 42.0), (21, 3.5), (496, 16.0), (351, 13.5), (528, 16.5), (28, 4.0), (1, 1.0), (500004500010, 500002.5), (325, 13.0), (2145, 33.0), (2211, 33.5), (45, 5.0), (561, 17.0), (3570, 42.5), (2346, 34.5), (500005500015, 500003.0), (3828, 44.0), (500006500021, 500003.5), (4999999250000028, 49999996.5), (2278, 34.0), (3403, 41.5), (500007500028, 500004.0), (630, 18.0), (3916, 44.5), (1225, 25.0), (3321, 41.0), (4371, 47.0), (2415, 35.0), (1176, 24.5), (4278, 46.5), (595, 17.5), (3240, 40.5), (36, 4.5), (499992500028, 499996.5), (500008500036, 500004.5)]

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
        func_name = "sum_average"
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
        for test_case in ['assert sum_average(10)==(55, 5.5)', 'assert sum_average(15)==(120, 8.0)', 'assert sum_average(20)==(210, 10.5)']:
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
