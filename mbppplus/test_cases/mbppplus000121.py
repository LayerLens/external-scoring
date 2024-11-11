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
inputs = [[10, 20], [15, 17], [100, 200], [-5, -10], [-100, -200], [-7, -3], [3.14, 2.718], [1.0, -0.5], [-100.5, 200.75], [5, 5], [-10, -10], [1.23, 1.23], [2.718, -0.5], [3.5839953593217544, 2.718], [5, -10], [-5, -11], [-8, -9], [-8, -10], [-8, -8], [1.0, 200.75], [200.75, 200.75], [-5, -8], [-100, -100], [200.0168272694265, 200.75], [6, -9], [1.7816735844630143, -0.5], [-5, -9], [-100.5, 1.7816735844630143], [1.110891875212232, 200.0168272694265], [-4, -11], [-5, -4], [-5, -5], [-102, -10], [0.9096439911291, 200.75], [-0.5, 200.75], [-8, -5], [-101, -100], [6, -11], [-9, -9], [-11, -11], [-4, -4], [-7, -10], [-11, -100], [-100.5, -0.6246510737114712], [1.110891875212232, 199.9586278490392], [199.80254729935734, 200.75], [200.0168272694265, 200.0168272694265], [-10, -200], [1.110891875212232, -100.5], [-4, -10], [-4, -12], [-0.34485327561456525, -0.5], [-4, -100], [-10, -12], [5, -3], [-7, -4], [-8, -7], [2.490084004197559, 1.7816735844630143], [201.10785660080364, 200.75], [-10, -8], [-10, -11], [109.06389054379079, 200.75], [1.110891875212232, 167.10351385707486], [-102, -101], [2.1330119070118485, -100.5], [True, 1.23], [124.61838179160847, 200.75], [-100, -10], [-9, -10], [-12, -10], [3.5839953593217544, -100.5], [2.1330119070118485, 124.14572872953535], [2.718, 200.0168272694265], [-13, -10], [2.1330119070118485, 200.75], [-102, -8], [-5, -13], [3.5839953593217544, 199.80254729935734], [0.9096439911291, 198.1727902022114], [-10, -4], [201.10785660080364, 201.10785660080364], [-13, -12], [-13, -13], [124.61838179160847, -0.24953757954867695], [-12, -12], [-5, 6], [2.22631597518509, 1.7816735844630143], [-9, -8], [-10, -9], [199.80254729935734, 247.7275752312867], [1.430105248193135, 200.75], [2.154236201660944, 2.4273044050861996], [1.7816735844630143, 1.7816735844630143], [-0.6246510737114712, 1.7816735844630143], [False, 266.8266128826292], [4.42809307831693, 2.718], [-7, -12], [124.61838179160847, 2.4273044050861996], [-13, -9], [-12, -11], [-0.6246510737114712, -0.6246510737114712], [-200, -11], [200.68795799999515, 200.75], [266.8266128826292, 266.8266128826292], [-7, -13], [0.4054844111976208, -0.5], [1.7816735844630143, 2.490084004197559], [4, 5], [-5, -101], [-5, -100], [5, -9], [-11, -10]]
results = [(20, 10), (17, 15), (200, 100), (-10, -5), (-200, -100), (-3, -7), (2.718, 3.14), (-0.5, 1.0), (200.75, -100.5), (5, 5), (-10, -10), (1.23, 1.23), (-0.5, 2.718), (2.718, 3.5839953593217544), (-10, 5), (-11, -5), (-9, -8), (-10, -8), (-8, -8), (200.75, 1.0), (200.75, 200.75), (-8, -5), (-100, -100), (200.75, 200.0168272694265), (-9, 6), (-0.5, 1.7816735844630143), (-9, -5), (1.7816735844630143, -100.5), (200.0168272694265, 1.110891875212232), (-11, -4), (-4, -5), (-5, -5), (-10, -102), (200.75, 0.9096439911291), (200.75, -0.5), (-5, -8), (-100, -101), (-11, 6), (-9, -9), (-11, -11), (-4, -4), (-10, -7), (-100, -11), (-0.6246510737114712, -100.5), (199.9586278490392, 1.110891875212232), (200.75, 199.80254729935734), (200.0168272694265, 200.0168272694265), (-200, -10), (-100.5, 1.110891875212232), (-10, -4), (-12, -4), (-0.5, -0.34485327561456525), (-100, -4), (-12, -10), (-3, 5), (-4, -7), (-7, -8), (1.7816735844630143, 2.490084004197559), (200.75, 201.10785660080364), (-8, -10), (-11, -10), (200.75, 109.06389054379079), (167.10351385707486, 1.110891875212232), (-101, -102), (-100.5, 2.1330119070118485), (1.23, True), (200.75, 124.61838179160847), (-10, -100), (-10, -9), (-10, -12), (-100.5, 3.5839953593217544), (124.14572872953535, 2.1330119070118485), (200.0168272694265, 2.718), (-10, -13), (200.75, 2.1330119070118485), (-8, -102), (-13, -5), (199.80254729935734, 3.5839953593217544), (198.1727902022114, 0.9096439911291), (-4, -10), (201.10785660080364, 201.10785660080364), (-12, -13), (-13, -13), (-0.24953757954867695, 124.61838179160847), (-12, -12), (6, -5), (1.7816735844630143, 2.22631597518509), (-8, -9), (-9, -10), (247.7275752312867, 199.80254729935734), (200.75, 1.430105248193135), (2.4273044050861996, 2.154236201660944), (1.7816735844630143, 1.7816735844630143), (1.7816735844630143, -0.6246510737114712), (266.8266128826292, False), (2.718, 4.42809307831693), (-12, -7), (2.4273044050861996, 124.61838179160847), (-9, -13), (-11, -12), (-0.6246510737114712, -0.6246510737114712), (-11, -200), (200.75, 200.68795799999515), (266.8266128826292, 266.8266128826292), (-13, -7), (-0.5, 0.4054844111976208), (2.490084004197559, 1.7816735844630143), (5, 4), (-101, -5), (-100, -5), (-9, 5), (-10, -11)]

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
        func_name = "swap_numbers"
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
        for test_case in ['assert swap_numbers(10,20)==(20,10)', 'assert swap_numbers(15,17)==(17,15)', 'assert swap_numbers(100,200)==(200,100)']:
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