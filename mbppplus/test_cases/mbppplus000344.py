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
inputs = [[[10, 15, 20, 25, 30, 35, 40], [25, 40, 35]], [[1, 2, 3, 4, 5], [6, 7, 1]], [[1, 2, 3], [6, 7, 1]], [[], []], [[], [1, 2, 3]], [[1, 2, 3], []], [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10]], [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]], [[1, 2, 3, 4, 5], [3, 3, 3, 3, 3]], [[10, 20, 30, 40, 50], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]], [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]], [[1, 1, 1, 2, 2, 3], [2, 2, 3, 3, 4]], [[1, 1, 1, 2, 2, 3, 2], [2, 2, 2, 3, 3, 4]], [[10, 20, 30, 40, 50], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 26, 55]], [[], [21.053827787412118, -26.99597124733289, -31.379141584827323, 92.96856462430469, 80.59200072494767, -33.39739721928059, 78.85020436951248, 63.482299506394384, -38.72845621707337, 80.59200072494767]], [[45, -1, -57, 10, 55, -6, -72, -10], [1, 2, 3]], [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 5]], [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 5]], [[78.85020436951248, 4.052029849956853, -33.39739721928059, 57.29229970397222, -63.90816106474213, -94.57327338374273, 57.29229970397222], [78.85020436951248, 4.052029849956853, -33.39739721928059, 57.29229970397222, -63.90816106474213, -94.57327338374273, 57.29229970397222]], [[2, 2, 3, 3, 2, 4], [2, 2, 3, 3, 2, 4]], [[1, 25, 2, 2, 3, 3, 4, 4, 5, 5], [1, 25, 2, 2, 3, 3, 4, 4, 5, 5]], [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 5, 6]], [[-1, -57, 10, 55, -6, -72, -10], [1, 3]], [[1, 2, 3, 4, 5], [2, 4, 6, 10, 2]], [[78.85020436951248, 4.052029849956853, 57.29229970397222, -33.39739721928059, 57.29229970397222, -63.90816106474213, -94.57327338374273, 57.29229970397222], [78.85020436951248, 4.052029849956853, 57.29229970397222, -33.39739721928059, 57.29229970397222, -63.90816106474213, -94.57327338374273, 57.29229970397222]], [[2, 3, 4, 5], [2, 4, 6, 10, 2]], [[5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 10], [5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 10]], [[5, 10, 15, 20, 30, 35, 4, 45, 55, 10], [5, 10, 15, 20, 30, 35, 4, 45, 55, 10]], [[78.85020436951248, 4.052029849956853, 57.29229970397222, -34.126255419632514, -63.90816106474213, -94.57327338374273, 57.29229970397222], [78.85020436951248, 4.052029849956853, 57.29229970397222, -34.126255419632514, -63.90816106474213, -94.57327338374273, 57.29229970397222]], [[2, 2, 3, 3, 3, 2, 4], [2, 2, 3, 3, 3, 2, 4]], [[92.96856462430469, 78.85020436951248, -31.379141584827323, -6.798645629977713, 4.052029849956853], []], [[78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213], [78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213]], [[21.053827787412118, -26.99597124733289, -31.379141584827323, 92.96856462430469, 80.59200072494767, -33.39739721928059, 78.85020436951248, 63.482299506394384, -38.72845621707337, 80.59200072494767], [21.053827787412118, -26.99597124733289, -31.379141584827323, 92.96856462430469, 80.59200072494767, -33.39739721928059, 78.85020436951248, 63.482299506394384, -38.72845621707337, 80.59200072494767]], [[6, 4, 5], [6, 4, 5]], [[-1, -57, 10, 55, -6, -72], [1, 3, 3]], [[21.053827787412118, -26.99597124733289, -31.379141584827323, 92.96856462430469, 80.59200072494767, -33.39739721928059, 78.85020436951248, 63.482299506394384, -38.72845621707337, 80.59200072494767, 80.59200072494767], [21.053827787412118, -26.99597124733289, -31.379141584827323, 92.96856462430469, 80.59200072494767, -33.39739721928059, 78.85020436951248, 63.482299506394384, -38.72845621707337, 80.59200072494767, 80.59200072494767]], [[1, 25, 2, 2, 3, 4, 5, 5, 5], [1, 25, 2, 2, 3, 4, 5, 5, 5]], [[2, 4, 6, 10, 2], [2, 4, 6, 10, 2]], [[78.85020436951248, 4.052029849956853, -33.39739721928059, -93.71866999005064, 57.29229970397222, -63.90816106474213, -94.57327338374273, 57.29229970397222], [78.85020436951248, 4.052029849956853, -33.39739721928059, -93.71866999005064, 57.29229970397222, -63.90816106474213, -94.57327338374273, 57.29229970397222]], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[45, 3, 4, 5], [45, 3, 4, 5]], [[True, True], [True, True]], [[1, 2, 3, 2], []], [[1, 3, 4, 4], [1, 3, 4, 4]], [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3]], [[1, 2, 2, 3, 6], [1, 2, 2, 3, 6]], [[78.85020436951248, 57.44201028672728, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213, -33.39739721928059], [78.85020436951248, 57.44201028672728, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213, -33.39739721928059]], [[1, 3, 4, 1, 5], [1, 3, 4, 1, 5]], [[1, 25, 2, 2, 3, 4, -57, 5, 5], [1, 25, 2, 2, 3, 4, -57, 5, 5]], [[1, 2, 3, 4], [5, 4, 3, 2, 1]], [[5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 10, 45], [5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 10, 45]], [[78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, 19.280231583546648, -63.90816106474213, 57.29229970397222, -63.90816106474213], [78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, 19.280231583546648, -63.90816106474213, 57.29229970397222, -63.90816106474213]], [[3, 3, 3, 3, 4, 3], [3, 3, 3, 3, 4, 3]], [[1, 2, 3, 4, 5], [5, 4, 3, 2, -57]], [[1, 2, 3], [5, 4, 3, 2, 1]], [[1, 1, 2, 2, 3, 3, 4, 4, 3, 5, 5, 3], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]], [[1, 2, 2, 3, 2], [1, 2, 2, 3, 2]], [[3, 3, 3, 3, 4, 3, 3, 4, 3], [3, 3, 3, 3, 4, 3, 3, 4, 3]], [[10, 20, 30, 40, 50], [10, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 26, 55]], [[1, 2, 3, 4], [8, 4, 3, 2, 1]], [[1, 1, 2, 2, 3, 3, 4, 4, 3, 5, 5, 4], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]], [[3, 3, 3, 3], [3, 3, 3, 3]], [[1, 3, 4], [1, 3, 4]], [[3, 3, 4, 4, 5, 5, 6, 6, 7, 7], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]], [[92.96856462430469, 78.85020436951248, -31.379141584827323, -6.798645629977713, 4.052029849956853, -6.798645629977713], []], [[1, 1, 2, 2, 3, 3, 4, 4, 3, 5, 5, 4], [3, 3, 4, 4, 5, 5, 7, 7]], [[10, 20, 26, 40, 50], [5, 10, 15, 20, 25, 30, 35, 30, 40, 45, 50, 55]], [[5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 15], [5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 15]], [[1, 1, 2, 2, 3, 3, 4, 4, 3, 5, 5, 4], [1, 1, 2, 2, 3, 3, 4, 4, 3, 5, 5, 4]], [[78.85020436951248, 57.44201028672728, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213, -33.39739721928059, 78.85020436951248], [78.85020436951248, 57.44201028672728, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213, -33.39739721928059, 78.85020436951248]], [[1, 2, 3, 3], [1, 2, 3, 3]], [[2, 50, 2, 3, 3, 3, 2, 4, 2], [2, 50, 2, 3, 3, 3, 2, 4, 2]], [[78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, -32.6127267841512, 34.11377601910786, -94.57327338374273, 57.29229970397222, -63.90816106474213], [78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, -32.6127267841512, 34.11377601910786, -94.57327338374273, 57.29229970397222, -63.90816106474213]], [[-72, 2, 3, 4], [-72, 2, 3, 4]], [[78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, 19.280231583546648, -63.90816106474213, 57.29229970397222, -63.90816106474213, -63.90816106474213], [78.85020436951248, 5.016938121201768, 57.29229970397222, -33.39739721928059, 19.280231583546648, -63.90816106474213, 57.29229970397222, -63.90816106474213, -63.90816106474213]], [[-1, -57, 10, 55, -6, -72, -10], [1, 3, 1]], [[92.96856462430469, 78.85020436951248, 4.052029849956853, 57.29229970397222, -34.126255419632514, -63.90816106474213, -94.57327338374273, 57.29229970397222], [92.96856462430469, 78.85020436951248, 4.052029849956853, 57.29229970397222, -34.126255419632514, -63.90816106474213, -94.57327338374273, 57.29229970397222]], [[10, 3, 4], [10, 3, 4]], [[4.052029849956853, -33.39739721928059, 57.29229970397222, -63.90816106474213, -94.57327338374273, -6.798645629977713, 45.00118380650045, 57.29229970397222, 57.29229970397222], [4.052029849956853, -33.39739721928059, 57.29229970397222, -63.90816106474213, -94.57327338374273, -6.798645629977713, 45.00118380650045, 57.29229970397222, 57.29229970397222]], [[5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 15, 10], [5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 15, 10]], [[-1, -57, 10, 55, -6, -72], [1, 3, 3, 1]], [[2, 3, 5, 5], [2, 3, 5, 5]], [[-1, -57, 10, 55, -6, -72], [-1, -57, 10, 55, -6, -72]], [[True], [True]], [[6, 4, 25], [6, 4, 25]], [[92.96856462430469, 78.85020436951248, -31.379141584827323, -6.798645629977713, 4.052029849956853, -6.798645629977713, 78.85020436951248], [92.96856462430469, 78.85020436951248, -31.379141584827323, -6.798645629977713, 4.052029849956853, -6.798645629977713, 78.85020436951248]], [[1, 2, 3], ['Dxjf', 'IPtogid', 'kZeTRnafBg', '', 'oQBAov', 'Zd', 'YuHlX', 'wH', 'nHgsGYA']], [[], [21.053827787412118, -26.99597124733289, -31.379141584827323, 92.96856462430469, 80.59200072494767, -33.39739721928059, 78.85020436951248, 63.482299506394384, -38.72845621707337, 80.59200072494767, 80.59200072494767]], [[-1, -57, 10, 55, -6, -72, 10], [-1, -57, 10, 55, -6, -72, 10]], [[5, 4, 2, 3, 2, -57], [5, 4, 2, 3, 2, -57]], [[1, 1, 2, 2, 3, 3, 4, 4, 3, 5, 3], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]], [[1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 5, 5, 35, 6, 7]], [[3, 3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3, 3]], [[True, True, True], [True, True, True]], [[1, 2, 3, 4, 5, 5], [1, 2, 3, 4, 5, 5]], [[92.96856462430469, -31.379141584827323, -6.798645629977713, 4.052029849956853, -6.798645629977713], [78.85020436951248, 92.96856462430469, -6.798645629977713, 19.280231583546648]], [[1, 2, 2, 6, 6], [1, 2, 2, 6, 6]], [[1, 1, 2, 3, 3, 4, 4, 5, 5], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7]], [[5, 10, 15, 16, 20, 35, 40, 45, 55, -1, 10], [5, 10, 15, 16, 20, 35, 40, 45, 55, -1, 10]], [[1, 25, 2, 2, 3, 4, -57, 5, 5, 4], [1, 25, 2, 2, 3, 4, -57, 5, 5, 4]], [['oQBAov', 'Dxjf', ''], []], [[1, 2, 2, 2, 2], [1, 2, 2, 2, 2]], [[4, 5, 4, 3, 2, -72, 3], [4, 5, 4, 3, 2, -72, 3]], [[-1, 10, 55, -6, -72, 3, 10, -1], [-1, 10, 55, -6, -72, 3, 10, -1]], [['Dxjf', 'IPtogid', 'kZeTRnafBg', '', 'oQBAov', 'Zd', 'YuHlX', 'wH'], ['Dxjf', 'IPtogid', 'kZeTRnafBg', '', 'oQBAov', 'Zd', 'YuHlX', 'wH']], [[1, 3, 3, 4, 4], [1, 3, 3, 4, 4]], [[1, 2, 2, 3, 2, 2], [1, 2, 2, 3, 2, 2]], [[3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 5, 7], [3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 5, 7]], [[78.85020436951248, 57.44201028672728, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213, -33.39739721928059, -63.90816106474213], [78.85020436951248, 57.44201028672728, 5.016938121201768, 57.29229970397222, -33.39739721928059, 34.11377601910786, -63.90816106474213, -94.57327338374273, 57.29229970397222, -63.90816106474213, -33.39739721928059, -63.90816106474213]], [[1, 25, 2, 2, 3, 4, 5, 5, 3], [1, 25, 2, 2, 3, 4, 5, 5, 3]], [[1, 26, 2, 2, 3, 2, 2], [1, 26, 2, 2, 3, 2, 2]], [[1, 2, 15], [5, 4, 3, 2, 1]]]
results = [[10, 20, 30, 15], [2, 3, 4, 5, 6, 7], [2, 3, 6, 7], [], [1, 2, 3], [1, 2, 3], [1, 3, 5, 8, 10, 6], [1, 2, 6, 7], [1, 2, 4, 5], [35, 5, 45, 15, 55, 25], [], [1, 4], [1, 4], [35, 5, 45, 15, 55, 25, 26], [-31.379141584827323, -26.99597124733289, 78.85020436951248, 80.59200072494767, 21.053827787412118, -38.72845621707337, 92.96856462430469, 63.482299506394384, -33.39739721928059], [-57, 10, 45, -10, 55, -72, -6, -1, 1, 2, 3], [1, 2, 6, 7], [], [], [], [], [1, 2, 6, 7], [-57, 10, -10, 55, -72, -6, -1, 1, 3], [1, 3, 5, 10, 6], [], [3, 5, 10, 6], [], [], [], [], [-31.379141584827323, 4.052029849956853, -6.798645629977713, 92.96856462430469, 78.85020436951248], [], [], [], [-57, 10, 55, -72, -6, -1, 1, 3], [], [], [], [], [], [], [], [1, 2, 3], [], [], [], [], [], [], [5], [], [], [], [1, -57], [4, 5], [1, 2, 6, 7], [], [], [35, 5, 45, 15, 55, 25, 26], [8], [1, 2, 6, 7], [], [], [], [-31.379141584827323, 4.052029849956853, -6.798645629977713, 92.96856462430469, 78.85020436951248], [1, 2, 7], [26, 35, 5, 45, 15, 55, 25, 30], [], [], [], [], [], [], [], [], [-57, 10, -10, 55, -72, -6, -1, 1, 3], [], [], [], [], [-57, 10, 55, -72, -6, -1, 1, 3], [], [], [], [], [], [1, 2, 3, '', 'kZeTRnafBg', 'wH', 'Zd', 'IPtogid', 'YuHlX', 'nHgsGYA', 'Dxjf', 'oQBAov'], [-31.379141584827323, -26.99597124733289, 78.85020436951248, 80.59200072494767, 21.053827787412118, -38.72845621707337, 92.96856462430469, 63.482299506394384, -33.39739721928059], [], [], [1, 2, 6, 7], [1, 2, 35, 6, 7], [], [], [], [-31.379141584827323, 4.052029849956853, 19.280231583546648, 78.85020436951248], [], [1, 2, 6, 7], [], [], ['Dxjf', '', 'oQBAov'], [], [], [], [], [], [], [], [], [], [], [15, 3, 4, 5]]

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
        func_name = "Diff"
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
        for test_case in ['assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]', 'assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]', 'assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]']:
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