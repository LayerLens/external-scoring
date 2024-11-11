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
inputs = [['python_program'], ['python_language'], ['programming_language'], ['___python_program'], ['__12_python__language___'], ['your_programming__langu__age___'], ['another__ex44ample___'], ['_'], ['word'], ['no_underscores'], ['_leading'], ['trailing_'], ['__multiple_consecutive__underscores__'], ['__12_python__languag_'], ['___p_ythonram'], ['your_nprogramming__langu__age___'], ['your_nprogramming_another__ex44ample____langu__age___'], ['__12_pythonno_underscores__languag_'], ['_lwordeading'], ['your_nprogramming_another__ex4no_underscores4ample____langu__age___'], ['your_programming__langu____12_python__languag_age___'], ['__12_pyth_'], ['__1__12_python__languag_2_pythonno_underscores__languag_'], ['___pgram'], ['_lwordeadin__12_python__language___g'], ['your_prtrailing___'], ['__12_pythonno_underscores__langu_ag_'], ['aiN'], ['worod'], ['_lwordeadin__12_python__languaage___g'], ['qaiNnJa'], ['aiN_lwordeading'], ['_lwordeadin__1_2_python__language___g'], ['your_nprogrammi__12_pyth_ng_another__ex4no_underscores4ample____langu__age___your_nprogramming__langu__age___'], ['your_pryour_nprogramming_another__ex4no_underscores4ample____langu__age___iling___'], ['__1____12_pythonno_underscores__langu_ag_12_python__languag_2_pythonno_underscores__languag_'], ['CVh'], ['_leadin_lwordeadin__12_python__languaage___gg'], ['_th_'], ['_lwordeadin__1_2_py__language___g'], ['trailing__12_python__languag__'], ['your_pr_th_ogramming__langu____12_python__languag_age___'], ['your_pryour_nprogramming_another__aiNex4no_underscores4ample____langu__age___iling___'], ['__12_python__language_g__'], ['aiN_lwordeadin__12_python__layour_nprogramming_another__ex4no_underscores4ample____langu__age___wordeading'], ['_lwordeadin__1_2_py__lawordnguaage___g'], ['__12_pythonno_underscores__lanuag_'], ['_____12_pyth_ram'], ['__1____12_pythonno_underscores__langu_a_lwordeadingg_12_python__languag_2_pythonno_underscores__languag_'], ['__'], ['_leadilng'], ['___python_progr__1____12_pythonno_underscores__langu_ag_12_python__l__languag_m'], ['__12_pythonno_underscores__langua_g_'], ['your_nprogramming_another__ex44ample_____12_pythonno_underscores__languag__langu__age___'], ['__12_python__l__'], ['__multiprlne_consecutive__underscores__'], ['___12_pyth_'], ['__1____12_pythonno_undngu_a_lwordeadingg_12_python__languag_2_pythonno_underscores__languag_'], ['your_nprogramming_another__ex44ample_____12_py___12_pyth_thonno_underscores__languag__langu__age___'], ['_____multiple_consecutive__underscores__python_program'], ['yo_ur_nprogr_amming_another__ex44ample____langu__age___'], ['_leadin_lwnordeadin__12_python__languaage___gg'], ['jzAx'], ['_leadin____12_pyth_lwordeadin__12_python__languaage___gg'], ['yo_ur_nprogr_amming_another__ex44am__multiprlne_consecutive__underscores__ple___1__12_python__languag_2_pythonno_underscores__languag___langu__age___'], ['__1____12_pythonno_underscores__langu_ag_12_python__languag_2_pythonno_underscores__languag_word'], ['_lwordeadin__12_python__lanuguage___g'], ['trailing___python_progr__1____12_pythonno_underscores__langu_ag_12_python__l__languag_m__12_python__languag__'], ['trailianguag_2_pythonno_underscores__languag__'], ['__1_2_p'], ['_leadil__multiple_consecutive__underscores__ng'], ['__1_2_qaiNnJap'], ['a__1_2_piN_lwordeading'], ['__NnJap'], ['__12_peythonno_underscores__lanuag_'], ['trailinig_'], ['trailiyour_yo_ur_nprogr_amming_another__ex44ample____langu__age___pryour_nprogramming_another__aiNex4no_underscores4ample____langu__ayour_nprogrammi__12_pyth_ng_another__ex4no_underscores4ample____langu__age___your_nprogramming__langu__age___ge___iling___'], ['X'], ['_leadin____12_pyth_lwordeadin__12_python__languaage___g1g'], ['_lwordeadin__1_2_py__lawordnguaage___g__1_2_p'], ['your_programming__langu____1y2_python__languag_age___'], ['your_pr_th_ogramming__langu____12__lwordeadingpython__languag_age___'], ['your_pr_th_ogramming__langu____12_your_programming__langu____1y2_python__languag_age____lwordeadingpython__languag_age___'], ['aiN_lwordeadiwordn__12_python__layour_nprogramming_another__ex4no_underscores4ample____langu__age___wordeading'], ['your_nprogr_lwordeadingammi__12_pyth_ng_another__ex4no_underscores4ample____langu__age___your_nprogramming__langu__age___'], ['___p_ythqaiNnJaonram'], ['12_python__l__'], ['_lwordeadin__12_python__lan_lwordeadin__12_python__languaage___gguaage___g'], ['__12_pythonaiN_lwordeading__l__'], ['trailing__12_python__layo_ur_nprogr_amming_another__ex44ample____langu__age___nguag__'], ['your__12_pythonno_underascores__langu_ag__nprogramming_another__ex4no_underscores4ample____langu__age'], ['your_pryour_nprotrailing__12_python__layo_ur_nprogr_amming_another__ex44ample____langu__age___nguag__gramming_another__ex4no_underscores4ample____langu__age___iling___'], ['__12n_pythonno_un_'], ['_____12_pyth__python_program'], ['_lwon__1__12_python__l__2_python__lanuguage___g'], ['your_programming__langu____12_python__languag_ag___pgram___'], ['____12n_pythonno_un_1_2_p'], ['_lwordeadin__12_python__lanugu_lwordeadingage___g'], ['aiyour_pryour_nprogramming_another__aiNex4no_undersco_lwordeadingres4ample____langu__age___iling___N'], ['__1_d___12_pythonno_underscores__langu_ag_12_python__languag_2_pythonno_underscores__languag_'], ['your_pr_th_ogramming__langu____12_your_programming__langu____1y2_python__languingpython__languag_age___'], ['your_nprogrammi__12__pyth_ng_another__ex4no_underscores4ample____langu__age___your_nprogramming__langu__age___'], ['your_pr_th_ogramming__langu____12_your_programming__langu____1y2_pythotn__languag_age____lwordeadingpython__languag_age___'], ['qaiNnJ_lwordeadin__1_2_py__language________12_pyth_ram'], ['your_pr_th_ogrammingyo_ur_nprogr_amming_another__ex44ample____langu__age_____langu____12_your_programming__langu____h1y2_python__languingpython__languag_age___'], ['____12n_pythonaiNno_un_1_2_p'], ['_lwordeadin__12_python__lanuguage_____pgram_g'], ['AOqPHkjh'], ['_lwon__1__12_python__l__2_python__lanuguage_no_underscores'], ['_____12_pyth_h_python_program_leadin_lwnordeadin__12_python__languaage___g'], ['your_pr_th_ogrammingyo_ur_nprogr_amming_another__ex44ample____langu__age_____ur_programming__langu____h1y2_python__languingpython__languag_age___'], ['your_pryour_nprotrailing__12_python__layo_ur_nprogr_amming_eanother__ex44ample____langu__age___nguag__gramming_another__ex4no_underscores4ample____langu__age___iling___'], ['your_pr_th_ogrammingyo_ur_nprogr_amming_another__ex44ample____langu__age_____ur_programming__langu____h1y2_python__lang__1_d___12_pythonno_underscores__langu_ag_12_python__languag_2_pythonno_underscores__languag_uingpython__languag_age___']]
results = ['PythonProgram', 'PythonLanguage', 'ProgrammingLanguage', '___PythonProgram', '__12Python_Language___', 'YourProgramming_Langu_Age___', 'Another_Ex44ample___', '__', 'Word', 'NoUnderscores', '_Leading', 'Trailing_', '__MultipleConsecutive_Underscores__', '__12Python_Languag_', '___PYthonram', 'YourNprogramming_Langu_Age___', 'YourNprogrammingAnother_Ex44ample___Langu_Age___', '__12PythonnoUnderscores_Languag_', '_Lwordeading', 'YourNprogrammingAnother_Ex4noUnderscores4ample___Langu_Age___', 'YourProgramming_Langu___12Python_LanguagAge___', '__12Pyth_', '__1_12Python_Languag2PythonnoUnderscores_Languag_', '___Pgram', '_Lwordeadin_12Python_Language__G', 'YourPrtrailing___', '__12PythonnoUnderscores_LanguAg_', 'Ain', 'Worod', '_Lwordeadin_12Python_Languaage__G', 'Qainnja', 'AinLwordeading', '_Lwordeadin_12Python_Language__G', 'YourNprogrammi_12PythNgAnother_Ex4noUnderscores4ample___Langu_Age__YourNprogramming_Langu_Age___', 'YourPryourNprogrammingAnother_Ex4noUnderscores4ample___Langu_Age__Iling___', '__1___12PythonnoUnderscores_LanguAg12Python_Languag2PythonnoUnderscores_Languag_', 'Cvh', '_LeadinLwordeadin_12Python_Languaage__Gg', '_Th_', '_Lwordeadin_12Py_Language__G', 'Trailing_12Python_Languag__', 'YourPrThOgramming_Langu___12Python_LanguagAge___', 'YourPryourNprogrammingAnother_Ainex4noUnderscores4ample___Langu_Age__Iling___', '__12Python_LanguageG__', 'AinLwordeadin_12Python_LayourNprogrammingAnother_Ex4noUnderscores4ample___Langu_Age__Wordeading', '_Lwordeadin_12Py_Lawordnguaage__G', '__12PythonnoUnderscores_Lanuag_', '_____12PythRam', '__1___12PythonnoUnderscores_LanguALwordeadingg12Python_Languag2PythonnoUnderscores_Languag_', '___', '_Leadilng', '___PythonProgr_1___12PythonnoUnderscores_LanguAg12Python_L_LanguagM', '__12PythonnoUnderscores_LanguaG_', 'YourNprogrammingAnother_Ex44ample____12PythonnoUnderscores_Languag_Langu_Age___', '__12Python_L__', '__MultiprlneConsecutive_Underscores__', '___12Pyth_', '__1___12PythonnoUndnguALwordeadingg12Python_Languag2PythonnoUnderscores_Languag_', 'YourNprogrammingAnother_Ex44ample____12Py__12PythThonnoUnderscores_Languag_Langu_Age___', '_____MultipleConsecutive_Underscores_PythonProgram', 'YoUrNprogrAmmingAnother_Ex44ample___Langu_Age___', '_LeadinLwnordeadin_12Python_Languaage__Gg', 'Jzax', '_Leadin___12PythLwordeadin_12Python_Languaage__Gg', 'YoUrNprogrAmmingAnother_Ex44am_MultiprlneConsecutive_Underscores_Ple__1_12Python_Languag2PythonnoUnderscores_Languag__Langu_Age___', '__1___12PythonnoUnderscores_LanguAg12Python_Languag2PythonnoUnderscores_LanguagWord', '_Lwordeadin_12Python_Lanuguage__G', 'Trailing__PythonProgr_1___12PythonnoUnderscores_LanguAg12Python_L_LanguagM_12Python_Languag__', 'Trailianguag2PythonnoUnderscores_Languag__', '__12P', '_Leadil_MultipleConsecutive_Underscores_Ng', '__12Qainnjap', 'A_12PinLwordeading', '__Nnjap', '__12PeythonnoUnderscores_Lanuag_', 'Trailinig_', 'TrailiyourYoUrNprogrAmmingAnother_Ex44ample___Langu_Age__PryourNprogrammingAnother_Ainex4noUnderscores4ample___Langu_AyourNprogrammi_12PythNgAnother_Ex4noUnderscores4ample___Langu_Age__YourNprogramming_Langu_Age__Ge__Iling___', 'X', '_Leadin___12PythLwordeadin_12Python_Languaage__G1g', '_Lwordeadin_12Py_Lawordnguaage__G_12P', 'YourProgramming_Langu___1y2Python_LanguagAge___', 'YourPrThOgramming_Langu___12_Lwordeadingpython_LanguagAge___', 'YourPrThOgramming_Langu___12YourProgramming_Langu___1y2Python_LanguagAge___Lwordeadingpython_LanguagAge___', 'AinLwordeadiwordn_12Python_LayourNprogrammingAnother_Ex4noUnderscores4ample___Langu_Age__Wordeading', 'YourNprogrLwordeadingammi_12PythNgAnother_Ex4noUnderscores4ample___Langu_Age__YourNprogramming_Langu_Age___', '___PYthqainnjaonram', '12Python_L__', '_Lwordeadin_12Python_LanLwordeadin_12Python_Languaage__Gguaage__G', '__12PythonainLwordeading_L__', 'Trailing_12Python_LayoUrNprogrAmmingAnother_Ex44ample___Langu_Age__Nguag__', 'Your_12PythonnoUnderascores_LanguAg_NprogrammingAnother_Ex4noUnderscores4ample___Langu_Age', 'YourPryourNprotrailing_12Python_LayoUrNprogrAmmingAnother_Ex44ample___Langu_Age__Nguag_GrammingAnother_Ex4noUnderscores4ample___Langu_Age__Iling___', '__12nPythonnoUn_', '_____12Pyth_PythonProgram', '_Lwon_1_12Python_L_2Python_Lanuguage__G', 'YourProgramming_Langu___12Python_LanguagAg__Pgram___', '____12nPythonnoUn12P', '_Lwordeadin_12Python_LanuguLwordeadingage__G', 'AiyourPryourNprogrammingAnother_Ainex4noUnderscoLwordeadingres4ample___Langu_Age__Iling__N', '__1D__12PythonnoUnderscores_LanguAg12Python_Languag2PythonnoUnderscores_Languag_', 'YourPrThOgramming_Langu___12YourProgramming_Langu___1y2Python_Languingpython_LanguagAge___', 'YourNprogrammi_12_PythNgAnother_Ex4noUnderscores4ample___Langu_Age__YourNprogramming_Langu_Age___', 'YourPrThOgramming_Langu___12YourProgramming_Langu___1y2Pythotn_LanguagAge___Lwordeadingpython_LanguagAge___', 'QainnjLwordeadin_12Py_Language_______12PythRam', 'YourPrThOgrammingyoUrNprogrAmmingAnother_Ex44ample___Langu_Age____Langu___12YourProgramming_Langu___H1y2Python_Languingpython_LanguagAge___', '____12nPythonainnoUn12P', '_Lwordeadin_12Python_Lanuguage____PgramG', 'Aoqphkjh', '_Lwon_1_12Python_L_2Python_LanuguageNoUnderscores', '_____12PythHPythonProgramLeadinLwnordeadin_12Python_Languaage__G', 'YourPrThOgrammingyoUrNprogrAmmingAnother_Ex44ample___Langu_Age____UrProgramming_Langu___H1y2Python_Languingpython_LanguagAge___', 'YourPryourNprotrailing_12Python_LayoUrNprogrAmmingEanother_Ex44ample___Langu_Age__Nguag_GrammingAnother_Ex4noUnderscores4ample___Langu_Age__Iling___', 'YourPrThOgrammingyoUrNprogrAmmingAnother_Ex44ample___Langu_Age____UrProgramming_Langu___H1y2Python_Lang_1D__12PythonnoUnderscores_LanguAg12Python_Languag2PythonnoUnderscores_LanguagUingpython_LanguagAge___']

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
        func_name = "snake_to_camel"
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
        for test_case in ["assert snake_to_camel('python_program')=='PythonProgram'", "assert snake_to_camel('python_language')==('PythonLanguage')", "assert snake_to_camel('programming_language')==('ProgrammingLanguage')"]:
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
