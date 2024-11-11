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
inputs = [['InValid'], ['TruE'], ['SenTenCE'], [''], ['True'], ['FALSE'], ['123'], ['StRiNg'], ['LOWER CASE'], ['nUmBeRs 123'], ['    extra spaces    '], ['camelCase'], ['UPPERCASE'], ['LOWER CASOE'], ['LOWER SE'], ['camelCacamelCasese'], ['1123'], ['LOWTrueER CASOE'], ['11123'], ['spaces'], ['LOWER CASCE'], ['LOWTrucamespaceslCacamelCaseseeER CASOE'], ['SE'], ['extra'], ['X'], ['LOWTrucamespaceslCacam11123 CASOE'], ['exxtra'], ['LOWTrucamespaceslCacam11123'], ['Trrue'], ['LOWRER CASOE'], ['LOWEWR CEASE'], ['LOWER CASROE'], ['TUPPERCASErue'], ['Trrrue'], ['LOWER CAROE'], ['LOWER'], ['LOWER CAS ROLOWRERE'], ['LOWER ROLOWRERECAS ROLOWRERE'], ['LOWER LCASCE'], ['CASCE'], ['camelCaese'], ['LOWRER'], ['CAROE'], ['xLOWER CASOexxtraE'], ['camelCasme'], ['eTrrCASOexxtraEue'], ['xLOWER'], ['11eTrrCASOexxtraEue123'], ['eTrrCASOexxtraaEue'], ['C'], ['camelCsme'], ['spnUmBeRsaces'], ['LOWEWR'], ['LOWER ALCASCE'], ['camelCslme'], ['LCASCE'], ['LR CASOE'], ['oa'], ['LOWTrueER'], ['SLOWER SE'], ['eTrrCASOexxtraaEuCASOexxtraEe'], ['LLOWTrueEROWER CASLOWEWR CEASE ROROLOWREREOLOWRERE'], ['TruenUmBeRs'], ['g'], ['CASE'], ['oaa'], ['LOWER ROLOWRERECAS ROLLOWER SEOWRERE'], ['11eTrrCASOexxte123'], ['SSE'], ['FvqXvHKtQ'], ['xLOWERO CASOexxtra'], ['ROROLOWREREOLOWRERE'], ['RACAROE'], ['LOWR SE'], ['cLLOWTrueEROWER CASLOWEWR CEASE ROROLOWREREOLOWREREamelCacamelCasese'], ['eLCASCExtra'], ['sspnUmBeRsaces'], ['LOWER ROLOWRERECAS ROLLOWER SEOWREREoa'], ['Trueg'], ['LOWER ROLOWRERxLOWERO CASOexxtraECAS ROLLOWER SEOWREREoa'], ['cLLOWTrueEROWER'], ['LOWTrueR'], ['11eTrrCASOexxtraExLOWEaROue123'], ['CCAROE'], ['ceamelCasme'], ['SL OWER SE'], ['eLCASCExtraSSE'], ['TUPPERCASErueSE'], ['caeTrrCASexxtraEuemelCase'], ['LOWOTrueER'], ['111323'], ['WLOWEWOR CEASE'], ['CASOexxtraE'], ['SEOWRERE'], ['123LOWTrueER CASOE'], ['cLLOWTrueEROWER CASLOWEWR CEASE ROROLOWREREOLEOWREREamelCacamelCaLOWRER CASOEsese'], ['camTruegelCaese'], ['oeTrrCASOexxtraEueaa'], ['SL OWER oeTrrCASOexxtraEueaaSE'], ['Tre'], ['ROLLOWER'], ['cLLOWTrueEROWERSLOWER SE'], ['CASOexxtra LCASRCE'], ['LOWER cLLOWTrueEROWERSLOWERASCE'], ['LOWER CCE'], ['LsspnUmBeRsacesOWER LCASCE'], ['cLLOWTrueEROWERSLOWERASCE'], ['CASOexxtra LC ASRCE'], ['LROROLOWREREOLEOWREREamelCacamelCaLOWRERER'], ['LCASRCE'], ['spaceROLOWREREs'], ['LR nUmBeRsxLOWERCASOE'], ['12LOWEROROLOWREREOLEOWREREamelCacamelCaLOWRERR CASE3LOWTrueER CASOE']]
results = ['invalid', 'true', 'sentence', '', 'true', 'false', '123', 'string', 'lower case', 'numbers 123', '    extra spaces    ', 'camelcase', 'uppercase', 'lower casoe', 'lower se', 'camelcacamelcasese', '1123', 'lowtrueer casoe', '11123', 'spaces', 'lower casce', 'lowtrucamespaceslcacamelcaseseeer casoe', 'se', 'extra', 'x', 'lowtrucamespaceslcacam11123 casoe', 'exxtra', 'lowtrucamespaceslcacam11123', 'trrue', 'lowrer casoe', 'lowewr cease', 'lower casroe', 'tuppercaserue', 'trrrue', 'lower caroe', 'lower', 'lower cas rolowrere', 'lower rolowrerecas rolowrere', 'lower lcasce', 'casce', 'camelcaese', 'lowrer', 'caroe', 'xlower casoexxtrae', 'camelcasme', 'etrrcasoexxtraeue', 'xlower', '11etrrcasoexxtraeue123', 'etrrcasoexxtraaeue', 'c', 'camelcsme', 'spnumbersaces', 'lowewr', 'lower alcasce', 'camelcslme', 'lcasce', 'lr casoe', 'oa', 'lowtrueer', 'slower se', 'etrrcasoexxtraaeucasoexxtraee', 'llowtrueerower caslowewr cease rorolowrereolowrere', 'truenumbers', 'g', 'case', 'oaa', 'lower rolowrerecas rollower seowrere', '11etrrcasoexxte123', 'sse', 'fvqxvhktq', 'xlowero casoexxtra', 'rorolowrereolowrere', 'racaroe', 'lowr se', 'cllowtrueerower caslowewr cease rorolowrereolowrereamelcacamelcasese', 'elcascextra', 'sspnumbersaces', 'lower rolowrerecas rollower seowrereoa', 'trueg', 'lower rolowrerxlowero casoexxtraecas rollower seowrereoa', 'cllowtrueerower', 'lowtruer', '11etrrcasoexxtraexlowearoue123', 'ccaroe', 'ceamelcasme', 'sl ower se', 'elcascextrasse', 'tuppercaseruese', 'caetrrcasexxtraeuemelcase', 'lowotrueer', '111323', 'wlowewor cease', 'casoexxtrae', 'seowrere', '123lowtrueer casoe', 'cllowtrueerower caslowewr cease rorolowrereoleowrereamelcacamelcalowrer casoesese', 'camtruegelcaese', 'oetrrcasoexxtraeueaa', 'sl ower oetrrcasoexxtraeueaase', 'tre', 'rollower', 'cllowtrueerowerslower se', 'casoexxtra lcasrce', 'lower cllowtrueerowerslowerasce', 'lower cce', 'lsspnumbersacesower lcasce', 'cllowtrueerowerslowerasce', 'casoexxtra lc asrce', 'lrorolowrereoleowrereamelcacamelcalowrerer', 'lcasrce', 'spacerolowreres', 'lr numbersxlowercasoe', '12lowerorolowrereoleowrereamelcacamelcalowrerr case3lowtrueer casoe']

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
        func_name = "is_lower"
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
        for test_case in ['assert is_lower("InValid") == "invalid"', 'assert is_lower("TruE") == "true"', 'assert is_lower("SenTenCE") == "sentence"']:
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
