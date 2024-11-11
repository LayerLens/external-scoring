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
inputs = [[35], [6], [9], [-5], [3.14], [0], [1], [-10], [2.0], [1000000], [99999999], [1000000000000], [3.7831588542515604], [5.302859454099729], [True], [2.4682613401002937], [99999998], [1.3453957712310967], [1.0399013203829814], [99999997], [5.684417641308899], [99999996], [4.510369394904734], [3.6621080850729113], [3.322051512362575], [1000000000001], [-11], [2.3742619906307163], [2.6748360710113177], [3.4473095447178936], [5.57812470410088], [99999995], [4.647261498089122], [1.5329222521720727], [2.6809843384176872], [-1], [False], [1.5107938841218733], [0.875196021901653], [4.529854518921115], [1.7032459621984142], [1.8504217376600358], [2.188160542701604], [1.8956297256654226], [2.4314765544566113], [5.813827850518426], [2.3809692137960456], [2.446463005958287], [1.9423279622572451], [2.1946783538521406], [2.6687036689581713], [2.0326735919423498], [100000000], [2.468678626532637], [1000001], [2.5238311325906344], [1.7822986116186494], [2.3311279543074095], [-22.844596598850202], [2.5605349010057803], [6.083079662936755], [100000001], [1.5746458078326158], [6.588039035035163], [3.1483586672721007], [1000000000002], [3.456020835359328], [34.43923911097559], [1.0089233418138062], [4.2295065796525115], [-78.55181920500208], [1.0803737520419845], [2.605728433563439], [38.98925404921724], [4.4174458158812255], [1.644335866314361], [1.8218151507901879], [3.037371820443729], [2.709277112928487], [4.378962886905937], [34.821872058003486], [-77.542809657578], [2.5759758416813416], [-12], [3.1543786398736704], [0.7865023181429288], [3.2249050005349247], [0.9910005166913101], [3.195728446958819], [1.614635244145928], [2.192134061504989], [-9], [3.47933130145955], [3.806186148917977], [1.4663753283678982], [0.945455886591849], [2.805849529482408], [-6], [1.909977828399661], [2.3945594411492657], [2.943996722081795], [4.945353788299947], [-80], [2.847513147814003], [2.040611668519119], [2.6516104349052276], [3.547091908942516], [999999999999], [-21.849993780773154], [2.09983974207191], [2.7416667760599114], [2.953394448977245]]
results = [36, 9, 16, 0, 4, 1, 4, 0, 4, 1002001, 100000000, 1000002000001, 4, 9, 4, 4, 100000000, 4, 4, 100000000, 9, 100000000, 9, 4, 4, 1000002000001, 0, 4, 4, 4, 9, 100000000, 9, 4, 4, 0, 1, 4, 1, 9, 4, 4, 4, 4, 4, 9, 4, 4, 4, 4, 4, 4, 100020001, 4, 1002001, 4, 4, 4, 0, 4, 9, 100020001, 4, 9, 4, 1000002000001, 4, 36, 4, 9, 0, 4, 4, 49, 9, 4, 4, 4, 4, 9, 36, 0, 4, 0, 4, 1, 4, 1, 4, 4, 4, 0, 4, 4, 4, 1, 4, 0, 4, 4, 4, 9, 0, 4, 4, 4, 4, 1000000000000, 0, 4, 4, 4]

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
        func_name = "next_Perfect_Square"
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
        for test_case in ['assert next_Perfect_Square(35) == 36', 'assert next_Perfect_Square(6) == 9', 'assert next_Perfect_Square(9) == 16']:
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
