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
inputs = [[10], [5], [4], [1000000], [1000001], [999999], [True], [1000002], [1000003], [999998], [999997], [19], [51], [999996], [18], [999995], [20], [999994], [50], [999993], [17], [49], [52], [21], [16], [78], [77], [48], [15], [1000004], [22], [1000005], [14], [999992], [53], [79], [76], [80], [81], [83], [43], [24], [13], [23], [75], [85], [55], [44], [47], [84], [46], [45], [82], [42], [1000006], [56], [86], [74], [41], [92], [1000007], [12], [25], [1000008], [87], [93], [73], [28], [91], [95], [54], [88], [57], [999991], [96], [97], [40], [26], [90], [2], [11], [89], [27], [94], [1000009], [1000010], [72], [29], [59], [71], [58], [60], [1000011], [30], [98], [70], [3], [99], [31], [64], [9], [100], [33]]
results = [62.83185307179586, 31.41592653589793, 25.132741228718345, 6283185.307179586, 6283191.590364893, 6283179.023994279, 6.283185307179586, 6283197.873550201, 6283204.156735508, 6283172.740808972, 6283166.457623664, 119.38052083641213, 320.4424506661589, 6283160.174438357, 113.09733552923255, 6283153.89125305, 125.66370614359172, 6283147.6080677435, 314.1592653589793, 6283141.324882436, 106.81415022205297, 307.8760800517997, 326.7256359733385, 131.94689145077132, 100.53096491487338, 490.0884539600077, 483.80526865282815, 301.59289474462014, 94.24777960769379, 6283210.439920815, 138.23007675795088, 6283216.723106123, 87.96459430051421, 6283135.041697129, 333.0088212805181, 496.37163926718733, 477.5220833456485, 502.6548245743669, 508.93800988154646, 521.5043804959057, 270.1769682087222, 150.79644737231007, 81.68140899333463, 144.51326206513048, 471.23889803846896, 534.0707511102648, 345.57519189487726, 276.46015351590177, 295.3097094374406, 527.7875658030853, 289.02652413026095, 282.7433388230814, 515.221195188726, 263.89378290154264, 6283223.0062914295, 351.85837720205683, 540.3539364174444, 464.9557127312894, 257.610597594363, 578.0530482605219, 6283229.289476736, 75.39822368615503, 157.07963267948966, 6283235.572662043, 546.637121724624, 584.3362335677015, 458.6725274241098, 175.92918860102841, 571.7698629533423, 596.9026041820607, 339.29200658769764, 552.9203070318035, 358.1415625092364, 6283128.758511822, 603.1857894892403, 609.4689747964198, 251.32741228718345, 163.36281798666926, 565.4866776461628, 12.566370614359172, 69.11503837897544, 559.2034923389832, 169.64600329384882, 590.6194188748811, 6283241.855847351, 6283248.139032658, 452.3893421169302, 182.212373908208, 370.7079331235956, 446.10615680975064, 364.424747816416, 376.99111843077515, 6283254.422217965, 188.49555921538757, 615.7521601035994, 439.822971502571, 18.84955592153876, 622.0353454107791, 194.77874452256717, 402.1238596594935, 56.548667764616276, 628.3185307179587, 207.34511513692635]

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
        func_name = "circle_circumference"
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
        for test_case in ['assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)', 'assert math.isclose(circle_circumference(5), 31.415000000000003, rel_tol=0.001)', 'assert math.isclose(circle_circumference(4), 25.132, rel_tol=0.001)']:
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
