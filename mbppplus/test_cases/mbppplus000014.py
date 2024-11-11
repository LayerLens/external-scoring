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
inputs = [[383], [254], [200], [123456789], [123456788], [123456790], [-71], [-43.858003490436445], [-29.61114685387961], [123456791], [True], [-26.959954047393943], [-36.19806730921029], [False], [123456792], [123456793], [-29.871125367901588], [-29.522652685174876], [-28.83173048562741], [-36.46340914477242], [-21.3952610510801], [-54.31098212859848], [-29.97825041127243], [-69.13149487461008], [-69.25331473635698], [-30.672425597981977], [-70], [-31.492472971818966], [-23.37512371019188], [-26.87584184061303], [-68.8018442158572], [-72], [-68.9582596167829], [-38.639304621786174], [-36.762574512172826], [-29.71114112102485], [-29.147181618179903], [-45.96312293984687], [-62.29011681998471], [-102.18510964864885], [-37.926042220673814], [-21.669838537346024], [-58.62219921432578], [-49.3200214561046], [-20.415110882873073], [-70.16424320159742], [-40.25945493003661], [-70.28083008878951], [-29.42426596564329], [-36.42835541123631], [-68.24706572951847], [-69.41855382525948], [-14.166058474029754], [-62.72457764448362], [-67.51407654646718], [-43.87699809663642], [-20.51986489168823], [-15.085356836638901], [-67.0567942382996], [-19.580182972529585], [-39.15390942077779], [-35.784031914737916], [-60.94797432645206], [-30.593131467080347], [-28.30344245006401], [-29.774227963592523], [88.42189273276318], [123456794], [-31.744787544004495], [-68.40811941759871], [-56.99871844685891], [92.98004923674453], [-29.38824771469962], [-28.112821077251972], [-59.66653455441657], [-28.408958976827417], [-34.246016042728264], [-37.459933039490544], [-69.08278583390873], [-31.39943780262713], [-27.08300242071865], [-32.23443641065063], [-16.35377974137643], [-34.49166282951802], [-80.04075575777426], [-15.990708397802807], [-37.17075988866512], [-12.266024087946377], [-42.995821326318705], [-36.571652101601906], [-36.40347054615233], [-70.43269469508628], [-28.726570985744708], [-14.941982364755784], [-26.521563448513206], [-52.0451679843239], [-41.16822642698813], [-27.427877745731756], [93.65722410276985], [-61.5774096007493], [-32.14674769877757], [-21.464380924877055], [-67.55449156821463], [91.99125730826226]]
results = [True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "is_woodall"
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
        for test_case in ['assert is_woodall(383) == True', 'assert is_woodall(254) == False', 'assert is_woodall(200) == False']:
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
