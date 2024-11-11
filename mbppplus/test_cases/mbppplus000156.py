import numpy as np
['import math']

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
inputs = [[1], [2], [3], [4], [5], [6], [10], [15], [20], [50], [100], [75], [200], [150], [1000], [1000000], [151], [1000001], [101], [102], [True], [51], [14], [9], [1001], [49], [13], [999], [21], [199], [22], [201], [999999], [24], [53], [1002], [999998], [52], [74], [16], [202], [17], [1000002], [18], [1000003], [203], [103], [998], [25], [23], [1004], [999997], [8], [19], [68], [198], [67], [197], [48], [204], [152], [1003], [11], [997], [12], [206], [73], [72], [196], [999996], [195], [205], [1005], [194], [54], [148], [996], [55], [1000004], [56], [66], [26], [76], [999995], [1000005], [149], [96], [71], [7], [207], [95], [64], [57], [58], [995], [63], [208], [97], [69], [153], [104], [94], [154], [90], [77], [994], [91], [79], [27], [1000006], [70], [98], [41], [88]]
results = [2.0, 6.0, 20.0, 70.0, 252.0, 924.0, 184756.0, 155117520.0, 137846528820.0, 1.0089134454556417e+29, 9.054851465610324e+58, 9.282606973670874e+43, 1.0295250013541446e+119, 9.37597027728274e+88, inf, inf, 3.737969607234577e+89, inf, 3.604010187302328e+59, 1.4345373882791625e+60, 2.0, 3.996088548667444e+29, 40116600.0, 48620.0, inf, 2.547761225898085e+28, 10400600.0, inf, 538257874440.0, 2.580263161288582e+118, 2104098963720.0, 4.107855975552358e+119, inf, 32247603683100.0, 6.272525058612252e+30, inf, inf, 1.5830658481259492e+30, 2.3362265873332747e+43, 601080390.0, 1.639075206086732e+120, 2333606220.0, inf, 9075135300.0, inf, 6.540152300149035e+120, 5.7102944581986025e+60, inf, 126410606437752.0, 8233430727600.0, inf, inf, 12870.0, 35345263800.0, 5.949105755928255e+39, 6.466906411793807e+117, 1.4982933014930424e+39, 1.620819581690092e+117, 6.4350670138663e+27, 2.6096490060398536e+121, 1.4902694618316825e+90, inf, 705432.0, inf, 2704156.0, 4.155144572733066e+122, 5.880298213015719e+42, 1.4802129984487867e+42, 4.0623595113606645e+116, inf, 1.0181872944075321e+116, 1.0413136033856605e+122, inf, 2.5520118561628384e+115, 2.485778449153744e+31, 5.899376589114938e+87, inf, 9.852721853009381e+31, inf, 3.905900448871579e+32, 3.773896661655409e+38, 495918532948104.0, 3.688614876379741e+44, inf, inf, 2.351832009351858e+88, 3.6097999082737723e+56, 3.726410345745197e+41, 3432.0, 1.658043196655807e+123, 9.07174846058331e+55, 2.39511460419281e+37, 1.5486552656929425e+33, 6.141219157058214e+33, inf, 6.034934435761404e+36, 6.616230063578461e+123, 1.4364770769006983e+57, 2.3623985175715127e+40, 5.941597200766839e+90, 2.273136447782905e+61, 2.2799367824217297e+55, 2.368922520305735e+91, 9.101224867283228e+52, 1.465865132691172e+45, inf, 3.6204872548972856e+53, 2.3156006494021205e+46, 1946939425648112.0, inf, 9.38209696978401e+40, 5.716592448890536e+57, 4.247845808487917e+23, 5.7523601921329e+51]

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
        func_name = "count_binary_seq"
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
        for test_case in ['assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)', 'assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)', 'assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)']:
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
