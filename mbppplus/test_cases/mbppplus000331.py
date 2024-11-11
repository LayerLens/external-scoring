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
inputs = [[[('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2], [[('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3], [[('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10)], 2], [[], 0], [[('John', 20)], 1], [[('John', 20)], 0], [[('John', 20), ('John', 20)], 0], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10)], 1], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10)], 0], [[], -1], [[('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], 1], [[('John', 20), ('John', 20), ('John', 20)], 1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], 0], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], 1], [[('John', 20), ('John', 20), ('John', 20), ('John', 20)], 1], [[('John', 20), ('John', 20)], -2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], -1], [[('John', 20), ('John', 20)], 1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Nikhil', 10)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -4], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -5], [[('John', 20), ('John', 20), ('John', 20), ('John', 20)], -5], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], -5], [[('John', 20), ('John', 20), ('John', 20)], -2], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Manjeet', 10)], -4], [[('John', 20), ('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Manjeet', 10)], -4], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], -1], [[('John', 20), ('John', 20)], -3], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], -2], [[('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], 1], [[('Nikhil', 10, 'Nikhil'), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], 1], [[('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], 1], [[('John', 20), ('John', 20), ('John', 20), ('John', 20)], -1], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], -1], [[('John', 20), ('John', 20), ('John', 20), ('John', 20)], -2], [[('Nikhil', -5), ('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10)], 0], [[('John', -4), ('John', 20)], -1], [[('John', 20, 20), ('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Manjeet', 10)], -2], [[('John', 20, 20), ('John', 20), ('John', 20, 20), ('John', 20)], -1], [[('John', 20), ('John', 20), ('John', 20, 20), ('John', 20)], 2], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], 1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Manjeet', 10)], 1], [[('John', 20), ('John', 20), ('John', 20)], 2], [[('John', 20), ('John', 20), ('John', 20)], -1], [[], -5], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], 0], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -3], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Manjeet', 10)], 1], [[('John', 20), ('John', 20), ('John', 20), ('John', 20)], 2], [[('John', 20, 'John'), ('John', 20), ('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akshat', 10, 'Akshat')], -1], [[('John', 20, 20), ('John', 20), ('John', 20, 20), ('John', 20), ('John', 20)], -1], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Nikhil', 10)], -1], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], -2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], -5], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], 0], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akshat', 0), ('Nikhil', 10)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Manjeet', 10, 10)], -4], [[('Manjeet', 10), ('Akshat', 10), ('Nikhil', 10), ('Akash', 10)], -3], [[('Manjeet', 10), ('Akshat', 10, 'Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Manjeet', 10, 10)], -4], [[('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], 0], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10)], 0], [[('John', 20), ('John', 20)], 2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], -4], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Nikhil', 10), ('Akshat', 10, 'Akshat')], -1], [[('John', -4), ('John', 20)], -5], [[('Manjeet', 10), ('Akshat', 10), ('Manjaeet', 10), ('Akash', 10), ('Nikhil', 10)], 0], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10)], 1], [[('Nikhil', 10, 'Nikhil'), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Nikhil', 10)], 0], [[('Manjeet', 10), ('Akshat', 10), ('Manjaeet', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], 0], [[('John', -3), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], 0], [[('Manjeet', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -3], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10)], -4], [[('Manjeet', 10), ('Akshat', 10), ('Manjaeet', 10), ('Akash', 10), ('Nikhil', 10)], -1], [[('Manjeet', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -1], [[('Manjeet', 10), ('Akshat', 10, 'kshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], -5], [[('Akshat', 10, 'Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Manjeet', 10, 10)], -2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10)], -2], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], -1], [[('John', 20, 20), ('John', 20, 20), ('John', 20), ('John', 20, 'John')], -2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Nikhil', 10), ('Manjeet', 10)], -2], [[('Nikhil', -5), ('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Nikhil', -5)], 0], [[('John', 10, 20, 20), ('John', 20)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Akash', 10, 'Akash'), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10)], 1], [[('John', 10, 20, 20)], -1], [[('John', 20, 20), ('John', 20)], 1], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akshat', 0), ('Nikhil', 10), ('Akash', 10)], -1], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Akash', 10, 'Akash'), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10), ('Manjeet', 10)], 1], [[('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Nikhil', 10)], -2], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10)], -1], [[('John', -2), ('John', 20)], 1], [[('Manjeet', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], -3], [[('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 11), ('Akash', -4), ('Akash', 10)], -4], [[('Akshat', 10, 'Akshat'), ('Nikhil', 10)], 1], [[('John', -4), ('John', 20), ('John', 20)], -5], [[('Akshat', 10, 'Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Manjeet', 10, 10), ('Manjeet', 10, 10)], -2], [[('Akshat', 10), ('Manjeet', 10), ('Akash', 10), ('Nikhil', 10), ('Manjeet', 10)], 1], [[('John', 20), ('John', 20), ('John', 20), ('John', -1), ('John', 20)], 0], [[('Manjeet', 10), ('Akshat', 10), ('Akash', 10), ('Manjeet', 10)], 1]]
results = [[('Akash', 2), ('Akshat', 4)], [('Akash', 3), ('Angat', 5), ('Nepin', 9)], [('Ayesha', 9)], [('Manjeet', 10), ('Akshat', 10)], [], [('John', 20)], [], [], [('Manjeet', 10)], [], [], [], [('Manjeet', 10)], [('John', 20)], [], [('Manjeet', 10)], [('John', 20)], [], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10)], [('John', 20)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [('Manjeet', 10), ('Akshat', 10, 'Akshat')], [('Manjeet', 10)], [], [], [('John', 20)], [('John', 20), ('John', 20), ('John', 20), ('John', 20)], [('Manjeet', 10), ('Akshat', 10, 'Akshat')], [('John', 20)], [('Manjeet', 10)], [('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [], [('John', 20), ('John', 20), ('John', 20)], [('Akshat', 10, 'Akshat')], [('Nikhil', 10, 'Nikhil')], [('Akshat', 10, 'Akshat')], [('John', 20), ('John', 20), ('John', 20)], [('John', 20), ('John', 20), ('John', 20), ('John', 20), ('John', 20)], [('John', 20), ('John', 20)], [], [('John', -4)], [('John', 20, 20)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10)], [('John', 20, 20), ('John', 20), ('John', 20, 20)], [('John', 20), ('John', 20)], [('Manjeet', 10)], [('Manjeet', 10)], [('John', 20), ('John', 20)], [('John', 20), ('John', 20)], [], [], [('Manjeet', 10), ('Akshat', 10), ('Akash', 10)], [('Akshat', 10)], [('John', 20), ('John', 20)], [('John', 20, 'John'), ('John', 20)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [('John', 20, 20), ('John', 20), ('John', 20, 20), ('John', 20)], [('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [('John', 20), ('John', 20), ('John', 20), ('John', 20)], [], [], [('Akshat', 0), ('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [('Manjeet', 10), ('Akshat', 10, 'Akshat')], [('Manjeet', 10)], [('Manjeet', 10), ('Akshat', 10, 'Akshat', 10)], [], [], [('John', 20), ('John', 20)], [], [('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Nikhil', 10)], [], [], [('Manjeet', 10)], [], [], [], [('Manjeet', 10), ('Akash', 10)], [], [('Manjeet', 10), ('Akshat', 10), ('Manjaeet', 10), ('Akash', 10)], [('Manjeet', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], [('Manjeet', 10)], [('Akshat', 10, 'Akshat', 10), ('Akash', 10), ('Nikhil', 10)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10)], [('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10)], [('John', 20, 20), ('John', 20, 20)], [('Manjeet', 10), ('Akshat', 10, 'Akshat')], [], [('John', 10, 20, 20)], [('Manjeet', 10)], [], [('John', 20, 20)], [('Akshat', 0), ('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Nikhil', 10)], [('Manjeet', 10)], [('Akshat', 10), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10)], [('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10), ('Akash', 10), ('Akash', 10), ('Akash', 10)], [('John', -2)], [('Manjeet', 10)], [('Akash', -4), ('Manjeet', 10), ('Akshat', 10, 'Akshat'), ('Akash', 10), ('Nikhil', 10)], [('Akshat', 10, 'Akshat')], [], [('Akshat', 10, 'Akshat', 10), ('Akash', 10), ('Nikhil', 10), ('Akash', 10)], [('Akshat', 10)], [], [('Manjeet', 10)]]

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
        func_name = "min_k"
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
        for test_case in ["assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]", "assert min_k([('Sanjeev', 11), ('Angat', 5), ('Akash', 3), ('Nepin', 9)], 3) == [('Akash', 3), ('Angat', 5), ('Nepin', 9)]", "assert min_k([('tanmay', 14), ('Amer', 11), ('Ayesha', 9), ('SKD', 16)], 1) == [('Ayesha', 9)]"]:
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
