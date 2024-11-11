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
inputs = [[[1, 2, 4, 5], 6], [[1, 2, 4, 5], 3], [[1, 2, 4, 5], 7], [[], 1], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 15], [[5], 5], [[], 5], [[], [24]], [[], 16], [[], 4], [[], []], [[], 24], [[], 26], [[], [24, 16, 15, -86, 25, 18, -63, 1, 5, 4]], [[], [30, 24]], [[], 30], [[], [False, False, True, True, True, False, True, False]], [[14], 14], [[], ['rfvEP', 'kSSJBNc', 'Ck', 'MlFV', 'NCpr']], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 0], [[], 22], [[], -86], [[], [3, 24, 16, 15, -86, 25, 18, -63, 1, 5, 4]], [[False, True, True], 26], [[], ['MlFV', 'IwZvTRzpU']], [[], [3, 24, 16, 15, -86, 25, 18, -63, 1, 5, 4, 16]], [[14, 14], 2], [[], [30, 25, 24]], [[], [-53.40737393286277]], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 19, 20, 22, 22, 26, 28, 30], 0], [[], 31], [[], 2], [[], [24, 16, 15, -86, 24, 18, -63, 1, 5, 4]], [[], [24, 24]], [[], 19], [[5, 5], 10], [[], 6], [[], [24, 16, 15, -86, 25, 18, -63, 22, 1, 5, 4, -86, 18]], [[], ['MlFV', 'IwZvTRkSSJBNczpU']], [[], 18], [[], [6, -56, 10, 15, 0]], [[0, 1, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 15], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu']], [[14, 14, 14], 3], [[5, 5], 3], [[5, 5], 24], [[], [6, -56, 10, 15, 0, 0]], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 14], [[], [30, 24, 30]], [[], 25], [[], [False, False, False, False, True, False, True, False]], [[], [True, False, True, True, True, False, True, False, False, True]], [[5, 5], 19], [[14], 2], [[], [30, 25, 25]], [[], [False, True, True]], [[5, 5], 22], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu', 'xu']], [[14], 1], [[14], 24], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23, 26, 28, 30], 1], [[], [False, True, False, True, True, True, False, True, False, False, True]], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu', 30]], [[], -85], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu', 30, 30]], [[], [30, 25, 26, 25]], [[], [False, False, True, True, False, True, False, True, False]], [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 26, 28, 30], 0], [[], 0], [[True, True], 25], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu', 10]], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu', 'xu', 10]], [[5, 5], 9], [[], -87], [[True, True, True], 26], [[], [{'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'xu']], [[], [70.96164714216567, -53.40737393286277]], [[4, 5], 9], [[5], 10], [[False, True, True, True, True], 11], [[3, 5, 5], 3], [[], ['hEMq', 'rfvEP', 'kSSJBNc', 'rfvEP', -16.540016490531514, -70.3664297248564, True, False, False, False]], [[5, 5], 11], [[9], 10], [[], 3], [[14, 14], 3], [[], [1, -63, 62, -85]], [[5, 5], 18], [[], [-84, {'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, 10, -16.540016490531514, 30, 'M', 'xu', 10]], [[True], 25], [[], [10, -16.540016490531514, 30, 'xu']], [[5, 5, 5], 10], [[], [{'Ck': 'MlFV', 'IwZvTRkSSJBNczpU': 'DlrME', 'rfvEP': 'M', 'xjY': 'IwZvTRzpU', 'GVfLSKzrND': 'IwZvTRkSSJBNczpU', 'MlFV': 'WghKoONC', '': ''}, -16.540016490531514, 30, 'xu']], [[], [10]], [[False, True, True, True, True], 12], [[5, 5, 5], 8], [[], [20, 24, 16, 15, -86, 25, 18, -63, 22, 1, 5, 4, -86, 18, 24]], [[5], 18], [[14, 14], 14], [[14, 14], 4], [[14], 31], [[], [True, True]], [[5, 5, 5, 5], 8], [[11, 22], 24], [[], 11], [[14, 14], 5], [[5], -84]]
results = [4, 2, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 8, 0, 0, 0, 2, 0, 7, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 3, 0, 0, 2, 1, 5, 0, 0, 2, 1, 0, 0, 0, 2, 0, 1, 0, 3, 0, 0, 5, 3, 0, 1, 0, 0, 1, 0, 4, 2, 0, 0, 0]

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
        func_name = "left_insertion"
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
        for test_case in ['assert left_insertion([1,2,4,5],6)==4', 'assert left_insertion([1,2,4,5],3)==2', 'assert left_insertion([1,2,4,5],7)==4']:
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
