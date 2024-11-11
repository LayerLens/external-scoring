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
inputs = [[2], [3], [4], [100], [1000], [True], [False], [1001], [1002], [999], [99], [98], [101], [35], [69], [998], [97], [96], [36], [65], [70], [66], [1003], [997], [996], [995], [71], [68], [72], [102], [64], [994], [103], [73], [993], [67], [37], [91], [104], [63], [62], [992], [34], [92], [1004], [95], [991], [33], [1005], [89], [90], [105], [93], [106], [59], [28], [39], [74], [94], [40], [1006], [60], [88], [55], [38], [75], [27], [87], [61], [26], [76], [58], [32], [56], [25], [57], [31], [29], [45], [30], [46], [44], [9], [8], [77], [990], [107], [54], [1007], [7], [43], [47], [42], [24], [6], [5], [108], [86], [989], [12], [1008], [53], [85], [988], [41]]
results = [72, 288, 800, 204020000, 2004002000000, 8, 0, 2012026024008, 2020074120072, 1996002000000, 196020000, 188257608, 212262408, 3175200, 46657800, 1988025976008, 180728072, 173426688, 3548448, 36808200, 49401800, 39108168, 2028146336288, 1980073880072, 1972145664288, 1964241280800, 52265088, 44029728, 55251072, 220752072, 34611200, 1956360681800, 229493888, 58363208, 1948503819528, 41514272, 3953672, 140180768, 238492800, 32514048, 30513672, 1940670646272, 2832200, 146410272, 2036242720800, 166348800, 1932861114368, 2517768, 2044363321800, 128320200, 134152200, 247753800, 152845128, 257281928, 25063200, 1318688, 4867200, 61605000, 159489800, 5379200, 2052508187528, 26791200, 122680448, 18972800, 4392648, 64980000, 1143072, 117228672, 28607048, 985608, 68491808, 23420168, 2230272, 20377728, 845000, 21859272, 1968128, 1513800, 8569800, 1729800, 9348488, 7840800, 16200, 10368, 72144072, 1925075176200, 267082272, 17641800, 2060677366272, 6272, 7159328, 10179072, 6523272, 720000, 3528, 1800, 277159968, 111960648, 1917312784200, 48672, 2068870906368, 16382088, 106872200, 1909573890848, 5930568]

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
        func_name = "cube_Sum"
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
        for test_case in ['assert cube_Sum(2) == 72', 'assert cube_Sum(3) == 288', 'assert cube_Sum(4) == 800']:
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
