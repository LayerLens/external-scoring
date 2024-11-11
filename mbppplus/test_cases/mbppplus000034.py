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
inputs = [['Hadoop'], ['great'], ['structure'], ['a'], ['longstringwithmixture'], ['lonlongstringwithmixturegstringwithmixture'], ['lonlongstringwithmixturegstringwithmixturlongstringwithmixturee'], ['lonlongstringwithmixturegstringwithmxture'], ['longstringwithmiixtiure'], ['lnongstringwithmixture'], ['alongstringwithmiixtiure'], ['lonlongstringwitlongstringwithmiixtiurehmixturegstringwithmxture'], ['lonlongstringwithmixturegstringwithlongstringwithmixturemixture'], ['lonlongstringwitringwithmixture'], ['lnongstringwithmixturea'], ['mlongstringwithmiixtiure'], ['lonlongstrringwithmixturegstringwithlongstringwitnhmixturemixture'], ['longstringwithmiixlonlongstringwithmixturegstringwithmxturetiure'], ['lonlongstringwitringwhithmixture'], ['lonlongstringwithmixturegstringwithmixturlongstringwithmixturelongstringwithmiixlonlongstringwithmixturegstringwithmxturetiuree'], ['lonlongstringwithmixlonlongstringwithmixturegstringwithmixtureturegstringwithmixture'], ['lonlongstringwitringwithmixtongtstringwitringwhithmixture'], ['lnongstringwithmixlonlongstringwithmixturegstringwithmxtureturea'], ['lnmlongstringwithmiixtiureongstringwithmixturea'], ['longstringwithmiixlonlongstringwithmixturegstlringwithmxturetiure'], ['TtYAzEr'], ['lonlongstrlonlongstrringwithmixturegstringwithlongstringwitnhmixturemixtureingwithmixturegstringwithmxture'], ['lnmlongstringwithmiixtiureongstringwithmixturelonlongstringwitringwhithmixturea'], ['longstlongstringwithmiixlonlongstringwithmixturegstringwithmxturetiureringwithmiixtiure'], ['lonlongstrlonlongstrringwithmixturegstringwithlongstringwitwnhmixturemixtureingwithmixturegstrinhmtxture'], ['aa'], ['longastringwithmiixtiure'], ['longastringxwithmiixtiure'], ['liongastringwithmixtiure'], ['lonlongstringwithmixlonlongstrilongstringwithmixturengwithmixturegstringwithmixtureturegstringwithmixture'], ['lnongstriengwithmixturea'], ['longstringwithmiixlonlongstringwithmialongstringwithmiixtiurexturegstringwithmxturetiure'], ['longstringwithmiixlonnlongstringwithmixturegstringwithmxturetiure'], ['alongslongastringwithmiixtiuretringwithmiixtiure'], ['lonlongstringwithmixturegstrinurlongstringwithmixturee'], ['longstringwithmiixlonlongstrinlonlongstringwithmixturelongstringwithmiixlonlongstringwithmixturegstringwithmxturetiuregstringwithlongstringwithmixturemixturethmxturetiure'], ['lonlongstringwitringwithmixtongtstringwitringwhitthmixture'], ['longstringwithmiixlonlongstringwithmialongstrilnmlongstringwithmiixtiureongstringwithmixtureangwithmiixtiurexturegstringwithmxturetiure'], ['lonlongstrinlonlongstringwithmixturegstringwithmxturegwitringwhithmixture'], ['lonlongstringwitringwithmixlonlongstringwithmixturegstringwithmxtureture'], ['mlongstringwithmiiwxtiure'], ['lionglongastringxwithmiixtiureastringwithmixtiure'], ['lonlongstringwitringwiithmixture'], ['longstlongstringwithmiixlonlongstringwithmixturegstringwithmxturetiurerinigwithmiixtiure'], ['mlongstringwwithmiixtiure'], ['lonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiureonlongstrlonlongstrringwithmixturegstringwithlongstringwitnhmixturemixtureingwithmixturegstringwithmxtureingwitnhmixturemixture'], ['lnongstringwithmirea'], ['lonlongstringwithmixturegstringwithmixturlongstlonlongstrlonlongstrringwithmixturegstringwitlonlongstringwitringwithmixlonlongstringwithmixturegstringwithmxtureturegwithmixturee'], ['mxlongstringwithmiixtiure'], ['lonlongstringwithmixturegstringwithmxturlongstringwithmixturee'], ['lnmlongstringwithmiixtiureongstringwithmixtulongstlongstringwithmiixlonlongstringwithmixturegstringwithmxturetiurerinigwithmiixtiure'], ['mlongstrintgwwithmiixtiure'], ['lonlongstringwitringwithmixtongtstringwitringwhtithmixture'], ['lonlongstringwithmixturegstringwithmixturlongstlonlongstringwithmixturegstringwithmixturlongstringwithmixturelongstringwithmiixlonlongstringwithmixturegstringwithmxturetiureeringwithmixturelongstringwithmiixlonllonlongstringwitringwiithmixturegstringwithmxturetiuree'], ['lonlongstrhingwithmixlonlongstrilongstringwithmixturengwithmixturegstrhgingwithmixtureturegstringwithmixture'], ['ltiongastringwithmixtiure'], ['liongastringwithmtixtiure'], ['lnongstringwgithlnongstringwithmixtureturegstringwithmxtureturea'], ['lgstringwithmixturee'], ['lonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiureonlongstrlonlongstrringwithmixturegstringwithlongstringwiwithmxtureingwitnhmixturemixture'], ['alonlongstringwithmixturegstringwithmixturlongstlonlongstrlonlongstrringwithmixturegstringwitlonlongstringwitringwithmixlonlongstringwithmixturegstringwithmxtureturegwithmixtureea'], ['lonlongstrhingwithmixlonlongstrilongstringwithmixturengwithmixturegstrhgingwithmixturture'], ['lonlongstrinlonlongstringwithmixturegstringwithmxturegwitringwhithmlongstringwithmiixlonlongstringwithmixturegstlringwithmxturetiureixture'], ['lnmlongstringwithmiixtiurreonwgstringwithmixturelonlongstringwitringwhithmixturea'], ['lonlongstrlongstringwithmiixlonlongstrinlonlongstringwithmixturelongstringwithmiixlonlongstringwithmixturegstringwithmxturetiuregstringwithlongstringwithmixturemixturethmxturetiureingwitringwithmixture'], ['lonlongstrlonlongstrringwithmixturegstringwithlongstringwitwnlongastringxwithmiixtiurehmixturemixtureingwithmixturegstrinhmtxture'], ['lonlongstringwitringwlonlongstrringwithmgwitnhmixturemixturehithmixture'], ['lonlongstringwitritngwithmixture'], ['lnongs'], ['alongslonlongstrlonlongstrrinlonlongstringwithmixturegstringwithmixturlongstringwithmixtureegwithmixturegstringwithlongstringwitnhmixturemixtureingwithmixturegstringwithmxturelongastringwithmiixtiuretringwithmiixtiure'], ['lnongstrilonlongstrringwithmixturegstringwithlongstringwitnhmixturemixturengwithmixlonlongstringwithmixturelonlongstrlonlongstrringwithmixturegstringwithlongstringwitwnlongastringxwithmiixtiurehmixturemixtureingwithmixturegstrinhmtxturegstringwithmxtureturea'], ['longastringxwithmiixtiurliongastringwithmtixtiuree'], ['lonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiulreonlongstrlonlongstrringwithmixturegstringwithlongstringwiwithmxtureingwitnhmixturemixture'], ['longstringwithmiixlonlongstringwitlongstringwithmiixtiuremixturegstlringwithmxturetiure'], ['lonlongstringwithmixturegstrinurlongstringwithhmixturee'], ['lonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiureonlongstrlonlongstrringwithmixturegstringwithlongstringwiwithmxtureingwitnhmixturemixre'], ['ltiongastringwithmixtinure'], ['lonlongstringwithmixturegstringwithmixturlongstlonlongstrlonlthmixturegstringwithmxtureturegwithmixturee'], ['lonlongstrlonlongstrringwithmixturegstringwithlongstringwitwnhmixtulonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiureonlongstrlonlongstrringwithmixturegstringwithlongstringwiwithmxtureingwitnhmixturemixreremixtureingwithmixturegstrinhmtxture'], ['lonlongstringwitrinthmixtongtstrinigwitringwhtithmixture'], ['longstringwitlongstringwithmiixlonlongstringwithmilonlongstringwitringwithmxturexturegstlringwithmxturetiurehmiixtiure'], ['mxllonlongstrlonlongstrringwithmixturegstringwithlongstringwitwnhmixturemixtustrinhmtxtureongstringwithmiixtiure'], ['lonlongstrlongstringwithmiixlonlongstrinlonlongstringwithmixturelongstringwithmiixlonlongstringwithmixturegstringwithmxturetiuoregstringwithlongstringwithmixturemixturethmxturetiureingwitringwithmixture'], ['lnmlongstringwithmiixtiureongstringwithmixturealonlongstringwithmixturegstringwithmixturlongstringwithmixturee'], ['longstlongstrsingwithmiixlonlongstringwithmixturegstringwithmxturetiuaare'], ['lgstringwithmlonlongstringwithmixturegstringwithmxtureixturee'], ['alongslonlongstrlonlongstrrinlonlongstringwithmixturegstringwithmixturlongstringwithmixtureegwithmixturegstringwithlongstringwitnhmtixturemixtureingwithmixturegstringwithmxturelongastringwithmiixtiuretringwithmiixtiure'], ['lithmiixtgwithmxturetiure'], ['lnmlongstringwithmiixtiurreonwgstringwithmixturelonlongstringwitlongstlongstringwithmiixlonlongstringwithmixturegstringwithmxturetiurerinigwithmiixtiureringwhithmixturlongstringwitlongstlonlongstringwitringwiithmixtureringwithmiixlonlongstringwithmilonlongstringwitringwithmxturexturegstlringwithmxturetiurehmiixtiureea'], ['mxllonlongstrlonlongstrringwithmixturegstringwithlongstringwitwnhmixturemixtustrinhmtxlonlongstringwithmixturegstringwithmixturlongstlonlongstrlonlthmixturegstringwithmxtureturegwithmixtureetureongstringwithmiixtiure'], ['lonlongstrlonlongstrringhwithmixturegstringwithlongstringwitnhmixturemixtureingwithmixturegstringwithure'], ['longstlongstrsingwithmiixlonlongsxtringwithmiithmxturetiuaare'], ['lgstringwithmixtlnongstringwithmireareelnmlongstringwithmiixtiureongstringwithmixturelonlongstringwitringwhithmixturea'], ['lolongastringxwithmiixtiurliongastringwithmtixtiureengstringwithmiixlonlongstrinlonlongstringwithmixturelongstringwithmiixlonlongstringwithmixturelongstringwithmiixlonnlongstringwithmixturegstringwithmxturetiuregstringwithmxturetiuregstringwithlongstringwithmixturemixturethmxturetiure'], ['lonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiulreonlongstrlonlongstrringwithmixturegstringwlonlongstringwitringwithmixturethmxtureingwitnhmixturemixture'], ['lnmlongstringwithmiimxtiureongstringwithmixturea'], ['lonlongstrringwithmixturegstringwithlongstrllongstringwithmiixtiulreliongastringwithmtixtiureonlongstrlonlongstrringwithmixturegstringwithlongstringwiwithmxtureingwitnhmixturemixture'], ['longstrinithmixture'], ['lgstringwithmixtlnongstringwithmireareelnmlongstringwithmiixtiurheongstringwithmixturelonlongstringwitringwhithmixturea'], ['longasntringxwithmiixtiure']]
results = [False, True, True, True, True, False, True, True, True, False, False, False, True, True, True, False, True, False, False, True, False, True, False, True, True, True, False, True, True, False, False, False, True, False, True, False, False, True, False, False, False, False, True, True, False, True, True, False, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, True, True, False, True, True, True, True, False, False, True, False, False, True, True, True, False, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, True, False, True, True, False, False, True, True, False]

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
        func_name = "word_len"
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
        for test_case in ['assert word_len("Hadoop") == False', 'assert word_len("great") == True', 'assert word_len("structure") == True']:
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
