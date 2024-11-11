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
inputs = [['python  program'], ['python   programming    language'], ['python                     program'], ['   python                     program'], ['    '], ['        '], ['          '], ['                        '], ['                           python   programming    language                             '], ['          python                     program                                       '], ['   python                     program                              '], ['python  program                                                          '], ['                   python   programming    language                                        python   programming    language                             '], ['          python                     program                                       python                     program                           '], ['   python                     program                              python                     program                          '], ['python  program                                                         python  program                                                             '], ['python\nprogram'], ['pythonprogramminglanguage'], [''], [' \t \n  python  \t \n  program  \t \n  python  \t \n  program  \t \n '], ['python\tprogram'], ['python\rprogram'], ['python\x0cprogram'], ['python\x0bprogram'], ['   python                     program                              python                     program                           '], [' \t \n  python  \t \n  program  \t \n    \t \n '], ['         '], ['python  prograpython\nprogramm                                                          '], ['python  program                                                         python  program                                                              '], ['                         '], ['python\rprogrpythonprogramminglanguageam'], [' \t \n  pytprogrpythonprogramminglanguageamhon  \t \n  program  \t \n  python  \t \n  program  \t \n '], ['                           python   programming g   language                             '], ['                   prython   programming    language                                        python   programming    language                             '], ['                                  '], ['python'], ['python\rprrogrpythonprogramminglanguageam'], ['language'], [' \t \n  python  \t \n m program  \t \n  python  \t \n  program  \t \n '], ['                              '], ['python  prograpython\nprogramm                                                        '], [' python\tprogram       '], ['  prython  '], ['pythyon\x0bprogram'], ['pytprogrammhonprogramminglanguage'], ['  prypython\x0bprogramon  '], ['python  program                                                         python  program                                                    \t \n  python  \t \n m program  \t \n  python  \t \n  program  \t \n           '], ['  pr                         ython  '], ['                     \t \n  python  \t \n  program  \t \n    \t \n      '], ['program'], ['ython\rprogram'], ['prython'], ['iEYji'], ['ythprogram'], ['   python                     program                              python                     program   r                        '], ['python   program                                                          '], [' \t \n  python  \t \n m program  \t \n  python  \t \n  program  \t \nython\rprogram'], ['python  program            pr                                             python  program                                                    \t \n  python  \t \n m program  \t \n  python  \t \n  program  \t \n           '], ['   python                     program                  ython\rprogram            python                     program                           '], ['                           python   programming    language        pytprogrammhonprogramminglanguage                      '], [' \t \n  python  \t \n m progroam  \t \n  pythoon  \t \n  program  \t \nython\rprogram'], ['          python                     program                       '], ['          python                     program                              python                     program                              python                     program                                       '], ['pythonprogramprogroamguage'], [' \t \n  pythonprogrpythonprogramminglanguageam  \t \n  program  \t \n    \t \n '], ['          python                     program                              python                     program                              python                     p rogram                                       '], ['          python                     program                              pyt hon                     program                              python                     program                                       '], ['  pr                         yt  '], ['                 python                     program                                                              '], ['pythonprogramprogroamguapytge'], ['  prythopythonprogramprogroamguapytgen  '], ['python  prograpython\nprogramm                                                      python\rprrogrpythonprogramminglanguageam  '], ['ythpm'], ['langythpr                         ogramuage'], ['ytmhtpm'], ['                           python   pro gramming g   language                             '], ['      '], [' pr         python                     program                                       '], ['python  program                                                         python  program       python\tprogram                                                               '], ['pythpython\tprogramon'], ['pythonprogrpythonprogramminglanguageam'], [' \t \n  python  \t \n  program \n    \t \n '], ['langythpr                          ogramuage'], ['programm'], [' \t \n  pythonprogrpythonprogramminglanguageam  \t \n  progra m  \t \n    \t \n '], ['pythonprogramprogroamgugapytge'], ['python  program                                                         python  program                                                            '], ['r  pr                         ython  ogram'], ['python  program                                                     pytprogrpythonprogramminglanguageamhon    python  program                                                          '], ['   python                     program                              python                                     \t \n  python  \t \n  program  \t \n    \t \n                 '], [' \t \n  pypthon  \t \n  program \n    \t \n '], ['gramming'], ['pro'], ['python\rprogrpythonpguageam'], ['   pyt hon     python\x0cprogram                program                              python                     program                           '], ['hon'], [' \t \n  pytprogrpythonprogramminglanguprageamhon  \t \n  program  \t \n  python  \t \n  program  \t \n '], ['python  program                     '], ['python  pprogrpythonprogrammi python\tprogram        python  program                                                          '], ['prograrm'], [' python  program                                                         python   program                                                    \t \n  python  \t \n m program  \t \n  python  \t \n  program  \t \n                  '], ['python   prograprogrammingm                                                          '], ['progrpythonpguageam'], ['prytprogrpythonprogramminglanguageamhon'], [' python  program                                                         python   program                                                    \t \n  py                           python   programming    language        pytprogrammhonprogramminglanguage                      thon  \t \n m program  \t \n  python  \t \n  program  \t \n                  '], ['   python pythpython\tprogramon                    program                              '], [' python  program                                                         python   program                                                    \t \n  pypythyonthon  \t \n m program  \t \n  python  \t \n  program  \t \n                  '], ['python  prograpython\nprogram m                                                        '], ['ogram'], ['                    pypythyonthonamming    language                             '], ['pythyon'], ['rogram'], ['pypythyonthon'], ['           '], [' python\tprogram   g    '], ['                           python   pro g                           python   programming g   language                             ramming g   language                             '], ['python  program                                                         python  program                                               '], ['pythonprogramprogroaamguage'], ['hhon'], ['python  program                                                         python  program                                                    \t \n  python  \t \n m program  \t \n  pyth     '], ['                    pypythyonthonammi   python                     propygram                              python                     program   r                        ng    language            '], ['python  program            pr                                             python  p pr         python                     program                                       rogram                                                    \t \n  python  \t \n m program  \t \n  python  \t \n  program  \t \n           '], ['  pprythopythonprogramprogroamguapytgen  '], ['python  program                                                         python  program               ']]
results = ['pythonprogram', 'pythonprogramminglanguage', 'pythonprogram', 'pythonprogram', '', '', '', '', 'pythonprogramminglanguage', 'pythonprogram', 'pythonprogram', 'pythonprogram', 'pythonprogramminglanguagepythonprogramminglanguage', 'pythonprogrampythonprogram', 'pythonprogrampythonprogram', 'pythonprogrampythonprogram', 'python\nprogram', 'pythonprogramminglanguage', '', '\t\npython\t\nprogram\t\npython\t\nprogram\t\n', 'python\tprogram', 'python\rprogram', 'python\x0cprogram', 'python\x0bprogram', 'pythonprogrampythonprogram', '\t\npython\t\nprogram\t\n\t\n', '', 'pythonprograpython\nprogramm', 'pythonprogrampythonprogram', '', 'python\rprogrpythonprogramminglanguageam', '\t\npytprogrpythonprogramminglanguageamhon\t\nprogram\t\npython\t\nprogram\t\n', 'pythonprogrammingglanguage', 'prythonprogramminglanguagepythonprogramminglanguage', '', 'python', 'python\rprrogrpythonprogramminglanguageam', 'language', '\t\npython\t\nmprogram\t\npython\t\nprogram\t\n', '', 'pythonprograpython\nprogramm', 'python\tprogram', 'prython', 'pythyon\x0bprogram', 'pytprogrammhonprogramminglanguage', 'prypython\x0bprogramon', 'pythonprogrampythonprogram\t\npython\t\nmprogram\t\npython\t\nprogram\t\n', 'prython', '\t\npython\t\nprogram\t\n\t\n', 'program', 'ython\rprogram', 'prython', 'iEYji', 'ythprogram', 'pythonprogrampythonprogramr', 'pythonprogram', '\t\npython\t\nmprogram\t\npython\t\nprogram\t\nython\rprogram', 'pythonprogramprpythonprogram\t\npython\t\nmprogram\t\npython\t\nprogram\t\n', 'pythonprogramython\rprogrampythonprogram', 'pythonprogramminglanguagepytprogrammhonprogramminglanguage', '\t\npython\t\nmprogroam\t\npythoon\t\nprogram\t\nython\rprogram', 'pythonprogram', 'pythonprogrampythonprogrampythonprogram', 'pythonprogramprogroamguage', '\t\npythonprogrpythonprogramminglanguageam\t\nprogram\t\n\t\n', 'pythonprogrampythonprogrampythonprogram', 'pythonprogrampythonprogrampythonprogram', 'pryt', 'pythonprogram', 'pythonprogramprogroamguapytge', 'prythopythonprogramprogroamguapytgen', 'pythonprograpython\nprogrammpython\rprrogrpythonprogramminglanguageam', 'ythpm', 'langythprogramuage', 'ytmhtpm', 'pythonprogrammingglanguage', '', 'prpythonprogram', 'pythonprogrampythonprogrampython\tprogram', 'pythpython\tprogramon', 'pythonprogrpythonprogramminglanguageam', '\t\npython\t\nprogram\n\t\n', 'langythprogramuage', 'programm', '\t\npythonprogrpythonprogramminglanguageam\t\nprogram\t\n\t\n', 'pythonprogramprogroamgugapytge', 'pythonprogrampythonprogram', 'rprythonogram', 'pythonprogrampytprogrpythonprogramminglanguageamhonpythonprogram', 'pythonprogrampython\t\npython\t\nprogram\t\n\t\n', '\t\npypthon\t\nprogram\n\t\n', 'gramming', 'pro', 'python\rprogrpythonpguageam', 'pythonpython\x0cprogramprogrampythonprogram', 'hon', '\t\npytprogrpythonprogramminglanguprageamhon\t\nprogram\t\npython\t\nprogram\t\n', 'pythonprogram', 'pythonpprogrpythonprogrammipython\tprogrampythonprogram', 'prograrm', 'pythonprogrampythonprogram\t\npython\t\nmprogram\t\npython\t\nprogram\t\n', 'pythonprograprogrammingm', 'progrpythonpguageam', 'prytprogrpythonprogramminglanguageamhon', 'pythonprogrampythonprogram\t\npypythonprogramminglanguagepytprogrammhonprogramminglanguagethon\t\nmprogram\t\npython\t\nprogram\t\n', 'pythonpythpython\tprogramonprogram', 'pythonprogrampythonprogram\t\npypythyonthon\t\nmprogram\t\npython\t\nprogram\t\n', 'pythonprograpython\nprogramm', 'ogram', 'pypythyonthonamminglanguage', 'pythyon', 'rogram', 'pypythyonthon', '', 'python\tprogramg', 'pythonprogpythonprogrammingglanguagerammingglanguage', 'pythonprogrampythonprogram', 'pythonprogramprogroaamguage', 'hhon', 'pythonprogrampythonprogram\t\npython\t\nmprogram\t\npyth', 'pypythyonthonammipythonpropygrampythonprogramrnglanguage', 'pythonprogramprpythonpprpythonprogramrogram\t\npython\t\nmprogram\t\npython\t\nprogram\t\n', 'pprythopythonprogramprogroamguapytgen', 'pythonprogrampythonprogram']

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
        func_name = "remove_all_spaces"
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
        for test_case in ["assert remove_all_spaces('python  program')==('pythonprogram')", "assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')", "assert remove_all_spaces('python                     program')==('pythonprogram')", "assert remove_all_spaces('   python                     program')=='pythonprogram'"]:
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
