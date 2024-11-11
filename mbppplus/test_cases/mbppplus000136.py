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
inputs = [[4], [6], [2], [10], [20], [100], [8], [9], [11], [19], [101], [True], [7], [12], [68], [67], [18], [5], [13], [102], [17], [82], [15], [66], [103], [64], [70], [14], [3], [81], [65], [45], [71], [83], [104], [84], [63], [24], [72], [69], [73], [74], [47], [23], [85], [44], [62], [48], [46], [80], [16], [105], [49], [50], [51], [22], [21], [43], [99], [25], [1], [28], [86], [75], [26], [29], [106], [94], [93], [79], [27], [92], [98], [107], [52], [61], [108], [109], [53], [95], [76], [60], [42], [78], [41], [87], [55], [91], [54], [96], [97], [89], [110], [90], [37], [36], [88], [77], [38], [39], [40], [30], [111]]
results = [8, 32, 2, 512, 524288, 633825300114114700748351602688, 128, 256, 1024, 262144, 1267650600228229401496703205376, 1, 64, 2048, 147573952589676412928, 73786976294838206464, 131072, 16, 4096, 2535301200456458802993406410752, 65536, 2417851639229258349412352, 16384, 36893488147419103232, 5070602400912917605986812821504, 9223372036854775808, 590295810358705651712, 8192, 4, 1208925819614629174706176, 18446744073709551616, 17592186044416, 1180591620717411303424, 4835703278458516698824704, 10141204801825835211973625643008, 9671406556917033397649408, 4611686018427387904, 8388608, 2361183241434822606848, 295147905179352825856, 4722366482869645213696, 9444732965739290427392, 70368744177664, 4194304, 19342813113834066795298816, 8796093022208, 2305843009213693952, 140737488355328, 35184372088832, 604462909807314587353088, 32768, 20282409603651670423947251286016, 281474976710656, 562949953421312, 1125899906842624, 2097152, 1048576, 4398046511104, 316912650057057350374175801344, 16777216, 1, 134217728, 38685626227668133590597632, 18889465931478580854784, 33554432, 268435456, 40564819207303340847894502572032, 9903520314283042199192993792, 4951760157141521099596496896, 302231454903657293676544, 67108864, 2475880078570760549798248448, 158456325028528675187087900672, 81129638414606681695789005144064, 2251799813685248, 1152921504606846976, 162259276829213363391578010288128, 324518553658426726783156020576256, 4503599627370496, 19807040628566084398385987584, 37778931862957161709568, 576460752303423488, 2199023255552, 151115727451828646838272, 1099511627776, 77371252455336267181195264, 18014398509481984, 1237940039285380274899124224, 9007199254740992, 39614081257132168796771975168, 79228162514264337593543950336, 309485009821345068724781056, 649037107316853453566312041152512, 618970019642690137449562112, 68719476736, 34359738368, 154742504910672534362390528, 75557863725914323419136, 137438953472, 274877906944, 549755813888, 536870912, 1298074214633706907132624082305024]

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
        func_name = "even_binomial_Coeff_Sum"
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
        for test_case in ['assert even_binomial_Coeff_Sum(4) == 8', 'assert even_binomial_Coeff_Sum(6) == 32', 'assert even_binomial_Coeff_Sum(2) == 2']:
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
