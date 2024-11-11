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
inputs = [['My Name is Dawood'], ['I am a Programmer'], ['I love Coding'], [''], ['I love Coding     '], ['My Name is Dawood     '], ['I am a Programmer     '], ['     '], ['I love\tCoding\n '], ['Hello\tWorld\n'], ['This is a test\tfor\tmultiple\nspaces.'], ['One space\tbetween each\tword.'], ['Multiple spaces\tat the\tend.'], ['Test\tfor\ttabs\tand\tspaces.'], ['No spaces\tin\tthis\tinput.'], ['A mix of\tspaces,\ttabs,\nand\nnewlines.'], ['   I love Coding   '], ['Hello    World'], ['   H@llo     W0r!d   '], ['Hello         World'], ['word.'], ['I love\tCAoding\n '], ['A mix of\tspaces,\ttabs,\nand\nnewlineWorld.'], ['One'], ['wordmultiple.'], ['I love\tCoOne space\tbetween each\tword.ding\n '], ['Multiple'], ['    Multiple  '], ['This'], ['I love oCoding     '], ['I log\nTest'], ['No spaces\tin\tthis\tinputis.'], ['   I log   '], ['tehe'], ['Name'], ['Hello    WorlMy Name is Dawood     d'], ['I love oCodi  '], ['word.ding'], ['am'], ['I love oCodi  s'], ['teh     e'], ['Test'], ['tabs'], ['A mix of\tspaces,s\ttabs,\nand\nnewlines.'], ['Hello'], ['Hello    Wo'], [' H  H@llo     W0r!d   '], ['between'], ['Wo'], ['MultiNo spaces\tin\tthis\tinputis.ple spaces\tat the\tend.'], ['My Naawood     '], ['MultiN\to spaces\tin\tthis\tinputis.ple spaces\tat the\tend.'], ['spaces.'], ['woinputis.rd.'], ['HelOnelo    World'], ['No spaces\t in\tthis\tinput.'], ['Coding'], ['My Nameinputis.wood     '], ['HelOnetabs   World'], ['teforhe'], ['A mix of\tspaces,\ttabs,\nand\nnDawoodewlines.'], ['   H@llo     W0r!dI love oCodi  s    '], ['tehhe'], ['A mix of\tspaces,sd\ttabs,\nand\nnewlines.'], ['Multiptle spaces\tt the\tend.'], ['MultiNN'], ['MultiN'], ['A mix of\tspaces,\ttabs,\nandam\nnDawoodewlines.'], ['Hello    I love oCoding     WorlMy Name is Dawood     d'], ['aat'], ['tehheWorld'], ['A mix of\tspaces,\tbMultiptle spaces\tt the\tend.tabs,\nand\nnDawoodewlines.'], ['A mix of\tspaced\nnewlineWorld.'], ['teheTest\tfor\ttabs\tand\tspaces.he'], ['spaces,s'], ['in.putis.'], ['newlineWorld.'], ['A mix nes.'], ['   H@llo  @   W0r!dI love oCodi  s    '], ['I love C oding     '], ['I lovding\n '], ['tetehhhe'], ['end.'], ['My'], ['sTest'], ['ses'], ['teforhee'], ['HelOOnelo'], ['A mix of\tspaces,\ttabs,\nand\nnDawoodewelinesnewlines..'], ['A mix of\tspaces,\ttabs,\nand\nnDawoodewelinesnewolines..'], ['oI love\tCoding\n '], ['odig'], ['WHello    Wo'], ['Codding'], ['My Nameinputis.d     '], ['love'], ['I love MultiNo '], ['Hello\tWo\nrld\n'], ['A s,s\ttabs,\nand\nnewlines.'], ['Nameinputis.wood'], ['I love oCoding bMultiptle I love\tCAoding\n  end.tabs, '], ['teefrhe'], ['No spaces\tin\tthis\tispaces,nput.'], ['tetethhhe'], ['word.diNong'], ['W0r!dI'], ['A mix of\tspaces,sd\ttabs,\nand\ntetethhhenewlines.'], ['MultiN\to spaces\tin\tthis\tinputis.    Multiple  ple spaces\tat the\tend.'], ['A mix of\tspaces,s\ttabs,\nands\nnewlines.'], ['eThis'], ['I love MultiNoCodingo '], ['Hello\tWold\n'], ['My Nameinputis.wood     aat'], ['Hello    A mix of\tspaces,\ttabs,\nandam\nnDawoodewlines.Wo'], ['I lovMe MultiNo '], ['A s,s\ttabas,\nand\nnewlines.'], ['A mix of\tspaces,s\ttaabs,\nand\nnewlines.'], ['tetethhhenewlines.'], ['this'], ['No spaces\tinh\tthis\tinput.']]
results = ['My%20Name%20is%20Dawood', 'I%20am%20a%20Programmer', 'I%20love%20Coding', '', 'I%20love%20Coding%20%20%20%20%20', 'My%20Name%20is%20Dawood%20%20%20%20%20', 'I%20am%20a%20Programmer%20%20%20%20%20', '%20%20%20%20%20', 'I%20love\tCoding\n%20', 'Hello\tWorld\n', 'This%20is%20a%20test\tfor\tmultiple\nspaces.', 'One%20space\tbetween%20each\tword.', 'Multiple%20spaces\tat%20the\tend.', 'Test\tfor\ttabs\tand\tspaces.', 'No%20spaces\tin\tthis\tinput.', 'A%20mix%20of\tspaces,\ttabs,\nand\nnewlines.', '%20%20%20I%20love%20Coding%20%20%20', 'Hello%20%20%20%20World', '%20%20%20H@llo%20%20%20%20%20W0r!d%20%20%20', 'Hello%20%20%20%20%20%20%20%20%20World', 'word.', 'I%20love\tCAoding\n%20', 'A%20mix%20of\tspaces,\ttabs,\nand\nnewlineWorld.', 'One', 'wordmultiple.', 'I%20love\tCoOne%20space\tbetween%20each\tword.ding\n%20', 'Multiple', '%20%20%20%20Multiple%20%20', 'This', 'I%20love%20oCoding%20%20%20%20%20', 'I%20log\nTest', 'No%20spaces\tin\tthis\tinputis.', '%20%20%20I%20log%20%20%20', 'tehe', 'Name', 'Hello%20%20%20%20WorlMy%20Name%20is%20Dawood%20%20%20%20%20d', 'I%20love%20oCodi%20%20', 'word.ding', 'am', 'I%20love%20oCodi%20%20s', 'teh%20%20%20%20%20e', 'Test', 'tabs', 'A%20mix%20of\tspaces,s\ttabs,\nand\nnewlines.', 'Hello', 'Hello%20%20%20%20Wo', '%20H%20%20H@llo%20%20%20%20%20W0r!d%20%20%20', 'between', 'Wo', 'MultiNo%20spaces\tin\tthis\tinputis.ple%20spaces\tat%20the\tend.', 'My%20Naawood%20%20%20%20%20', 'MultiN\to%20spaces\tin\tthis\tinputis.ple%20spaces\tat%20the\tend.', 'spaces.', 'woinputis.rd.', 'HelOnelo%20%20%20%20World', 'No%20spaces\t%20in\tthis\tinput.', 'Coding', 'My%20Nameinputis.wood%20%20%20%20%20', 'HelOnetabs%20%20%20World', 'teforhe', 'A%20mix%20of\tspaces,\ttabs,\nand\nnDawoodewlines.', '%20%20%20H@llo%20%20%20%20%20W0r!dI%20love%20oCodi%20%20s%20%20%20%20', 'tehhe', 'A%20mix%20of\tspaces,sd\ttabs,\nand\nnewlines.', 'Multiptle%20spaces\tt%20the\tend.', 'MultiNN', 'MultiN', 'A%20mix%20of\tspaces,\ttabs,\nandam\nnDawoodewlines.', 'Hello%20%20%20%20I%20love%20oCoding%20%20%20%20%20WorlMy%20Name%20is%20Dawood%20%20%20%20%20d', 'aat', 'tehheWorld', 'A%20mix%20of\tspaces,\tbMultiptle%20spaces\tt%20the\tend.tabs,\nand\nnDawoodewlines.', 'A%20mix%20of\tspaced\nnewlineWorld.', 'teheTest\tfor\ttabs\tand\tspaces.he', 'spaces,s', 'in.putis.', 'newlineWorld.', 'A%20mix%20nes.', '%20%20%20H@llo%20%20@%20%20%20W0r!dI%20love%20oCodi%20%20s%20%20%20%20', 'I%20love%20C%20oding%20%20%20%20%20', 'I%20lovding\n%20', 'tetehhhe', 'end.', 'My', 'sTest', 'ses', 'teforhee', 'HelOOnelo', 'A%20mix%20of\tspaces,\ttabs,\nand\nnDawoodewelinesnewlines..', 'A%20mix%20of\tspaces,\ttabs,\nand\nnDawoodewelinesnewolines..', 'oI%20love\tCoding\n%20', 'odig', 'WHello%20%20%20%20Wo', 'Codding', 'My%20Nameinputis.d%20%20%20%20%20', 'love', 'I%20love%20MultiNo%20', 'Hello\tWo\nrld\n', 'A%20s,s\ttabs,\nand\nnewlines.', 'Nameinputis.wood', 'I%20love%20oCoding%20bMultiptle%20I%20love\tCAoding\n%20%20end.tabs,%20', 'teefrhe', 'No%20spaces\tin\tthis\tispaces,nput.', 'tetethhhe', 'word.diNong', 'W0r!dI', 'A%20mix%20of\tspaces,sd\ttabs,\nand\ntetethhhenewlines.', 'MultiN\to%20spaces\tin\tthis\tinputis.%20%20%20%20Multiple%20%20ple%20spaces\tat%20the\tend.', 'A%20mix%20of\tspaces,s\ttabs,\nands\nnewlines.', 'eThis', 'I%20love%20MultiNoCodingo%20', 'Hello\tWold\n', 'My%20Nameinputis.wood%20%20%20%20%20aat', 'Hello%20%20%20%20A%20mix%20of\tspaces,\ttabs,\nandam\nnDawoodewlines.Wo', 'I%20lovMe%20MultiNo%20', 'A%20s,s\ttabas,\nand\nnewlines.', 'A%20mix%20of\tspaces,s\ttaabs,\nand\nnewlines.', 'tetethhhenewlines.', 'this', 'No%20spaces\tinh\tthis\tinput.']

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
        for test_case in ['assert replace_spaces("My Name is Dawood") == \'My%20Name%20is%20Dawood\'', 'assert replace_spaces("I am a Programmer") == \'I%20am%20a%20Programmer\'', 'assert replace_spaces("I love Coding") == \'I%20love%20Coding\'']:
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
