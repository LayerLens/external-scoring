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
inputs = [['Jumanji The Jungle'], ['The_Avengers'], ['Fast and Furious'], [''], ['abcdefg'], ['  Jumanji The Jungle  '], ['        '], ['Hello, world!'], ['12345'], ['world!'], ['HelloThe, wolrld!'], ['BeWEijdkI'], ['BeWEidkI'], ['  Jumanji The JungJunglele  '], ['BeWEijkdkI'], ['abcdecfg'], ['abcdecfgJungle'], ['  Jumanji The JungJgunglele  '], ['BeWEijkdkIHeoThe,'], ['HelloThe, ,wolrld!'], ['HlelloThe, ,wolrld!'], ['HelloThe, Hwolrld!'], ['bRZaAd'], ['Hello,'], ['41234'], ['BeTheWEijkdkIHeoThe,'], ['JungJgunglele'], ['BeWEijkdhe,'], ['JungJgwolrld!unglele'], ['kHi'], ['BkeTheWEijkdkIHeoThe,'], ['BeWEijkdhBeTheWEijkdkIHeoThe,e,'], ['HlTelloThe,'], ['B,wolrld!jkdhBeTheWEEijkdkIHeoThe,e,'], ['jBeWEijkdhe,'], ['BJungJgunglele  Jumanji The JungJgunglele  eWEijkdhe,'], ['  Jumanji The JungJgunglele  abcdefg'], ['worl!'], ['BeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,'], ['world!bRZaAd'], ['BeTheWEijkdkIHeoThee,'], ['BBeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,eWEijkdhe,'], ['BeTheWEijdkIHeoThee,kHi'], ['d  Jumanji The JungJgunglele  abcdefg'], ['  JuBeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,lelle  '], ['BeWE  Jumanji The Jungle  ijjkdhe,'], ['afg'], ['  Jumanji The JuJungJunglelengJunglele  '], ['eWEijkdhe,'], ['wBeWEijkdkIHeoThe,orl!'], ['Theijkdhe,'], ['JungJgBkeTheWEijkdkIHeoThe,wolrld!unglele'], ['wBeWEijkdkIwBeWEijHelloThe, ,wolrld!e,orl!HeoThe,orl!'], ['  Jumanji The JungJung  Jumanji The JungJunglele  lele  '], ['HlelloThe,'], ['B,wolrld!jkdhBeTheWEEijkdkIHJungJgBkeTheWEijkdkIHeoThe,wolrld!ungleleThe,e,'], ['  Jumanji  '], ['BeBTheWEijkdkIHeoThe,'], ['  JuBeWEijkdhBeTheWEiijkdabce e '], ['JuBeWEijkdhBeTheWEiijkdabce'], ['BeWEijkdhBeTheWEij  Jumanji The Jungle  kdkIHeoThe,e,'], ['HelloThe,'], ['BeWEihjkdhBeTheWEijkdkIHeoThe,e,'], ['JJungJgwolJumanjinglele'], ['JungBeWE  Jumanji The Jungle  ijjkdhe,Jgunglele'], ['dBeWEijdkI'], ['ijjkdhe,'], ['4123afg4'], ['Hello,abcdecfg world!'], ['JuJukHingJunglHello,elengJunglele'], ['w!BeWEijkdkIwBeWEijHelloThe, ,wolrld!e,orl!HeoThe,orl!'], ['ijjkdheJ,JgunglelJungJung'], ['HelloThe, ,wwolrld!'], ['JungJgHello, world!unglele'], ['kkHi'], ['4123afg4BeWEijkdhe,'], ['JungJung'], ['wBeWEijkdkIwBeWEijHellooThe,'], ['JuJungJunglelengJunglele'], ['JuJungJafgunglelengJunglele'], ['JuBeWEabcdefgijkdhBeTheWEiijkdabce'], ['kHHelloThe, Hwolrld!i'], ['BeTheTheee,'], ['JuBeWEabcdefgijkdhBeTheWEiijkdabceBxSULfV'], ['BeTheTheeekHHelloThe,'], ['wBeWEijkdkIwBeWEijBHellooThe,'], ['Bele'], ['Ju  Jumanji The JungJung  Jumanji The JungJunglele  lele  JungJunglelengJunglele'], ['B,wolrld!jkdhBeTheWEEijkd,kIHeoThe,e,'], ['wworAd'], ['uYzKuQBHee'], ['w!BeWEijkEijHeolloTjhe,'], ['BeWEijkdhBeTheWEijkdabcdefgkIHeoworld!bRZaAdThe,e,'], ['  Jumanji The JungJgunglele cdefg'], ['  Jumanji The JungJu Jumanji The JungJunglele  lele  '], ['BBeTheWEijkdkIHeoThe,eWEijkdhBeTheWEij'], ['lHlelleoThe,'], ['BeTheWEijdkIHeoTheeJungJungllelengJunglele,kHi'], ['BeWhEijikdhBeTheWEijkdabcdefgkIHeoworld!bRZaAdThe,de,'], ['wwBeTheWEijdkIHeoThee,kHiirAd'], ['kk'], ['HelloThe,JuJungJunglelengJunglele'], ['HelloTBeWhEijikdhBeTheWEijkdabcdefgkIHeoworld!bRZaAdThe,de,,wolrld!'], ['  Jumanji The JungabcdecfgJung  Jumanji The JungJunglele  lele  '], ['JuBeWEijkjdhBeTheWEiijkdabce'], ['BeWEiijdkI'], ['  Jumanji The JungJgunglele '], ['  JuBeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,lell '], ['HelloThe,JuJungJunglelengJukkHiele']]
results = ['Jumanji_The_Jungle', 'The Avengers', 'Fast_and_Furious', '', 'abcdefg', '__Jumanji_The_Jungle__', '________', 'Hello,_world!', '12345', 'world!', 'HelloThe,_wolrld!', 'BeWEijdkI', 'BeWEidkI', '__Jumanji_The_JungJunglele__', 'BeWEijkdkI', 'abcdecfg', 'abcdecfgJungle', '__Jumanji_The_JungJgunglele__', 'BeWEijkdkIHeoThe,', 'HelloThe,_,wolrld!', 'HlelloThe,_,wolrld!', 'HelloThe,_Hwolrld!', 'bRZaAd', 'Hello,', '41234', 'BeTheWEijkdkIHeoThe,', 'JungJgunglele', 'BeWEijkdhe,', 'JungJgwolrld!unglele', 'kHi', 'BkeTheWEijkdkIHeoThe,', 'BeWEijkdhBeTheWEijkdkIHeoThe,e,', 'HlTelloThe,', 'B,wolrld!jkdhBeTheWEEijkdkIHeoThe,e,', 'jBeWEijkdhe,', 'BJungJgunglele__Jumanji_The_JungJgunglele__eWEijkdhe,', '__Jumanji_The_JungJgunglele__abcdefg', 'worl!', 'BeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,', 'world!bRZaAd', 'BeTheWEijkdkIHeoThee,', 'BBeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,eWEijkdhe,', 'BeTheWEijdkIHeoThee,kHi', 'd__Jumanji_The_JungJgunglele__abcdefg', '__JuBeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,lelle__', 'BeWE__Jumanji_The_Jungle__ijjkdhe,', 'afg', '__Jumanji_The_JuJungJunglelengJunglele__', 'eWEijkdhe,', 'wBeWEijkdkIHeoThe,orl!', 'Theijkdhe,', 'JungJgBkeTheWEijkdkIHeoThe,wolrld!unglele', 'wBeWEijkdkIwBeWEijHelloThe,_,wolrld!e,orl!HeoThe,orl!', '__Jumanji_The_JungJung__Jumanji_The_JungJunglele__lele__', 'HlelloThe,', 'B,wolrld!jkdhBeTheWEEijkdkIHJungJgBkeTheWEijkdkIHeoThe,wolrld!ungleleThe,e,', '__Jumanji__', 'BeBTheWEijkdkIHeoThe,', '__JuBeWEijkdhBeTheWEiijkdabce_e_', 'JuBeWEijkdhBeTheWEiijkdabce', 'BeWEijkdhBeTheWEij__Jumanji_The_Jungle__kdkIHeoThe,e,', 'HelloThe,', 'BeWEihjkdhBeTheWEijkdkIHeoThe,e,', 'JJungJgwolJumanjinglele', 'JungBeWE__Jumanji_The_Jungle__ijjkdhe,Jgunglele', 'dBeWEijdkI', 'ijjkdhe,', '4123afg4', 'Hello,abcdecfg_world!', 'JuJukHingJunglHello,elengJunglele', 'w!BeWEijkdkIwBeWEijHelloThe,_,wolrld!e,orl!HeoThe,orl!', 'ijjkdheJ,JgunglelJungJung', 'HelloThe,_,wwolrld!', 'JungJgHello,_world!unglele', 'kkHi', '4123afg4BeWEijkdhe,', 'JungJung', 'wBeWEijkdkIwBeWEijHellooThe,', 'JuJungJunglelengJunglele', 'JuJungJafgunglelengJunglele', 'JuBeWEabcdefgijkdhBeTheWEiijkdabce', 'kHHelloThe,_Hwolrld!i', 'BeTheTheee,', 'JuBeWEabcdefgijkdhBeTheWEiijkdabceBxSULfV', 'BeTheTheeekHHelloThe,', 'wBeWEijkdkIwBeWEijBHellooThe,', 'Bele', 'Ju__Jumanji_The_JungJung__Jumanji_The_JungJunglele__lele__JungJunglelengJunglele', 'B,wolrld!jkdhBeTheWEEijkd,kIHeoThe,e,', 'wworAd', 'uYzKuQBHee', 'w!BeWEijkEijHeolloTjhe,', 'BeWEijkdhBeTheWEijkdabcdefgkIHeoworld!bRZaAdThe,e,', '__Jumanji_The_JungJgunglele_cdefg', '__Jumanji_The_JungJu_Jumanji_The_JungJunglele__lele__', 'BBeTheWEijkdkIHeoThe,eWEijkdhBeTheWEij', 'lHlelleoThe,', 'BeTheWEijdkIHeoTheeJungJungllelengJunglele,kHi', 'BeWhEijikdhBeTheWEijkdabcdefgkIHeoworld!bRZaAdThe,de,', 'wwBeTheWEijdkIHeoThee,kHiirAd', 'kk', 'HelloThe,JuJungJunglelengJunglele', 'HelloTBeWhEijikdhBeTheWEijkdabcdefgkIHeoworld!bRZaAdThe,de,,wolrld!', '__Jumanji_The_JungabcdecfgJung__Jumanji_The_JungJunglele__lele__', 'JuBeWEijkjdhBeTheWEiijkdabce', 'BeWEiijdkI', '__Jumanji_The_JungJgunglele_', '__JuBeWEijkdhBeTheWEijkdabcdefgkIHeoThe,e,lell_', 'HelloThe,JuJungJunglelengJukkHiele']

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
        func_name = "replace_spaces"
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
        for test_case in ["assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'", "assert replace_spaces('The_Avengers') == 'The Avengers'", "assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'"]:
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
