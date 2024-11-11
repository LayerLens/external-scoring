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
inputs = [[3], [4], [5], [1000000], [543210], [98765432], [999999], [999998], [543211], [543212], [999997], [True], [543213], [543214], [1000001], [999996], [1000002], [1000004], [1000003], [98765433], [543215], [543209], [1000005], [98765434], [67], [98765435], [98765430], [98765431], [77], [76], [75], [78], [999995], [53], [1000006], [74], [73], [52], [98765429], [1000007], [98765428], [999994], [54], [543216], [72], [543208], [543207], [999993], [71], [543217], [68], [50], [66], [55], [543206], [51], [70], [98765427], [543205], [56], [17], [49], [1000008], [543204], [57], [1000009], [98765436], [999992], [24], [1000010], [1000011], [1000012], [16], [59], [58], [23], [1000013], [93], [15], [22], [94], [48], [543218], [14], [98765426], [95], [79], [92], [98765437], [18], [69], [1000014], [46], [543219], [98765425], [91], [45], [25], [98765423], [21], [13], [47], [27], [80], [1000015], [26]]
results = [37, 73, 121, 5999994000001, 1770459365341, 58527662756287153, 5999982000013, 5999970000037, 1770465883861, 1770472402393, 5999958000073, 1, 1770478920937, 1770485439493, 6000006000001, 5999946000121, 6000018000013, 6000042000073, 6000030000037, 58527663941472337, 1770491958061, 1770452846833, 6000054000121, 58527665126657533, 26533, 58527666311842741, 58527660385916821, 58527661571101981, 35113, 34201, 33301, 36037, 5999934000181, 16537, 6000066000181, 32413, 31537, 15913, 58527659200731673, 6000078000253, 58527658015546537, 5999922000253, 17173, 1770498476641, 30673, 1770446328337, 1770439809853, 5999910000337, 29821, 1770504995233, 27337, 14701, 25741, 17821, 1770433291381, 15301, 28981, 58527656830361413, 1770426772921, 18481, 1633, 14113, 6000090000337, 1770420254473, 19153, 6000102000433, 58527667497027961, 5999898000433, 3313, 6000114000541, 6000126000661, 6000138000793, 1441, 20533, 19837, 3037, 6000150000937, 51337, 1261, 2773, 52453, 13537, 1770511513837, 1093, 58527655645176301, 53581, 36973, 50233, 58527668682213193, 1837, 28153, 6000162001093, 12421, 1770518032453, 58527654459991201, 49141, 11881, 3601, 58527652089621037, 2521, 937, 12973, 4213, 37921, 6000174001261, 3901]

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
        func_name = "find_star_num"
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
        for test_case in ['assert find_star_num(3) == 37', 'assert find_star_num(4) == 73', 'assert find_star_num(5) == 121']:
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
