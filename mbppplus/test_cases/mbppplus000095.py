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
inputs = [[5], [10], [15], [0], [-10], [1000000], [3.5], [1.5], [1.0505829058331777], [0.8232153234250026], [-11], [1.1423795213926284], [0.09982566847914054], [-1], [False], [1000001], [-2], [0.8077261706133441], [True], [1.1028493478364014], [-0.6792391618130493], [0.909551532381226], [1000002], [-0.005504686729706451], [0.9868175569774722], [-9], [0.9232556249681736], [1000003], [0.6965793033660621], [0.6294263989650178], [0.6535078983353], [1.6349329383768112], [0.7902235974897384], [1.5172735829864554], [-0.934803278457003], [-1.1192650882858737], [1.2342082553789273], [-1.698603118139952], [0.5935859571226136], [1.6830234032997775], [0.785792688601003], [31.370495378968002], [84.01235804122422], [1.1276189613088303], [107.78498426566843], [-0.0029078677287501745], [-12], [75.6566983607087], [1.554842829586259], [-15.68855646866227], [0.5528325585260435], [1.9252801407864577], [0.7737942113653675], [1.2772250645310455], [0.3658008762332865], [1.2131766463211393], [0.9390038351214784], [2.2831918031216305], [1.882254037648374], [-8], [0.13542016819864997], [0.1399805018824617], [-0.021518766852972826], [1.2249594487730122], [4.73142092326178], [2.5041511619949257], [-29.226547220922924], [1.232187069270112], [0.9315663577437784], [0.16130662172278876], [-3], [1.2353805704290877], [-0.23618264271757206], [-1.9412533512158896], [0.7590332508942004], [1.8855707948477347], [0.12461000378614799], [3.713397178947464], [1.1646860674476625], [5.061520744124105], [2.362488974509084], [1.8219258427481917], [0.7781797011317402], [16.251173065770736], [1.2275912517626453], [0.26717467520648097], [-7], [0.7750635059012929], [0.9746470744694342], [0.8564961031500605], [-0.8398787134682071], [0.6562631390141311], [0.860561999847218], [0.9087877034647631], [89.7106724186805], [-0.575457086018061], [-28.33971230831976], [0.11108589002626337], [0.38766169842712256], [-4], [0.7952111107175209], [0.2900179424349849], [-15.637668202519894], [1.4496382242194237], [147.8513725235397], [-0.7256171557364777], [-1.8438320948223208], [-0.1244805889183841]]
results = [25, 50, 75, 0, -50, 5000000, 17.5, 7.5, 5.2529145291658885, 4.116076617125013, -55, 5.711897606963142, 0.4991283423957027, -5, 0, 5000005, -10, 4.038630853066721, 5, 5.514246739182007, -3.3961958090652464, 4.54775766190613, 5000010, -0.027523433648532252, 4.934087784887361, -45, 4.616278124840868, 5000015, 3.4828965168303103, 3.1471319948250893, 3.2675394916764997, 8.174664691884056, 3.9511179874486917, 7.586367914932277, -4.674016392285015, -5.596325441429368, 6.171041276894637, -8.493015590699759, 2.967929785613068, 8.415117016498888, 3.9289634430050153, 156.85247689484, 420.0617902061211, 5.638094806544151, 538.9249213283422, -0.014539338643750873, -60, 378.2834918035435, 7.774214147931295, -78.44278234331135, 2.7641627926302177, 9.626400703932289, 3.8689710568268376, 6.386125322655227, 1.8290043811664325, 6.065883231605697, 4.695019175607392, 11.415959015608152, 9.41127018824187, -40, 0.6771008409932499, 0.6999025094123085, -0.10759383426486413, 6.124797243865061, 23.6571046163089, 12.520755809974629, -146.13273610461462, 6.16093534635056, 4.657831788718892, 0.8065331086139438, -15, 6.176902852145439, -1.1809132135878602, -9.706266756079447, 3.7951662544710016, 9.427853974238673, 0.62305001893074, 18.56698589473732, 5.823430337238312, 25.307603720620527, 11.81244487254542, 9.10962921374096, 3.8908985056587007, 81.25586532885367, 6.137956258813226, 1.3358733760324049, -35, 3.8753175295064644, 4.873235372347171, 4.2824805157503025, -4.199393567341035, 3.2813156950706555, 4.30280999923609, 4.543938517323816, 448.5533620934025, -2.8772854300903052, -141.6985615415988, 0.5554294501313168, 1.9383084921356128, -20, 3.9760555535876048, 1.4500897121749245, -78.18834101259947, 7.248191121097118, 739.2568626176985, -3.6280857786823884, -9.219160474111604, -0.6224029445919205]

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
        func_name = "perimeter_pentagon"
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
        for test_case in ['assert perimeter_pentagon(5) == 25', 'assert perimeter_pentagon(10) == 50', 'assert perimeter_pentagon(15) == 75']:
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
