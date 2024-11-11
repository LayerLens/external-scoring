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
inputs = [['python'], ['program'], ['language'], [''], ['Hello, world!'], ['acegikmoqsuwy'], ['world!'], ['Hello,'], ['e,Hello,'], ['e,He'], ['e,Hellol,'], ['e,Held!'], ['e,Hello,Hello, world!'], ['e,'], ['e,Hdeld!'], ['Hewllo, world!'], ['e,,'], ['Hee,Held!llo,'], ['Hello,e,Held!'], ['e,Hel'], ['e,HelHello,'], ['wor!ld!'], ['acegiHello,e,Held!kmoqsuwy'], ['e,Hell,'], ['Hello,orld!'], ['eHello, world!,,'], ['Hewllo, lworld!'], ['lworld!'], ['e,Hello,Hee,Held!world!'], ['lworld!e,Hello,Hee,Held!world!'], ['world!,,'], ['eHello, worlld!,,'], ['wore,Hee,Helle,Hdeld!o,Hee,Held!world!l!,,'], ['wore,Hee,Hellelworld!,Hdeld!o,Hee,Held!world!l!,,'], ['eHello, world!,e,,'], ['eHello,'], ['Hello,ore,Hdeld!'], ['e,HdeldHello,orld!!'], ['Hello,ore,Hdel!'], ['Hewllo,'], ['aceHello,ore,HdelHello,ore,Hdeld!d!Hello,e,Held!kmoqsuwy'], ['acegiHello,Hewllo, world!e,Held!kHello,ore,Hdel!suwy'], ['eeHello,'], ['RrjlJwpJaM'], ['e,Held!e,Hell,'], ['e,Hddeld!'], ['HewllHo,e,Held! lworld!'], ['Hello, wHello, world!ld!'], ['e,eHello, world!,,Held!e,Hell,'], ['eHe'], ['HewllHo,e,Held!'], ['He,ore,Hdel!'], ['eeeHello, world!,e,,Hello,'], ['e,eHHello, wHello, world!ld!ello, world!,,Held!e,Hell,'], ['eeHelolo,'], ['e,HdeldHell!!'], ['e!,Hdeld!'], ['wore,Hee,Helle,Hdeld!o,Hee,Held!world!l!,,lworld!'], ['e,eld!e,Hell,'], ['wore,Hee,Helle,Hdeld!eeeHello,o,Hee,Held!world!l!,,lworld!'], ['lwHello,orld!orld!'], ['HewllHo,e,Held! lw!orld!'], ['Hewllo, worl'], ['e,He,ld!e,Hell,'], ['eeHello, worlld!,,,Hell,'], ['lorld!'], ['e,,,'], ['lwlHello,orld!orld!'], ['e,Hee,ld!e,Hee,Hello,Hee,Held!world!ll,e,eHello, world!,,Held!e,Hell,'], ['eeeHello,'], ['aworlld!,,,Hell,cegikmoqsuwy'], ['e,Heee,ld!e,Hee,Hello,Hee,Held!world!ll,e,eHello, world!,,Held!e,Hell,'], ['wore,Hee,Hellelworld!,Hdeld!o,H!ee,Held!world!l!,,'], ['loe,Hello,Hello,rld!'], ['wolrld!,,Held!e,Hell,'], ['world!,e,,Hello,'], ['wore,Hee,HHellelworld!,He,HdeldHello,orld!!deld!o,H!ee,Held!world!l!,,'], ['e,Hel!'], ['Hello,ore,world!,,Hdel!'], ['acegikmoqsuwore,Hee,Helle,Hdeld!o,Hee,Held!world!l!,,'], ['eHello,Hee,Held!llo,'], ['e,,,Hewllo, worl'], ['e,Heee,ld!e,Hee,Hello,H,ee!world!ll,e,!eHello,'], ['e,Hreee,ld!e,Hee,Hello,Hee,Held!world!ll,e,eHello, world!,,Held!e,Hell,'], ['He wllHo, world!'], ['wllHo,'], ['eHello,Heo,'], ['e,Hee,ld!e,Hee,Hello,Hee,Held!world!ll,e,eHello,'], ['e,HHddeld!'], ['e,,eHe'], ['lwHello,orlHee,Held!llo,d!orld!'], ['Hello, wHello, world!Hewllo, worlld!'], [',e,,'], ['ld!'], ['e,Hreee,ld!e,Hee,Hello,Hee,Held!world!ll,e,eHello,'], ['mvWHEUyrs'], ['lwHello,orlHee,Held!llo,d!olw!orld!rld!'], ['wore,Hee,Helworld!le,Hdeld!o,Hee,Held!world!l!,,lworld!'], ['nhh'], ['e,Hreee,ld!e,HeeHee,Held!llo,,Hello,Hee,Held!world!ll,e,eHello,'], ['wore,Hee,HHellelworld!,He,HdeldHello,orld!!deld!o,H!ee,Held!world!l!,world!ld!ello,'], ['ee,eHHaworlld!,,,Hell,cegikmoqsuwyello, wHello, orld!ld!ello, worlmd!,,Held!e,Hell,elle!!'], ['worlld!,,'], [',,e,,'], ['e,He,ld!e,Hee,Heee,ld!e,Hee,Hello,Hee,Held!world!ll,e,eHello, world!,,Held!e,Hell,l,'], ['e,HeHl']]
results = ['yhn', 'rga', 'agae', '', 'el,wrd', 'cgkosw', 'ol!', 'el,', ',el,', ',e', ',ell', ',ed', ',el,el,wrd', ',', ',dl!', 'elo ol!', ',', 'e,edlo', 'el,,ed', ',e', ',eHlo', 'o!d', 'cgHloeHl!mquy', ',el', 'el,rd', 'Hlo ol!,', 'elo wrd', 'wrd', ',el,e,edwrd', 'wrdeHloHeHl!ol!', 'ol!,', 'Hlo old,', 'oeHeHleHedoHeHl!ol!!,', 'oeHeHlewrd,dl!,e,edwrdl,', 'Hlo ol!e,', 'Hlo', 'el,r,dl!', ',dlHlool!', 'el,r,dl', 'elo', 'cHlooeHeHlooeHeddHloeHl!mquy', 'cgHloHwl,wrdeHl!HlooeHe!uy', 'eel,', 'rlwJM', ',edeHl,', ',ded', 'elH,,ed wrd', 'el,wel,wrdl!', ',Hlo ol!,edeHl,', 'H', 'elH,,ed', 'eoeHe!', 'eHlo ol!e,el,', ',Hel,wel,wrdl!lo ol!,edeHl,', 'eeoo', ',dlHl!', '!Hed', 'oeHeHleHedoHeHl!ol!!,wrd', ',l!,el', 'oeHeHleHedeeel,,e,edwrdl,lol!', 'wel,rdol!', 'elH,,ed wol!', 'elo ol', ',el!,el', 'eel,wrl!,Hl,', 'ol!', ',,', 'wHlool!rd', ',e,deHeHloHeHl!ol!leeel,wrd,Hl!,el', 'eHlo', 'wrl!,Hl,eimquy', ',eel!,e,el,e,edwrdl,,Hlo ol!,edeHl,', 'oeHeHlewrd,dl!,!eHl!ol!!,', 'o,el,el,l!', 'ord,Hl!,el', 'ol!e,el,', 'oeHeHellol!H,dlHlool!dl!,!eHl!ol!!,', ',e!', 'el,r,ol!,dl', 'cgkoswr,e,el,dl!,e,edwrdl,', 'HloHeHl!l,', ',,elo ol', ',eel!,e,el,,ewrdl,,eel,', ',re,deHeHloHeHl!ol!leeel,wrd,Hl!,el', 'ewlo ol!', 'lH,', 'HloHo', ',e,deHeHloHeHl!ol!leeel,', ',Hdl!', ',ee', 'wel,rHeHl!l,!rd', 'el,wel,wrdHwl,wrl!', 'e,', 'd', ',re,deHeHloHeHl!ol!leeel,', 'vHUr', 'wel,rHeHl!l,!l!rdrd', 'oeHeHlol!eHedoHeHl!ol!!,wrd', 'h', ',re,deHee,edlo,el,e,edwrdl,,Hlo', 'oeHeHellol!H,dlHlool!dl!,!eHl!ol!!wrdl!lo', 'eeHwrl!,Hl,eimquylo Hlo rdl!lo old,Hl!,elel!', 'old,', ',,', ',el!,e,eel!,e,el,e,edwrdl,,Hlo ol!,edeHl,,', ',el']

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
        func_name = "remove_odd"
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
        for test_case in ['assert remove_odd("python")==("yhn")', 'assert remove_odd("program")==("rga")', 'assert remove_odd("language")==("agae")']:
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
