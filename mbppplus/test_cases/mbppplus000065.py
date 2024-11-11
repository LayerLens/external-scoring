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
inputs = [['python programming'], ['lists tuples strings'], ['write a program'], [''], ['   python      programming    '], ['1234 5678 9101'], ['string1,string2,string3'], ['My favorite programming language is Python'], ['string1,     string2,       string3'], ['string1,string2,strin3'], ['language'], ['1234 5678 91string1,string2,string301'], ['string1,string2,3'], ['My'], ['1234'], ['l'], ['5678'], ['192314 5678 9101'], ['python'], ['12314'], ['   ng    '], ['56678'], ['favorite'], ['string2,'], ['AeFmnNDd'], ['56'], ['programming'], ['pronggrammin12314g'], ['prog'], ['5striing1,stringg2,strin3'], ['language  ng    '], ['favorit'], ['gvZn'], ['languPythonage  ng    '], ['Python'], ['SfDBdGHKU'], ['is'], ['5stprogriing1,stringg2,strin3'], ['fvorrite'], ['porog'], ['pAeFmnNDdor'], ['propg'], ['languag5678e  ng    '], ['My favorite programming lamnguage is Python'], ['12My favorite programming language is Python34 5678 9101'], ['programmming'], ['My favorite prolanguPythonagegramminlg language is Python'], ['te'], ['fvorrrite'], ['string1,     string2,       sstring3'], ['1234 5678  9101'], ['556is78'], ['My favorite prol anguPythonagegramminlg lanage is Python'], ['vksoeiMq'], ['12My favorite programming language is Python34 5678string2,'], ['5striing1,My favorite proMye ythonpstringg2,strin3'], ['1234 5678 91string1,sPython342,string301'], ['fvorofrite'], ['fvorrreite'], ['favoritprogrammming'], ['Python34'], ['556iss78'], ['peMsMC'], ['ffvorrreite'], ['5striing1,My favorite proMylanguagee ythonpstringg2,strin3'], ['556iss788'], ['spythonring2'], ['string3'], ['Pstring3ython'], ['My favorit5678e prol anguPythonagegramminlg lanage is Pgython'], ['12334 5678  9101'], ['prol'], ['langua g5678e  ng    '], ['rfvorrrite'], ['PlanguPythonage'], ['123My favorite prolanguPythonagegramminlg language is Python4 5678 9101'], ['12 334 5678  9101'], ['fvorofritre'], ['192314'], ['string1,     st ring2,,       string3'], ['lanage'], ['gprolanguPythonagegramminlgvZ12n'], ['fvoorrite'], ['st'], ['anguPythonagegramminlg'], ['12My favorite programming glanguage is Python34 5678string2,'], ['12python3My'], ['languPythonage  ngn    '], ['gg5678e'], ['rfvorrtristring1,     st ring2,,       string3te'], ['languag5678e'], ['string1,     st ring2,languag5678e  ng      string3'], ['5stprogriing1,stiringg2,strin3'], ['My favorite programming language is PytlanguPythonagehon'], ['programmmipng'], ['flvorofrite'], ['tt'], ['1212314M3y'], ['pronggrrammin12314g'], ['string1,     st ring2,,        string3'], ['123My favorite prolanguPythonagegramminlg language is Pythstring1,     string2,       string3on4 5678 9101'], ['fvsstring3e'], ['Pst3ring3ython'], ['string1,     st ring2,languag5678e  ng      string'], ['lan12334 5678  9101gua g5678e  ng    '], ['faorite'], ['91nstring1,string2,string301'], ['prrfvorrtristring1,     st ring2,,       string3teol'], ['556667string1,string2,string3']]
results = [['python', 'programming'], ['lists', 'tuples', 'strings'], ['write', 'a', 'program'], [''], ['', '', '', 'python', '', '', '', '', '', 'programming', '', '', '', ''], ['1234', '5678', '9101'], ['string1,string2,string3'], ['My', 'favorite', 'programming', 'language', 'is', 'Python'], ['string1,', '', '', '', '', 'string2,', '', '', '', '', '', '', 'string3'], ['string1,string2,strin3'], ['language'], ['1234', '5678', '91string1,string2,string301'], ['string1,string2,3'], ['My'], ['1234'], ['l'], ['5678'], ['192314', '5678', '9101'], ['python'], ['12314'], ['', '', '', 'ng', '', '', '', ''], ['56678'], ['favorite'], ['string2,'], ['AeFmnNDd'], ['56'], ['programming'], ['pronggrammin12314g'], ['prog'], ['5striing1,stringg2,strin3'], ['language', '', 'ng', '', '', '', ''], ['favorit'], ['gvZn'], ['languPythonage', '', 'ng', '', '', '', ''], ['Python'], ['SfDBdGHKU'], ['is'], ['5stprogriing1,stringg2,strin3'], ['fvorrite'], ['porog'], ['pAeFmnNDdor'], ['propg'], ['languag5678e', '', 'ng', '', '', '', ''], ['My', 'favorite', 'programming', 'lamnguage', 'is', 'Python'], ['12My', 'favorite', 'programming', 'language', 'is', 'Python34', '5678', '9101'], ['programmming'], ['My', 'favorite', 'prolanguPythonagegramminlg', 'language', 'is', 'Python'], ['te'], ['fvorrrite'], ['string1,', '', '', '', '', 'string2,', '', '', '', '', '', '', 'sstring3'], ['1234', '5678', '', '9101'], ['556is78'], ['My', 'favorite', 'prol', 'anguPythonagegramminlg', 'lanage', 'is', 'Python'], ['vksoeiMq'], ['12My', 'favorite', 'programming', 'language', 'is', 'Python34', '5678string2,'], ['5striing1,My', 'favorite', 'proMye', 'ythonpstringg2,strin3'], ['1234', '5678', '91string1,sPython342,string301'], ['fvorofrite'], ['fvorrreite'], ['favoritprogrammming'], ['Python34'], ['556iss78'], ['peMsMC'], ['ffvorrreite'], ['5striing1,My', 'favorite', 'proMylanguagee', 'ythonpstringg2,strin3'], ['556iss788'], ['spythonring2'], ['string3'], ['Pstring3ython'], ['My', 'favorit5678e', 'prol', 'anguPythonagegramminlg', 'lanage', 'is', 'Pgython'], ['12334', '5678', '', '9101'], ['prol'], ['langua', 'g5678e', '', 'ng', '', '', '', ''], ['rfvorrrite'], ['PlanguPythonage'], ['123My', 'favorite', 'prolanguPythonagegramminlg', 'language', 'is', 'Python4', '5678', '9101'], ['12', '334', '5678', '', '9101'], ['fvorofritre'], ['192314'], ['string1,', '', '', '', '', 'st', 'ring2,,', '', '', '', '', '', '', 'string3'], ['lanage'], ['gprolanguPythonagegramminlgvZ12n'], ['fvoorrite'], ['st'], ['anguPythonagegramminlg'], ['12My', 'favorite', 'programming', 'glanguage', 'is', 'Python34', '5678string2,'], ['12python3My'], ['languPythonage', '', 'ngn', '', '', '', ''], ['gg5678e'], ['rfvorrtristring1,', '', '', '', '', 'st', 'ring2,,', '', '', '', '', '', '', 'string3te'], ['languag5678e'], ['string1,', '', '', '', '', 'st', 'ring2,languag5678e', '', 'ng', '', '', '', '', '', 'string3'], ['5stprogriing1,stiringg2,strin3'], ['My', 'favorite', 'programming', 'language', 'is', 'PytlanguPythonagehon'], ['programmmipng'], ['flvorofrite'], ['tt'], ['1212314M3y'], ['pronggrrammin12314g'], ['string1,', '', '', '', '', 'st', 'ring2,,', '', '', '', '', '', '', '', 'string3'], ['123My', 'favorite', 'prolanguPythonagegramminlg', 'language', 'is', 'Pythstring1,', '', '', '', '', 'string2,', '', '', '', '', '', '', 'string3on4', '5678', '9101'], ['fvsstring3e'], ['Pst3ring3ython'], ['string1,', '', '', '', '', 'st', 'ring2,languag5678e', '', 'ng', '', '', '', '', '', 'string'], ['lan12334', '5678', '', '9101gua', 'g5678e', '', 'ng', '', '', '', ''], ['faorite'], ['91nstring1,string2,string301'], ['prrfvorrtristring1,', '', '', '', '', 'st', 'ring2,,', '', '', '', '', '', '', 'string3teol'], ['556667string1,string2,string3']]

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
        func_name = "string_to_list"
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
        for test_case in ['assert string_to_list("python programming")==[\'python\',\'programming\']', 'assert string_to_list("lists tuples strings")==[\'lists\',\'tuples\',\'strings\']', 'assert string_to_list("write a program")==[\'write\',\'a\',\'program\']']:
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
