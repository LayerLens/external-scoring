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
inputs = [[5], [9], [10], [100], [256], [500], [1000], [498], [501], [99], [66.89191997931741], [499], [101], [58.21525080612692], [255], [56.54995057201372], [66.89685310561087], [83.57157718204266], [257], [56.515998521878785], [502], [94], [44.81065373727037], [57.988194173394064], [258], [254], [44.14277592544646], [56.21634924802973], [89.96609117849408], [66.1048816215708], [88.13624919640782], [79.6724987089057], [39.52432765735469], [True], [90.07330615375426], [88.87446543484394], [80.34469028251331], [49.60482371300252], [72.10961391578658], [45.66474918863301], [49.36550800651825], [96.36174327164798], [49.5519341974717], [46.77734594153838], [58.60446127338968], [43.96898505055638], [71.53271932911613], [74.8787595686315], [503], [46.16814427525153], [111.66234638131426], [88.08382305305746], [49.49303485405071], [61.37019967563893], [32.91553737053482], [66.36780157713834], [57.29823626732467], [22.379094693696736], [54.96499328054807], [36.1581754122743], [66.92178864353467], [46.768786306758976], [45.70770179810679], [167.1370719989952], [47.58561323936907], [177.1807622449919], [88.511622782816], [75.47079545748679], [131.7505984206982], [47.072828054103255], [44.70281907116363], [39.63955404134835], [204.65193122740226], [74.5525427247953], [99.26181704026428], [21.120055544612296], [79.31702556710835], [74.78374726509155], [76.34666896378033], [87.40201417119114], [81.44166666320646], [103.47341378006003], [80.48426490964339], [150.05803234410334], [83.47216295269475], [149.60372427578594], [58.449276101423614], [89.42036866377818], [261.58475368046663], [74.10117623814627], [88.29944030057857], [44.370912453575414], [71.18054521166749], [90.63536438039682], [235.15522010358956], [149.81299725780573], [82], [22], [55.29773209779792], [57.762852719453875], [33.23388199757163], [78.68210551259803], [86.74383027879837], [54.974906483559266], [16.361378713598747], [82.82980927890722], [62.87886571752386]]
results = [100, 324, 400, 40000, 262144, 1000000, 4000000, 992016, 1004004, 39204, 17898.115834077613, 996004, 40804, 13556.061705681042, 260100, 12791.58763878878, 17900.755821734718, 27936.83405077645, 264196, 12776.23235570002, 1008016, 35344, 8031.978753446172, 13450.522653965012, 266256, 258064, 7794.338665616701, 12641.11169110581, 32375.59024774844, 17479.421496807554, 31071.99368964519, 25390.828202082324, 6248.689907063731, 4, 32452.80192587178, 31594.68242531708, 25821.077026371957, 9842.554142392228, 20799.185676335208, 8341.077273843037, 9747.81352296647, 37142.34226540398, 9821.576730842262, 8752.480373337428, 13737.931524576923, 7733.0865855042, 20467.71973847242, 22427.31453814769, 1012036, 8525.990183281761, 49873.91839752243, 31035.039534569347, 9798.241996257115, 15065.20563291117, 4333.730401564298, 17618.740344729624, 13132.351517384639, 2003.2955172377815, 12084.601945322778, 5229.654596579192, 17914.103180999704, 8749.277490429144, 8356.776014658619, 111739.20334558922, 9057.562349467267, 125572.0900388654, 31337.229470590053, 22783.363867943233, 69432.88073684832, 8863.404564044682, 7993.368131636764, 6285.1769783879045, 167529.65182042154, 22232.326506929716, 39411.6332885396, 1784.2269848300343, 25164.762179253277, 22370.435420036352, 23315.255447460237, 30556.448324724388, 26530.98027552334, 42826.98943719806, 25910.867592182614, 90069.65228393585, 27870.4079520049, 89525.09726874153, 13665.271507121799, 31984.00932786401, 273706.3334322816, 21963.937279507252, 31187.16462958175, 7875.111487851415, 20266.68006652096, 32859.07710546922, 221191.9101678706, 89775.73658946923, 26896, 1936, 12231.35670063932, 13346.188617157279, 4417.9636505140625, 24763.494911582435, 30097.968365747907, 12088.961371504347, 1070.7788536392086, 27443.10922072058, 15815.007015689589]

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
        func_name = "lateralsurface_cube"
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
        for test_case in ['assert lateralsurface_cube(5)==100', 'assert lateralsurface_cube(9)==324', 'assert lateralsurface_cube(10)==400']:
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
