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
inputs = [[2], [3], [4], [1000000.0], [10000000.0], [100000000.0], [1], [10], [100], [123456789], [999999999], [5], [7], [15], [50000], [999999], [1234567890], [14], [8], [6], [9], [16], [1000000000], [999999998], [95], [13], [123456788], [101], [123456787], [17], [True], [12], [89], [1234567891], [102], [90], [1000000001], [88], [26], [1000000], [98], [96], [23], [24], [103], [25], [91], [1234567889], [1000000002], [27], [1000000003], [11], [97], [999998], [18], [50002], [104], [99], [1000000004], [49999], [50001], [19], [94], [93], [22], [20], [1234567892], [74], [59], [92], [28], [77], [1000001], [58], [999997], [999996], [75], [999999997], [60], [123456790], [50003], [50004], [87], [78], [76], [999995], [21], [999994], [50005], [123456791], [29], [85], [73], [49998], [50006], [123456792], [1234567888], [999999996], [57], [1234567893], [86], [84], [1234567887], [83], [50007], [49997], [79], [30], [50008], [31], [64], [105], [1234567886], [61], [62], [1234567885], [999999994]]
results = [10.0, 35.0, 84.0, 1.333333333333e+18, 1.33333333333333e+21, 1.3333333333333333e+24, 1.0, 1330.0, 1333300.0, 2.5089018290522064e+24, 1.3333333293333333e+27, 165.0, 455.0, 4495.0, 166666666650000.0, 1.333329333337e+18, 2.508901829052206e+27, 3654.0, 680.0, 286.0, 969.0, 5456.0, 1.3333333333333333e+27, 1.3333333253333334e+27, 1143135.0, 2925.0, 2.508901768085892e+24, 1373701.0, 2.5089017071195784e+24, 6545.0, 1.0, 2300.0, 939929.0, 2.508901835148838e+27, 1414910.0, 971970.0, 1.3333333373333335e+27, 908600.0, 23426.0, 1.333333333333e+18, 1254890.0, 1179616.0, 16215.0, 18424.0, 1456935.0, 20825.0, 1004731.0, 2.508901822955575e+27, 1.3333333413333334e+27, 26235.0, 1.3333333453333333e+27, 1771.0, 1216865.0, 1.333325333349e+18, 7770.0, 166686667450010.0, 1499784.0, 1293699.0, 1.3333333493333333e+27, 166656666849999.0, 166676666850001.0, 9139.0, 1107414.0, 1072445.0, 14190.0, 10660.0, 2.5089018412454697e+27, 540274.0, 273819.0, 1038220.0, 29260.0, 608685.0, 1.333337333337e+18, 260130.0, 1.333321333369e+18, 1.333317333397e+18, 562475.0, 1.3333333213333334e+27, 287980.0, 2.508901890018522e+24, 166696668450035.0, 166706669850084.0, 877975.0, 632710.0, 585276.0, 1.333313333433e+18, 12341.0, 1.3333093334769997e+18, 166716671650165.0, 2.5089019509848386e+24, 32509.0, 818805.0, 518665.0, 166646667449990.0, 166726673850286.0, 2.508902011951156e+24, 2.5089018168589433e+27, 1.3333333173333335e+27, 246905.0, 2.508901847342101e+27, 848046.0, 790244.0, 2.508901810762312e+27, 762355.0, 166736676450455.0, 166636668449965.0, 657359.0, 35990.0, 166746679450680.0, 39711.0, 349504.0, 1543465.0, 2.5089018046656805e+27, 302621.0, 317750.0, 2.508901798569049e+27, 1.3333333093333334e+27]

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
        func_name = "square_Sum"
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
        for test_case in ['assert square_Sum(2) == 10', 'assert square_Sum(3) == 35', 'assert square_Sum(4) == 84']:
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
