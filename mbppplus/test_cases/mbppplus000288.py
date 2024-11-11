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
inputs = [['person'], ['final'], ['Valid'], [''], ['abcdefghijklmnopqrstuvwxyz'], ['He11o W0r1d!'], ['Thi5 is @ complex 1nput!'], ['Test1ng fUtur3'], ['I l0v3 c0d1ng!!'], ['H@ppy New Year 2022'], ['Th3 Qu1ck Br0wn F0x Jumps 0ver the L@zy D0g!'], ['@!$'], ['Thi5 is lnput!'], ['D0g!'], ['W0r1d!'], ['Thi5 is lnput!!'], ['l03'], ['l003'], ['Th3 Qu1ck Br0wn F0x Jumps 0veD0g!he L@zy D0g!'], ['YearHe1is1o We0r1d!'], ['cBr0wn0d1ng!!'], ['Thi5 @is @ complex 1nput!'], ['Thi5 @is @ comnplex 1nput!'], ['H@ppy New Yea0verr 2022'], ['F0x'], ['complelx'], ['lnput!F0x'], ['Qu1ck'], ['Thi5'], ['l00@is3'], ['@isQu1ck'], ['Th3 Qu1ck Br0wn F0xNew Jumps 0ver the L@zy D0g!'], ['c0d1ngg!!'], ['Thi5 lnput!!is lnput!!'], ['@!$Th3 Qu1ck Br0wn F0xNew Jumps 0ver the L@zy D0g!'], ['YearHe1is1oa We0r1d!'], ['Thi5 @is @ lnput!comnplex 1nput!'], ['D0g!cBr0wn0d1ng!!'], ['YearHe1is1o'], ['Yea0verr'], ['lnput!!'], ['c0d1ngg!!@is'], ['l0v3'], ['0ver'], ['YearHe1is1oa'], ['F0Thi5'], ['1nput!'], ['Th3 Qu1ck Br0wn F0xNew Jumps 0ver the L@zy D0g!Thi5'], ['D0g!Thi5'], ['c0d1Thi5Thi5 is lnput!! @is @ complex 1nput!ngg!!@is'], ['c0d1Thi5Tt!ngg!!@is'], ['compelx'], ['rrr'], ['I l0v3 c0Th3d1ng!!'], ['1nnput!'], ['Year'], ['2022'], ['abcdhijklmnopqrstuvwxyz'], ['YYea0verr'], ['New'], ['0W0r1d!'], ['Thi5 @is @ comnplrrrex 1nput!'], ['D0gTest1ng!cBr0wn0d1ng!!'], ['Test1ng efUtur'], ['@isQH@ppyu1ck'], ['Thi5 @is @ F0Thi5comnplrrresx 1nput!'], ['l0YearHe1is1oa We0r1d!0@is3'], ['c0d1Thiput!ngg!!@is'], ['Dg!g!'], ['Ye1nput!ngg!!@isarHYearHe1is1oae1is1o'], ['YearH1e1is1o We0r1d!'], ['Th3 Qu1ck Br0wn F0xNew Jumps 0ver the L@zy 0g!'], ['0W0r1d!0complelx'], ['Testur'], ['I l0veD0g!hed1ng!!'], ['Thi5 @is @ lnput!ccomnplrrrexomnplex 1nput!'], ['He11o'], ['YearHe1is1oa WeH0r1d!'], ['lnput!Fn0x'], ['Dc0d1ngg!!g!!g!'], ['1npu!'], ['He11o Wr0r1d!'], ['c0d1!ngg!!@is'], ['H@ppy New Year 2l0veD0g!hed1ng!!022'], ['YearHe1ioa'], ['abcdhijklmnopqrstuvwxyzYearHe1is1oa WeH0r1d!'], ['l0@is3'], ['YearHe1is1io'], ['l0v03'], ['D0Tg!Thi5'], ['0g!'], ['@isQcH@ppyu1ck'], ['Thi5 @is @ comt!'], ['YearH1e1is1o!'], ['OOoPGHemh'], ['lnp!!'], ['D0WeH0r1d!gTest1ng!cBr0wn0d1ng!!'], ['00veer'], ['rrrr'], ['Th3 Qu1ck He11oBr0wn F0xNew Jumps 0ver the L@zy D0g!'], ['r0Qu1cklx'], ['I'], ['fUtur3'], ['abcstuxvwxxyz'], ['T h3 Qu1ck Br0wn F0xNew Jumps 0ver the L@zy D0g!Thi5'], ['@!$Th3 Qu1ck Br0wn F0xNew Ju0g!'], ['@isQH@Yea0verrppyu1ck'], ['He11o Wr0r1Testur0W0r1d!d!'], ['NoCsH'], ['He1111o'], ['D0WHD0g!cBr0wn0d1ng!!0r1d!gTest1ng!cBr0wn0d1ng!!'], ['He11111o']]
results = ['PERSON', 'FINAL', 'VALID', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'HE11O W0R1D!', 'THI5 IS @ COMPLEX 1NPUT!', 'TEST1NG FUTUR3', 'I L0V3 C0D1NG!!', 'H@PPY NEW YEAR 2022', 'TH3 QU1CK BR0WN F0X JUMPS 0VER THE L@ZY D0G!', '@!$', 'THI5 IS LNPUT!', 'D0G!', 'W0R1D!', 'THI5 IS LNPUT!!', 'L03', 'L003', 'TH3 QU1CK BR0WN F0X JUMPS 0VED0G!HE L@ZY D0G!', 'YEARHE1IS1O WE0R1D!', 'CBR0WN0D1NG!!', 'THI5 @IS @ COMPLEX 1NPUT!', 'THI5 @IS @ COMNPLEX 1NPUT!', 'H@PPY NEW YEA0VERR 2022', 'F0X', 'COMPLELX', 'LNPUT!F0X', 'QU1CK', 'THI5', 'L00@IS3', '@ISQU1CK', 'TH3 QU1CK BR0WN F0XNEW JUMPS 0VER THE L@ZY D0G!', 'C0D1NGG!!', 'THI5 LNPUT!!IS LNPUT!!', '@!$TH3 QU1CK BR0WN F0XNEW JUMPS 0VER THE L@ZY D0G!', 'YEARHE1IS1OA WE0R1D!', 'THI5 @IS @ LNPUT!COMNPLEX 1NPUT!', 'D0G!CBR0WN0D1NG!!', 'YEARHE1IS1O', 'YEA0VERR', 'LNPUT!!', 'C0D1NGG!!@IS', 'L0V3', '0VER', 'YEARHE1IS1OA', 'F0THI5', '1NPUT!', 'TH3 QU1CK BR0WN F0XNEW JUMPS 0VER THE L@ZY D0G!THI5', 'D0G!THI5', 'C0D1THI5THI5 IS LNPUT!! @IS @ COMPLEX 1NPUT!NGG!!@IS', 'C0D1THI5TT!NGG!!@IS', 'COMPELX', 'RRR', 'I L0V3 C0TH3D1NG!!', '1NNPUT!', 'YEAR', '2022', 'ABCDHIJKLMNOPQRSTUVWXYZ', 'YYEA0VERR', 'NEW', '0W0R1D!', 'THI5 @IS @ COMNPLRRREX 1NPUT!', 'D0GTEST1NG!CBR0WN0D1NG!!', 'TEST1NG EFUTUR', '@ISQH@PPYU1CK', 'THI5 @IS @ F0THI5COMNPLRRRESX 1NPUT!', 'L0YEARHE1IS1OA WE0R1D!0@IS3', 'C0D1THIPUT!NGG!!@IS', 'DG!G!', 'YE1NPUT!NGG!!@ISARHYEARHE1IS1OAE1IS1O', 'YEARH1E1IS1O WE0R1D!', 'TH3 QU1CK BR0WN F0XNEW JUMPS 0VER THE L@ZY 0G!', '0W0R1D!0COMPLELX', 'TESTUR', 'I L0VED0G!HED1NG!!', 'THI5 @IS @ LNPUT!CCOMNPLRRREXOMNPLEX 1NPUT!', 'HE11O', 'YEARHE1IS1OA WEH0R1D!', 'LNPUT!FN0X', 'DC0D1NGG!!G!!G!', '1NPU!', 'HE11O WR0R1D!', 'C0D1!NGG!!@IS', 'H@PPY NEW YEAR 2L0VED0G!HED1NG!!022', 'YEARHE1IOA', 'ABCDHIJKLMNOPQRSTUVWXYZYEARHE1IS1OA WEH0R1D!', 'L0@IS3', 'YEARHE1IS1IO', 'L0V03', 'D0TG!THI5', '0G!', '@ISQCH@PPYU1CK', 'THI5 @IS @ COMT!', 'YEARH1E1IS1O!', 'OOOPGHEMH', 'LNP!!', 'D0WEH0R1D!GTEST1NG!CBR0WN0D1NG!!', '00VEER', 'RRRR', 'TH3 QU1CK HE11OBR0WN F0XNEW JUMPS 0VER THE L@ZY D0G!', 'R0QU1CKLX', 'I', 'FUTUR3', 'ABCSTUXVWXXYZ', 'T H3 QU1CK BR0WN F0XNEW JUMPS 0VER THE L@ZY D0G!THI5', '@!$TH3 QU1CK BR0WN F0XNEW JU0G!', '@ISQH@YEA0VERRPPYU1CK', 'HE11O WR0R1TESTUR0W0R1D!D!', 'NOCSH', 'HE1111O', 'D0WHD0G!CBR0WN0D1NG!!0R1D!GTEST1NG!CBR0WN0D1NG!!', 'HE11111O']

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
        func_name = "is_upper"
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
        for test_case in ['assert is_upper("person") =="PERSON"', 'assert is_upper("final") == "FINAL"', 'assert is_upper("Valid") == "VALID"']:
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
