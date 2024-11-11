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
inputs = [['abcdef'], ['python'], ['data'], ['lambs'], [''], ['abcdefghijklmnopqrstuvwxyz'], ['bbbbbbbb'], ['abcdijklmnopqrstuvwxyz'], ['ZD'], ['ZZD'], ['abcdefghiZDjklmnopqrstuvwxyz'], ['babcdefghijklmnopqrstuvwxyzbbbbbbb'], ['bbbbbbbbb'], ['abcdefghbbbbbbbbbijklabcdijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklabcdijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdijkljmnopqrstuvwxyz'], ['bbbbbbbbbZZD'], ['abcdlefghijklmnopqrstuvwxyz'], ['abcdlmnopqrstuvwxyz'], ['babcdefghijklmnopqrstuvwxyzbbbbbbbb'], ['bbbbbbbbbbb'], ['abcdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdefghijkqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklabcdijklmnopqrbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqrstuvwxyz'], ['ZDZD'], ['DAxuCd'], ['abicdijklmnopqrstuvwxyz'], ['ababcdefghiZDjklmnopqrstuvwxyzcdefghbbbbbbbbbijklabcdijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdefghiZDjkelmnopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqrstuvwxyz'], ['abicdijklmnopqrwstuvwxyz'], ['babcdefghijklmnopqrsabcdlefghijklmnopqrstuvwxyz'], ['bbbb'], ['bbbbbbbabcdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyzbbZZD'], ['zz'], ['abcdefghijkqrstuvwxwyz'], ['ZDDZD'], ['xy'], ['abcdefghijkqrstuvwxyzbabcdefghijklmnopqrsabcdlefghijklmnopqrstuvwxyz'], ['abcdefghiZDjokelmnopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopyzmnopqrstuvwxy'], ['abcdlmnwxyz'], ['abcdlefghijklmnabcdefghijkqrstuvwxwyzopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklazbbbbbbbstuvwxyzmnopqrstuvwxyz'], ['xabcdijklmnopqrstuvwxmyz'], ['abcdefghabcdefghijkqrstuvwxyzbbbbbbbbbijpklabcdijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklabcdijklmnopqrstuvwxyzmnoZDpqrstuvwxyz'], ['ababcdefghbbbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopyzmnopqrstuvwxycdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqruvwxyz'], ['babcdbefghijklmnopqrszztuvwxyzbbbbbbbb'], ['abcdefghbbbbbbbbbiojpklabcdijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['abcdefghbbbbbbbbbijpkbabcdefghijklmnopqrstuvwxyzbbbbbbbblabcdijklmnopqbabcdbefghijklmnopqrszztuvwxyzbbbbbbbbrstuvwxyzmnopqrstuvwxyz'], ['zabicdijklmnopqrstuvwxyz'], ['bbbbbbbabcdbefghijklmnopqrszztuvwxyzbbbbbbbb'], ['babcdefghijklmnopqrstuabicdijklmnopqrstuvwxyzzbbbbbbb'], ['abcdefghbbbbbbbbbiqrabcdefghijklmnopqrstuvwxyzwxyz'], ['ababcdefghbubbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopyzmnopqrstuvwxycdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['babcdefbabcdefghijklmnopqrsabcdlefghijklmnopqrstuvwxyzghijklmnopqrstuvwuxyzbbbbbbbb'], ['bbababcdefghiZDjklmnopqrstuvwxyzcdefghbbbbbbbbbijklabcdijklmnopqrstuvwxyzmnopqrstuvwxyzbbbbbb'], ['ababcdeffghbubbbbbbbbijpklabbcdwijklmnopqrbabcdefghijklmnopyzmnopqrstuvwxycdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['babcdefghijklmnopqrstuvbbababcdefghiZDjklmnopqrstuvwxyzcdefghbbbbbbbbbijklabcdijklmnopqrstuvwxyzmnopqrstuvwxyzbbbbbbbbb'], ['abcdefghbbbbbbbbbijpklabbcdijklmnopqrbbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqruvwxyz'], ['abcdefghiZDjklmnopqrstuvabcdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyzwxyz'], ['abcdefghbbbbbbbbbijpklabcdijklmnopqrstuvwxyzmnoZDpqrstuvwxy'], ['abcdefghbbbbbbbbbijpkuvwxyz'], ['abcdefghiZDjklmnvopqrstuvabcdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyzwxyz'], ['ZZZD'], ['bbababcdefghiZDjklmnopqrstuvwxyzcdefghbbbbbbbbbijklabcdijklmnopqrstuvwxyzmnopqrstuvwxyzbbbbb'], ['zabicdijklmnopqrjstuvwxyz'], ['abcdefghbbbbbbbbbijpklabcdijkzmnoZDpqrstuvwxyz'], ['abcdlefghijklmnabcdefghijkqrstustuvwxyz'], ['abicdijklmnopqrstbabcdefghijklmnopqrstuvwxyzbbbbbbbbuvwxyz'], ['aibcdlefghijklabcdefghbbbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopyzmnopqrstuvwxymnopqrstuvwxyz'], ['abcdefghbbpbbbbbbbiojpklabcdijklmnopqrstuvwxyzmnopqrstuvwxyz'], ['bbababcdefghiZDjklmnopqrstuvwxyzcdefghbbbbbbbbbijklabcdijklmnopqrstuvwxy'], ['zabicdipqrstuvwxyz'], ['bbbbbbbabcdefghbbbbbbbbbijklabcbdmijklmnopqrstuvwxyzmnopqrstuvwxyzbbZZD'], ['babcdefghijklmnopqrsabcdmnopqrstuvwxyz'], ['abcdefghabcdefghijkqrstuvwxyzbbbbbbbbbijpklabcdijklmnopwqrstuvwxyzmnopqrstuvwxyz'], ['abicdijklmnabcdlefghijklmnabcdefghibjkqrstustuvwxyzopqrwstuvwxyz'], ['abicdipqrwstuvwxayz'], ['abcdefghbbbbbbbbbiqrabcdefghijklmnbopqrstuvwxyzwxyz'], ['abcdijklmnopqrstababcdefghiZDjklmnopqrstuvwxyzcdefghbbbbbbbbbbijklabcdijklmnopyqrstuvwxyzmnopqrstuvwxyzuvwxyz'], ['ZabcdefghbbbbbbbbbijpklabcdijklmnopqrbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqrstuvwxyzDZD'], ['bbbbbbbbbbbbbbbbbbb'], ['abcdefghijkrstuvwxwyz'], ['bbbDAxuCdbbbbbbZZD'], ['abicbabcdefghijklmnopqrstuvbbababcdefghiZDjklmnqrwstuvwxayz'], ['ZZDD'], ['abicdijklmnabcdlefghijklmjnabcdefghibjkqrstustuvwxyzopqrwstuvwxyz'], ['babcdefghijklmnopqrsabcdlefghijkmlmnopqrstuvwxyz'], ['uI'], ['zabicdipqabicdijklmnotuvwxyzrstuvwxyz'], ['jabcdefghbbbbbbbbbijpkuvwxyzZZZD'], ['abcdefghiZDjklmnopqrstuqvwxyz'], ['abicdijklmnabcdlefghijklmnabcdefghibjkqrvwxyzopqrwstuvwxyz'], ['babcdbefghijklmnopqrszztuvwxyzkbbbbbbbb'], ['abcdefghiZDjklmnopqrstuvabcdefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyizwxyz'], ['abcdefghbbbbbbbbbiqrabcdefghijklmnopqrabcdefghabcdefghijkqrstuvwxyzbbbbbbbbbijpklabcdijklmnopwqrstuvwxyzmnopqrstuvwxyzstuvwxyzwxyz'], ['aibcdlefghijklabcdefghbbbbbbbabcdefghbbbbbbbbbijpklabbcdijklmnopqrbbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqruvwxyzbbijpklabbcdijklmnopqrbabcdefghijklmnopyzmnopqrstuvwxymnopqrstuvwxyz'], ['babcdefghijklmnopqdrstuvwxyzbbbbbbb'], ['ZabcdefghbbxybbbbbbbijpkltabcdijklmnopqrbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqrstuvwxyzDZD'], ['babcdefbabcdefghijklmnopqrsabcdlefghijklmnopqrstuvwxyzlghijklmnopqrstuvwuxyzbbbbbbbb'], ['abcdefghiZDjklmnopqrstuvabcdabcdefghbbbbbbbbbijpklabbcdijklmnopqrbabcdefghijklmnopqrstuvwxyzbbbbbbbstuvwxyzmnopqruvwxyzefghbbbbbbbbbijklabcdmijklmnopqrstuvwxyzmnopqrstuvwxyizwxyz'], ['aZDbcdefghijkqrstuvwxyz'], ['abcdefghbbbbbbebbbijklabcdijklmnopqrstuvwxzabicdijklmnopqrstuvwxyzyzmnopqrstuvwxyz'], ['abcadijklmnopqrstuvwxyz']]
results = ['ace', 'pto', 'dt', 'lms', '', 'acegikmoqsuwy', 'bbbb', 'acikmoqsuwy', 'Z', 'ZD', 'acegiDkmoqsuwy', 'bbdfhjlnprtvxzbbb', 'bbbbb', 'acegbbbbbjlbdjlnprtvxznprtvxz', 'acegbbbbbjkacikmoqsuwymoqsuwy', 'acikjnprtvxz', 'bbbbbZ', 'aclfhjlnprtvxz', 'aclnprtvxz', 'bbdfhjlnprtvxzbbbb', 'bbbbbb', 'acegbbbbbjlbdikmoqsuwymoqsuwy', 'acegikrtvxz', 'acegbbbbbjkacikmoqbbdfhjlnprtvxzbbbsuwymoqsuwy', 'ZZ', 'DxC', 'aidjlnprtvxz', 'aacegiDkmoqsuwycegbbbbbjlbdjlnprtvxznprtvxz', 'acegiDklnprtvxz', 'acegbbbbbjkabdjlnpracegikmoqsuwybbbbtvxznprtvxz', 'aidjlnprsuwy', 'bbdfhjlnpraclfhjlnprtvxz', 'bb', 'bbbbbdfhbbbbikacmjlnprtvxznprtvxzbZ', 'z', 'acegikrtvxy', 'ZDD', 'x', 'acegikrtvxzacegikmoqsbdegikmoqsuwy', 'acegiDoemoqsuwy', 'acegbbbbbjkabdjlnpracegikmoymoqsuwy', 'aclnxz', 'aclfhjlnbdfhjqsuwwzprtvxz', 'acegbbbbbjkabbbbtvxznprtvxz', 'xbdjlnprtvxy', 'acegacegikrtvxzbbbbiplbdjlnprtvxznprtvxz', 'acegbbbbbjkacikmoqsuwymoDqsuwy', 'aacegbbbbbjkabdjlnpracegikmoymoqsuwydfhbbbbikacmjlnprtvxznprtvxz', 'acegbbbbbjkabdjlnpracegikmoqsuwybbbbtvxznprvxz', 'bbdegikmoqszuwybbbb', 'acegbbbbboplbdjlnprtvxznprtvxz', 'acegbbbbbjkacegikmoqsuwybbbblbdjlnpbbdegikmoqszuwybbbbrtvxznprtvxz', 'zbcikmoqsuwy', 'bbbbbdegikmoqszuwybbbb', 'bbdfhjlnprtaidjlnprtvxzbbbb', 'acegbbbbbqacegikmoqsuwywy', 'aacegbbbbbiplbcikmoqbbdfhjlnpznprtvxcegbbbbbjlbdikmoqsuwymoqsuwy', 'bbdfacegikmoqsbdegikmoqsuwygikmoqsuwxzbbbb', 'baacegiDkmoqsuwycegbbbbbjlbdjlnprtvxznprtvxzbbb', 'aacefhubbbbjkabdikmoqbbdfhjlnpznprtvxcegbbbbbjlbdikmoqsuwymoqsuwy', 'bbdfhjlnprtvbbbdfhZjlnprtvxzdfhbbbbikacikmoqsuwymoqsuwybbbbb', 'acegbbbbbjkabdjlnprbbdfhjlnprtvxzbbbsuwymoquwy', 'acegiDkmoqsuacegbbbbbjlbdikmoqsuwymoqsuwywy', 'acegbbbbbjkacikmoqsuwymoDqsuwy', 'acegbbbbbjkvxz', 'acegiDkmvprtvbdfhbbbbikacmjlnprtvxznprtvxzxz', 'ZZ', 'baacegiDkmoqsuwycegbbbbbjlbdjlnprtvxznprtvxzbb', 'zbcikmoqjtvxz', 'acegbbbbbjkacikmoDqsuwy', 'aclfhjlnbdfhjqsutvxz', 'aidjlnprtacegikmoqsuwybbbbuwy', 'abdegikacegbbbbbjkabdjlnpracegikmoymoqsuwynprtvxz', 'acegbpbbbijkacikmoqsuwymoqsuwy', 'baacegiDkmoqsuwycegbbbbbjlbdjlnprtvx', 'zbciqsuwy', 'bbbbbdfhbbbbikacdikmoqsuwymoqsuwybZD', 'bbdfhjlnpracmoqsuwy', 'acegacegikrtvxzbbbbiplbdjlnpqsuwymoqsuwy', 'aidjlnbdegikmacegijqsutvxzprsuwy', 'aidprsuwaz', 'acegbbbbbqacegikmbprtvxzxz', 'acikmoqsaacegiDkmoqsuwycegbbbbbikacikmoyrtvxznprtvxzvxz', 'ZbdfhbbbbiplbdjlnpracegikmoqsuwybbbbtvxznprtvxzZ', 'bbbbbbbbbb', 'acegiksuwwz', 'bbAudbbbZ', 'aibbdfhjlnprtvbbbdfhZjlnrsuwaz', 'ZD', 'aidjlnbdegikmnbdfhbkrtsuwyoqwtvxz', 'bbdfhjlnpraclfhjmmoqsuwy', 'u', 'zbciqbcikmouwyrtvxz', 'jbdfhbbbbipuwyZZ', 'acegiDkmoqsuvxz', 'aidjlnbdegikmacegijqvxzprsuwy', 'bbdegikmoqszuwykbbbb', 'acegiDkmoqsuacegbbbbbjlbdikmoqsuwymoqsuwyzxz', 'acegbbbbbqacegikmoqacegacegikrtvxzbbbbiplbdjlnpqsuwymoqsuwysuwywy', 'abdegikacegbbbbbdfhbbbbiplbcikmoqbacegikmoqsuwybbbbtvxznprvxzbjkabdjlnpracegikmoymoqsuwynprtvxz', 'bbdfhjlnpdsuwybbbb', 'ZbdfhbybbbiplacikmoqbbdfhjlnprtvxzbbbsuwymoqsuwyDD', 'bbdfacegikmoqsbdegikmoqsuwylhjlnprtvuybbbb', 'acegiDkmoqsuacacegbbbbbjkabdjlnpracegikmoqsuwybbbbtvxznprvxzfhbbbbikacmjlnprtvxznprtvxiwy', 'aDcegikrtvxz', 'acegbbbebikacikmoqsuwzbcikmoqsuwyymoqsuwy', 'acdjlnprtvxz']

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
        func_name = "odd_values_string"
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
        for test_case in ["assert odd_values_string('abcdef') == 'ace'", "assert odd_values_string('python') == 'pto'", "assert odd_values_string('data') == 'dt'", "assert odd_values_string('lambs') == 'lms'"]:
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