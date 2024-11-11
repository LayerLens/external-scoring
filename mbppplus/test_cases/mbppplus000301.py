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
inputs = [['pythonzabc.'], ['zxyabc.'], ['  lang  .'], ['zzzxyabczzz'], ['zzzxyabczzz xxzzxxyz zzzz abczyz baaz azzbzz'], [''], ['baaz'], ['zzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzz'], ['zzzz'], ['zzzzzzzxyabczzz'], ['zzzzbaaz'], ['xxzzxxyz'], ['zzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyyz baaz azzbzz'], ['zzzzzzzxyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzz'], ['azzbzzz'], ['baabaazz'], ['yabczyyz'], ['gfzzzzzzzxyabczzzzzxyabczzz'], ['zzzzzabczyz'], ['yz'], ['baabazazz'], ['zzzzzzzxyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczyz baaz azzbzzz'], ['zzzzxzzxyabczyz'], ['zzzxyabczzz xxzzxxyz zzzzczxyabczzzzz abczyz baaz azzbzz'], ['zzzxyabczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzz'], ['zzzxyabczzz xxzzxxyz zzzzzxyabzzzzzzzxzyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzczzzzz abczyz baaz azzbzz'], ['azazzbzzzczzzzzzbzzz'], ['azabzzz'], ['abczyyz'], ['yabczyyzzzxyabczzzz'], ['zzzzzzzxyabczyyzzzxyabczzzzyabczzz'], ['zzzzzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczzzxyabczyyzzzxyabczzzzyabczzz'], ['xxzzxxyzzzzzzxyabczzzzz'], ['yabczyyzzzxyxabczzzz'], ['yabczyyzzxxzzxxyzzxyabczzzz'], ['gfzzzzzzz'], ['yabczyyabczzzz'], ['yabczzxxyzzxyabczz'], ['zzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzz'], ['zzzzazzbzzzczzzzz'], ['azbczyyz'], ['zzzzzzz'], ['zzzzzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczzzxyzabczyyzzzxyabczzzzyabczzz'], ['zzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzz'], ['azzbzzzzzxyabczzz xxzzxxyz zzzzzxyabzzzzzzzxzyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzczzzzz abczyz baaz azzbzzz'], ['yabczzzzczxyabczzzzzzzxyabczzzzyyzzxxzzxxyzzxyabczzzz'], ['zzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczzz abczyz baaz azzbzz'], ['azzbzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczzz'], ['zzzxyabczzz xxzzxxyz zzzz xxzzxxyzzzzzzxyabczzzzzabczyz baaz azzbzz'], ['zzzz zzzxyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzz'], ['yzz'], ['zzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyyz baaxz azzbzz'], ['azzbzzzzzxyabczzz xxzzxxyz zzzzzxyabzzzzzzzxzyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzczzzzz abczyz baaz azzbzzzaabaazz'], ['zzzz zzzxyabczzzzzxyabczzabczzzzz abczyz baaz azzbzzz'], ['zzzxyabczzz xxzzxxyz zzzzczxyzzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzzabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zyzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzz'], ['azzbzzzzzxyabczzz xxzzxxyz zzzzzxyabzazzzzzzxzyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzczzzzz abczyz baaz azzbzzzaabaazz'], ['yabczyyzzzxybxabczzzz'], ['zzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczzz abczyz baaz azzbzz'], ['zzzzazzbzzzczzzzzzzzz'], ['yabczzxxyzzxy'], ['azbczzzzxzzxyabczyzyz'], ['zzzzazzbzbaazzzczzzzz'], ['zzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxzyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzz'], ['zzzxyabczzz xxzzxxyz zzzzczxyazzbzzzzzxyabczzzabczzzzz abczyz baaz azzbzz'], ['azazzbzzzczzzzzzbzzzzzzczxyabczzzzzzzxyabxczzz'], ['zzzzz zzzxyabczzzxyabczzzzzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzz'], ['zzzz zzzxyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzaaz azzbzzz'], ['zzzzzzzzzzzxyabczzzzzxyabczzz zzzxyabczzzzzxyazabzzzabczzz xxzzxxyz zzzzzxyabczzzaaz azzbzzz'], ['azazzbzzzczzzzazzbzzzzzzczxyazzzzzzzxyabczzzzzzzxyabxczzz'], ['gfzzzzzzzzxyabczzz xxzzxxyz zzzzczxyzzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzzabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zyzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzzzz'], ['yabczyyabczzzzxxzzxxyz'], ['yabczzzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzczxyabczzzzzzzxyabczzzzyyzzxxzzxxyzzxyabczzzz'], ['zzzzzzxyabczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz'], ['yabczzxxxyzzxy'], ['zzzzzzzz'], ['zzzxyazzzzzzzzbczzz'], ['zzzzzxyabczzzzz'], ['zzzxyabczzz xxzzxxzzzxyabczzz xxzzxxyz zzzzczxyzzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzzabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zyzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzzxyabczzzzz abczyyz baaxz azzbzz'], ['zzzxyabczzz xxzzxxyz zzzzczzzzzczxyabczzzzzzzxyabczzzxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczzz abczyz baaz azzbzz'], ['azazzbzzzczzzzazzbzzzzzzzzzzzxyabczzzzzxyabczzz zzzxyabczzzzzxyazabzzzabczzz xxzzxxyz zzzzzxyabczzzaaz azzbzzzzzzzzzczxyazzzzzzzxyabczzzzzzzxyabxzzz'], ['zzzzz zzzxyabczzzxyabczzzzzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzz'], ['azzbzzzzzzzzxyabzzzzzzzxzyabczzzzzxyabczyzzzxyabczzzyzzxxzzxxyzzxyabczzzzyabczzz'], ['yabczzzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzczxyabczzzzzzzxyayabczyyzxyzzxyabczzzz'], ['zzzzzzzzzzzzzxyabczzzzz'], ['yyzzz'], ['xxzzzxzxyz'], ['zzzzazzbzzzczzzzzzzz'], ['zzzzazzbzzzxyabczzz xxzzxxyz zzzzczxyabczzzzzzzxyabxczzz xxzzxxyzzzzzzxyabczzzzz zzzzczxyabczzzzz abczyz baaz azzbzzz abczyz baaz azzbzzzzzczzzzzzzzz'], ['azzbzzzzzxyabczzz xxzzxxyz zzzzzxyabzzzzzzzxzyabczzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzzbzzzczzzzz abczyz baaz azzbzzzaabaazz'], ['zzzzzxyabczzzaaz'], ['zzzzazzbzzzxyabczzz'], ['yyzzzzzzazzbzzzczzzzzz'], ['gfzzzzczxyzzzxyabczzzzzzzzzz'], ['azzzzzz zzzxyabczzzxyabczzzzzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzz'], ['azazzbzzzczzzzazzbzzzzzzzczxyazzzzzzzxyabczzzzzzzxyabxczzz'], ['yyzzzzzzzzabczyz'], ['zzzzzz'], ['yyyzzz'], ['zzzzzxyabczyz'], ['zzzzz'], ['azzbzzzaabaazz'], ['azazzbzzzczzzzazzbzzzzzzzzzzzxyabczzzzzxyabczzz'], ['yabczzzzz zzzxyabczzzxyabczzzzzzzzxyabczzz xxzzxxyz zzzzzxyabczzzzz abczyz baaz azzbzzzxy'], ['zzzzzzzzzzxyabczzzaaz'], ['yabyabczyyzzzxyxabczzzzczyyzzzxybxabczzzz'], ['zzzzzxzzxyabczyz']]
results = [True, False, False, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

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
        func_name = "text_match_wordz_middle"
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
        for test_case in ['assert text_match_wordz_middle("pythonzabc.")==True', 'assert text_match_wordz_middle("zxyabc.")==False', 'assert text_match_wordz_middle("  lang  .")==False']:
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
