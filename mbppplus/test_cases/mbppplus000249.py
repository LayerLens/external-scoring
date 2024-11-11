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
inputs = [[4], [21], [30], [0], [100], [1000], [2.5], [3.8], [23.074387180674933], [1002], [3.6549340293875163], [1], [1001], [1004], [1005], [2.7450543076525977], [2.984088088976573], [False], [1.5869584267664152], [4.4891610250151395], [3.089056366033627], [5.3027554376354065], [4.028700461024416], [3.3725660528964188], [2.659818066786769], [101], [3.9892249182433384], [43.22021574103846], [1003], [3.4810848948595883], [3.1692815338650804], [1.0650899101182285], [4.8986268408429705], [3.69259942495845], [4.010566044386772], [2.46052609812118], [4.3768561489787015], [3.6713224100924298], [6.935501596893169], [True], [5.576255197840953], [3.1502544356560356], [2], [4.300091801377514], [52], [3.9155933853489917], [1.2988016591670484], [3.1345443196257796], [4.702845843512329], [5.7904698753969095], [5.08429332701897], [2.70011255752315], [4.2559869433188195], [102], [3.406797610867242], [99], [4.435038737799036], [1.4008586626684183], [4.651659050694365], [53.1496871886536], [0.8498008825679926], [4.236748701784517], [3.0176093048380817], [5.133463974586371], [3.393657330126743], [4.344750174563699], [4.837864419812973], [2.6908650361350013], [5.772166921072477], [0.5074731900068552], [69.33184166028241], [3.3762535480187235], [7.243263284188997], [4.974431164462356], [5.469285749841541], [1.5343753447253605], [2.5781387688594126], [3.918207627535553], [0.9205123885721357], [103.48263235407262], [69.56546331692546], [52.786214360228406], [1.1082663739985814], [1.5553181988910334], [3.6259722043628435], [1.512932111354384], [5.427953835612454], [5.301127862149642], [3.101495225095455], [5.053328029880188], [2.827561476523175], [69.55434074938697], [999], [0.3200065092069435], [6.517544303154645], [5.969669418741442], [6.995408755091795], [3.779793140475027], [39.76359690298631], [4.837924418596985], [53.87971805413539], [6.222949720825474], [2.1433527265004884], [2.7823798633471695], [3.315018436042766], [4.0729861275073915], [1.9387560331276734], [2.5216632117725064]]
results = [4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1.5869584267664152, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0650899101182285, 0, 0, 0, 0, 0, 0, 0, True, 0, 0, 2, 0, 0, 0, 1.2988016591670484, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4008586626684183, 0, 0, 0.8498008825679926, 0, 0, 0, 0, 0, 0, 0, 0, 0.5074731900068552, 0, 0, 0, 0, 0, 1.5343753447253605, 0, 0, 0.9205123885721357, 0, 0, 0, 1.1082663739985814, 1.5553181988910334, 0, 1.512932111354384, 0, 0, 0, 0, 0, 0, 0, 0.3200065092069435, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.9387560331276734, 0]

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
        func_name = "last_Digit_Factorial"
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
        for test_case in ['assert last_Digit_Factorial(4) == 4', 'assert last_Digit_Factorial(21) == 0', 'assert last_Digit_Factorial(30) == 0']:
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
