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
inputs = [[90], [60], [120], [0], [-90], [-180], [-270], [-91], [-92], [-181], [False], [True], [-89], [-269], [-268], [-267], [-93], [-182], [-88], [-179], [-178], [-177], [-266], [-1], [-176], [-80], [-87], [-81], [-86], [-183], [-79], [-184], [-271], [1], [87], [-78], [-185], [-175], [-264], [-28], [-263], [-262], [-265], [32], [-16], [-2], [-272], [-3], [-174], [-4], [-273], [-29], [88], [-17], [-173], [-5], [-274], [-261], [31], [-77], [-61], [-30], [-85], [86], [-172], [89], [-186], [-171], [-27], [-8], [-170], [85], [43], [-36], [-169], [-15], [18], [-76], [-82], [-84], [-18], [-9], [-26], [-7], [29], [42], [-35], [-83], [-14], [-168], [-75], [9], [-187], [-10], [28], [-94], [-167], [63], [-62], [-63], [-95], [91], [-64], [62], [17], [44]]
results = [1.5707963267948966, 1.0471975511965976, 2.0943951023931953, 0.0, -1.5707963267948966, -3.141592653589793, -4.71238898038469, -1.5882496193148399, -1.605702911834783, -3.159045946109736, 0.0, 0.017453292519943295, -1.5533430342749535, -4.694935687864747, -4.677482395344803, -4.6600291028248595, -1.6231562043547263, -3.1764992386296798, -1.53588974175501, -3.12413936106985, -3.106686068549907, -3.0892327760299634, -4.642575810304916, -0.017453292519943295, -3.07177948351002, -1.3962634015954636, -1.5184364492350666, -1.413716694115407, -1.5009831567151233, -3.193952531149623, -1.3788101090755203, -3.211405823669566, -4.729842272904633, 0.017453292519943295, 1.5184364492350666, -1.361356816555577, -3.2288591161895095, -3.0543261909900763, -4.60766922526503, -0.4886921905584123, -4.590215932745087, -4.572762640225144, -4.625122517784973, 0.5585053606381855, -0.2792526803190927, -0.03490658503988659, -4.747295565424577, -0.05235987755982988, -3.036872898470133, -0.06981317007977318, -4.76474885794452, -0.5061454830783556, 1.53588974175501, -0.29670597283903605, -3.01941960595019, -0.08726646259971647, -4.782202150464463, -4.5553093477052, 0.5410520681182421, -1.3439035240356338, -1.064650843716541, -0.5235987755982988, -1.4835298641951802, 1.5009831567151233, -3.0019663134302466, 1.5533430342749535, -3.2463124087094526, -2.9845130209103035, -0.47123889803846897, -0.13962634015954636, -2.9670597283903604, 1.4835298641951802, 0.7504915783575616, -0.6283185307179586, -2.949606435870417, -0.2617993877991494, 0.3141592653589793, -1.3264502315156903, -1.43116998663535, -1.4660765716752369, -0.3141592653589793, -0.15707963267948966, -0.4537856055185257, -0.12217304763960307, 0.5061454830783556, 0.7330382858376184, -0.6108652381980153, -1.4486232791552935, -0.24434609527920614, -2.9321531433504737, -1.3089969389957472, 0.15707963267948966, -3.2637657012293966, -0.17453292519943295, 0.4886921905584123, -1.6406094968746698, -2.9146998508305306, 1.0995574287564276, -1.0821041362364843, -1.0995574287564276, -1.6580627893946132, 1.5882496193148399, -1.117010721276371, 1.0821041362364843, 0.29670597283903605, 0.767944870877505]

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
        func_name = "radian_degree"
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
        for test_case in ['assert radian_degree(90)==1.5707963267948966', 'assert radian_degree(60)==1.0471975511965976', 'assert radian_degree(120)==2.0943951023931953']:
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
