import numpy as np
['import math']

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
inputs = [[5, 12], [10, 15], [19, 17], [3.5, 8.2], [2.2, 4.7], [6.9, 2.3], [1000, 2000], [1.234, 5.678], [10.567, 7.89], [456.789, 123.456], [987.654, 321.098], [10.567, 10.567], [987.654, 3.5], [10.567, 1.234], [456.3381444428326, 123.456], [456.789, 3.5], [1.234, 1.234], [321.098, 168.94178585748298], [10.062162623290103, 10.062162623290103], [456.789, 5.678], [456.789, 388.7528921290703], [456.789, 4.222046540766119], [987.654, 3.3318554794950845], [11.081962312637511, 11.081962312637511], [1.234, 1.8683657303042116], [1.7994502519997089, 1.6146639261873168], [418.9192385760365, 5.678], [418.9192385760365, 2.3], [456.789, 4.928071889937876], [3.212703762340813, 2.3], [7.6622497831772085, 7.89], [2.378587054952834, 4.7], [10.062162623290103, 456.3381444428326], [987.654, 6.9], [1.7994502519997089, 4.928071889937876], [987.654, 2.705632224815191], [1.88487391345283, 3.5], [4.973822145742326, 5.678], [1.234, 2.2], [1.234, 8.2], [1.88487391345283, 7.89], [418.9192385760365, 2.1821425592540242], [7.6622497831772085, 123.456], [3.5, 5.307457074898993], [3.212703762340813, 3.212703762340813], [7.89, 10.999978928538894], [123.456, 122.94268835587204], [1.234, 1.0143813429712258], [4.462763515521088, 4.928071889937876], [4.886498233097042, 4.886498233097042], [5.678, 5.678], [8.164810097091653, 7.6622497831772085], [14.696773684181256, 4.7], [2.4747825820340905, 2.3], [10.567, 7.194070932537068], [7.89, 4.886498233097042], [7.6622497831772085, 183.12244565865572], [122.8191510847481, 117.12499057645937], [5.722833818810574, 2.1821425592540242], [7.89, 4.195516279600971], [4.462763515521088, 1.7994502519997089], [4.195516279600971, 168.94178585748298], [456.3381444428326, 388.7528921290703], [4.584255552437924, 2.3], [1.7803467811689282, 1.6146639261873168], [10.567, 321.098], [3.930531091978424, 4.7], [3.930531091978424, 1.0143813429712258], [3.5, 3.5], [1.0725091193999579, 1.0143813429712258], [1.88487391345283, 3.3318554794950845], [4.462763515521088, 1.3297034614252445], [0.5561103655828992, 1.0143813429712258], [10.999978928538894, 4.195516279600971], [4.615962386993007, 2.1821425592540242], [11.980439670399893, 7.787216662850671], [1.474604255550374, 5.184525170511173], [6.695658956768952, 6.695658956768952], [1.3834538242508858, 1.88487391345283], [17.146104995225684, 456.3381444428326], [4.886498233097042, 1.8683657303042116], [1.88487391345283, 4.615962386993007], [12.052676270488469, 14.696773684181256], [17.146104995225684, 7.89], [123.456, 122.84983443418058], [388.7528921290703, 1.234], [0.5561103655828992, 122.86850838444352], [456.789, 1.6616184514399182], [418.9192385760365, 8.2], [1.0725091193999579, 16.746701140899006], [True, True], [2.8997575884253255, 987.654], [6.695658956768952, 1.8683657303042116], [2.4484913418894525, 3.5], [456.789, 3.1688227707140735], [456.789, 2.4747825820340905], [7.6622497831772085, 4.973822145742326], [456.3381444428326, 456.3381444428326], [4.973822145742326, 388.7528921290703], [5.722833818810574, 12.052676270488469], [987.654, 2.099492328965713], [7.89, 4.928071889937876], [2.4747825820340905, 122.84983443418058], [10.567, 456.8519227964984], [1.88487391345283, 2.2], [4.886498233097042, 3.212703762340813], [3.776854528744753, 4.321001736599134], [1.544964412295513, 2.2], [456.3381444428326, 1.0143813429712258], [418.9192385760365, 418.9192385760365], [6.695658956768952, 4.886498233097042]]
results = [314.15926535897927, 1570.7963267948965, 6426.651371693521, 105.19099401769823, 23.82164989462021, 114.67127344868103, 2094395102.3931954, 9.05428843954464, 922.5906225873124, 26975660.904739592, 328001532.18564004, 1235.6166170950735, 3575249.184516067, 144.29364109920704, 26922436.660926428, 764764.8811446067, 1.967768921169089, 18240674.76015016, 1066.8481639713873, 1240667.1414683077, 84944159.81248873, 922535.1202674282, 3403489.5959971976, 1425.2092245652937, 2.979345232957873, 5.475079753009438, 1043481.1716349394, 422685.2227475098, 1076804.6609086907, 24.85981072626636, 485.0854320827397, 27.846112787917676, 48383.586091332596, 7048348.392331676, 16.710342126540883, 2763802.6872488298, 13.021507639123675, 147.0972350659654, 3.508177979393838, 13.075936105013394, 29.354198649338795, 401025.83205439494, 7590.2036886193555, 68.08496163596222, 34.72487280493758, 717.0913397915556, 1962256.2757118903, 1.6175592227816376, 102.78113292105007, 122.18611496680354, 191.6967643770718, 534.9055446017102, 1063.0911162011912, 14.75130883100813, 841.2144969057871, 318.5520252015669, 11258.559021087076, 1850164.6096911286, 74.8400393976022, 273.5067412039093, 37.529796574848795, 3114.1284337694856, 84776561.00227496, 50.616730979387576, 5.359446845986977, 37546.51504835752, 76.03769584001937, 16.41089787715669, 44.89859500755413, 1.2218892896451155, 12.395937593914661, 27.73263687434789, 0.3285124636016199, 531.615622536235, 48.68960600334884, 1170.4594954098457, 11.805613776134363, 314.3464732881296, 3.777811273396877, 140490.30255193845, 46.71818939312254, 17.17336842403914, 2235.7210096869608, 2429.050695484118, 1960774.258415863, 195294.96363961083, 39.79158002867054, 363070.6964351813, 1506964.707186774, 20.172507018923532, 1.0471975511965976, 8696.746922511824, 87.71566501901751, 21.973225244053754, 692401.248460992, 540750.5163451555, 305.79577498987527, 99515088.69335516, 10071.235568172551, 413.3656452025127, 2144630.924866401, 321.26222214627944, 787.911238076876, 53420.44358466822, 8.18494765887774, 80.33314912525033, 64.546630233262, 5.499057475644073, 221209.317134593, 76987378.98727356, 229.41035321846311]

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
        func_name = "volume_cone"
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
        for test_case in ['assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)', 'assert math.isclose(volume_cone(10,15), 1570.7963267948965, rel_tol=0.001)', 'assert math.isclose(volume_cone(19,17), 6426.651371693521, rel_tol=0.001)']:
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