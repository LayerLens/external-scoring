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
inputs = [['annie'], ['dawood'], ['Else'], ['H3llo'], ['_Eelse'], ['Anna18'], ['__Danielle'], ['_aBbbb'], ['!Uuiouy'], ['1Abb'], ['1Abb_Eelse'], ['H3ll__lDanielle'], ['_BaBbbb'], ['Ann_aBbbba18'], ['H3!Uuiouylo'], ['b_BaBbbb'], ['!1Abb_Eelseouy'], ['1AbH3!Uuiouyloelse'], ['An_aBbbba18'], ['An_aBbbba1Anna188'], ['1AbH3!Uuiou__Danielleyloelse'], ['_Eels'], ['H3!Uylo'], ['13AbH3!Uuiouyloelse'], ['1AbH3!Uuio13AbH3An_aBbbba1Anna188Uuiouyloelseu__Danielleyloelse'], ['1Ab'], ['!1Abb_E__Danielleelseouy'], ['13AbH3!UuiouyAnn_aBbbba18loelse'], ['H3!yUylo'], ['AnAnna18n_aBbbba18'], ['AAn_aBbbba18'], ['!1Abb_E__DanielleelAnA!1Abb_E__Danielleelseouynna18n_aBbbba18seou1ABbH3!Uuiouyloaelsey'], ['1AbH3!Uuiou__Danielleeyloelse'], ['!UuH3ll__lDanielleiouy'], ['Anna1n8'], ['1AbAnAnna18n_aBbbba18'], ['!1Abb_E__DanielleelAnA!1Abb_E__Daniellleelseouynna18n_aBbbba18seou1ABbH3!Uuiouyloaelsey'], ['13AbH3!UuiouyAnn_aBbbba18lo3else'], ['!AAn_aBbbba181Abb_Eels_eouy'], ['H3ll__lDaniell'], ['!AAn_aBbbba181_EelsAy'], ['H3!ylo'], ['1AbH3!Uuio13AbH1AbH3!Uuiou__Danielleyloelse3An_aBb_aBbbblseu__Danielleyloelse'], ['!Uy'], ['1AbAnAnna18n_aH3ll__lDanielleBbbba18'], ['A1AbAnAnna18n_aH3ll!1Abb_E__DanielleelAnA!1Abb_E__Danielleelseouynna18n_aBbbba18seou1ABbH3!UuiouyloaelseynielleBbbba18'], ['13AbH3!3Uuiouyloelse'], ['1AbH3!Uuio13AbH3An_aBbbba1Anna188Uuiouyloelseu__Danielleyloele'], ['An_aB'], ['__DanDielle'], ['1AbH3!Uuio11AbH3!Uuio13AbH3An_aBbbba1Anna188Uuiouyloelseu__Danielleyloele3AbH3An_aBbbba1Anna188Uuiouyloelseu__Danielleyloelse'], ['1AbAnAnna18n_aH3ll__lDanielleBbbba181Ab'], ['A1AbAnAnna18n_aH3ll!1Abb_E__DanielleeH3ll__lDanielllAnA!1Abb_E__Danielleelseouynna18n_aBbbba18seou1ABbH3!UuiouyloaelseynielleBbbba18'], ['H3!yl!o'], ['__DanDiel13AbHi3!UuiouyAnn_aBbbba18loelsele'], ['Annan1n8'], ['1AbAnAnnaa18n_aBbb1AbH3!Uuiouyloelseba18'], ['!1Abb_E__DanielleelseoEuy'], ['!1Abb_E__DanielleelAnA!1Abb_E__Daniellleelseouynna18n_aBbb1AbAnAnna18n_aH3ll__lDanielleBbbba181Abba18seou1ABbH3!Uuiouyloaelsey'], ['y'], ['An_aaBbbbaA1Anna188'], ['Aan_aB'], ['H3llH3!yl!oo'], ['!1Abb_Eelseou1Ab'], ['13AbH3!Uuioulyloelse'], ['H3!yo'], ['H3!yylo'], ['1AbH3!Uuiou__Danielleeyloe!AAn_aBbbba181Abb_Eels_eouy'], ['1AbAnAnnaa18nb_aBbb1AbH3!Uuiouyloelseba18'], ['13AbH3!U_uiouyAnn_aBbbba18loelH3!yUylose'], ['!1Abb_1AbH3!Uuiou__Danielleeyloe!AAn_aBbbba181Abb_Eels_eouyEelseouy'], ['1AbAnAnnaa18n_aBbb1AbH3!Uuiouyloelseba18Annan1n8'], ['fXdDfqe'], ['H3!yllo'], ['1AbH3!Uuio13AbH3An_aBbbba1Anna188Uuiouylboelseu__Danielleyloele'], ['H!Uy3!Uylo'], ['13AbH3!Uuiouyloelsee'], ['1AbAnAnna18n_aH3ll__lDanielleBbbba181__DanDielleAb'], ['!U!uH3ll__lDanielleiouy'], ['1Abb_EelseAan_aB'], ['13AbH3!Uuiou1AbH3!Uuiou__Danielleeyloelseyloelse'], ['AnnH3!yl!oa1n8'], ['An_aaBbbbaA1Ann8'], ['1AbAnAnnaa18nb_aBb1AbH3!Uuiouyloelseb1AbH3!Uuiouyloelseba18'], ['An_aaBbbbaA1Anna18'], ['!AAn_aBbbba181Abb_Eel1AbH3!Uuiou__Danielleyloelses_eouy'], ['!UuH3!Uyloiouy'], ['Ann_aBbbbba18'], ['PQYQGaD'], ['!1Abb_1AbH3!Uuiou__Danielleeyloe!AAn_aBbbba181Abb_Eels_e'], ['1AbAnAnna18n_aH3ll_l_lDanielleBbbba18'], ['!1Abb_1AbH3!Uuiou__Danielleeyloe!AAn_aBbbba181AAbb_Eels_e'], ['1AbH3!Uuio131AbH3!Uuiou__DanielleeyloelseAbH3An_aBbb1AbAnAnnaa18nb_aBbb1AbH3!Uuiouyloelseba18ba1Anna188Uuiouylboelseu__Danielleyloele'], ['_'], ['1AbH3!UuiHo13AbH3An_aBbbba1Anna188Uuiouyloelseu__Danielleyloelse'], [''], ['!1Abb_1A'], ['1AbH3!Uuio13AbH3An_aBbbba1Anna188aUuiouyelboelseu__DanielleyloelAn_aaBbbbaA1Ann8e'], ['__DaAnn_aBbbba18nielle'], ['1AbH3!Uu_io13AbH3An_aBbbba1Anna188Uuiouylboelseu__Danielleyloele'], ['1AbH3!Uuio131AbH3!Uuiou__DanielleeyloelseAbH3An_aBbb1AbAnAnnaa18nb_aBbb1AbH3!Uuiouyloelseba18ba1Anna188Unielleyloe1AbH3!Uuiou__Danielleyloelsee'], ['H3!Uuioouo'], ['Ann_AaBbbbba18'], ['H!Uy3!Uyloo'], ['__DaAnn_aB1AbAnAnna18n_aH3ll__lDanielleBbbba181Abbbba18nielle'], ['oH3lHlo'], ['A1AbAnAnna18n_aH3ll_l_lDanielleBbbba18nn_aBbbba18'], ['!AAn_aBbbba181Abb_Eels_eouey'], ['!U!uH3ll__lDanielle1Abb_EelseAan_aBiouy'], ['_Ba!AAn_aBbbba181Abb_Eel1AbH3!Uuiou__Danielleyloelses_eouyBbbb']]
results = [True, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, True, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, False, False]

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
        func_name = "check_str"
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
        for test_case in ['assert check_str("annie")', 'assert not check_str("dawood")', 'assert check_str("Else")']:
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
