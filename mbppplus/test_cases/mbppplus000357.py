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
inputs = [[[1, 2, 4, 5], 6], [[1, 2, 4, 5], 3], [[1, 2, 4, 5], 7], [[], 6], [[], 7], [[], 3], [[True, True, False, False, False, True, True, False, True, False], 7], [[True, False, False, True, True], 6], [[3, 6], True], [[True, True, False, False, False, False, True, True, False, True, False], 7], [[50.64327388212607, -72.16612625583227, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 7], [[50.64327388212607, -72.16612625583227, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 8], [[50.64327388212607, -72.16612625583227, 95.25630303581863, -75.73998556144497, 11.857449640680656, -90.20293226837086, -12.02758648076636, -35.964731488229475], False], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 7], [[57, 3, True], 6], [[57, 3, True], 7], [[7, 3, True], 7], [[7, 3, True], 57], [[True, False, False, False, True, True], 7], [[], 2], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 7], [[7, 3, 6], True], [[True, True, False, False, False, False, True, True, False, True, False, False], 7], [[], 8], [[7, True, 3, 6], True], [[True, False, True, True], 3], [[58, 3, True], 6], [[50.64327388212607, -72.16612625583227, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 58], [[48.73417838625409, -35.964731488229475, 82.81444880501536, 11.857449640680656, 17.182050219901072, 21.593943255744534], 57], [[51, 7, -18, 57, 58, 57, False], 2], [[57, 3, True], False], [[51, 7, -18, 57, 58, 57, False], 3], [[48.73417838625409, -35.964731488229475, 82.81444880501536, 11.857449640680656, 17.182050219901072, 21.593943255744534, 21.593943255744534], 57], [[-12.02758648076636, -35.964731488229475, 82.81444880501536, 11.857449640680656, 17.182050219901072, 21.593943255744534], 57], [[True, True, False, False, False, False, True, False, False, True, False, False], True], [[58, 3, False], True], [[57, 3, True], True], [[58, 7, 3, True], 6], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, 17.182050219901072, -12.02758648076636, -35.964731488229475], -18], [[True, True, False, False, False, False, True, True, True, False, True, False], 7], [[57, 3, True, 57], False], [[50.64327388212607, -72.16612625583227, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475, -90.20293226837086], 7], [[True, True, False, False, False, False, True, True, False, True, False, False, False], 7], [[-88.67190659296908, 21.593943255744534, -35.964731488229475, -90.20293226837086, 91.16324571161306, 50.64327388212607, 33.65983917911731], 2], [[False, True, True, False, False, False, True, True, True, True, False, True, False], 7], [[True, True, False, False, False, False, True, True, False, True, False, False, False], 58], [[58, 3, True], False], [[50.64327388212607, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 7], [[50.64327388212607, 95.25630303581863, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], -18], [[True, True, False, False, False, False, True, True, False, True, False, False], False], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 2], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 6], [[50.64327388212607, -72.16612625583227, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 6], [[50.64327388212607, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475, -35.906723367430125, 50.64327388212607], 6], [[False], 8], [[True, False, False, True], 58], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, -6.981753345954178, -35.964731488229475], 2], [[7, 3, 3, True], 7], [[58, -18, 58, 3, 3, True], False], [[50.64327388212607, -72.16612625583227, -12.02758648076636, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475, -12.02758648076636], 6], [[50.64327388212607, -107.06961552249132, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 7], [[True, False, True], 51], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475, 50.64327388212607], 7], [[True, True, False, False, False, True, True, False, True, False, False, False], 58], [[50.64327388212607, -72.16612625583227, -75.73998556144497, -75.73998556144497, 90.05081633927793, -90.20293226837086, -6.981753345954178, -35.964731488229475], 3], [[], 56], [[50.64327388212607, -106.14126259013264, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 58], [[True, True, False, False, False, False, False, True, True, False, False, True, False], 7], [[True, 58, 3, True, True], 6], [[True, False, False, False, True, True, True], 7], [[51, 7, -18, 57, 58, 57, False], 4], [[58, -18, 58, 3, 3, True, True], False], [[51, 7, -18, -18, 57, 58, 57, False], True], [[True, False, False, False, True, True, True], 56], [[True, True, False, False, False, False, True, False, False, True, False, False], False], [[True, True, False, False, False, True, True, False, True, False, False, False], 59], [[48.73417838625409, -35.964731488229475, 82.81444880501536, 11.857449640680656, 21.593943255744534], 57], [[-18, -18, 58, 3, 3, True], False], [[True, True, False, False, False, True, True, False, True, False, False, False], 8], [[True, True, False, False, False, False, True, True, False, True, False, False], 6], [[True, False, True, False], 3], [[True, True, False, False, False, True, True, False, True, False, False, False], 56], [[True, True, False, False, False, False, True, True, False, True, False, False, False], False], [[True, True, False, False, False, True, False, True, False], 7], [[True, True, False, False, False, False, True, True, False, True, False, False, False], 59], [[True, True, False, False, False, False, True, True, False, True, False], False], [[57, 3, True, 57], True], [[3, True, 57], True], [[58, 58, 3, 3, True], True], [[7, 3, True], 56], [[True, False, False, True, False], 58], [[17.182050219901072, -35.964731488229475, 82.81444880501536, 11.857449640680656, 21.593943255744534], 57], [[57, True, 57], False], [[True, True, False, False, False, False, True, True, False, True, False], True], [[True, True, False, False, False, False, True, True, False, True, False, False, True], 7], [[50.64327388212607, -72.16612625583227, -12.02758648076636, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475, -12.02758648076636], 3], [[50.64327388212607, -107.06961552249132, -75.73998556144497, -75.73998556144497, 90.05081633927793, -12.02758648076636, -35.964731488229475], 7], [[50.64327388212607, 95.25630303581863, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475, -35.906723367430125, 50.64327388212607], 6], [[58, 7, True], 6], [[50.64327388212607, -72.16612625583227, -12.02758648076636, -12.02758648076636, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -12.02758648076636], 57], [[50.64327388212607, -106.14126259013264, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.712014625788704, -35.964731488229475, 90.05081633927793], 4], [[50.64327388212607, 95.25630303581863, -75.73998556144497, 11.857449640680656, 90.05081633927793, -90.20293226837086, -12.02758648076636, -35.964731488229475], 8], [[50.64327388212607, -72.16612625583227, -12.02758648076636, -75.73998556144497, 90.05081633927793, -90.20293226837086, -12.02758648076636, -12.02758648076636], 57], [[True, True, False, False, False, False, True, True, True, True, True, False, False], 7], [[95.25630303581863, 46.77615975283183, -72.16612625583227, -49.67713786505266, -59.21876350427635, 63.40916885926825, -106.14126259013264, 48.73417838625409], 8], [[True, True, False, False, False, True, True, False, True, False, False, False, False], 59]]
results = [4, 2, 4, 0, 0, 0, 10, 5, 0, 11, 2, 2, 2, 4, 3, 3, 3, 3, 6, 0, 4, 0, 12, 0, 2, 4, 3, 9, 6, 0, 0, 0, 7, 6, 12, 0, 0, 4, 4, 12, 0, 2, 13, 4, 13, 13, 0, 3, 0, 6, 4, 4, 2, 9, 1, 4, 4, 4, 2, 4, 4, 3, 4, 12, 4, 0, 9, 13, 5, 7, 0, 2, 4, 7, 6, 12, 2, 2, 12, 12, 4, 12, 6, 9, 13, 11, 3, 2, 0, 3, 5, 2, 0, 11, 13, 4, 7, 8, 0, 9, 2, 3, 4, 13, 7, 13]

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
        func_name = "right_insertion"
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
        for test_case in ['assert right_insertion([1,2,4,5],6)==4', 'assert right_insertion([1,2,4,5],3)==2', 'assert right_insertion([1,2,4,5],7)==4']:
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
