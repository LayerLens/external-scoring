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
inputs = [['cAstyoUrFavoRitETVshoWs'], ['wAtchTheinTernEtrAdIo'], ['VoicESeaRchAndreComMendaTionS'], [''], ['ABCDEFG'], ['ThiS%^%!s&a(mY)TesTStR%i*ng'], ['ThiS%^%!s&a(mY)TsesTStR%i*ng'], ['ThiS%^%!%s*ng'], ['ABCDABCDEFGEFG'], ['ABFCDABCDEFGEFG'], ['CABCDEFG'], ['CACDEFG'], ['ThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ng'], ['ABFCDABCDCEEFG'], ['ABFCDABCGEFG'], ['AABCDEFGABCGEFG'], ['ThiS%^%ABCABFCDABCDCEEFGDEFG!s&a(mY)TsesTStR%i*ng'], ['ThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngABCDABCDEFGEFG'], ['ABFCDABCGEF'], ['ABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ng'], ['ThiSS%^%ABCDEFG!s&a(mY)TsesTStR%i*ng'], ['ThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(mY)TesTStR%i*ng'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTStR%i*ngABCDABCDEFGEFG'], ['AABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABCGEFG'], ['ThiS%^%ABCDEFG!ABCDEFGsTStR%i*ngABCDABCDEFGEFG'], ['ABFCDAABCCDCEEFG'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngStR%i*ngABCDABCDEFGEFG'], ['ABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(mY)TesTStR%i*ngDCEEFG'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFG'], ['ThiS%^%ABCABFCDABCDCEEFGDThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(mY)TesTStR%i*ngEFG!s&a(mY)TsesTStR%i*ng'], ['ABFCDABCDCFG'], ['CABCDEEFG'], ['AEBCDEFG'], ['ThiS%^%!s&a(mY)TsesTStR%i*nAABCDEFGABCGEFG'], ['ABCDEFGThiS%^%)!s&a(mY)TsesTAEBCDEFGStR%i*ng'], ['ThiSS%^%ABCDEFGT!s&a(mY)TsesTStR%i*ng'], ['ThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCGEFG'], ['CACDEFCG'], ['ABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFG'], ['A)TsesTStR%i*ng'], ['ThiSS%^%ABCDEFGT!s&a(mY)TsesTStR%i*ngABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ng'], ['ABFCDABCThiSS%^%ABCDEFGT!s&a(mY)TsesTStR%i*ngGEFG'], ['AABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFGCGEFG'], ['ThiS%^%!s&a(mY)TsesTStR%i*CnAABCDGABCGEFG'], ['ThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCA)TsesTStR%i*ngGEFG'], ['ThiS%^%!s&a(mY)TsesTStRs%i*nAABCDEFGABCGEFG'], ['ThThiSS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngiS%^%ABThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCGEFG%i*ngABCDABCDEFGEFG'], ['AABCDEGEFG'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)ABFCDAABCCDCEEFGTsesTStABCDEFGEFG'], ['ThiSS%^%ABCDEFG!s&a(mY)TsesTABCDEFGThiS%^%)!s%&a(mY)TsesTStR%i*ngStR%i*ng'], ['ThiSS%^%ABCDEFGAABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABCGEFGT!s&a(mY)TsesTStR%i*ngABCDEFGThiS%^%ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFG%i*ng'], ['ABFCDAABCCDDEEFG'], ['ThiS%^%ABCDEFABAABCDEGEFGDEFGThiS%^%)!s&a(mY)ABFCDAABCCDCEEFGTsesTStABCDEFGEFG'], ['ThisS%^%!s&a(mY)TsesTStRs%i*nAABCDEFGABCGEFG'], ['ThBiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngABCDABCDEFGEFG'], ['CABCDE'], ['ABCDEFGThiS%^%)!s&a(mEFGStR%i*ng'], ['ThiSS%^%ABCDEFGA(ABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABCGEFGT!s&a(mY)TsesTStR%i*ngABCDEFGThiS%^%ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesAABCDEFGABCGEFGTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFG%i*ng'], ['CACDEFCThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngAG'], ['ThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFG'], ['ThiS%^%ABCABFCDABCDCEEFGDThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(ThiS%^%!s&a(mY)TsesTStRs%i*nAABCDEFGABCGEFGmY)TesTStR%i*ngEFG!s&a(mY)TsesTStR%i*ng'], ['CABCABFCDABCThiSS%^%ABCDEFGT!s&a(mY)TsesTStR%i*ngGEFGEFG'], ['ThThiSS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngiS%^A%ABThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCGEFG%i*ngABCDABCDEFGEFG'], ['ABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)Tse%sTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFG'], ['ABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)Tse%sTStThBiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngABCDABCDEFGEFGR%i*n%!s&a(mY)TesTStR%i*ngDCEEFG'], ['ThThiSS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngiS%^%ABThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCGEFG%iS*ngABCDABCDEFGEFG'], ['AABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABABFCDABCThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFGT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFGCGEFG'], ['AAABFCDAABCCDCEEFGCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABABFCDABCThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFGT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFGCGEFG'], ['ThiS%^%!s&a(mY)TemsTStR%i*ng'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiSThiS%^%ABCABFCDABCDCEEFGDThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(ThiS%^%!s&a(mY)TsesTStRs%i*nAABCDEFGABCGEFGmY)TesTStR%i*ngEFG!s&a(mY)TsesTStR%i*ng%^%)!s&a(mY)ABFCDAABCCDCEEFGTsesTStABCDEFGEFG'], ['ThiS%^%ABCABFCDABCDCEEFGDThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(mY)TesTStR%i*ngEFG!ABFCDABCDCFGs&a(mY)TsesTStR%i*ng'], ['ThBiS%^%ABCDThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(mY)TesTStR%i*ngEFG!s&a(mY)TsesTStR%i*ngABCDABCDEFGEFG'], ['ACABCCDE'], ['ABCDFEFG'], ['ThBiS%^%ABCDEFG!s&a(mY)TsesThiS%^%ABCDEFABAABCDEGEFGDEFGThiS%^%)!s&a(mY)ABFCDAABCCDCEEFGTsesTStABCDEFGEFGTStR%i*ngABCDABCDEFGEFG'], ['ThiS%^%!s&a(mY)TemsTStR%i*ngAmCABCCDE'], ['ThiS%^%!s&a(mY)(TemsTStR%i*ngAmCABCCDE'], ['ThiSS%^%ABCDEFGA(ABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABCGEFGT!s&a(ThiSS%^%ABCDEFGAABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABCGEFGT!s&a(mY)TsesTStR%i*ngABCDDEFGThiS%^%ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFG%i*ng%ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesAABCDEFGABCGEFGTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFG%i*ng'], ['AABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABABFCDABCThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFGT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTStRCEEFGCGEFG'], ['AThBiS%^%ABCDEFG!s&a(mY)TsesThiS%^%ABCDEFABAABCDEGEFGDEFGThiS%^%)!s&a(mY)ABFCDAABCCDCEEFGTsesTStABCDEFGEFGTStR%i*ngABCDABCDEFGEFGABCDEGEFG'], ['ThiS%^%!s&a(mY)TemsTStR%i*ngABFCDABCGEFAmCABCCDE'], ['CABCDEF'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(m)Y)TsesTStABCDEFGEFG'], ['AABCDEFGABCDEFGThiS%^%)!s&aC(mY)TsesTStR%i*ngABCGEFG'], ['ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCsDEFGThiS%^%)!s&a(m)Y)TsesTStABCDEFGEFG'], ['ThThR%i*ngiS%^%ABThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCGEFG%iS*ngABCDABCDEFGEFG'], ['AABCDEFGABCDEFGThiS%^%)!s&aC(mY)TsesTStR%i*ngABCGEThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFGFG'], ['AABCDThiS%^%!s&a(mY)TemsTStR%i*ngEFGABCGEFG'], ['ABFCDAABCCDDEEEFG'], ['ABFCDABCDEFGGEFG'], ['ThiSS%^%ABCDEFGT!s&a(mY)TsesTStR%i*ngABCDEFGThiS%^%)!s&a(mY)Tse%sTStR%i*ng'], ['AABThThiSS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngiS%^%ABThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCGEFG%i*ngABCDABCDEFGEFGCDEFGABCDEFGThiS%^%)!s&aC(mY)TsesTStR%i*ngABCGEThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFGFG'], ['AABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTSetR%i*ngDCEEFGCGEFG'], ['ABFCDAABCCEDDEEFG'], ['ThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGABCA)TsesTStR%ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFGi*ngGEFG'], ['ACABCABFCDABCT%hiThiS%^%ABCDEFG!s&a(mY)Tse%sTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFGCDE'], ['AThiS%^%!s&a(mY)TsesTStR%i*nAABCDEFGABCGEFGBCDABCDG'], ['ThiSS%^%ABCDEFGAABCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABCGEFGT!s&a(mY)TsesTStR%i*ngABCDEFGThiS%^%ThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStABCThiS%^%ABCABFCDABCDCEEFGDThiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngS%^%!s&a(mY)TesTStR%i*ngEFG!s&a(mY)TsesTStR%i*ngDEFGEFG%i*ng'], ['ThiSAAABFCDAABCCDCEEFGCDEFGABCDEFGThiS%^%)!s&a(mY)TsesTStR%i*ngABSABFCDABCThiS%^%!s&a(mY)TsesTStR%i**CnAABCDGABCGEFGT%hiThiS%^%ABCDEFG!s&a(mY)TsesTStR%i*n%!s&a(mY)TesTStR%i*ngDCEEFGCGEFG%^%!s&a(mY)TsesTStR%i*ng'], ['ThThiSS%^%ABCDEFG!s&a(mY)TsesTStR%i*ngiS%^A%ABThiS%^%!s&a(mY)TsesTStR%i*CnAABCDEFGACDEFGEFG'], ['ABCDEFGThiS%^%)!s&a(mY)TsesTThiS%^%!s&a(mY)TemsTStR%i*ngABAFCDABCGEFAmCABCCDEAEBCDEFGStR%i*ng'], ['CACDEFCThiS%^%ABCDEFG!s&a(mY)TsesTStR%%i*ngAG'], ['AABFCDABCGEFG'], ['ThABFCDABCDEFGGEFGiS%^%!%sg'], ['CAThiS%^%ABCDEFABCDEFGG!s&a(mY)TsesTABCDEFGThiS%^%)!s&a(mY)TsesTStABCDEFGEFGBCDEEFG'], ['ThisS%^%!s&a(mY)ABFCDABCDEFGEFGTsesTStRs%i*nAABCDEFGABCGEFG']]
results = ['cstyoravoitshos', 'wtchheinerntrdo', 'oiceachndreomendaion', '', '', 'hisamesting', 'hisamsesting', 'hisng', '', '', '', '', 'hisamsesting', '', '', '', 'hisamsesting', 'hisamsesting', '', 'hisamsesting', 'hisamsesting', 'hihisamsestingsamesting', 'hisamsesting', 'hisamsesting', 'histing', '', 'hisamseshisamsestingting', 'hihisamsestingsamesting', 'hisamseshisamsest', 'hihihisamsestingsamestingsamsesting', '', '', '', 'hisamsestin', 'hisamsesting', 'hisamsesting', 'hisamsestin', '', 'hihisamsestinsamesting', 'sesting', 'hisamsestinghisamsesting', 'hisamsesting', 'hisamsestinghihisamsestinsamesting', 'hisamsestin', 'hisamsestinsesting', 'hisamsestsin', 'hhisamsestingihisamsestining', '', 'hisamseshisamsest', 'hisamseshisamsestingting', 'hihisamsestingsamsestinghihisamseshisamsesting', '', 'hihisamsest', 'hissamsestsin', 'hisamsesting', '', 'hisamting', 'hihisamsestingsamsestinghihisamseshisamsesting', 'hisamsesting', 'hisamsestin', 'hihihisamsestingsahisamsestsinmestingsamsesting', 'hisamsesting', 'hhisamsestingihisamsestining', 'hihisamsestinsamesting', 'hihisamsesthisamsestinginsamesting', 'hhisamsestingihisamsestining', 'hisamsestinghisamsestinhihisamsestinsamesting', 'hisamsestinghisamsestinhihisamsestinsamesting', 'hisamemsting', 'hisamseshihihihisamsestingsahisamsestsinmestingsamsestingsamsest', 'hihihisamsestingsamestingsamsesting', 'hihihisamsestingsamestingsamsesting', '', '', 'hisamseshihisamsestting', 'hisamemstingm', 'hisamemstingm', 'hihisamsestingsahihisamsestingsamsestinghihisamseshisamsestinghisamseshisamsesting', 'hisamsestinghisamsestinhihisamsestinsamest', 'hisamseshihisamsestting', 'hisamemstingm', '', 'hisamseshisamsest', 'hisamsesting', 'hisamsesshisamsest', 'hhingihisamsestining', 'hisamsestinghisamsestin', 'hisamemsting', '', '', 'hisamsestinghisamsesting', 'hhisamsestingihisamsestininghisamsestinghisamsestin', 'hisamsestinghihisamsestinsameseting', '', 'hisamsestinsesthisamseshisamsesting', 'hihisamsestinsamesting', 'hisamsestin', 'hihisamsestingsamsestinghihisamseshisamsesthihihisamsestingsamestingsamsestinging', 'hihisamsestinghisamsestinhihisamsestinsamestingsamsesting', 'hhisamsestingihisamsestin', 'hisamseshisamemstingmting', 'hisamsesting', '', 'hisg', 'hisamseshisamsest', 'hissamsestsin']

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
        func_name = "remove_uppercase"
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
        for test_case in ["assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'", "assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'", "assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'"]:
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
