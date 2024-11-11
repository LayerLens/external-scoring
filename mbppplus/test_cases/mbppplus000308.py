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
inputs = [['Cortex "A53" Based "multi" tasking "Processor"'], ['Cast your "favorite" entertainment "apps"'], ['Watch content "4k Ultra HD" resolution with "HDR 10" Support'], ["Watch content '4k Ultra HD' resolution with 'HDR 10' Support"], ['This is a "nested \'quote\'" example'], [''], ['No quotation marks in this input'], ['Nested quotation marks: "This is the "nested" quote"'], ['Two sets of quotation marks: "First" and "second"'], ['Quotation marks within single quotes: \'This is a "quoted" phrase\''], ['Multiple nested quotation marks: "This is the "nested "and "more nested" quote""'], ['Quotation marks within single quotes within double quotes: "This is a \'quoted\' phrase within double quotes"'], ['Multiple nested quotation marks within single quotes: \'This is a "nested "and "more nested" quote" within single quotes\''], ['Quotation marks with "escaped" inside'], ['Nested quotation marks with multiple levels: "This is the "first" quote" and "This is the "second" quote"'], ['Overlapping quotation marks: "This is the "first quote"" and "This is the "second quote""'], ['the'], ["Quotation marks within single quoe'"], ['Thilse is a "nested \'quote\'" example'], ['MuQuotation marks within single quotes: \'This is a "quoted" phrase\'ltiple'], ['Quotation marks within single quotes within double quotes: "This isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"'], ['"second"'], ['Nested quotation marks with multiple levels: "This is the "first" quote" and "iThis is the "second" quote"'], ["'quoted'of"], ['in'], ['"First"'], ['and'], ['ls:'], ['Overlapping Quotation the "first quote"" and "This "'], ['"iThis'], ['Quotation marksa with "escaped" inside'], ['quotes:'], ['ITjhLBoMY'], ['qQuotation marksa with "escaped" insideuotes:'], ['Overlapping quotation marks: "This igs the "first quote"" and "This is the "second quote""'], ['iMultiple nested quotation marks within single quotes: \'This is a "nested "and "more nested" quote" within single quotes\''], ['This is a "nested \'isquote\'" exame'], ['of'], ['insideuotes:'], ['""secondiThsis'], ['inseideuotes:'], ['"iThiis'], ['tquotes:'], ['iMultiple'], ['Overlapping Quotation the a"first quote"" and "This "'], ['Overlapping quotation marks: """'], ['tmultiple'], ['Overlapping quotation marks: "This is quotes\'the "first quote"" and "This is the "second quote""'], ['MuQQuotation marks within single quotes within double quotes: "This isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"uotation marks within single quotes: \'This is a "quoted" phrase\'ltiple'], ['\'qMuQQuotation marks within single quotes within double quotes: "This isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"uotation marks within single quotes: \'This is a "quoted" phrarse\'ltipleuoted\'of'], ['Quotation marks within single quotes: \'This is a \'qMuQQuotation marks within single quotes within double quotthees: "This isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"uotation marks within single quotes: \'This is a "quoted" phrarse\'ltipleuoted\'of"quoted" phrase\''], ['Overlappi"ng quotation marks: """'], ['tmulti'], ['\'quote\'"'], ['quote""'], ['example'], ['Overlapping quotation marks: "This quotes\'theis the "first quote"" and "This is the "second quote""'], ["phrasee'ltiple"], ['\'qMuQQuotation marks within single quotes within double quotes: "This isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"uotation marks within single quotes: \'This is a "quoted" phrarse\'ltipleuoted\'ofls:'], ['This is a "nested \'quote\'"insideuotes: example'], ["Quotation marks wiethin single quoe'"], ['Multiple nested quotation marks: "This is the "nested "and "more rnested" quote""'], ['"morNested quotation marks: "This is the "nested" quote"e'], ['YITjhLBBoMY'], ['Multiple nested quontation marks: "This is the "nested "and "more rnested" quote""'], ['nRYitGiW'], ['This is a "nested \'quote\'"oinsideuotes: example'], ['Q uotation marks within single quotes: \'This is a "quoted" phrase\''], ['\'quote\'"insideuotes:'], ['nRYitGiYW'], ['nRYitGW'], ['Overlapping quotation marks: "This quotes\'theis the "first quote"" and "This is the "suecond quote""'], ['setsls:'], ["MuQuotation marks within single quotes: 'This e"], ["Quaotation marks within single quoe'"], ['\'quote\'"insideuootes:'], ['OvThilse is a "nested \'quote\'" exampleerlapping quotation marks: "This is the "first quote"" and "This is the "second quote""'], ['This is a "nested\'isquote\'" \'quote\'"oinsideuotes: example'], ['i'], ["phrarse'ltipleuoted'of"], ['exame'], ['quotes"'], ["'quoted'"], ["ITjhLBQ uotation marksj within sie'Y"], ['MuQQuotation marks within single quotes within double quotes: "This isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"uotquote"ation marks within single quotes: \'This is a "quoted" phrase\'ltiple'], ['ame'], ['Multiple nested quotation marks: "This irnested" quote""'], ['marksa'], ['ITjhLBBoMY'], ['Overlapping quotation marks: "This quotes\'theis the "first quote"" and "This is the "second qouote""'], ['nThis is a "nested\'isquote\'" \'quote\'"oinsideuotes: exampleRYitGW'], ['This is a "nested\'isquote\'" \'quote\'"oinsideuotess: example'], ['"suecondTwo sets irnested"of quotation marks: "First" and "marks:s'], ['qouote""'], ['qQuotation marksa with "escape:'], ['Overlapping quotation marks: "This quotes\'theis the "first quote""Thilse""'], ['irnested"of'], ['iin'], ['This isQuotation marks within single quoe\' a "neste \'quote\'" example'], ['"neste'], ['double'], ['a"suecondTwome'], ['Overlapping quotation mphrarse\'ltipleuoted\'ofls:arks: """'], ['\'quote\'"insideuoos:'], ['phrarse\'ltiplquote"eeuoted\'of'], ['Two sets of quotation marks: "First" and "snested"econd"'], ['quote""Thilse""'], ['\'quote\'"in"morNested quotation marks: "This is the "nested" quote"edeuoos:'], ['This is a "nested \'quote\'" examplle'], ["Quotaton marks wiethin siongle quoe'"], ['ii\'quote\'"in"morNestedn'], ['\'qMuQQuotation marks within single quotes within double quotes: "Thi"firsts isNested quotation marks: "This is the "nested" quote" a \'quoted\' phrase within double quotes"uotation marks within single quotes: \'This is a "quoted" phrarse\'ltipleuoted\'ofls:'], ['exampleerlapping'], ['"nested"'], ['smYPGQnHV'], ['aminpute']]
results = [['A53', 'multi', 'Processor'], ['favorite', 'apps'], ['4k Ultra HD', 'HDR 10'], [], ["nested 'quote'"], [], [], ['This is the ', ' quote'], ['First', 'second'], ['quoted'], ['This is the ', 'and ', ' quote'], ["This is a 'quoted' phrase within double quotes"], ['nested ', 'more nested'], ['escaped'], ['This is the ', ' quote', 'This is the ', ' quote'], ['This is the ', '', 'This is the ', ''], [], [], ["nested 'quote'"], ['quoted'], ['This isNested quotation marks: ', 'nested', " a 'quoted' phrase within double quotes"], ['second'], ['This is the ', ' quote', 'iThis is the ', ' quote'], [], [], ['First'], [], [], ['first quote', ' and '], [], ['escaped'], [], [], ['escaped'], ['This igs the ', '', 'This is the ', ''], ['nested ', 'more nested'], ["nested 'isquote'"], [], [], [''], [], [], [], [], ['first quote', ' and '], [''], [], ["This is quotes'the ", '', 'This is the ', ''], ['This isNested quotation marks: ', 'nested', " a 'quoted' phrase within double quotes", 'quoted'], ['This isNested quotation marks: ', 'nested', " a 'quoted' phrase within double quotes", 'quoted'], ['This isNested quotation marks: ', 'nested', " a 'quoted' phrase within double quotes", 'quoted', 'quoted'], ['ng quotation marks: ', ''], [], [], [''], [], ["This quotes'theis the ", '', 'This is the ', ''], [], ['This isNested quotation marks: ', 'nested', " a 'quoted' phrase within double quotes", 'quoted'], ["nested 'quote'"], [], ['This is the ', 'and ', ' quote'], ['morNested quotation marks: ', 'nested'], [], ['This is the ', 'and ', ' quote'], [], ["nested 'quote'"], ['quoted'], [], [], [], ["This quotes'theis the ", '', 'This is the ', ''], [], [], [], [], ["nested 'quote'", 'This is the ', '', 'This is the ', ''], ["nested'isquote'"], [], [], [], [], [], [], ['This isNested quotation marks: ', 'nested', " a 'quoted' phrase within double quotes", "ation marks within single quotes: 'This is a "], [], ['This irnested', ''], [], [], ["This quotes'theis the ", '', 'This is the ', ''], ["nested'isquote'"], ["nested'isquote'"], ['suecondTwo sets irnested', 'First'], [''], [], ["This quotes'theis the ", '', ''], [], [], ["neste 'quote'"], [], [], [], [''], [], [], ['First', 'snested'], ['', ''], ['in', 'This is the ', ' quote'], ["nested 'quote'"], [], ['in'], ['Thi', 'This is the ', ' quote', "uotation marks within single quotes: 'This is a "], [], ['nested'], [], []]

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
        func_name = "extract_quotation"
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
        for test_case in ['assert extract_quotation(\'Cortex "A53" Based "multi" tasking "Processor"\') == [\'A53\', \'multi\', \'Processor\']', 'assert extract_quotation(\'Cast your "favorite" entertainment "apps"\') == [\'favorite\', \'apps\']', 'assert extract_quotation(\'Watch content "4k Ultra HD" resolution with "HDR 10" Support\') == [\'4k Ultra HD\', \'HDR 10\']', 'assert extract_quotation("Watch content \'4k Ultra HD\' resolution with \'HDR 10\' Support") == []']:
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
