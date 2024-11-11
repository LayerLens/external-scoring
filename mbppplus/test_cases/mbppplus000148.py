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
inputs = [[2], [3], [4], [100], [0], [1], [1000000], [10], [10000], [90], [89], [1000002], [91], [1000001], [False], [True], [1000003], [92], [9], [17], [10001], [101], [93], [99], [8], [999999], [87], [102], [9999], [94], [103], [86], [98], [105], [88], [49], [85], [50], [1000004], [9998], [104], [1000005], [51], [10002], [5], [7], [106], [52], [84], [35], [97], [11], [72], [999998], [16], [12], [1000006], [96], [48], [47], [6], [13], [999997], [95], [36], [999996], [14], [15], [1000007], [9997], [37], [1000008], [18], [999995], [81], [46], [38], [19], [82], [107], [83], [39], [45], [53], [999994], [44], [54], [55], [108], [10003], [25], [10004], [71], [999993], [28], [73], [20], [40], [26], [27], [1000009], [56], [43], [10005], [9996], [109]]
results = [20.0, 56.0, 120.0, 1353400.0, 0.0, 4.0, 1.333335333334e+18, 1540.0, 1333533340000.0, 988260.0, 955860.0, 1.333343333358e+18, 1021384.0, 1.333339333342e+18, 0.0, 4.0, 1.333347333382e+18, 1055240.0, 1140.0, 7140.0, 1333933420004.0, 1394204.0, 1089836.0, 1313400.0, 816.0, 1.333331333334e+18, 893200.0, 1435820.0, 1333133340000.0, 1125180.0, 1478256.0, 862924.0, 1274196.0, 1565620.0, 924176.0, 161700.0, 833340.0, 171700.0, 1.333351333414e+18, 1332733419996.0, 1521520.0, 1.333355333454e+18, 182104.0, 1334333580020.0, 220.0, 560.0, 1610564.0, 192920.0, 804440.0, 59640.0, 1235780.0, 2024.0, 508080.0, 1.3333273333419999e+18, 5984.0, 2600.0, 1.3333593335020004e+18, 1198144.0, 152096.0, 142880.0, 364.0, 3276.0, 1.3333233333579999e+18, 1161280.0, 64824.0, 1.3333193333819999e+18, 4060.0, 4960.0, 1.3333633335580006e+18, 1332333579980.0, 70300.0, 1.333367333622001e+18, 8436.0, 1.3333153334139999e+18, 721764.0, 134044.0, 76076.0, 9880.0, 748660.0, 1656360.0, 776216.0, 82160.0, 125580.0, 204156.0, 1.3333113334539999e+18, 117480.0, 215820.0, 227920.0, 1703016.0, 1334733820056.0, 22100.0, 1335134140120.0, 487344.0, 1.3333073335019996e+18, 30856.0, 529396.0, 11480.0, 88560.0, 24804.0, 27720.0, 1.3333713336940012e+18, 240464.0, 109736.0, 1335534540220.0, 1331933819944.0, 1750540.0]

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
        func_name = "square_Sum"
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
        for test_case in ['assert square_Sum(2) == 20', 'assert square_Sum(3) == 56', 'assert square_Sum(4) == 120']:
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
