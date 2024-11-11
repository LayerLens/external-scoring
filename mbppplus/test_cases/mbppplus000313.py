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
inputs = [['Python language, Programming language.'], ['a b c,d e f'], ['ram reshma,ram rahim'], ['1,2 3,4 5.6'], ['This is a sentence with multiple spaces. It also has multiple commas, and some dots.'], ['1.2.3.4,5,6,7 8,9.10 11.12'], ['First line. Second line, with a comma and a dot. Third line with only spaces.'], ['   This     is   a  sentence     with      random    spaces.    '], ['Hello...world.....testing,,123'], ['.....,.. .,. ...'], ['1,,,,,,23...456,,,,78......9,,,,0'], ['Python language.....Programming language...'], [''], ['First line... Second line,,, with a comma and a dot....'], ['No special characters here'], ['dot.'], ['multiple'], ['1,,,,,,23...456,,,,78.......9,,,,0'], ['Second'], ['.....,...'], ['First line. Second line, with a comma and a dot. 1,2 3,4 5.6 only spaces.'], ['It'], ['aprKPinjxV'], ['line,,,'], ['charactrers'], ['No spPythonecial characters here'], ['This'], ['SeThiscond'], ['chareactrers'], ['cond'], ['Selanguage.....ProgrammingThis.s....,..d'], ['is'], ['coond'], ['No spPytho1,,,,,,23...456,,,,P78.......9,,,,0necial characters here'], ['1.2.3.4,5,6,7 18,9.10 11.12'], ['special'], ['dcoond'], ['   Thsis     is   a    '], ['First line... Second line,,, with a comma and a dont....'], ['c'], ['First loine. Second line, with a comma and a dot. 1,2 3,4 5.6 only spaces.'], ['lin,e,'], ['coondFirst line. Second line, with a comma and a dot. 1,2 3,4 5.6 only spaces.'], ['dcodont....ond'], ['No'], ['comma'], ['1,2 4 5.6'], ['No spPythonecial charaFirst line... Second line,,, with a comma and a dot....cters here'], ['VWtW'], ['dot....'], ['No spPythonecial charachere'], ['1,2 3,5.6'], ['...'], ['Python languagoe.....Programmionlyng language...'], ['3,5.6'], ['No spPytho1,,,,,,23...456,,,,P78.......9,also,,,0necial characters here'], ['1,,,,,,23...456,,,,78....0'], ['5.6'], ['TThis'], ['3,545,6,7.6'], ['ionlys'], ['18,9.10'], ['33,545,6,7.6'], ['chVWtWareactrers'], ['Selanguage.....Progrdont....ammingThis.s....,..d'], ['has'], ['dcoondVWtW'], ['61,2 4 5.6'], ['haThis is a sentence with multiple spaces. It also has multiple commas, and some dots.s'], ['1.2.3.14,5,6,7 8,9.10 11.12'], ['1,2d'], ['651,2 4 5.6'], ['haThis'], ['and'], ['1line.2.3.14,5,6,7 8,9.10 11.12'], ['1,2 4.....,... 5.6'], ['1,,,,,,,78.......9,,,,0'], ['1,,,,,,23comma...456,,,,78.......9,,,,0'], ['nYdDDY'], ['TThichVWtWareactrerss'], ['ccommma'], ['language.....ProgrNo special characters hereamming'], ['First loine. Secondlanguage.....Programming line, with a comma an4 5.6 only spaces.'], ['dSecond'], ['1.2.3.4,5,6,87 18,9.10 11.12'], ['1,2 3,4,545,6,7.6 5.6'], ['3,56.6'], ['lin,1line.2.3.14,5,6,7,'], ['1,,,,,commas,,23...456,,,,78.......9,,,,0'], ['6ccommma51,2'], ['1line.2.3.14,5,6,7'], ['3,545'], ['1.2.3.4,15,6,7 8,9.10 11.12'], ['....'], ['VWWtW'], ['First line. Second line, with a comma and a dot. Third line with only   This     is   a  sentence     with      random    spaces.     spaces.'], ['dot....cters'], ['1.2   Thsis     is   a    .3.4,5,6,7'], ['1.line.2.3.14,5,6,7'], ['First line. Second line, with a comma and a dot. Third line with o is   a  sentence     with      random    spaces.     spaces.'], ['mcomma'], ['1,,,,,,,78.......9,,,,0This is a sentence with multiple spaces. It also has multiple commas, and some dots.'], ['1.2'], ['dots.'], ['Hello...world.....testin1,2 4.....,... 5.623'], ['SecondhaThidSeconds'], ['languagoe.....Programmionlyng'], ['Thi1,,,,,,,78.......9,,,,0This is a sentence with multiple spaces. It also has multiple commas, and some dots.s'], ['1,,,,,,,78.......9,,,,0This is a sentence with multihaThisple spaces. It also has multiple commas, and some dots.'], ['1.2.3.4,5,6,7 81.12'], ['55.6'], ['dScondecond'], ['1language.....Programming'], ['   This     is   a  sentence     with      randoms.    '], ['coma']]
results = ['Python:language::Programming:language:', 'a:b:c:d:e:f', 'ram:reshma:ram:rahim', '1:2:3:4:5:6', 'This:is:a:sentence:with:multiple:spaces::It:also:has:multiple:commas::and:some:dots:', '1:2:3:4:5:6:7:8:9:10:11:12', 'First:line::Second:line::with:a:comma:and:a:dot::Third:line:with:only:spaces:', ':::This:::::is:::a::sentence:::::with::::::random::::spaces:::::', 'Hello:::world:::::testing::123', '::::::::::::::::', '1::::::23:::456::::78::::::9::::0', 'Python:language:::::Programming:language:::', '', 'First:line::::Second:line::::with:a:comma:and:a:dot::::', 'No:special:characters:here', 'dot:', 'multiple', '1::::::23:::456::::78:::::::9::::0', 'Second', ':::::::::', 'First:line::Second:line::with:a:comma:and:a:dot::1:2:3:4:5:6:only:spaces:', 'It', 'aprKPinjxV', 'line:::', 'charactrers', 'No:spPythonecial:characters:here', 'This', 'SeThiscond', 'chareactrers', 'cond', 'Selanguage:::::ProgrammingThis:s:::::::d', 'is', 'coond', 'No:spPytho1::::::23:::456::::P78:::::::9::::0necial:characters:here', '1:2:3:4:5:6:7:18:9:10:11:12', 'special', 'dcoond', ':::Thsis:::::is:::a::::', 'First:line::::Second:line::::with:a:comma:and:a:dont::::', 'c', 'First:loine::Second:line::with:a:comma:and:a:dot::1:2:3:4:5:6:only:spaces:', 'lin:e:', 'coondFirst:line::Second:line::with:a:comma:and:a:dot::1:2:3:4:5:6:only:spaces:', 'dcodont::::ond', 'No', 'comma', '1:2:4:5:6', 'No:spPythonecial:charaFirst:line::::Second:line::::with:a:comma:and:a:dot::::cters:here', 'VWtW', 'dot::::', 'No:spPythonecial:charachere', '1:2:3:5:6', ':::', 'Python:languagoe:::::Programmionlyng:language:::', '3:5:6', 'No:spPytho1::::::23:::456::::P78:::::::9:also:::0necial:characters:here', '1::::::23:::456::::78::::0', '5:6', 'TThis', '3:545:6:7:6', 'ionlys', '18:9:10', '33:545:6:7:6', 'chVWtWareactrers', 'Selanguage:::::Progrdont::::ammingThis:s:::::::d', 'has', 'dcoondVWtW', '61:2:4:5:6', 'haThis:is:a:sentence:with:multiple:spaces::It:also:has:multiple:commas::and:some:dots:s', '1:2:3:14:5:6:7:8:9:10:11:12', '1:2d', '651:2:4:5:6', 'haThis', 'and', '1line:2:3:14:5:6:7:8:9:10:11:12', '1:2:4::::::::::5:6', '1:::::::78:::::::9::::0', '1::::::23comma:::456::::78:::::::9::::0', 'nYdDDY', 'TThichVWtWareactrerss', 'ccommma', 'language:::::ProgrNo:special:characters:hereamming', 'First:loine::Secondlanguage:::::Programming:line::with:a:comma:an4:5:6:only:spaces:', 'dSecond', '1:2:3:4:5:6:87:18:9:10:11:12', '1:2:3:4:545:6:7:6:5:6', '3:56:6', 'lin:1line:2:3:14:5:6:7:', '1:::::commas::23:::456::::78:::::::9::::0', '6ccommma51:2', '1line:2:3:14:5:6:7', '3:545', '1:2:3:4:15:6:7:8:9:10:11:12', '::::', 'VWWtW', 'First:line::Second:line::with:a:comma:and:a:dot::Third:line:with:only:::This:::::is:::a::sentence:::::with::::::random::::spaces::::::spaces:', 'dot::::cters', '1:2:::Thsis:::::is:::a:::::3:4:5:6:7', '1:line:2:3:14:5:6:7', 'First:line::Second:line::with:a:comma:and:a:dot::Third:line:with:o:is:::a::sentence:::::with::::::random::::spaces::::::spaces:', 'mcomma', '1:::::::78:::::::9::::0This:is:a:sentence:with:multiple:spaces::It:also:has:multiple:commas::and:some:dots:', '1:2', 'dots:', 'Hello:::world:::::testin1:2:4::::::::::5:623', 'SecondhaThidSeconds', 'languagoe:::::Programmionlyng', 'Thi1:::::::78:::::::9::::0This:is:a:sentence:with:multiple:spaces::It:also:has:multiple:commas::and:some:dots:s', '1:::::::78:::::::9::::0This:is:a:sentence:with:multihaThisple:spaces::It:also:has:multiple:commas::and:some:dots:', '1:2:3:4:5:6:7:81:12', '55:6', 'dScondecond', '1language:::::Programming', ':::This:::::is:::a::sentence:::::with::::::randoms:::::', 'coma']

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
        func_name = "replace_specialchar"
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
        for test_case in ["assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')", "assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')", "assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')"]:
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
