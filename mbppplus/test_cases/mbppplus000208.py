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
inputs = [[' Google    Flutter '], [' Google    Dart '], [' iOS    Swift '], [''], ['1234567890'], ['\n\t'], [' \t\n\n\t'], ['iOS\u180e\u200b\u200c\u200d\u2060Swift'], ['This    is    a    long    string    with    multiple    spaces'], ['Google\u200bDart'], [' \u180e\u200b\u200c\u200d\u2060 '], ['  1234567890  '], [' \u180e\u200b\u200c\u200d\u2060  '], ['  12384567890  '], ['This    is    a    long    string    with    mltiple    spaces'], ['1234567\n\t890'], ['1234567'], [' \u180e\u200b '], ['is'], ['   12384567890  \u180e\u200b '], [' \u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060 '], ['string'], ['   12384567890  \u180e\u200b multiple'], ['multipl'], [' \u180e\u200b\u200c\u200d '], ['spacses'], ['iss'], [' \u180e\u200b1234567\n\t890\u200c\u200d '], ['aspacses'], ['31234567890'], [' \u180e\u200biOS\u180e\u200bO\u200c\u200d\u20601234567890Swift\u200c\u200d\u2060 '], [' \u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012string34567890Swif9t\u200c\u200d\u2060 '], ['iOS\u180e\u200b\u200c\u200d\u2060Stwift'], ['Googgle\u200bD\u180e\u200biOS\u180e\u200bO\u200c\u200d\u20601234567890Swift\u200c\u200d\u2060art'], ['hGMmu'], [' \u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060\u2060 '], ['stri'], ['aspacsesis'], [' \u180e\u200biOS\u180e\u200bO\u200c\u200d\u20601234567890Swift0\u200c\u200d\u2060 '], ['multiple'], ['This    is p   a    long    string    with    mltiple    spaces'], ['\u180e\u200b\u200c\u200d\u2060'], ['mullongtipl'], ['\u180e\u200b1234567'], [' \u180e\u200bi890\u200c\u200dOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060 '], ['mupl'], ['12384567890'], ['   12384567890  \u180e\u200b multiple \u180e\u200b '], ['tstring'], ['iis'], [' \u180e\u200b12345\n67\n\t890\u200c\u200d '], ['mutmipl'], ['iOS\u180e12345678 \u180e\u200bi890\u200c\u200dOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060 90\u200b\u200c\u200d\u2060Swift'], ['\u180e\u200d\u200b\u200c\u200d\u2060'], ['long'], ['890\u200c\u200d'], ['lon'], [' \u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012s\u180e\u200b\u200c\u200dtring34567890Swif9t\u200c\u200d\u2060 '], [' This\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060 '], ['This    is    a    long    strin31234567890ltiple    spaces'], [' \u180e\u200b12890\u200c\u200c\u200d '], [' \u180e\u200b123\u200d4567\n\t890\u200c\u200d '], ['  123 '], ['\u180e\u200b\u200c\u200d'], ['\u180e\u200b1\u180e\u200b123\u200d4567234567'], [' \u180e\u200b\u200ciOS\u180e12345678 \u180e\u200bi890\u200c\u200dOS \u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012s\u180e\u200b\u200c\u200dtring34567890Swif9t\u200c\u200d\u2060 \u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060 90\u200b\u200c\u200d\u2060Swift\u200d\u2060  '], ['67'], ['This    is    a    long    strin31234567890ltie    spaces'], ['\u180e\u200bi890\u200c\u200dOS'], [' \u180e\u200b\u200ciOS\u180e12345678 \u180e\u200bi890\u200c\u200dOS \u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012s\u180e\u200b\u200c\u200dtring34567890Swif9t\u200c\u200d\u2060 \u180e\u200b\u200cThis    is p   a    long    string    with    mltiple    spaces\u200d\u2060Swift\u200c\u200d\u2060 90\u200b\u200c\u200d\u2060Swift\u200d\u2060  '], [' \u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060\u2060 \u180e\u200b1\u180e\u200b123\u200d4567234567'], ['iOS\u180e\u200b\u200c\u200d\u2060St'], [' \u180e\u200b12890\u200d\u200c\u200c\u200d '], ['loiisn'], ['This    is    a    long    stri    spaces'], ['spaces\u200d\u2060Swift\u200c\u200d\u2060'], ['This    is    a    long    strinmultipl31234567890ltiple    spaces'], ['h890\u200c\u200dGhMmu'], ['\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swiftmultipl\u200c\u200d\u2060\u2060'], [' \u180e\u200b123\u200d4\n567\n\t890\u200c\u200d '], ['This\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060'], [' \t\n\n'], ['\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swif890\u200c\u200dtmultipl\u200c\u200d\u2060\u2060'], ['   12384567890  \u180e\u200b multipleThis\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060\u180e\u200b '], ['spaces\u200d\u2060Swif\u2060t\u200cf\u200d\u2060'], ['iOS\u180eS\u200b\u200c\u200d\u2060Stwift'], ['This    i123s    a    longiOS\u180e\u200b\u200c\u200d\u2060St    strinmultipl31234567890l tiple    spaces'], ['90\u200b\u200c\u200d\u2060Swift'], ['strin3p1234567890ltiple'], ['  \u180e\u200b12345\n67\n\t890\u200c\u200d This\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060 '], [' \u180e\u200biO0S\u180e\u200bO\u200c\u200d\u206012sString34567890Swif9t\u200c\u200d\u2060 '], ['hGMmuiOS\u180eS\u200b\u200c\u200d\u2060Stwift'], ['  \u180e\u200b \u180e\u200b\u200c\u200d\u2060 \u200c\u200d\u2060 '], ['iOS\u180e\u200b\u200c\u200diOS\u180e\u200b\u200c\u200d\u2060Stwift\u2060Swift'], ['\u180e\u200d\u200b\u200c\u200d\u2060hGMmuiOS\u180eS\u200b\u200c\u200d\u2060Stwift'], ['56'], ['  13 '], ['hwplSpwh'], [' \u180e\u200b\u200c\u200d  '], ['  \u180e\u200b\u200c\u200d '], ['\u180e\u200b\u200cThis'], ['\u180e\u200b123\u200d4'], ['   \u180e\u200b\u200c\u200d\u200b '], ['\u180e\u200d\u200b\u200c\u200d\u2060hGMmuwitht'], ['strin31234567890ltielon'], ['naXeNJpPR'], ['lstrin3167890ltielon'], ['\u180e\u200d\u200b\u200cG\u200d\u2060hGMmuwitht'], ['90\u200b\u200cstringSwift'], ['spacewift\u200c\u200d\u2060'], ['longiOS\u180e\u200b\u200c\u200d\u2060St'], ['spaceswift\u200c\u200d\u2060']]
results = ['GoogleFlutter', 'GoogleDart', 'iOSSwift', '', '1234567890', '\n\t', '\t\n\n\t', 'iOS\u180e\u200b\u200c\u200d\u2060Swift', 'Thisisalongstringwithmultiplespaces', 'Google\u200bDart', '\u180e\u200b\u200c\u200d\u2060', '1234567890', '\u180e\u200b\u200c\u200d\u2060', '12384567890', 'Thisisalongstringwithmltiplespaces', '1234567\n\t890', '1234567', '\u180e\u200b', 'is', '12384567890\u180e\u200b', '\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060', 'string', '12384567890\u180e\u200bmultiple', 'multipl', '\u180e\u200b\u200c\u200d', 'spacses', 'iss', '\u180e\u200b1234567\n\t890\u200c\u200d', 'aspacses', '31234567890', '\u180e\u200biOS\u180e\u200bO\u200c\u200d\u20601234567890Swift\u200c\u200d\u2060', '\u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012string34567890Swif9t\u200c\u200d\u2060', 'iOS\u180e\u200b\u200c\u200d\u2060Stwift', 'Googgle\u200bD\u180e\u200biOS\u180e\u200bO\u200c\u200d\u20601234567890Swift\u200c\u200d\u2060art', 'hGMmu', '\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060\u2060', 'stri', 'aspacsesis', '\u180e\u200biOS\u180e\u200bO\u200c\u200d\u20601234567890Swift0\u200c\u200d\u2060', 'multiple', 'Thisispalongstringwithmltiplespaces', '\u180e\u200b\u200c\u200d\u2060', 'mullongtipl', '\u180e\u200b1234567', '\u180e\u200bi890\u200c\u200dOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060', 'mupl', '12384567890', '12384567890\u180e\u200bmultiple\u180e\u200b', 'tstring', 'iis', '\u180e\u200b12345\n67\n\t890\u200c\u200d', 'mutmipl', 'iOS\u180e12345678\u180e\u200bi890\u200c\u200dOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u206090\u200b\u200c\u200d\u2060Swift', '\u180e\u200d\u200b\u200c\u200d\u2060', 'long', '890\u200c\u200d', 'lon', '\u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012s\u180e\u200b\u200c\u200dtring34567890Swif9t\u200c\u200d\u2060', 'This\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060', 'Thisisalongstrin31234567890ltiplespaces', '\u180e\u200b12890\u200c\u200c\u200d', '\u180e\u200b123\u200d4567\n\t890\u200c\u200d', '123', '\u180e\u200b\u200c\u200d', '\u180e\u200b1\u180e\u200b123\u200d4567234567', '\u180e\u200b\u200ciOS\u180e12345678\u180e\u200bi890\u200c\u200dOS\u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012s\u180e\u200b\u200c\u200dtring34567890Swif9t\u200c\u200d\u2060\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u206090\u200b\u200c\u200d\u2060Swift\u200d\u2060', '67', 'Thisisalongstrin31234567890ltiespaces', '\u180e\u200bi890\u200c\u200dOS', '\u180e\u200b\u200ciOS\u180e12345678\u180e\u200bi890\u200c\u200dOS\u180e\u200biOS\u180e\u200bO\u200c\u200d\u206012s\u180e\u200b\u200c\u200dtring34567890Swif9t\u200c\u200d\u2060\u180e\u200b\u200cThisispalongstringwithmltiplespaces\u200d\u2060Swift\u200c\u200d\u206090\u200b\u200c\u200d\u2060Swift\u200d\u2060', '\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060\u2060\u180e\u200b1\u180e\u200b123\u200d4567234567', 'iOS\u180e\u200b\u200c\u200d\u2060St', '\u180e\u200b12890\u200d\u200c\u200c\u200d', 'loiisn', 'Thisisalongstrispaces', 'spaces\u200d\u2060Swift\u200c\u200d\u2060', 'Thisisalongstrinmultipl31234567890ltiplespaces', 'h890\u200c\u200dGhMmu', '\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swiftmultipl\u200c\u200d\u2060\u2060', '\u180e\u200b123\u200d4\n567\n\t890\u200c\u200d', 'This\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060', '\t\n\n', '\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swif890\u200c\u200dtmultipl\u200c\u200d\u2060\u2060', '12384567890\u180e\u200bmultipleThis\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060\u180e\u200b', 'spaces\u200d\u2060Swif\u2060t\u200cf\u200d\u2060', 'iOS\u180eS\u200b\u200c\u200d\u2060Stwift', 'Thisi123salongiOS\u180e\u200b\u200c\u200d\u2060Ststrinmultipl31234567890ltiplespaces', '90\u200b\u200c\u200d\u2060Swift', 'strin3p1234567890ltiple', '\u180e\u200b12345\n67\n\t890\u200c\u200dThis\u180e\u200biOS\u180e\u200b\u200c\u200d\u2060Swift\u200c\u200d\u2060', '\u180e\u200biO0S\u180e\u200bO\u200c\u200d\u206012sString34567890Swif9t\u200c\u200d\u2060', 'hGMmuiOS\u180eS\u200b\u200c\u200d\u2060Stwift', '\u180e\u200b\u180e\u200b\u200c\u200d\u2060\u200c\u200d\u2060', 'iOS\u180e\u200b\u200c\u200diOS\u180e\u200b\u200c\u200d\u2060Stwift\u2060Swift', '\u180e\u200d\u200b\u200c\u200d\u2060hGMmuiOS\u180eS\u200b\u200c\u200d\u2060Stwift', '56', '13', 'hwplSpwh', '\u180e\u200b\u200c\u200d', '\u180e\u200b\u200c\u200d', '\u180e\u200b\u200cThis', '\u180e\u200b123\u200d4', '\u180e\u200b\u200c\u200d\u200b', '\u180e\u200d\u200b\u200c\u200d\u2060hGMmuwitht', 'strin31234567890ltielon', 'naXeNJpPR', 'lstrin3167890ltielon', '\u180e\u200d\u200b\u200cG\u200d\u2060hGMmuwitht', '90\u200b\u200cstringSwift', 'spacewift\u200c\u200d\u2060', 'longiOS\u180e\u200b\u200c\u200d\u2060St', 'spaceswift\u200c\u200d\u2060']

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
        func_name = "remove_whitespaces"
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
        for test_case in ["assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'", "assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'", "assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'"]:
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
