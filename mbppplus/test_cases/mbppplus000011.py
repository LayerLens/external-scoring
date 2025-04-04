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
inputs = [[10], [5], [4], [3.5], [3.867338210205425], [4.017438434643324], [4.487089891527536], [2.6642890317066636], [5.887984312046749], [6.072194086423373], [3.642116465724614], [3.695469856787123], [4.141400647038825], [6.035071486216641], [3.271150304405481], [True], [84], [22], [5.654807546008664], [4.820511953305605], [6.577316776519947], [5.002581120259965], [6.969535253031167], [3.718379579422467], [6.322289576625546], [5.632673587071418], [5.3345589524375985], [6.725440141493683], [6.516564500761447], [8.993452545033046], [5.319836337788916], [6.043399656495942], [6.185578656467972], [4.217038121909214], [87], [4.005528059933441], [6.208925187146142], [85], [2.5181655036830994], [82], [4.1150925428079805], [5.484648231650928], [6.701524882996955], [21], [5.568439992700058], [88], [6.843276090129513], [3.4382125488926367], [6.388475480286746], [7.660073820339544], [2.769573374810499], [6.898645835852767], [7.826927755593033], [2.4985782322950842], [5.8695983810477985], [4.773486580932547], [3.001034234443808], [5.395838439745376], [3.577918724597513], [5.170120644837316], [6.99185332198154], [3.449246178521576], [5.5411783354818605], [6.436883135688541], [3.49384577169542], [5.015277110821801], [3.4631036701381923], [3.38643188343381], [1.9894160159593337], [1.837789735808722], [5.245639801999035], [4.465805726769371], [5.309603748296835], [3.3070853809486187], [8.803439557651616], [5.447584681806455], [2.6402987239829994], [5.81268658921342], [2.203529850744147], [2.413369661283704], [2.8444882558095452], [2.9679176613024727], [5.635919297098677], [7.106142255754484], [3.673088666908028], [11.501115163046252], [3.3172795455753574], [3.2120053514572735], [6.650019959695511], [23], [2.413305987922484], [3.453597614102104], [6.8216792009730725], [1.2676205462665886], [6.866125113001431], [4.423165960786375], [1.9765423457339029], [4.395641502661771], [2.9248802236697493], [1.6520153932594805], [8.099418388939899], [5.066661526673157], [6.345597309471013], [2.66964983620433]]
results = [40, 20, 16, 14.0, 15.4693528408217, 16.069753738573297, 17.948359566110145, 10.657156126826655, 23.551937248186995, 24.288776345693492, 14.568465862898456, 14.781879427148493, 16.5656025881553, 24.140285944866562, 13.084601217621923, 4, 336, 88, 22.619230184034656, 19.28204781322242, 26.309267106079787, 20.01032448103986, 27.87814101212467, 14.873518317689868, 25.289158306502184, 22.53069434828567, 21.338235809750394, 26.901760565974733, 26.06625800304579, 35.97381018013218, 21.279345351155666, 24.173598625983768, 24.742314625871888, 16.868152487636856, 348, 16.022112239733765, 24.835700748584568, 340, 10.072662014732398, 328, 16.460370171231922, 21.93859292660371, 26.80609953198782, 84, 22.27375997080023, 352, 27.373104360518052, 13.752850195570547, 25.553901921146984, 30.640295281358178, 11.078293499241996, 27.594583343411067, 31.307711022372132, 9.994312929180337, 23.478393524191194, 19.093946323730187, 12.004136937775232, 21.583353758981502, 14.311674898390052, 20.680482579349263, 27.96741328792616, 13.796984714086303, 22.164713341927442, 25.747532542754165, 13.97538308678168, 20.061108443287203, 13.85241468055277, 13.54572753373524, 7.957664063837335, 7.351158943234888, 20.98255920799614, 17.863222907077486, 21.23841499318734, 13.228341523794475, 35.213758230606466, 21.79033872722582, 10.561194895931997, 23.25074635685368, 8.814119402976589, 9.653478645134816, 11.377953023238181, 11.87167064520989, 22.543677188394707, 28.424569023017938, 14.692354667632111, 46.00446065218501, 13.26911818230143, 12.848021405829094, 26.600079838782044, 92, 9.653223951689936, 13.814390456408416, 27.28671680389229, 5.070482185066354, 27.464500452005723, 17.6926638431455, 7.9061693829356114, 17.582566010647085, 11.699520894678997, 6.608061573037922, 32.397673555759596, 20.26664610669263, 25.382389237884052, 10.67859934481732]

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
        func_name = "square_perimeter"
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
        for test_case in ['assert square_perimeter(10)==40', 'assert square_perimeter(5)==20', 'assert square_perimeter(4)==16']:
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
