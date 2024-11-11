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
inputs = [['"Python", "PHP", "Java"'], ['"python","program","language"'], ['"red","blue","green","yellow"'], ['This is a test input.'], ['"red" "blue" "green" "yellow" "red" "blue" "green" "yellow"'], [''], ['"This is a "complex" input with nested "quotes" inside a string"'], ['""""""""""'], ['"This is a "nested"" input string."'], ['withtt'], ['Th.is is a test input.'], ['Th.is tis a test input.'], ['"nested""'], ['"red" "blue" "green" "yellow" "red" "blue" "green" "yeltestlow"'], ['"yeltestlow"'], ['This is a tesnt input.'], ['Th.is tis a test inpTut.'], ['"""""inside"""""'], ['is'], ['"red" "blue" "green" "yellow" "red" "blue" "green" e"yeltestlow"'], ['"red" "blue" "green" "yellow" "red"e "blue" "green" "yeltestlow"'], ['i"""""inside""""""nested""s'], ['""tesnt""""""""'], ['"testlow"'], ['"red" "blue" "green" "yow"'], ['"string"yeltestlow"'], ['This is withtt input.'], ['"red" "bluetesnt" "green" "yellow" "red" "blue" "green" "yellow"'], ['nested'], ['"bluetesnt"Th.is'], ['Th.is tis a test inputinpTut..'], ['""tesnt"""""""""'], ['"red" "blue" "grinpTut.een" "yow"'], ['i""""is"inside""""""nested""s'], ['"red" "blue" "green" "yellow" "red""yellow" "blue" "green" e"yeltestlow"'], ['Th"red"ut.'], ['"green"'], [' This is a test input.'], ['AuCeUjnbN'], ['Te"yeltestlow"h.is tis a utinpTut..'], ['"red" "blue" "green" "yellow" "red" "blue" "green"""tesnt""""""""" "yello"w"'], ['Te"yeltestlow"h.iis tis a utinpTut..'], ['Th.is tis a test iTnpTut.'], ['l"complex"CWE'], ['"yeltetisstlow"'], ['Te"yeltestlow"h.iis tis a utinpTut"..'], ['Th.is is a test input .'], ['"yTe"yeltestlow"h.iiseltetisstlow"is'], ['"yTe"yisstlow"is'], ['"red" "blue" "green" "yellow" d" "blue" "green" '], ['"This is a "nested"" in put stringt."'], ['l"comple"x"CWE'], ['"yTe"yeltestlow"h.iiseltetl"complex"CWEisstlow"is'], ['a test input.'], ['""tes"nt"""""""""'], ['a'], ['stringt."'], ['"yetestlow"'], ['"yTe"yisstlow"yeltelstlow""is'], ['whith'], ['"red" "blue" "green" "yellow" "red" "blue"a test input.n" e"yeltestlow"'], ['"red" "blue" "blue" "green" '], ['"This is a "complex" input with nested "quotes" inside  a string"'], ['"This is a "nested"" input string."This is a "complex" input with nested "quotes" inside  a string"'], ['"quotes"'], ['"r"yow"ed" "blue" "grinpTut.een" "yow"'], ['""string."Thistesnt"""""""""'], ['"qThisuTh.is tis a test inpTut.tes"'], ['"red" "blue"tlow"'], ['Th.is tis a test i"green"npTuut.'], ['l"compl"ex""red" "blue" "green" "yellow" "red""yelllow" "blue" "green" e"yeltestlow"CWE'], ['"yTe"yeltestlow"h.iiseltetl"compThis is a test input.lex"CWEisstlow"is'], ['This is  a tesnt input.'], ['"greenn"'], ['"red" "blue" "green" ""string"yeltestlow"estlow"'], ['Th.iis'], ['"red" "blue" "grestring."Thisen" ""string"yeltestlow"testlow"'], ['""string"yeltestlow"estlow"'], ['""string"yeltestlow"testlow"'], ['This is  a tesnt inpuut.'], ['"string"tyeltestlTe"yeltestlow"h.iis tis a utinpTut..ow"'], ['"This is a "nested"" input string."This is a "complex" input with  nested "quotes" inside  a string"'], ['"red" "blue" "green" "yellow" "red" "blue" "green" "yeltesbtlow"'], ['"This'], ['"string"tyeltestlTe"yeltestlow"h.iis'], ['l"compl"ex"inpTut.tes""red" "blue" "green" "yellow" "red""yelllow" "blue" "gereen" e"yeltestlow"CWE'], ['"red" "blue" "green" "yellow" d"Th.is tis a test iTnpTut. "blue" "green" '], ['l"compwhithlex"CWE'], ['TTh.is tis a test iTnpTut.'], ['iutinpTut..s'], ['"yTe"yeltestlow"h.iiseltetl"compThis is a test input.lex"l"compl"ex"inpTut.tes""red"CWEisstlow"is'], ['string."This'], ['nesteThisd'], ['Te"yeltestlow"th.iis tis a utinpTtestut"..'], ['AuC"testlow"eUjnbN'], ['"red" "bluetesnt" "green" "yellow" "red" "blue" ""qThisuTh.isgreen" "yellow"'], ['tesnt'], [' This is a test input""tesnt"""""""".'], ['e"yeltestlow"CWE'], ['""qThisuTh.isgreen"'], ['"r"yow"ed" "blue" "grinpTut".een" "yow"'], ['""string"yeltestlowinput.lex"CWEisstlow"isow"'], ['inpu'], ['"quote"red" "blue" "green" "yellow" d"Th.is tis a test iTnpTut. "blue" "green" "'], ['ah"gres"Thisen" test input.'], ['iutinpi"""""inside""""""nested""s.s'], ['"grinpTut".een"'], ['"greenTTh.isn"'], ['"yTe"yeltestlo"red" "blue" "green" "yellow" "red" "blue" "green" "yeltesbtlow"low"is']]
results = [['Python', 'PHP', 'Java'], ['python', 'program', 'language'], ['red', 'blue', 'green', 'yellow'], [], ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow'], [], ['This is a ', ' input with nested ', ' inside a string'], ['', '', '', '', ''], ['This is a ', ''], [], [], [], ['nested'], ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yeltestlow'], ['yeltestlow'], [], [], ['', '', 'inside', '', ''], [], ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yeltestlow'], ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yeltestlow'], ['', '', 'inside', '', '', 'nested'], ['', '', '', '', ''], ['testlow'], ['red', 'blue', 'green', 'yow'], ['string'], [], ['red', 'bluetesnt', 'green', 'yellow', 'red', 'blue', 'green', 'yellow'], [], ['bluetesnt'], [], ['', '', '', '', ''], ['red', 'blue', 'grinpTut.een', 'yow'], ['', '', 'inside', '', '', 'nested'], ['red', 'blue', 'green', 'yellow', 'red', 'yellow', 'blue', 'green', 'yeltestlow'], ['red'], ['green'], [], [], ['yeltestlow'], ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', '', '', '', '', '', ' ', 'w'], ['yeltestlow'], [], ['complex'], ['yeltetisstlow'], ['yeltestlow'], [], ['yTe', 'h.iiseltetisstlow'], ['yTe'], ['red', 'blue', 'green', 'yellow', ' ', ' '], ['This is a ', ''], ['comple'], ['yTe', 'h.iiseltetl', 'CWEisstlow'], [], ['', 'nt', '', '', '', ''], [], [], ['yetestlow'], ['yTe', 'yeltelstlow'], [], ['red', 'blue', 'green', 'yellow', 'red', 'blue', ' e'], ['red', 'blue', 'blue', 'green'], ['This is a ', ' input with nested ', ' inside  a string'], ['This is a ', '', 'This is a ', ' input with nested ', ' inside  a string'], ['quotes'], ['r', 'ed', 'blue', 'grinpTut.een', 'yow'], ['', 'Thistesnt', '', '', '', ''], ['qThisuTh.is tis a test inpTut.tes'], ['red', 'blue'], ['green'], ['compl', '', ' ', ' ', ' ', ' ', '', ' ', ' ', ' e'], ['yTe', 'h.iiseltetl', 'CWEisstlow'], [], ['greenn'], ['red', 'blue', 'green', '', 'yeltestlow'], [], ['red', 'blue', 'grestring.', ' ', 'string', 'testlow'], ['', 'yeltestlow'], ['', 'yeltestlow'], [], ['string', 'yeltestlow'], ['This is a ', '', 'This is a ', ' input with  nested ', ' inside  a string'], ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yeltesbtlow'], [], ['string', 'yeltestlow'], ['compl', 'inpTut.tes', 'red', 'blue', 'green', 'yellow', 'red', 'yelllow', 'blue', 'gereen', 'yeltestlow'], ['red', 'blue', 'green', 'yellow', 'Th.is tis a test iTnpTut. ', ' '], ['compwhithlex'], [], [], ['yTe', 'h.iiseltetl', 'l', 'ex', '', 'CWEisstlow'], [], [], ['yeltestlow'], ['testlow'], ['red', 'bluetesnt', 'green', 'yellow', 'red', 'blue', '', ' '], [], ['', '', '', '', ''], ['yeltestlow'], [''], ['r', 'ed', 'blue', 'grinpTut', ' '], ['', 'yeltestlowinput.lex', 'isow'], [], ['quote', ' ', ' ', ' ', ' d', 'blue', 'green'], ['gres'], ['', '', 'inside', '', '', 'nested'], ['grinpTut'], ['greenTTh.isn'], ['yTe', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yeltesbtlow']]

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
        func_name = "extract_values"
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
        for test_case in ['assert extract_values(\'"Python", "PHP", "Java"\')==[\'Python\', \'PHP\', \'Java\']', 'assert extract_values(\'"python","program","language"\')==[\'python\',\'program\',\'language\']', 'assert extract_values(\'"red","blue","green","yellow"\')==[\'red\',\'blue\',\'green\',\'yellow\']']:
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
