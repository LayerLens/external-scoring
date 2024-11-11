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
inputs = [['Python'], ['PythonProgrammingExamples'], ['GetReadyToBeCodingFreak'], [''], ['MyNameIsAIAndIAmHereToHelpYou'], ['ThisIsATestStringWithMultipleCamelCaseWords'], ['IAmAProgrammerAndIWritingCodeInPython'], ['ThisStringHasSomeNumbers123InIt'], ['PleaseDOntDisturbWhileTestIsRunning'], ['LetsUseThisOPportunityToLearnSomethingNew'], ['ImSureYouWillFigureItOut'], ['ILOVEPYTHON'], ['pythonprogrammingexamples'], ['LetsUseThisOPsportunityToLearnSomethingNew'], ['ThisStriingHasSomeNumbers123InIt'], ['ThisStringHasSomeNumbers123InThisStriingHasSomeNumbers123InItIt'], ['cCTa'], ['ThisStringHasSomeNumThisStriingHasSomeNumbers123InItbers123InThisStriingHasSomeNumbers123InItIt'], ['LetsUseThisOPsportunityTosLearnSomethingNew'], ['ThisStringHasSomeNumbeers12t3InIt'], ['ImOSureYouWillFigureItOut'], ['ThisStringHasSomeNumbeLetsUseThisOPsportunityToLearnSomethingNewrs123InIt'], ['LetsUseThisOPsomethingNew'], ['PleaseDOntDIAmAProgrammerAndIWritingCodeInPythonisturbWhileTestIsRunning'], ['LetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123InItbers123InThisStriingHasSomeNumbers123InItItomethingNew'], ['PleaseDOntDistImSureYouWillFigureItOuturbWhileTestIsRunning'], ['pmingexamples'], ['ThisIsATestStringWiothMultipleCamelCasePleaseDOntDisturbWhileTestIsRunningWords'], ['ThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123IHasSomeNumbers123InItItomethingNewngHasSomeNumbers123InItIt'], ['ImOThisIsATestStringWiothMultipleCamelCasePleaseDOntDisturbWhileTestIsRunningWordsSureYouWillFigureItOut'], ['ImOSureYouWillFigureItOu'], ['pmingexamplles'], ['ThisStringHasSomeNumbers123InThisStriingHThisIsATestStringWiothMultipleCamelCasePleaseDOntDisturbWhileTestIsRunningWordsasSomeNumbers123InItIt'], ['ThisStringHasSomeNumbeLetsUseThisOPsportunityToLearnSomethingNewrs1MyNameIsAIAndIAmHereToHelpYou23InIt'], ['LetsUseThisOPsppythonprogrammingexamplesortuThisIsATestStringWithMultipleCamelCaseWordsnityToLearnSomethingNew'], ['ThisStringHasLetsUseThisOPportunityToLearnSomethingNewbeers12t3InIt'], ['ThisIsATesitStringWithMultipleCamelCaseWords'], ['PleaseDOntDIAmAProgrammerAndIWritingCodeInPytThisStriingHasSomeNumbers123InIthonisturbWhileTestIsRunning'], ['ImSureYouWillFiureItOut'], ['pythonprogramMyNameIsAIAndIAmHereToHelpYoumingexamples'], ['ThisStringHasSomeNumbers123InThisStriingHasSoThisIsATestStringWiothMultipleCamelCasePleaseDOntDisturbWhileTestIsRunningWordsmeNumbers123InItIt'], ['LetsUseThisOPsomethinPleaseDOntDIAmAProgrammerAndIWritingCodeInPythonisturbWhileTestIsRunninggNew'], ['ThisStringHasSomeNumbers123InThisStriingHaesSomeNumbers123InItIt'], ['pythondprogramMyNameIsAIAndIAmHereToHelpYoumingexamples'], ['ITntIt'], ['ILOVEPIAmAProgrammerAndIWritingCodeInPythonYTHON'], ['ThisThisStringHasSomeNumbers123InThisStriingHasSoThisIsATestStringWiothMultipleCamelCasePleaseDOntDisturbWhileTestIsRunningWordsmeNumbers123InItItStringHasSomeNumbeLetsUseThisOPsportunityToLearnSomethingNewrs123InIt'], ['LToLearnSomImSureYouWillFigureItOutethingNew'], ['pythonprogramMyNameIsAIAondIAmHereToHelpYoumingexamples'], ['LetsUseThisOPPsporLtunityTosLearnSomethingNew'], ['TITtntIt'], ['ImSuruWuillFigureItOut'], ['ThisStringHasSoumeNumbeLetsUseThisOPsportunityToLearnSomethingNewrs123InIt'], ['LToLearnSomImSureYouWillFigureItOupythondprogramMyNameIsAIAnThisStringHasSomeNumbers123InItdIAmHereToHelpYoumingexamplestethingNew'], ['LetsUseThisOPsportunityToLearnSomethiPleaseDOntDistImSureYouWillFigureItOuturbWhileTestIsRunningngNew'], ['pythonprogramMyNameIsAIAeToHelpYoumingexamples'], ['aXv'], ['tOut'], ['LetsUseThisOPPsporLtunyityTosLearnSomethingNew'], ['LetsUseThisOPsportunityToLearnSomethiPleaseDOntDistImSureYouWillFigureIteOuturbWhileTestIsRunningngNew'], ['LetsUseThisOPPsporLtunyityTosLearnSomsethingNew'], ['pythonprogramMyNameIsAIAes'], ['ThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123IHasSomeNumbers123InItgHasSomeNumbers123InItIt'], ['ImOThisIsATestStringWiothMultipleCamelCasePleaseDOntDistsRunningWordsSureYouWillFigureItOut'], ['ITtntIt'], ['ThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123IHasSomeNumbers123InItItomethingNewngHasSomeNumbers123InItItThisStringHasSomeNumbers123InIt'], ['LetsUseThiw'], ['ThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThiisStriingHasSomILOVEPIAmAProgrammerAndIWritingCodeInPythonYTHONomeNumbers123InItIt'], ['ThisStrPleaseDOntDIAmAProgrammerAndIWritingCodeInPytThisStriingHasSomeNumbers123InIthonisturbWhileTestIsRunningiingHasSomeNumbers123InIt'], ['pythonprogramMyNameIsAIAeToHelpYoumingexamplesut'], ['pmingexammplles'], ['LetsUseThisOPPsporLtunyityTLosLearnSomsethingNew'], ['ILOVLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123InItbers123InThisStriingHasSomeNumbers123InItItomethingNewEPYTHON'], ['PleaseDOntDIAmAProgrammerAndIWritingCodeInPytThisStriingHasSomeNumberThisStrPleaseDOntDIAmAProgrammerAndIWritingCodeInPytThisStriingHasSomeNumbers123InIthonisturbWhileTestIsRunningiingHasSomeNumbers123InIts123InIthonisturbWhileTestIsRunning'], ['ThisStringHasSomeNumThisStriingHasSomeNumbers123InItbers123InThisStriingHasSoILOVEPYTHONmeNumbers123InItIt'], ['ThisStringHLetsUseThisOPPsporLtunyityTosLearnSomethingNewasSoumeNumbeLetsUseThisOPsportunityToLearnSomethingNewrs123InIt'], ['pythondprogramMyNameIsAIAndIAmHereToHelpYoumingxexamples'], ['ImSureYouWillFiureLetsUseThisOPsomethingNewItOut'], ['LetsUseThisOPsportunityToLearnSomethiPleaseDOntDistIgmSureYouWillFigureItOuturbWhileTestIsRunningngNew'], ['ThisStringHasSomeNumThisStriingHasSomeNumbers123InItbers123InThisStriingHasSoILOVEPYTHONmeNumbers123It'], ['LThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSoTngNewngHasSomeNumbers123InItItetsUseThisOPPsporLtunyityTLosLearnSomsethingNew'], ['LetsUseThisOPPsporLtunyityTLosLearnSomsethinITtntItgNew'], ['LetsUseThisOPsportunityToLearnSomethiPleaseDOntDistYouWillFigureItOuturbWhileTestIsRunningngNew'], ['ThisStringHasSom1eNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123IHasSomeNumbers123InItgHasSomeNumbers123InItIt'], ['ttOut'], ['LToLearnSomImSureYouWillFigureItOupythondprogramMyNameIsAIAnThisStringHasSomhingNew'], ['TIt'], ['pmingeImSureYouWillFigureItOutamplles'], ['LetsUseThisOPPsporLtunyityTosILOVESPYTHONLearnSomsethingNew'], ['LetsUseThisOPsomethinPleaseDOntDIAmAProgrammeLetsUseThisOPPsporLtunyityTosLearnSomsethingNewnninggNew'], ['ImSuruWuillFigureItOaXv'], ['ThisStringHasSomeNumbeLetsUseThisOPsportunityToLearnSomethgingNewrs123InIt'], ['PleaseDOntDIAImOSureYouWillFigureItOutmAProgrammerAndIWritingCodeInPythonisturbWhileTestIsRunning'], ['ThisStriingHassSomeNumbers123InIt'], ['ImOSureYouuWillFigureItOut'], ['PleaseDOntDIAmAProgrammerAndIWritintgCodeInPythonyisturbWhIAmAProgrammerAndIWritingCodeInPythonileTestIsRunning'], ['IThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123IHasSomeNumbers123InItItomethingNewngHasSomeNumbers123InItIttIt'], ['pythonprogramMyNameIsAIAeToHelpYouminmgexamples'], ['cCTThisStringHLetsUseThisOPPsporLtunyityTosLearnSomethingNewasSoumeNumbeLetsUseThisOPsportunityToLearnSomethingNewrs123InIt'], ['ImSureYouWillFiureLetsUseThisOPsomethingNewnItOut'], ['ThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThiLetsUseThisOPsportunityToLearnSomethingNewsStringHasSomeNumThiisStriingHasSomILOVEPIAmAProgrammerAndIWritingCodeInPythonYTHONomeNumbers123InItIt'], ['ILOVEPIAmAProgrammerAndIWritEingCodeInPythonYLToLearnSomImSureYouWillFigureItOupythondprogramMyNameIsAIAnThisStringHasSomhingNewTHON'], ['ThisStringHasSomeNumbers123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasThisIsATesitStringWithMultipleCamelCaseWordstItomethingNewngHasSomeNumbers123InItIt'], ['MyNameIsAILOVEPYTHONIAndIAmHereToHelpYou'], ['TIPleaseDOntDIAmAProgrammerAndIWritintgCodeInPythonyisturbWhIAmAProgrammerAndIWritingCodeInPythonileTestIsRunningt'], ['LetsUseThisOPsppythonprogrammingexamplesortuThisIsATestStringWithMultipleCamelCaseWordsnityToLearnsSomethingNew'], ['LetsUseThisOPPsporLtunyityTosILOVESPYTHONLearnSomsethigNew'], ['ImOThisIsATestStriWordsSureYouut'], ['ThisStringHasSomeNumbersThisIsATesitStringWithMultipleCamelCaseWords123InThisStriiLetsUseThisOPportunityToLearnSThisStringHasSomeNumThisStriingHasSomeNumbers123IHasSomeNumbers123InItItomethingNewngHasSomeNumbers123InItIt'], ['ImSuruWuillFiguThisIsATestStringWithMultipleCamelCaseWordsreItOaXv'], ['LetsUseThisOPssportunityToLearnSomethiPleaseDOntDistIgmSureYouWillFigureItOuturibWhileTestIsRunningngNew'], ['PleaseDOntDIAImOSureYouWillFigureItOutmAProgrammeILOVEPYTHONrAndIWrOitingCodeInPythonisturbnning'], ['LetsUseThisOPsportunityToLeasrnSomethingNew']]
results = ['Python', 'Python Programming Examples', 'Get Ready To Be Coding Freak', '', 'My Name Is AI And IAm Here To Help You', 'This Is ATest String With Multiple Camel Case Words', 'I Am AProgrammer And IWriting Code In Python', 'This String Has Some Numbers123 In It', 'Please DOnt Disturb While Test Is Running', 'Lets Use This OPportunity To Learn Something New', 'Im Sure You Will Figure It Out', 'I LO VE PY TH ON', 'pythonprogrammingexamples', 'Lets Use This OPsportunity To Learn Something New', 'This Striing Has Some Numbers123 In It', 'This String Has Some Numbers123 In This Striing Has Some Numbers123 In It It', 'c CTa', 'This String Has Some Num This Striing Has Some Numbers123 In Itbers123 In This Striing Has Some Numbers123 In It It', 'Lets Use This OPsportunity Tos Learn Something New', 'This String Has Some Numbeers12t3 In It', 'Im OSure You Will Figure It Out', 'This String Has Some Numbe Lets Use This OPsportunity To Learn Something Newrs123 In It', 'Lets Use This OPsomething New', 'Please DOnt DI Am AProgrammer And IWriting Code In Pythonisturb While Test Is Running', 'Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 In Itbers123 In This Striing Has Some Numbers123 In It Itomething New', 'Please DOnt Dist Im Sure You Will Figure It Outurb While Test Is Running', 'pmingexamples', 'This Is ATest String Wioth Multiple Camel Case Please DOnt Disturb While Test Is Running Words', 'This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 IHas Some Numbers123 In It Itomething Newng Has Some Numbers123 In It It', 'Im OThis Is ATest String Wioth Multiple Camel Case Please DOnt Disturb While Test Is Running Words Sure You Will Figure It Out', 'Im OSure You Will Figure It Ou', 'pmingexamplles', 'This String Has Some Numbers123 In This Striing HThis Is ATest String Wioth Multiple Camel Case Please DOnt Disturb While Test Is Running Wordsas Some Numbers123 In It It', 'This String Has Some Numbe Lets Use This OPsportunity To Learn Something Newrs1 My Name Is AI And IAm Here To Help You23 In It', 'Lets Use This OPsppythonprogrammingexamplesortu This Is ATest String With Multiple Camel Case Wordsnity To Learn Something New', 'This String Has Lets Use This OPportunity To Learn Something Newbeers12t3 In It', 'This Is ATesit String With Multiple Camel Case Words', 'Please DOnt DI Am AProgrammer And IWriting Code In Pyt This Striing Has Some Numbers123 In Ithonisturb While Test Is Running', 'Im Sure You Will Fiure It Out', 'pythonprogram My Name Is AI And IAm Here To Help Youmingexamples', 'This String Has Some Numbers123 In This Striing Has So This Is ATest String Wioth Multiple Camel Case Please DOnt Disturb While Test Is Running Wordsme Numbers123 In It It', 'Lets Use This OPsomethin Please DOnt DI Am AProgrammer And IWriting Code In Pythonisturb While Test Is Runningg New', 'This String Has Some Numbers123 In This Striing Haes Some Numbers123 In It It', 'pythondprogram My Name Is AI And IAm Here To Help Youmingexamples', 'I Tnt It', 'I LO VE PI Am AProgrammer And IWriting Code In Python YT HO N', 'This This String Has Some Numbers123 In This Striing Has So This Is ATest String Wioth Multiple Camel Case Please DOnt Disturb While Test Is Running Wordsme Numbers123 In It It String Has Some Numbe Lets Use This OPsportunity To Learn Something Newrs123 In It', 'L To Learn Som Im Sure You Will Figure It Outething New', 'pythonprogram My Name Is AI Aond IAm Here To Help Youmingexamples', 'Lets Use This OP Pspor Ltunity Tos Learn Something New', 'T ITtnt It', 'Im Suru Wuill Figure It Out', 'This String Has Soume Numbe Lets Use This OPsportunity To Learn Something Newrs123 In It', 'L To Learn Som Im Sure You Will Figure It Oupythondprogram My Name Is AI An This String Has Some Numbers123 In Itd IAm Here To Help Youmingexamplestething New', 'Lets Use This OPsportunity To Learn Somethi Please DOnt Dist Im Sure You Will Figure It Outurb While Test Is Runningng New', 'pythonprogram My Name Is AI Ae To Help Youmingexamples', 'a Xv', 't Out', 'Lets Use This OP Pspor Ltunyity Tos Learn Something New', 'Lets Use This OPsportunity To Learn Somethi Please DOnt Dist Im Sure You Will Figure Ite Outurb While Test Is Runningng New', 'Lets Use This OP Pspor Ltunyity Tos Learn Somsething New', 'pythonprogram My Name Is AI Aes', 'This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 IHas Some Numbers123 In Itg Has Some Numbers123 In It It', 'Im OThis Is ATest String Wioth Multiple Camel Case Please DOnt Dists Running Words Sure You Will Figure It Out', 'I Ttnt It', 'This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 IHas Some Numbers123 In It Itomething Newng Has Some Numbers123 In It It This String Has Some Numbers123 In It', 'Lets Use Thiw', 'This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num Thiis Striing Has Som IL OV EP IAm AProgrammer And IWriting Code In Python YT HO Nome Numbers123 In It It', 'This Str Please DOnt DI Am AProgrammer And IWriting Code In Pyt This Striing Has Some Numbers123 In Ithonisturb While Test Is Runningiing Has Some Numbers123 In It', 'pythonprogram My Name Is AI Ae To Help Youmingexamplesut', 'pmingexammplles', 'Lets Use This OP Pspor Ltunyity TLos Learn Somsething New', 'I LO VLets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 In Itbers123 In This Striing Has Some Numbers123 In It Itomething New EP YT HO N', 'Please DOnt DI Am AProgrammer And IWriting Code In Pyt This Striing Has Some Number This Str Please DOnt DI Am AProgrammer And IWriting Code In Pyt This Striing Has Some Numbers123 In Ithonisturb While Test Is Runningiing Has Some Numbers123 In Its123 In Ithonisturb While Test Is Running', 'This String Has Some Num This Striing Has Some Numbers123 In Itbers123 In This Striing Has So IL OV EP YT HO Nme Numbers123 In It It', 'This String HLets Use This OP Pspor Ltunyity Tos Learn Something Newas Soume Numbe Lets Use This OPsportunity To Learn Something Newrs123 In It', 'pythondprogram My Name Is AI And IAm Here To Help Youmingxexamples', 'Im Sure You Will Fiure Lets Use This OPsomething New It Out', 'Lets Use This OPsportunity To Learn Somethi Please DOnt Dist Igm Sure You Will Figure It Outurb While Test Is Runningng New', 'This String Has Some Num This Striing Has Some Numbers123 In Itbers123 In This Striing Has So IL OV EP YT HO Nme Numbers123 It', 'L This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has So Tng Newng Has Some Numbers123 In It Itets Use This OP Pspor Ltunyity TLos Learn Somsething New', 'Lets Use This OP Pspor Ltunyity TLos Learn Somsethin ITtnt Itg New', 'Lets Use This OPsportunity To Learn Somethi Please DOnt Dist You Will Figure It Outurb While Test Is Runningng New', 'This String Has Som1e Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 IHas Some Numbers123 In Itg Has Some Numbers123 In It It', 'tt Out', 'L To Learn Som Im Sure You Will Figure It Oupythondprogram My Name Is AI An This String Has Somhing New', 'T It', 'pminge Im Sure You Will Figure It Outamplles', 'Lets Use This OP Pspor Ltunyity Tos IL OV ES PY TH ON Learn Somsething New', 'Lets Use This OPsomethin Please DOnt DI Am AProgramme Lets Use This OP Pspor Ltunyity Tos Learn Somsething Newnningg New', 'Im Suru Wuill Figure It Oa Xv', 'This String Has Some Numbe Lets Use This OPsportunity To Learn Somethging Newrs123 In It', 'Please DOnt DI AIm OSure You Will Figure It Outm AProgrammer And IWriting Code In Pythonisturb While Test Is Running', 'This Striing Hass Some Numbers123 In It', 'Im OSure Youu Will Figure It Out', 'Please DOnt DI Am AProgrammer And IWritintg Code In Pythonyisturb Wh IAm AProgrammer And IWriting Code In Pythonile Test Is Running', 'I This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 IHas Some Numbers123 In It Itomething Newng Has Some Numbers123 In It Itt It', 'pythonprogram My Name Is AI Ae To Help Youminmgexamples', 'c CT This String HLets Use This OP Pspor Ltunyity Tos Learn Something Newas Soume Numbe Lets Use This OPsportunity To Learn Something Newrs123 In It', 'Im Sure You Will Fiure Lets Use This OPsomething Newn It Out', 'This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThi Lets Use This OPsportunity To Learn Something News String Has Some Num Thiis Striing Has Som IL OV EP IAm AProgrammer And IWriting Code In Python YT HO Nome Numbers123 In It It', 'I LO VE PI Am AProgrammer And IWrit Eing Code In Python YL To Learn Som Im Sure You Will Figure It Oupythondprogram My Name Is AI An This String Has Somhing New TH ON', 'This String Has Some Numbers123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has This Is ATesit String With Multiple Camel Case Wordst Itomething Newng Has Some Numbers123 In It It', 'My Name Is AI LO VE PY TH ON IAnd IAm Here To Help You', 'T IPlease DOnt DI Am AProgrammer And IWritintg Code In Pythonyisturb Wh IAm AProgrammer And IWriting Code In Pythonile Test Is Runningt', 'Lets Use This OPsppythonprogrammingexamplesortu This Is ATest String With Multiple Camel Case Wordsnity To Learns Something New', 'Lets Use This OP Pspor Ltunyity Tos IL OV ES PY TH ON Learn Somsethig New', 'Im OThis Is ATest Stri Words Sure Youut', 'This String Has Some Numbers This Is ATesit String With Multiple Camel Case Words123 In This Strii Lets Use This OPportunity To Learn SThis String Has Some Num This Striing Has Some Numbers123 IHas Some Numbers123 In It Itomething Newng Has Some Numbers123 In It It', 'Im Suru Wuill Figu This Is ATest String With Multiple Camel Case Wordsre It Oa Xv', 'Lets Use This OPssportunity To Learn Somethi Please DOnt Dist Igm Sure You Will Figure It Outurib While Test Is Runningng New', 'Please DOnt DI AIm OSure You Will Figure It Outm AProgramme IL OV EP YT HO Nr And IWr Oiting Code In Pythonisturbnning', 'Lets Use This OPsportunity To Leasrn Something New']

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
        func_name = "capital_words_spaces"
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
        for test_case in ['assert capital_words_spaces("Python") == \'Python\'', 'assert capital_words_spaces("PythonProgrammingExamples") == \'Python Programming Examples\'', 'assert capital_words_spaces("GetReadyToBeCodingFreak") == \'Get Ready To Be Coding Freak\'']:
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
