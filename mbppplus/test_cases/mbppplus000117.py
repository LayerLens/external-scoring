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
inputs = [[(1+0j)], [(4+0j)], [(5+0j)], [(1+2j)], [(-3+4j)], [(2-5j)], [(2+3j)], [(-4-2j)], [5j], [(1-1j)], [(6+0j)], [(3+0j)], [-3j], [(0.5+0.5j)], [(3-4j)], [(-2+3j)], [1j], [(4+3j)], [0j], [(4+2j)], [(-1-4j)], [6j], [(2+2j)], [(5-3j)], [(-3+5j)], [(69.02761442257642+0j)], [4.480282583176166j], [(-0-2.8866591213002657j)], [1.8339464931468865j], [1.1632560023978717j], [5.586903526274092j], [4.9325950056031465j], [5.982229804759806j], [(69.9026432060336+0j)], [(68.89398657521126+0j)], [(-0-1.7734628811885071j)], [(-0-1.3923179090484485j)], [(-0-2.4244997922730285j)], [1.0653576332470696j], [5.654751542806139j], [(-0-3.3513367267140888j)], [(69.95759903803496+0j)], [(64.60629626821124+0j)], [2.523101886352822j], [2.4723827442830064j], [1.5954448547729851j], [0.28095482047285447j], [(-0-2.8437961395593727j)], [2.718200483696477j], [(81.61240705438665+0j)], [2.427286174918197j], [(-0-3.1383875539106447j)], [0.7671828756486694j], [0.5646275311487383j], [1.3241308894242676j], [1.9653544762525699j], [0.483965259991584j], [1.2806038249577065j], [(-0-2.742593821091259j)], [(39.14336844635568+0j)], [(-0-1.554220231492268j)], [(-0-0.06002590618992332j)], [0.359476671590649j], [(-0-1.4780861733597002j)], [(84.71154294399365+0j)], [(65.87093338696945+0j)], [1.4148452935192064j], [(63.68365464704737+0j)], [(-0-2.453133050376202j)], [(-0-3.365888737477067j)], [5.119849769359963j], [(-0-2.9770669277716193j)], [1.0268278439540401j], [(-0-2.2848792242860476j)], [(-0-2.5315094242643674j)], [5.946927975746798j], [(-0-2.6888219799266664j)], [(-0-1.4026270187478314j)], [(-0-0.7647685359700735j)], [5.799372252854404j], [(69.20131118955786+0j)], [2.824626575647983j], [0.11045819635759302j], [1.781743445228249j], [(-0-1.0570051223587917j)], [(-0-0.40367510752848546j)], [(-0-1.0945668230765322j)], [1.4422081370591302j], [(66.37710776621364+0j)], [0.7954150660711281j], [2.0205767116812545j], [(83.7742294602561+0j)], [(-0-0.5105311516531497j)], [(64.07916373840905+0j)], [0.6460925139263856j], [(-0-0.20205617139005683j)], [3.4342717587111635j], [1.534974182792563j], [1.0987650448789927j], [0.31022207996584994j], [5.929383106401057j], [2.1996207875536746j], [(-0-1.9502206049649806j)], [(-0-0.05372412411858196j)], [1.8654862042995812j], [(-0-1.2613497262525142j)], [(-58.97820691559647+0j)], [2.3409994111314996j], [(69.52491267479274+0j)], [1.2048735288511763j], [(-0-0.8775801175894351j)], [2.4348272708295844j], [6.428277805264403j], [3.3735223968848786j], [(-0-3.102461443790692j)], [6.246725845665113j], [5.617377472771601j], [(-0-3.178715770909393j)], [(68.96072133838915+0j)], [0.8803089947178533j], [(-0-1.4610235926529014j)], [1.307920964727237j], [(-0-1.1043456934929188j)]]
results = [(1.0, 0.0), (4.0, 0.0), (5.0, 0.0), (2.23606797749979, 1.1071487177940904), (5.0, 2.214297435588181), (5.385164807134504, -1.1902899496825317), (3.605551275463989, 0.982793723247329), (4.47213595499958, -2.677945044588987), (5.0, 1.5707963267948966), (1.4142135623730951, -0.7853981633974483), (6.0, 0.0), (3.0, 0.0), (3.0, -1.5707963267948966), (0.7071067811865476, 0.7853981633974483), (5.0, -0.9272952180016122), (3.605551275463989, 2.158798930342464), (1.0, 1.5707963267948966), (5.0, 0.6435011087932844), (0.0, 0.0), (4.47213595499958, 0.4636476090008061), (4.123105625617661, -1.8157749899217608), (6.0, 1.5707963267948966), (2.8284271247461903, 0.7853981633974483), (5.830951894845301, -0.5404195002705842), (5.830951894845301, 2.1112158270654806), (69.02761442257642, 0.0), (4.480282583176166, 1.5707963267948966), (2.8866591213002657, -1.5707963267948966), (1.8339464931468865, 1.5707963267948966), (1.1632560023978717, 1.5707963267948966), (5.586903526274092, 1.5707963267948966), (4.9325950056031465, 1.5707963267948966), (5.982229804759806, 1.5707963267948966), (69.9026432060336, 0.0), (68.89398657521126, 0.0), (1.7734628811885071, -1.5707963267948966), (1.3923179090484485, -1.5707963267948966), (2.4244997922730285, -1.5707963267948966), (1.0653576332470696, 1.5707963267948966), (5.654751542806139, 1.5707963267948966), (3.3513367267140888, -1.5707963267948966), (69.95759903803496, 0.0), (64.60629626821124, 0.0), (2.523101886352822, 1.5707963267948966), (2.4723827442830064, 1.5707963267948966), (1.5954448547729851, 1.5707963267948966), (0.28095482047285447, 1.5707963267948966), (2.8437961395593727, -1.5707963267948966), (2.718200483696477, 1.5707963267948966), (81.61240705438665, 0.0), (2.427286174918197, 1.5707963267948966), (3.1383875539106447, -1.5707963267948966), (0.7671828756486694, 1.5707963267948966), (0.5646275311487383, 1.5707963267948966), (1.3241308894242676, 1.5707963267948966), (1.9653544762525699, 1.5707963267948966), (0.483965259991584, 1.5707963267948966), (1.2806038249577065, 1.5707963267948966), (2.742593821091259, -1.5707963267948966), (39.14336844635568, 0.0), (1.554220231492268, -1.5707963267948966), (0.06002590618992332, -1.5707963267948966), (0.359476671590649, 1.5707963267948966), (1.4780861733597002, -1.5707963267948966), (84.71154294399365, 0.0), (65.87093338696945, 0.0), (1.4148452935192064, 1.5707963267948966), (63.68365464704737, 0.0), (2.453133050376202, -1.5707963267948966), (3.365888737477067, -1.5707963267948966), (5.119849769359963, 1.5707963267948966), (2.9770669277716193, -1.5707963267948966), (1.0268278439540401, 1.5707963267948966), (2.2848792242860476, -1.5707963267948966), (2.5315094242643674, -1.5707963267948966), (5.946927975746798, 1.5707963267948966), (2.6888219799266664, -1.5707963267948966), (1.4026270187478314, -1.5707963267948966), (0.7647685359700735, -1.5707963267948966), (5.799372252854404, 1.5707963267948966), (69.20131118955786, 0.0), (2.824626575647983, 1.5707963267948966), (0.11045819635759302, 1.5707963267948966), (1.781743445228249, 1.5707963267948966), (1.0570051223587917, -1.5707963267948966), (0.40367510752848546, -1.5707963267948966), (1.0945668230765322, -1.5707963267948966), (1.4422081370591302, 1.5707963267948966), (66.37710776621364, 0.0), (0.7954150660711281, 1.5707963267948966), (2.0205767116812545, 1.5707963267948966), (83.7742294602561, 0.0), (0.5105311516531497, -1.5707963267948966), (64.07916373840905, 0.0), (0.6460925139263856, 1.5707963267948966), (0.20205617139005683, -1.5707963267948966), (3.4342717587111635, 1.5707963267948966), (1.534974182792563, 1.5707963267948966), (1.0987650448789927, 1.5707963267948966), (0.31022207996584994, 1.5707963267948966), (5.929383106401057, 1.5707963267948966), (2.1996207875536746, 1.5707963267948966), (1.9502206049649806, -1.5707963267948966), (0.05372412411858196, -1.5707963267948966), (1.8654862042995812, 1.5707963267948966), (1.2613497262525142, -1.5707963267948966), (58.97820691559647, 3.141592653589793), (2.3409994111314996, 1.5707963267948966), (69.52491267479274, 0.0), (1.2048735288511763, 1.5707963267948966), (0.8775801175894351, -1.5707963267948966), (2.4348272708295844, 1.5707963267948966), (6.428277805264403, 1.5707963267948966), (3.3735223968848786, 1.5707963267948966), (3.102461443790692, -1.5707963267948966), (6.246725845665113, 1.5707963267948966), (5.617377472771601, 1.5707963267948966), (3.178715770909393, -1.5707963267948966), (68.96072133838915, 0.0), (0.8803089947178533, 1.5707963267948966), (1.4610235926529014, -1.5707963267948966), (1.307920964727237, 1.5707963267948966), (1.1043456934929188, -1.5707963267948966)]

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
        func_name = "convert"
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
        for test_case in ['assert convert(1) == (1.0, 0.0)', 'assert convert(4) == (4.0,0.0)', 'assert convert(5) == (5.0,0.0)']:
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