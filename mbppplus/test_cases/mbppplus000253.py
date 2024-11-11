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
inputs = [[3, 4], [4, 5], [1, 2], [10, 20], [100, 50], [1000, 200], [100, 49], [200, 49], [100, 100], [1000, 199], [200, 200], [100, 200], [200, 50], [99, 100], [100, 101], [99, 99], [200, 201], [20, 100], [999, 1000], [20, 50], [21, 200], [99, 21], [998, 1000], [50, 51], [999, 100], [21, 100], [201, 199], [100, 998], [21, 21], [50, 50], [49, 200], [199, 199], [1000, 1000], [51, 100], [20, 1000], [201, 200], [20, 51], [10, 1000], [100, 1000], [201, 201], [49, 201], [999, 49], [21, 998], [101, 101], [998, 100], [998, 998], [100, 99], [99, 999], [200, 199], [21, 22], [999, 20], [200, 10], [999, 1001], [True, True], [99, 998], [199, 200], [10, 10], [198, 199], [21, 51], [198, 1000], [998, 999], [101, 100], [20, 10], [19, 20], [100, 21], [20, 20], [102, 102], [48, 201], [20, True], [199, 100], [1000, 102], [199, 50], [1001, 200], [49, 49], [22, 49], [51, 50], [101, 201], [48, 999], [101, 102], [199, 48], [99, True], [20, 201], [21, 9], [18, 19], [100, 11], [998, 49], [197, 197], [1001, 197], [20, 21], [10, 21], [999, 999], [199, 49], [1000, 21], [197, 196], [997, 101], [19, 997], [22, 48], [1000, 999], [200, 198], [1000, 1001], [1001, 101], [197, 201], [200, 8], [997, 997], [200, 196], [1001, 999]]
results = [33, 56, 5, 500, 20000, 1400000, 19800, 59600, 30000, 1398000, 120000, 50000, 60000, 29601, 30200, 29403, 120400, 4400, 2996001, 2400, 8841, 13959, 2992004, 7600, 1197801, 4641, 120399, 209600, 1323, 7500, 22001, 118803, 3000000, 12801, 40400, 120801, 2440, 20100, 210000, 121203, 22099, 1095903, 42357, 30603, 1195604, 2988012, 29800, 207603, 119600, 1365, 1037961, 44000, 2997999, 3, 207405, 119201, 300, 118008, 2583, 435204, 2990008, 30401, 800, 1121, 14200, 1200, 31212, 21600, 440, 79401, 1204000, 59501, 1402401, 7203, 2640, 7701, 50803, 98208, 30805, 58705, 9999, 8440, 819, 1008, 12200, 1093808, 116427, 1396395, 1240, 520, 2994003, 59103, 1042000, 116033, 1195403, 38247, 2596, 2998000, 119200, 3002000, 1204203, 118003, 43200, 2982027, 118400, 3001999]

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
        func_name = "surface_Area"
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
        for test_case in ['assert surface_Area(3,4) == 33', 'assert surface_Area(4,5) == 56', 'assert surface_Area(1,2) == 5']:
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
