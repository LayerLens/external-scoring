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
inputs = [[2], [3], [1], [10], [100], [1000], [1000000], [500000], [250000], [100000], [249999], [999], [101], [62], [11], [249998], [99], [499999], [61], [102], [63], [249997], [64], [999999], [35], [997], [36], [100001], [1000001], [9], [499997], [True], [996], [499996], [499995], [250001], [37], [98], [65], [97], [999998], [34], [60], [59], [12], [500001], [66], [13], [93], [67], [500002], [92], [103], [68], [100002], [1000002], [1000003], [995], [94], [500003], [8], [1001], [80], [96], [1003], [499998], [79], [95], [78], [90], [999997], [499994], [29], [91], [30], [28], [999996], [100003], [999995], [1002], [998], [999994], [100004], [89], [250002], [58], [999993], [994], [26], [999991], [88], [33], [1000004], [100005], [999990], [81], [1000005], [99999], [57], [1000006], [32], [87], [249996], [999992], [993], [104], [82], [76]]
results = [1056, 8832, 32, 7066400, 5494666640000, 5349346666664000000, 5333349333346666666666664000000000000, 83333833334166666666666000000000000, 1302098958385416666666500000000000, 5333493334666666666640000000000, 1302067708385416666666500000000000, 5317346666664000000, 5830989856032, 317789722656, 12220032, 1302036459010411666686499960000032, 5174666640000, 83332833334166666666666000000000000, 288473472032, 6184295713056, 349547692032, 1302005210260391666846499320001056, 383907430400, 5333317333346666666666664000000000000, 10664438400, 5253825069541281056, 12599356032, 5333813350666986669840016000032, 5333381333506666986666984000160000032, 3866400, 83330833364166466667385998640001056, 32, 5222302198168328832, 83329833394166106669545992160008832, 83328833434165466674665971680041600, 1302130209010421666686500040000032, 14818362656, 4870349824032, 421036730400, 4581095169056, 5333285333506666346666983999840000032, 8983738400, 261446390400, 236563190400, 20182656, 83334833344166706666746000080000032, 461111372832, 32064032, 3562921830432, 504315376256, 83335833364166866667386001360001056, 3340301552256, 6555263416832, 550841250432, 5334133382668266695440272001056, 5333413333826668266669544002720001056, 5333445334306671146678184015680008832, 5190937098607401600, 3797771117600, 83336833394167226669546007840008832, 1976832, 5381506986984160032, 1451076249600, 4306300280832, 5446311158199688832, 83331833344166626666745999920000032, 1346218649600, 4045381017600, 1247752844832, 2929705178400, 5333253333826665066669543997280001056, 83327833484164466684665921680141600, 3509997600, 3129395464832, 4287597600, 2853640832, 5333221334306662186678183984320008832, 5334453430671146781841568008832, 5333189334946657066698663943360041600, 5413828269546721056, 5285506346983840032, 5333157335746649066738663843360141600, 5334773494676266986645664041600, 2740748378400, 1302161460260441666846500680001056, 213685612832, 5333125336706637546807783636000390432, 5159729138507501600, 1843744032, 5333061339106601387081382596481976832, 2562058476032, 7529804832, 5333477334946676266698664056640041600, 5335093574684267386655664141600, 5333029340546575467314661546723866400, 1562653350432, 5333509335746684266738664156640141600, 5333173334666666666640000000000, 192682196256, 5333541336706695786807784364000390432, 6277472256, 2393184262656, 1301973962135346667386496080008832, 5333093337826621866917543251840928256, 5128677687420390432, 6944592345600, 1681290100256, 1068746172032]

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
        func_name = "even_Power_Sum"
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
        for test_case in ['assert even_Power_Sum(2) == 1056', 'assert even_Power_Sum(3) == 8832', 'assert even_Power_Sum(1) == 32']:
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
