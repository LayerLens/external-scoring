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
inputs = [['I1love143you55three3000thousand'], ['Avengers124Assemble'], ['Its11our12path13to14see15things16do17things'], ['Hello! My age is 28. I was born on the 1st of January, 1992.'], [''], ['1234567890'], ['Hello! This string contains no numbers'], ['Hello! My age is 28. I was borln on the 1st of January, 1992.'], ['was'], ['Hello! My age is 28.. I was borln on the 1st of January 1992.'], ['Hello!  on the 1st of January 1992.'], ['Helloa! My age is 22.'], ['Helloa!.'], ['waws'], ['Hellorn on the 1st of January, 1992.'], ['wawMys'], ['1992.'], ['brorln'], ['Hello! My age is 28. I was born on the 1st of 28.January, 1992.'], ['string'], ['Hellorn on onry, 1992.'], ['199Hello! My age is 28.. I was borln on the 1st of January 1992.2.'], ['Hello! My age is 28. I was born on the 1st of JanuaHello!ry, 1992.'], ['TThis'], ['numbers'], ['199Hello! My age iln on the 1st of January 1992.2.'], ['199Hello! My age is 28.. I was borln on the 1st of JanuarHellorn on the 1st of January, 1992.y 1992.2.'], ['swawsing'], ['Hello! My age is 28. I was born on the 1st of anuary, 1992.'], ['stnumbersring'], ['I'], ['Hello! 28.My agei is 28.. I was borln wawson the 1st of January 1992.'], ['Hello! My age is 28. , 1992.'], ['Hello! My age is 28a. , 1992.brorln'], ['Hellorn on the 1sHellorn on onry, 1992.t of January, 1992.'], ['Hellorn on the 1lst of January, 1992.'], ['January,'], ['He.'], ['Hello! 2f January 1992.'], ['19912.'], ['num1sHers'], ['age'], ['1992.y'], ['He.H'], ['Hel My age is 28. I was born yon the 1st of January, 1 992.'], ['28a.'], ['Hello! This strings'], ['MMy'], ['TThiHello! My age is 28.. I was borln on the 1st of January 1992.s'], ['TThiHellothe e1st of January 1992.s'], ['1st'], ['Hello! This string contains no numbersHello! 2f January 1992.'], ['1992.Hellorn on the 1sHellorn on onry, 1992.t of January, 1992.y'], ['28.My'], ['1992.brorln'], ['anuary,'], ['Hello! My age is 28. I was borln on the 1st of January, 19born92.'], ['II199Hello! My age is 28.. I was borln on the 1st of January 1992.2.'], ['1'], ['199Hello! My age is 28.. I was borln on9 the 1st of January 1992.2.'], ['1992.t'], ['TThiHellolthe e1st of January 1992.s'], ['January'], ['strin1g'], ['Hello! My age is 28.. hI was borln on the 1st of January 1992January.'], ['Hellorn on the 1lst of Januaory, 1992.'], ['yon'], ['anu,ary,'], ['1Hellorn on the 1lst of Januaory, 1992.st'], ['199Hello! My age is 28.. I was borln on the 1st of JanuarHellorn on the 1st of Ja'], ['1992January.'], ['1sHello! My age is 28. I was born on the 1st of JanuaHello!ry, 1992.t'], ['borln'], ['b992.orln'], ['199Hel'], ['HeHellorn on the 1lst of January, 1992.lloa!.'], ['Hello! My age is 28. I was bo rn on the 1st of anuary, 1992.'], ['He.Hb992.orln'], ['TThiHelonlolthe e1st of January 1992.s1992.TThiHello!brorln'], ['Hello! My age is 28. I was born on the 1st o f 28.January, 1992.'], ['sHello! My age is 28. I was born on the 1st of 28.January, 1992.tring'], ['Hello! My age is 28. I wlas born on the 1st of JanuaHello!ry, 1992.'], ['onstnumbersring9'], ['Helloaa!.'], ['no'], ['stsrin1g'], ['Hellorn on onry, 91992n.'], ['992.'], ['wlas'], ['11992.tring992.'], ['Helloa!'], ['sn1g'], ['JanuarHellorn'], ['1sHello!'], ['waJas'], ['199Hello! My age is 28.. I was borln on the 1st ofTThiHello! My age i28.January,s 28.. I was borln on the 1st of January 1992.s JanuarHellorn on the 1st of Ja'], ['yHello! This string contains no numbers'], ['anu,ary,1'], ['born'], ['anuabornry,'], ['199Hello!'], ['b9922.orln'], ['TThis992.'], ['ofTThiHello!'], ['9992no.'], ['oof'], ['1992January.y']]
results = ['Iloveyouthreethousand1143553000', 'AvengersAssemble124', 'Itsourpathtoseethingsdothings11121314151617', 'Hello! My age is . I was born on the st of January, .2811992', '', '1234567890', 'Hello! This string contains no numbers', 'Hello! My age is . I was borln on the st of January, .2811992', 'was', 'Hello! My age is .. I was borln on the st of January .2811992', 'Hello!  on the st of January .11992', 'Helloa! My age is .22', 'Helloa!.', 'waws', 'Hellorn on the st of January, .11992', 'wawMys', '.1992', 'brorln', 'Hello! My age is . I was born on the st of .January, .281281992', 'string', 'Hellorn on onry, .1992', 'Hello! My age is .. I was borln on the st of January ..19928119922', 'Hello! My age is . I was born on the st of JanuaHello!ry, .2811992', 'TThis', 'numbers', 'Hello! My age iln on the st of January ..199119922', 'Hello! My age is .. I was borln on the st of JanuarHellorn on the st of January, .y ..1992811199219922', 'swawsing', 'Hello! My age is . I was born on the st of anuary, .2811992', 'stnumbersring', 'I', 'Hello! .My agei is .. I was borln wawson the st of January .282811992', 'Hello! My age is . , .281992', 'Hello! My age is a. , .brorln281992', 'Hellorn on the sHellorn on onry, .t of January, .119921992', 'Hellorn on the lst of January, .11992', 'January,', 'He.', 'Hello! f January .21992', '.19912', 'numsHers1', 'age', '.y1992', 'He.H', 'Hel My age is . I was born yon the st of January,  .2811992', 'a.28', 'Hello! This strings', 'MMy', 'TThiHello! My age is .. I was borln on the st of January .s2811992', 'TThiHellothe est of January .s11992', 'st1', 'Hello! This string contains no numbersHello! f January .21992', '.Hellorn on the sHellorn on onry, .t of January, .y1992119921992', '.My28', '.brorln1992', 'anuary,', 'Hello! My age is . I was borln on the st of January, born.2811992', 'IIHello! My age is .. I was borln on the st of January ..19928119922', '1', 'Hello! My age is .. I was borln on the st of January ..199289119922', '.t1992', 'TThiHellolthe est of January .s11992', 'January', 'string1', 'Hello! My age is .. hI was borln on the st of January January.2811992', 'Hellorn on the lst of Januaory, .11992', 'yon', 'anu,ary,', 'Hellorn on the lst of Januaory, .st111992', 'Hello! My age is .. I was borln on the st of JanuarHellorn on the st of Ja1992811', 'January.1992', 'sHello! My age is . I was born on the st of JanuaHello!ry, .t12811992', 'borln', 'b.orln992', 'Hel199', 'HeHellorn on the lst of January, .lloa!.11992', 'Hello! My age is . I was bo rn on the st of anuary, .2811992', 'He.Hb.orln992', 'TThiHelonlolthe est of January .s.TThiHello!brorln119921992', 'Hello! My age is . I was born on the st o f .January, .281281992', 'sHello! My age is . I was born on the st of .January, .tring281281992', 'Hello! My age is . I wlas born on the st of JanuaHello!ry, .2811992', 'onstnumbersring9', 'Helloaa!.', 'no', 'stsring1', 'Hellorn on onry, n.91992', '.992', 'wlas', '.tring.11992992', 'Helloa!', 'sng1', 'JanuarHellorn', 'sHello!1', 'waJas', 'Hello! My age is .. I was borln on the st ofTThiHello! My age i.January,s .. I was borln on the st of January .s JanuarHellorn on the st of Ja1992812828119921', 'yHello! This string contains no numbers', 'anu,ary,1', 'born', 'anuabornry,', 'Hello!199', 'b.orln9922', 'TThis.992', 'ofTThiHello!', 'no.9992', 'oof', 'January.y1992']

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
        func_name = "move_num"
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
        for test_case in ["assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'", "assert move_num('Avengers124Assemble') == 'AvengersAssemble124'", "assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'"]:
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
