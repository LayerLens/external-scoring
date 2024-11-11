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
inputs = [[['Python', 'list', 'exercises', 'practice', 'solution'], 8], [['Python', 'list', 'exercises', 'practice', 'solution'], 6], [['Python', 'list', 'exercises', 'practice', 'solution'], 9], [[], 5], [[], 0], [['abcdef', 'xyz', 'pqr', 'lmnop', 'abcde'], 5], [['abc', 'defg', 'hijkl', 'mnopqr'], 3], [[], 3], [['abc', 'defg', 'mnopqr'], 3], [['abc', 'defg', 'hijkl'], 0], [[], 6], [['abcdef', 'xyz', 'pqr', 'lmnop', 'abcde'], 0], [['abc', 'defg', 'hijkl'], 3], [['hijkl', 'KpROouj', 'xyz', 'vRyohLy'], 5], [['abc', 'defg', 'hijkl', 'defg'], 6], [['abcddef', 'xyz', 'pqr', 'lmnop', 'abcde', 'abcde'], 5], [['abc', 'defg', 'hijkl', 'defg'], 3], [['abc', 'defg', 'mnopqr', 'hijkl'], 3], [['abcdef', 'xyz', 'pqr', 'lmnabc', 'abcde'], 5], [['abc', 'defg', 'hijkl', 'abc'], 0], [['abcdef', 'xyz', 'pqr', 'lmnop', 'abcddef'], 5], [['abc', 'hijkl', 'defg', 'abc'], 3], [['hijkl', 'KpROouj', 'xyz', 'vRyohLy', 'hijkl'], 5], [['abc', 'defg', 'deffg', 'mnopqr', 'hijkl'], 3], [['abc', 'mnopqr', 'hijkl', 'defg', 'abc', 'abc', 'abc'], 3], [['abcdef', 'xyz', 'pqr', 'lmnop', 'abcde'], 3], [['abc', 'defg', 'mnopqr'], 4], [['abcddef', 'xyz', 'pqr', 'lmnop', 'abcde', 'abcde'], 4], [['abc', 'mnopqr', 'hijkl', 'defg', 'abc', 'abc', 'abc', 'abc'], 4], [['abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 3], [['abc', 'defg'], -1], [['abc', 'defg', 'hijkl', 'hijkl'], 3], [['deffg', 'defg'], 3], [['deffg', 'defg', 'deffg'], 3], [['abc', 'defg', 'dedfg', 'hijkl', 'defg'], 6], [['defg', 'mnopqr'], 4], [['abc', 'defg', 'mnopqr', 'hijkl'], 4], [['abc', 'hijkl', 'mnopqr'], 3], [['abc', 'defg', 'dedfg', 'hijkl', 'defg', 'abc'], 6], [['xyz', 'pqr', 'lmnop', 'abcde', 'abcde'], 4], [['abc', 'defg', 'hijkl', 'abc', 'defg'], 0], [['hijkl', 'xyz', 'vRyohLy', 'hijkl', 'KpROouj'], 5], [['ddeffg', 'defg', 'deffg'], 3], [['abc', 'defg', 'hijkl', 'mnopqr', 'mnopqr', 'abc'], 0], [['abc', 'KpROouj', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 3], [['abc', 'defg', 'mnopqr', 'hijkl'], 2], [['abc', 'defg', 'xyzabc', 'hijkl'], 0], [['abc', 'pqr', 'defg', 'mnopqr', 'hijkl'], -1], [['abc', 'defg', 'hijkl', 'abc'], 1], [['abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], -1], [[], 2], [['abc', 'defg', 'hijklmnabcl', 'abc'], 1], [['abcdef', 'xyz', 'pqr', 'lmnop', 'defg'], 3], [['abc', 'KpROouj', 'hijkldefg', 'hijkl', 'abbc', 'defg', 'abc', 'aabcdec', 'babc', 'abc', 'abc'], 3], [['hijkl', 'abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 3], [['abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], -2], [['abc', 'hijkl', 'abc', 'defg'], 0], [['abc', 'defg', 'hijkl', 'defg'], 1], [['abc', 'hijkl', 'mnopqr'], 4], [['abc', 'defg', 'dedfg', 'hijkl', 'dedfddeffgg', 'defg', 'abc'], 6], [['abc', 'defg', 'xyzabc', 'hijkl'], 4], [['xz', 'hijkl', 'KpROouj', 'xyz', 'vRyohLy'], 5], [['abc', 'defg', 'hijkl', 'defg'], -1], [['abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 1], [['abc', 'mnopqr', 'hijkl', 'defg', 'abc', 'abc', 'aabcdec'], 3], [['abc', 'defg', 'xyzabc', 'hijkl'], 2], [['abc', 'defg', 'hijkl', 'defg'], 0], [['abc', 'defg', 'mnopqr'], 5], [['abc', 'mnopqr', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 3], [['abc', 'mnopqr', 'hijkl', 'dgefg', 'abc', 'abc', 'abc', 'abc'], -1], [['deffg', 'defg', 'deffg'], 2], [['ddeffg', 'abc'], 3], [['abc', 'mnopqr', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 2], [['defgabcddef', 'abc', 'defg', 'mnopqr'], 3], [['hijkl', 'mnopqr', 'hijkl'], 4], [['abc', 'mnopqr', 'hijkl', 'hijk', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], -2], [['abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 4], [['hijkl', 'xyz', 'vRyohLy', 'hijkl', 'KpROouj', 'vRyohLy'], 5], [['abc', 'defg', 'xyzabc', 'hijkl'], 5], [['abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'abc', 'babc', 'abc', 'abc'], 5], [['abc', 'defg', 'dedfg', 'hijkl', 'defg'], 5], [['hijk', 'abc', 'defg', 'hijkl', 'defg'], 3], [['abcddef', 'xyz', 'pqr', 'lmnop', 'abcde', 'abcde', 'lmnop'], 3], [['abc', 'defg', 'dedfg', 'hijkl', 'defg', 'abc', 'dedfg'], 6], [['abc', 'defg', 'abc', 'abc'], -1], [['abc', 'hijkl', 'hijklmnabcl', 'abc', 'defg'], 0], [['abc', 'mnopqr', 'hijkl', 'dgefg', 'abc', 'abc', 'abc', 'abc', 'dgefg'], -1], [['defg', 'defddeffgg', 'xyzabc', 'hijkl'], 5], [[], -1], [['abc', 'defg', 'deffg', 'mnopqr', 'hijkl'], 4], [['deffg', 'defg', 'deffg'], 1], [['abc', 'defg', 'deffg', 'mnopqr', 'hijhijklkl'], 3], [['abc', 'defg', 'deffg', 'hijkl', 'defg'], 2], [['abc', 'defg', 'xyzabc', 'hijkl'], 6], [['abc', 'hijkl', 'defg'], 3], [['ababcdefc', 'defg', 'deffg', 'hijkl', 'defg', 'defg'], 2], [['abc', 'defg', 'deffg', 'mnopqr', 'hijkl', 'hijkl'], 4], [['xz', 'hijkl', 'KpROouj', 'xyz', 'vRyohLy'], 4], [['hijkl', 'ababcdefc', 'xyz', 'vRyohLy'], 5], [['abbc', 'abc', 'defg', 'hijklmnabcl', 'abc'], 1], [['abcdef', 'xyz', 'pqr', 'lmnop', 'defg'], 2], [['ababcdefc', 'defg', 'deffg', 'hijkl', 'defg', 'defg'], 0], [['abcddef', 'xyz', 'pqr', 'lmnop', 'abcde', 'ababcdefc', 'lmnop'], 3], [['hijkl', 'abc', 'mnopqr', 'hijkl', 'abbc', 'defg', 'aabbc', 'abc', 'babc', 'abc', 'abc'], 3], [['abc', 'defg', 'dedfg', 'hijkl', 'defg'], 4], [['abc', 'defg', 'hijkl', 'mnopqr'], 1], [['ddeffg', 'abc'], -2], [['abc', 'defg', 'hijkl', 'dedfddeffgg', 'abc', 'defg'], 0]]
results = [['practice', 'solution'], ['Python'], ['exercises'], [], [], ['lmnop', 'abcde'], ['abc'], [], ['abc'], [], [], [], ['abc'], ['hijkl'], [], ['lmnop', 'abcde', 'abcde'], ['abc'], ['abc'], ['abcde'], [], ['lmnop'], ['abc', 'abc'], ['hijkl', 'hijkl'], ['abc'], ['abc', 'abc', 'abc', 'abc'], ['xyz', 'pqr'], ['defg'], [], ['defg'], ['abc', 'abc', 'abc', 'abc'], [], ['abc'], [], [], [], ['defg'], ['defg'], ['abc'], [], [], [], ['hijkl', 'hijkl'], [], [], ['abc', 'abc', 'abc', 'abc'], [], [], [], [], [], [], [], ['xyz', 'pqr'], ['abc', 'abc', 'abc', 'abc'], ['abc', 'abc', 'abc', 'abc'], [], [], [], [], [], ['defg'], ['hijkl'], [], [], ['abc', 'abc', 'abc'], [], [], [], ['abc', 'abc', 'abc', 'abc'], [], [], ['abc'], [], ['abc'], [], [], ['abbc', 'defg', 'babc'], ['hijkl', 'hijkl'], ['hijkl'], ['hijkl'], ['dedfg', 'hijkl'], ['abc'], ['xyz', 'pqr'], [], [], [], [], ['hijkl'], [], ['defg'], [], ['abc'], [], ['xyzabc'], ['abc'], [], ['defg'], [], ['hijkl'], [], [], [], ['xyz', 'pqr'], ['abc', 'abc', 'abc', 'abc'], ['defg', 'defg'], [], [], []]

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
        func_name = "extract_string"
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
        for test_case in ["assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']", "assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']", "assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']"]:
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
