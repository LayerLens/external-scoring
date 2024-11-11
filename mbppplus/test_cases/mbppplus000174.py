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
inputs = [[1, 2], [-5, -4], [0, 0], [1000, 999], [-1000, -999], [0.5, 0.4], [-0.5, -0.4], [1.23456789, 1.23456788], [-1.23456789, -1.23456788], [3, -5], [-10, 8], [-7, -3], [-inf, inf], [0, 1], [0, -1], [0.12345678901234568, 0.9876543210987654], [10000000000000000000000, -9999999999999999999999], [-9999999999999999999999, -10000000000000000000000], [1e-30, 2e-30], [-1e-30, 1e-30], [1e+22, -1e+22], [-1e+22, -1e+22], [1e+100, 1e+101], [9999999999999999999999999, 1e+100], [9999999999999999999999999, -1e+100], [-1e+100, 9999999999999999999999999], [-inf, 1e-30], [0.12345678901234568, 0.6227470969848448], [-9999999999999999999999, -1], [-5, 1e+100], [10000000000000000000000, 3], [0.12345678901234568, 0.12345678901234568], [-1, -2], [1.23456788, 0.9876543210987654], [1.23456789, 1.23456789], [0.3393732857470154, 0.4], [0.9876543210987654, 0.9876543210987654], [-0.5, -1.23456789], [0.5, 1.23456788], [1.23456788, 1.23456788], [3, -9999999999999999999999], [-inf, 0.9876543210987654], [1000, 1000], [1e-30, -1.23456788], [0.9876543210987654, 1.23456789], [-1e+100, -1e+100], [-inf, -inf], [9999999999999999999999, -9999999999999999999999], [-0.07506072001847719, 1e-30], [1.23456788, 1.23456789], [1e-30, -0.7328249760252548], [2e-30, -inf], [1e-30, 1.23456788], [-inf, -0.5], [3, 10000000000000000000000], [1e+100, 0.4], [0, -9999999999999999999999], [-3, -1], [-0.5, 0.4], [-1e-30, 0.4], [1e-30, -1e+100], [1e-30, -6.511591469260396e+99], [2e-30, 2e-30], [-inf, 0.6227470969848448], [-1e+22, 0.4], [0.6227470969848448, -0.29444729972854533], [-9999999999999999999999, -9999999999999999999999], [0.46026738039655424, 1.23456788], [-1e+100, inf], [-999, -9999999999999999999999], [-1e+22, 0.6227470969848448], [1.23456788, 1.3699399338796618], [inf, 0.6227470969848448], [1.23456789, 1.4183245112641576], [2e-30, -1e+100], [-3, 1], [-0.5, -0.5], [3, 10000000000000000000001], [-1.23456789, -0.8219041516621808], [-5, -5], [1e+22, -inf], [-5, -3], [-3, -3], [-9999999999999999999999, 9999999999999999999999999], [0.4, 0.5], [9999999999999999999999999, 9999999999999999999999998], [0.4, 0.4], [9999999999999999999999999, 10000000000000000000000], [-0.07506072001847719, 0.6227470969848448], [10000000000000000000001, 3], [-0.4565540470320447, -0.9016404675969094], [-0.7328249760252548, 1.3699399338796618], [0.46582533596598436, 0.33863302089208697], [1e+100, 1e+100], [0.5170315488171091, 1.23456788], [inf, inf], [1e-30, -inf], [-3, -4], [0.9844734927681069, 0.9844734927681069], [1e+100, 9.775453772147561e+99], [-3, -5], [-7, 999], [-1e-30, -0.30387334753977924], [-0.4340218895905736, -0.5], [1.0499093088834509e-30, 1.0499093088834509e-30], [-0.30387334753977924, 9999999999999999999999999], [-0.07506072001847719, -0.056386079676076895], [999, -10000000000000000000000], [10000000000000000000000, -999], [0.5502904923114273, 0.9876543210987654], [1.3699399338796618, -0.8219041516621808], [-0.7328249760252548, 0.4], [-1e-30, 1e+101], [0.4, 1e-30], [9999999999999999999999999, -1], [-999, -999], [-0.4399369615846679, 9999999999999999999999999], [-0.47412425472639685, -0.07506072001847719], [9999999999999999999999999, -1.23456789], [-9999999999999999999999, 3], [-1, 9999999999999999999999], [0.46582533596598436, -1.2456261076289474], [1.137575447277081e+100, 1e+101], [-0.2805435883831953, -0.3079438825335931], [-6.7523459788417035e-31, 7.414663687211649e-31], [-0.10974338446002693, 1e-30]]
results = [1, -5, 0, 999, -1000, 0.4, -0.5, 1.23456788, -1.23456789, -5, -10, -7, -inf, 0, -1, 0.12345678901234568, -9999999999999999999999, -10000000000000000000000, 1e-30, -1e-30, -1e+22, -1e+22, 1e+100, 9999999999999999999999999, -1e+100, -1e+100, -inf, 0.12345678901234568, -9999999999999999999999, -5, 3, 0.12345678901234568, -2, 0.9876543210987654, 1.23456789, 0.3393732857470154, 0.9876543210987654, -1.23456789, 0.5, 1.23456788, -9999999999999999999999, -inf, 1000, -1.23456788, 0.9876543210987654, -1e+100, -inf, -9999999999999999999999, -0.07506072001847719, 1.23456788, -0.7328249760252548, -inf, 1e-30, -inf, 3, 0.4, -9999999999999999999999, -3, -0.5, -1e-30, -1e+100, -6.511591469260396e+99, 2e-30, -inf, -1e+22, -0.29444729972854533, -9999999999999999999999, 0.46026738039655424, -1e+100, -9999999999999999999999, -1e+22, 1.23456788, 0.6227470969848448, 1.23456789, -1e+100, -3, -0.5, 3, -1.23456789, -5, -inf, -5, -3, -9999999999999999999999, 0.4, 9999999999999999999999998, 0.4, 10000000000000000000000, -0.07506072001847719, 3, -0.9016404675969094, -0.7328249760252548, 0.33863302089208697, 1e+100, 0.5170315488171091, inf, -inf, -4, 0.9844734927681069, 9.775453772147561e+99, -5, -7, -0.30387334753977924, -0.5, 1.0499093088834509e-30, -0.30387334753977924, -0.07506072001847719, -10000000000000000000000, -999, 0.5502904923114273, -0.8219041516621808, -0.7328249760252548, -1e-30, 1e-30, -1, -999, -0.4399369615846679, -0.47412425472639685, -1.23456789, -9999999999999999999999, -1, -1.2456261076289474, 1.137575447277081e+100, -0.3079438825335931, -6.7523459788417035e-31, -0.10974338446002693]

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
        func_name = "minimum"
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
        for test_case in ['assert minimum(1,2) == 1', 'assert minimum(-5,-4) == -5', 'assert minimum(0,0) == 0']:
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