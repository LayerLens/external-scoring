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
inputs = [[{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 180], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 190], [{}, 0], [{}, -5], [{}, -10], [{}, 10], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10}, 10], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 200], [{}, 8], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grorangeape': -10}, 10], [{}, -1], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, 10], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 201], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180, 'Pierre': 12}, 10], [{'-1': 12, '201': -11, '-58': -5, '10': -94}, 165], [{'Cantrell': 10, 'Gentry': -31, 'apple': 44, 'Nw': -33, 'IhVdpFDGMV': 200, 'abM': 20, 'JDnQ': -11}, -5], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, -11], [{'-1': 12, '201': -11, '-58': -5}, 165], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}, 200], [{'-1': 12, '201': -11, '-58': -5}, 164], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grorangeape': -10}, -10], [{'-1': 12, '-58': -5, '10': -94}, 165], [{}, 180], [{'-72': -33}, 0], [{'-1': 12, '201': -11, '-58': -5}, -33], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, 166], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}, 199], [{'75.87572329200214': False, '79.71274224615752': False}, 8], [{'-1': 12, '10': -94}, 165], [{'175': False, '-57': True, '-32': True, '5': False}, 8], [{'-1': 12, '-58': 199, '10': -94}, 190], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}, 165], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, -1], [{'Alden Cantrell': False, 'Vega': False, 'Cierra Vega': True, 'x': True, 'abM': True}, 11], [{'-1': 12, '201': -11, '-58': -31}, 8], [{'-1': 12, '201': -11, '-58': -5, '10': -94}, True], [{'15': False}, 8], [{'-72': -34}, 20], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, -12], [{'Alden Cantrell': False, 'Vega': False, 'Cierra Vega': True, 'x': True, 'abM': True}, 201], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, 167], [{'Alden Cantrell': False, 'Vega': False, 'Cierra Vega': True, 'x': True, 'abM': True}, -11], [{'Cierra Vega': 176, 'Alden Cantrell': 180, 'Pierre Cox': 190}, 165], [{}, 9], [{'-1': 12, '-58': -5, '10': -94}, -58], [{'-1': 12, '201': -11, '-58': -5, '10': -94, '-57': -93, '0': -1}, True], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, 0], [{'apple': 5, 'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180, 'Pierre': 12, 'kikwi': 6}, 10], [{'-58': -5}, 165], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190, 'Alden Cantrel': -57}, 200], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 11}, 10], [{'-1': 12, '-58': 199, '10': -94, '166': -93}, 190], [{'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 176, 'ore': 11}, 10], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'Cantrel': True}, 10], [{'Alden Cantrell': 180, 'Pierre Cox': 190}, 199], [{'-1': 12, '201': -11, '-58': -5}, 8], [{'Alden Cantrell': 180, 'Pierre Cox': 190}, 165], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, 20], [{'75.87572329200214': False, '79.71274224615752': False}, 9], [{'-1': 12, '201': -11, '-58': -31, '200': 12}, 9], [{'-1': 12, '-58': 199, '10': -94, '166': -93}, 189], [{'Alden Cantrell': False, 'Vega': False, 'Cierra Vega': True, 'abM': True}, -11], [{'15': False}, 15], [{'-1': 12, '-58': -5, '10': -94}, 44], [{'-1': 12, '10': -94, '0': -93}, 167], [{'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, -12], [{'-1': 12, '-58': -5, '10': -94, '0': -92, '-2': -32}, 166], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'Cantrel': True}, 167], [{'Pierre Cox': 190}, 198], [{'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 176, 'ore': 11, 'kiwigrape': 20}, 10], [{'-1': 12, '10': -94}, 164], [{'-1': 12, '201': -11, '-58': -5, '10': -94, '-57': -93, '0': -1}, False], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 166, 'watermelon': 20, 'kiwi': 10, 'grorangeape': -10}, 10], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, 199], [{}, 165], [{'175': False, '-57': True, '-32': True, '5': False}, -94], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, -93], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 11}, 167], [{'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, 9], [{'Cantrell': 10, 'Gentry': -31, 'apple': 44, 'Nw': -33, 'IhVdpFDGMV': 200, 'abM': 20, 'JDnQ': -93}, -5], [{'75.87572329200214': True, '79.71274224615752': True}, 180], [{'-58': 199, '10': -94}, 190], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 11, 'appKierrae': 5}, 167], [{'-1': 12, '10': -94, '0': -93}, -93], [{'Pierre Cox': 190}, 166], [{'-1': 12, '-58': -5, '10': -94, '190': -93}, 165], [{'-1': 12, '10': -94, '0': -93, '176': -34}, -93], [{'Alden Cantrell': False, 'Cierra Vega': True, 'x': True, 'abM': True}, 44], [{'-1': 12, '10': -94, '-2': -32}, 166], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, 11], [{'-72': -34}, -33], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180, 'Pierre': 12, 'oraCantrelnge': 44}, 10], [{'-1': 12, '-58': -5, '10': -94, '-57': -93, '0': -1}, True], [{'-1': 12, '201': -11, '-58': -5}, 5], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, -94], [{'-1': 12, '-58': -5, '10': -94, '0': -93}, -95], [{'-72': -33}, 1], [{}, 19], [{'75.87572329200214': False, '79.71274224615752': False, '95.84649191478275': False}, 9], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, 175], [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190, 'Alden Cantrel': -57, 'Alden CantreAldenl': -12}, 200], [{'-1': 12, '10': -94}, 180], [{'-58': 199, '10': -94, '166': -93, '176': 200}, 190], [{'-72': -34, '-73': 165}, 20], [{'75.87572329200214': True, '79.71274224615752': True}, 5], [{'-1': 12, '-58': 199, '10': -94, '-73': -94}, 190], [{'-1': 12, '-58': 199, '10': -94, '166': -93}, 191], [{'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 11, 'appKierrae': 5}, 166]]
results = [{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}, {'Alden Cantrell': 180, 'Pierre Cox': 190}, {'Pierre Cox': 190}, {}, {}, {}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10}, {}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180, 'Pierre': 12}, {}, {'Cantrell': 10, 'apple': 44, 'IhVdpFDGMV': 200, 'abM': 20}, {'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, {}, {}, {}, {'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grorangeape': -10}, {}, {}, {}, {'-1': 12, '201': -11, '-58': -5}, {}, {}, {}, {}, {}, {'-58': 199}, {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}, {'-1': 12}, {}, {'-1': 12}, {'-1': 12}, {}, {}, {'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, {}, {}, {'Alden Cantrell': False, 'Vega': False, 'Cierra Vega': True, 'x': True, 'abM': True}, {'Cierra Vega': 176, 'Alden Cantrell': 180, 'Pierre Cox': 190}, {}, {'-1': 12, '-58': -5}, {'-1': 12}, {'-1': 12}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180, 'Pierre': 12}, {}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 11}, {'-58': 199}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 176, 'ore': 11}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10}, {}, {'-1': 12}, {'Alden Cantrell': 180, 'Pierre Cox': 190}, {}, {}, {'-1': 12, '200': 12}, {'-58': 199}, {'Alden Cantrell': False, 'Vega': False, 'Cierra Vega': True, 'abM': True}, {}, {}, {}, {'banana': 12, 'orange': 8, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, {}, {}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'wamtermelon': 176, 'ore': 11, 'kiwigrape': 20}, {}, {'-1': 12}, {'banana': 12, 'grape': 166, 'watermelon': 20, 'kiwi': 10}, {}, {}, {'175': False, '-57': True, '-32': True, '5': False}, {'-1': 12, '-58': -5, '0': -93}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180}, {'Cantrell': 10, 'apple': 44, 'IhVdpFDGMV': 200, 'abM': 20}, {}, {'-58': 199}, {}, {'-1': 12, '0': -93}, {'Pierre Cox': 190}, {}, {'-1': 12, '0': -93, '176': -34}, {}, {}, {'-1': 12}, {}, {'banana': 12, 'grape': 15, 'watermelon': 20, 'kiwi': 10, 'grrape': 180, 'Pierre': 12, 'oraCantrelnge': 44}, {'-1': 12}, {'-1': 12}, {'-1': 12, '-58': -5, '10': -94, '0': -93}, {'-1': 12, '-58': -5, '10': -94, '0': -93}, {}, {}, {}, {'grrape': 180}, {}, {}, {'-58': 199, '176': 200}, {'-73': 165}, {}, {'-58': 199}, {'-58': 199}, {}]

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
        func_name = "dict_filter"
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
        for test_case in ["assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}", "assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}", "assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}"]:
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
