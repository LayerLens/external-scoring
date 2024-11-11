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
inputs = [[['Red', 'Green', 'Blue', 'White', 'Black']], [['john', 'amal', 'joel', 'george']], [['jack', 'john', 'mary']], [[]], [['John', 'aMaL', 'jOeL', 'George']], [['John', '', 'George']], [['John']], [['']], [['John', '']], [['John', '', 'George', 'George']], [['John', 'George', '', 'George']], [['John', 'George']], [['', '']], [['aMaL', 'George']], [['John', '', 'George', 'George', '']], [['John', '', 'George', 'Geoerge', '', '']], [['John', '', 'George', 'George', 'George', '']], [['John', 'aMaL', 'jOeL', 'George', 'John']], [['aMaL', 'John']], [['John', '', 'George', 'jOeL', 'George']], [['aMaL', 'John', '', 'George']], [['aMaL', 'John', 'George']], [['John', '', 'George', 'jOeL', 'Geoerge', '']], [['John', '', 'George', '']], [['aMaL', 'John', '', 'George', 'John']], [['John', '', '']], [['JohnJohn', 'John']], [['aMaL', 'Geoorge', 'John', '', 'George', 'John']], [['John', '', 'GeorgGeoergee']], [['JohGeorgGeoergee', 'JohnJohn', 'John']], [['', 'John']], [['JohnGeorge', 'John', '', 'George', 'jOeL', 'Geoerge', '']], [['JohnJohn', 'Geoerge', 'John']], [['JohaMaLnJohn', 'JohnJohn']], [['oJohn', '', 'George', 'George', '']], [['John', 'Geoorge', 'John']], [['John', 'JaMaLn', '', 'George', 'George', '']], [['aMaL', 'John', 'aMaL', 'George', 'John']], [['John', 'aMaL', 'jOeL', 'aM', 'George', 'jOeL']], [['John', 'aMaL', 'Geoorge', 'jOeL', 'George', 'John', 'aMaL']], [['John', 'aMaL', 'jOeL', 'aM', 'George', 'jOeL', 'jOeL']], [['aMaL', 'John', 'GeorgGeoergee']], [['John', '', 'JohnGeorge', 'George']], [['', '', '']], [['aMaL', 'Geoorge', 'John', '', 'George', 'John', 'George']], [['aMaL', 'John', 'John']], [['Geoerge', 'John', '', 'George']], [['aMaL', 'John', 'George', 'John']], [['John', 'George', 'jOeL', 'George']], [['JohnJohn', 'JaMaLn']], [['John', '', 'George', 'jOeL', 'Geoerge', 'JohnGeorge', 'George', 'jOeL']], [['aMaL', 'John', 'aMaL', 'John']], [['oJohn', '', 'George', 'Geoerge', '', '']], [['Geoorge', 'George', 'jOeL', 'George']], [['aMaL', 'Geoorge', 'Joh', 'aMaL', 'George', 'nJohn']], [['aMaL', 'aMaL', 'George', 'John', 'George']], [['', 'George', 'Geoerge', '', '']], [['aM', 'aMaL', 'Geoorge', 'John', '', 'George', 'John', 'George', 'aM']], [['JohnGeorge', 'John', '', 'GeorgGeoergee', 'jOeL', 'Geoerge', '']], [['aMaL', 'Geoeorge', 'John', '', 'aMaLL', 'George', 'John']], [['John', 'aMaL', 'JoJohnGeorgehn', 'Geoorge', 'jOeL', 'George', 'John', 'aMaL']], [['aMaL', 'John', 'GeorgGeoergee', 'Joh', 'John']], [['GeorgGeoergee', 'Geoerge', 'John', '', 'George']], [['GeorgGeoergee', 'Geoerge', '', 'George', 'John']], [['JohaMaLnJohn', 'FTlwsSD', 'wPcq', 'vI', 'JohaMaLnJohn', 'SqPn', 'aM', 'JocyrPAB', 'qMHbL']], [['John', 'George', 'George', '']], [['John', '', 'George', 'jOeL', 'Geoerge', 'GeorgGeoergee', 'George', 'Geoorge', 'jOeL']], [['aMaL', 'John', 'aMaL']], [['JohaMaLnJohn', 'JohnJohn', 'JohaMaLnJohn']], [['John', '', 'George', 'Geoerge', '', 'Geoerge', '', '']], [['John', 'George', 'George', 'George', '']], [['aMaL', 'John', '', 'George', '']], [['', 'George', '', 'orge', 'SqPn']], [['vI', 'John', '', 'George', 'jOeL', 'Geoerge', '', 'John']], [['JohnJohnJohnJohn', 'John', 'JohnJohn', 'GeGeoergeoerge', 'Geoerge', 'JohnJohnJohnJohn']], [['aMaL', 'John', 'George', 'John', 'John']], [['JohaMaLnJohn', 'FTlwsSD', 'wPcq', 'vI', 'JohaMaLnJohn', 'SqPn', 'aM', 'JocyrPAB']], [['', 'JohnGeorge', '', '', '']], [['John', '', '', '', '']], [['John', 'John']], [['JohGeorgen', 'JohGeorgGeoergee', 'JohnJohn', 'John']], [['aGeorgeMaL']], [['John', 'George', '', 'GeorgGeoergee', 'John']], [['', 'George', 'Geoerge', 'orge', '', '', 'aGeorgeMaL', 'George']], [['aMaL', 'John', 'aMJohGeorgenaL', '', 'George']], [['John', '', 'George', 'aM', 'Ge', 'jOeL', 'Geoerge', 'JohnGeorge', 'George', 'jOeL']], [['John', 'Geoerge', '', '', '']], [['aMaL', 'JaMaLn', 'JaMaLn']], [['', 'George', 'aGeorgeMaL', 'Geoerge', '', '']], [['John', '', 'George', '', '']], [['', 'aMaL', 'jOeL', 'George']], [['oJohn', '', 'George', 'Geoerge', '', 'Geoerege', '']], [['aMaL', 'John', 'aMaL', 'JohaMaLnJohn', 'aMaL', 'John']], [['', '', '', '']], [['aMaL', 'John', 'JoGeorgGeoergee', 'GeorgGeoergee', 'Joh', 'John']], [['nJohn', 'JohnGeorge', '', '', '']], [['', 'George', 'aGeorgeMaL', '', '']], [['George']], [['aMaL']], [['aMaL', 'aMaL', 'John', '', '']], [['John', 'aMaL', 'John', 'aMaL', 'George', 'John']], [['Geoorge', 'George', 'jOeL', 'Geoorge']], [['nJohn', 'JohnGeorge', '', 'JohGeorgGeoergee', '', '']], [['JohGeorgGeoergee', 'John', 'aMaL', 'John', 'aMaL', 'George', 'John']], [['aMaL', 'JocyrPAB', 'Geoeorge', 'John', '', 'aMaLL', 'George', 'John']], [['Geoerge', 'Geooerge', 'John', '', 'George']], [['John', 'aMaL', 'aMaGeoeregeL', 'jOeL', 'aM', 'George', 'jOeL', 'jOeL']], [['aMaL', 'Geoeorge', 'John', '', 'aMaLL', 'GeorgaMaLe', 'John']], [['aMaL', 'Geoorge', 'John', '', 'George', 'John', 'GeorgGeoergee']]]
results = [['deR', 'neerG', 'eulB', 'etihW', 'kcalB'], ['nhoj', 'lama', 'leoj', 'egroeg'], ['kcaj', 'nhoj', 'yram'], [], ['nhoJ', 'LaMa', 'LeOj', 'egroeG'], ['nhoJ', '', 'egroeG'], ['nhoJ'], [''], ['nhoJ', ''], ['nhoJ', '', 'egroeG', 'egroeG'], ['nhoJ', 'egroeG', '', 'egroeG'], ['nhoJ', 'egroeG'], ['', ''], ['LaMa', 'egroeG'], ['nhoJ', '', 'egroeG', 'egroeG', ''], ['nhoJ', '', 'egroeG', 'egreoeG', '', ''], ['nhoJ', '', 'egroeG', 'egroeG', 'egroeG', ''], ['nhoJ', 'LaMa', 'LeOj', 'egroeG', 'nhoJ'], ['LaMa', 'nhoJ'], ['nhoJ', '', 'egroeG', 'LeOj', 'egroeG'], ['LaMa', 'nhoJ', '', 'egroeG'], ['LaMa', 'nhoJ', 'egroeG'], ['nhoJ', '', 'egroeG', 'LeOj', 'egreoeG', ''], ['nhoJ', '', 'egroeG', ''], ['LaMa', 'nhoJ', '', 'egroeG', 'nhoJ'], ['nhoJ', '', ''], ['nhoJnhoJ', 'nhoJ'], ['LaMa', 'egrooeG', 'nhoJ', '', 'egroeG', 'nhoJ'], ['nhoJ', '', 'eegreoeGgroeG'], ['eegreoeGgroeGhoJ', 'nhoJnhoJ', 'nhoJ'], ['', 'nhoJ'], ['egroeGnhoJ', 'nhoJ', '', 'egroeG', 'LeOj', 'egreoeG', ''], ['nhoJnhoJ', 'egreoeG', 'nhoJ'], ['nhoJnLaMahoJ', 'nhoJnhoJ'], ['nhoJo', '', 'egroeG', 'egroeG', ''], ['nhoJ', 'egrooeG', 'nhoJ'], ['nhoJ', 'nLaMaJ', '', 'egroeG', 'egroeG', ''], ['LaMa', 'nhoJ', 'LaMa', 'egroeG', 'nhoJ'], ['nhoJ', 'LaMa', 'LeOj', 'Ma', 'egroeG', 'LeOj'], ['nhoJ', 'LaMa', 'egrooeG', 'LeOj', 'egroeG', 'nhoJ', 'LaMa'], ['nhoJ', 'LaMa', 'LeOj', 'Ma', 'egroeG', 'LeOj', 'LeOj'], ['LaMa', 'nhoJ', 'eegreoeGgroeG'], ['nhoJ', '', 'egroeGnhoJ', 'egroeG'], ['', '', ''], ['LaMa', 'egrooeG', 'nhoJ', '', 'egroeG', 'nhoJ', 'egroeG'], ['LaMa', 'nhoJ', 'nhoJ'], ['egreoeG', 'nhoJ', '', 'egroeG'], ['LaMa', 'nhoJ', 'egroeG', 'nhoJ'], ['nhoJ', 'egroeG', 'LeOj', 'egroeG'], ['nhoJnhoJ', 'nLaMaJ'], ['nhoJ', '', 'egroeG', 'LeOj', 'egreoeG', 'egroeGnhoJ', 'egroeG', 'LeOj'], ['LaMa', 'nhoJ', 'LaMa', 'nhoJ'], ['nhoJo', '', 'egroeG', 'egreoeG', '', ''], ['egrooeG', 'egroeG', 'LeOj', 'egroeG'], ['LaMa', 'egrooeG', 'hoJ', 'LaMa', 'egroeG', 'nhoJn'], ['LaMa', 'LaMa', 'egroeG', 'nhoJ', 'egroeG'], ['', 'egroeG', 'egreoeG', '', ''], ['Ma', 'LaMa', 'egrooeG', 'nhoJ', '', 'egroeG', 'nhoJ', 'egroeG', 'Ma'], ['egroeGnhoJ', 'nhoJ', '', 'eegreoeGgroeG', 'LeOj', 'egreoeG', ''], ['LaMa', 'egroeoeG', 'nhoJ', '', 'LLaMa', 'egroeG', 'nhoJ'], ['nhoJ', 'LaMa', 'nhegroeGnhoJoJ', 'egrooeG', 'LeOj', 'egroeG', 'nhoJ', 'LaMa'], ['LaMa', 'nhoJ', 'eegreoeGgroeG', 'hoJ', 'nhoJ'], ['eegreoeGgroeG', 'egreoeG', 'nhoJ', '', 'egroeG'], ['eegreoeGgroeG', 'egreoeG', '', 'egroeG', 'nhoJ'], ['nhoJnLaMahoJ', 'DSswlTF', 'qcPw', 'Iv', 'nhoJnLaMahoJ', 'nPqS', 'Ma', 'BAPrycoJ', 'LbHMq'], ['nhoJ', 'egroeG', 'egroeG', ''], ['nhoJ', '', 'egroeG', 'LeOj', 'egreoeG', 'eegreoeGgroeG', 'egroeG', 'egrooeG', 'LeOj'], ['LaMa', 'nhoJ', 'LaMa'], ['nhoJnLaMahoJ', 'nhoJnhoJ', 'nhoJnLaMahoJ'], ['nhoJ', '', 'egroeG', 'egreoeG', '', 'egreoeG', '', ''], ['nhoJ', 'egroeG', 'egroeG', 'egroeG', ''], ['LaMa', 'nhoJ', '', 'egroeG', ''], ['', 'egroeG', '', 'egro', 'nPqS'], ['Iv', 'nhoJ', '', 'egroeG', 'LeOj', 'egreoeG', '', 'nhoJ'], ['nhoJnhoJnhoJnhoJ', 'nhoJ', 'nhoJnhoJ', 'egreoegreoeGeG', 'egreoeG', 'nhoJnhoJnhoJnhoJ'], ['LaMa', 'nhoJ', 'egroeG', 'nhoJ', 'nhoJ'], ['nhoJnLaMahoJ', 'DSswlTF', 'qcPw', 'Iv', 'nhoJnLaMahoJ', 'nPqS', 'Ma', 'BAPrycoJ'], ['', 'egroeGnhoJ', '', '', ''], ['nhoJ', '', '', '', ''], ['nhoJ', 'nhoJ'], ['negroeGhoJ', 'eegreoeGgroeGhoJ', 'nhoJnhoJ', 'nhoJ'], ['LaMegroeGa'], ['nhoJ', 'egroeG', '', 'eegreoeGgroeG', 'nhoJ'], ['', 'egroeG', 'egreoeG', 'egro', '', '', 'LaMegroeGa', 'egroeG'], ['LaMa', 'nhoJ', 'LanegroeGhoJMa', '', 'egroeG'], ['nhoJ', '', 'egroeG', 'Ma', 'eG', 'LeOj', 'egreoeG', 'egroeGnhoJ', 'egroeG', 'LeOj'], ['nhoJ', 'egreoeG', '', '', ''], ['LaMa', 'nLaMaJ', 'nLaMaJ'], ['', 'egroeG', 'LaMegroeGa', 'egreoeG', '', ''], ['nhoJ', '', 'egroeG', '', ''], ['', 'LaMa', 'LeOj', 'egroeG'], ['nhoJo', '', 'egroeG', 'egreoeG', '', 'egereoeG', ''], ['LaMa', 'nhoJ', 'LaMa', 'nhoJnLaMahoJ', 'LaMa', 'nhoJ'], ['', '', '', ''], ['LaMa', 'nhoJ', 'eegreoeGgroeGoJ', 'eegreoeGgroeG', 'hoJ', 'nhoJ'], ['nhoJn', 'egroeGnhoJ', '', '', ''], ['', 'egroeG', 'LaMegroeGa', '', ''], ['egroeG'], ['LaMa'], ['LaMa', 'LaMa', 'nhoJ', '', ''], ['nhoJ', 'LaMa', 'nhoJ', 'LaMa', 'egroeG', 'nhoJ'], ['egrooeG', 'egroeG', 'LeOj', 'egrooeG'], ['nhoJn', 'egroeGnhoJ', '', 'eegreoeGgroeGhoJ', '', ''], ['eegreoeGgroeGhoJ', 'nhoJ', 'LaMa', 'nhoJ', 'LaMa', 'egroeG', 'nhoJ'], ['LaMa', 'BAPrycoJ', 'egroeoeG', 'nhoJ', '', 'LLaMa', 'egroeG', 'nhoJ'], ['egreoeG', 'egreooeG', 'nhoJ', '', 'egroeG'], ['nhoJ', 'LaMa', 'LegereoeGaMa', 'LeOj', 'Ma', 'egroeG', 'LeOj', 'LeOj'], ['LaMa', 'egroeoeG', 'nhoJ', '', 'LLaMa', 'eLaMagroeG', 'nhoJ'], ['LaMa', 'egrooeG', 'nhoJ', '', 'egroeG', 'nhoJ', 'eegreoeGgroeG']]

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
        func_name = "reverse_string_list"
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
        for test_case in ["assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']", "assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']", "assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']"]:
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
