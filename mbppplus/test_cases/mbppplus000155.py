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
inputs = [[[('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]], [[('Juan Whelan', 50), ('Sabah Colley', 48), ('Peter Nichols', 37), ('Juan Whelan', 22), ('Sabah Colley', 14)]], [[('Juan Whelan', 10), ('Sabah Colley', 20), ('Peter Nichols', 30), ('Juan Whelan', 40), ('Sabah Colley', 50)]], [[('Alice', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Charlie', 40)]], [[('Alice', -50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40)]], [[('Alice', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 80), ('Bob', 70), ('Charlie', 70)]], [[('Alice', 50), ('Bob', 60), ('Charlie', 70), ('David', 80), ('Alice', 90), ('Bob', 100), ('Charlie', 110), ('David', 120), ('Alice', 130), ('Bob', 140), ('Charlie', 150), ('David', 160)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40)]], [[('Alice', -50), ('Alice', -50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bob', 50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40), ('Bob', -90)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bob', 50), ('Charlie', 70), ('Charlie', 70)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Charlie', 40), ('Bob', 50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bobb', 50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Bob', 50)]], [[('Alice', -50), ('AlDavidice', -50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bobb', 50), ('Charlie', 40)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40), ('Alice', 80), ('Charlie', 40)]], [[('AlDavidice', -50), ('Alice', -50), ('Alice', -50)]], [[('Bob', 110), ('Alice', 80), ('Bob', -90)]], [[('Alice', 80), ('Bob', -90), ('Bob', -89), ('Charlie', 70), ('Alice', -60), ('Bob', 50)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), (41, 40), ('Charlie', 40), ('Bob', 50)]], [[('Alice', -50), ('AlDavidice', -50), ('Alice', -50)]], [[('Bob', -90), ('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 70)]], [[('Alice', -50), ('Alice', -50), ('Alice', -50)]], [[('AlDavidice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50)]], [[('Alice', 80), ('Bob', 90), ('Alice', 80), ('Bob', 70), ('Charlie', 70), ('Bob', 70)]], [[('Alice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50)]], [[('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bo', -90), ('Bobb', 50), ('Charlie', 40)]], [[('AlDavidice', -50)]], [[('Alice', 80), ('Bob', 41), ('Charlie', 70), ('Alice', -60)]], [[('AlDavidice', 70)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Charlie', 40), ('Bob', 50), ('Charlie', 70)]], [[('AlDavidice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50)]], [[('Alice', 80), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40), ('Bob', -90)]], [[('Alice', 80), ('Charlie', 70), ('Alice', -60), ('Bobb', 50)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Bob', 50), ('Charlie', 70)]], [[('Alice', 80), ('Bob', 40), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40)]], [[('Alice', 80), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Bobb', 50), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bobb', 50)]], [[('Alice', 50), ('Bob', 60), ('Charlie', 70), ('David', 80), ('Alice', 90), ('Bob', 100), ('Charlie', 110), ('David', 120), ('Bob', 140), ('Charlie', 150), ('David', 160), ('David', 80)]], [[('Alice', 80), ('Bob', 90), ('Alice', 80), ('Bob', 70), ('Charlie', 70), ('Bob', 70), ('Bob', 70)]], [[('Bob', 90), ('Charlie', 70), ('Alice', 80), ('Bob', 70), ('Charlie', 70)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 100), ('Alice', 60), ('Bob', 50), ('Charlie', 40), ('Bob', 50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bo', -90), ('Bobb', 50), ('Charlie', 40)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Charlie', 40), ('Bob', 50), ('Alice', 60)]], [[('Alice', 80), ('Charlie', 70), ('Bob', 50), ('Charlie', 70), ('Charlie', 70)]], [[('Alice', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 80), ('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Alice', -60), ('Bob', 50), ('Charlie', 70)]], [[('BoBob', 110), ('Alice', 80), ('Bob', -90), ('Bob', -90)]], [[('Alice', -51), ('Alice', -50)]], [[('Alice', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 80), ('Bob', 70)]], [[('Alice', 80), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40), ('Bob', -90), ('Bob', 50)]], [[('Alice', -50), ('AlDavidice', -49), ('Alice', -50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Alice', 80)]], [[('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bobb', 50), ('Charlie', 40)]], [[('Chare', 70), ('Alice', 80), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40), ('Bob', -90)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Bob', -90)]], [[('BoBob', 110), ('Alice', 80), ('Bob', -90), ('Bob', -90), ('Alice', 80), ('Alice', 80)]], [[('Alice', 50), ('Bob', 60), ('Charlie', 70), ('David', 80), ('Alice', 90), ('Bob', 100), ('Charlie', 110), ('David', 120), ('Bob', 140), ('Charlie', 150), ('David', 160), ('David', 80), ('Bob', 60)]], [[('Ali', 80), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Charlie', 40), ('Bob', 50), ('Alice', 60)]], [[('Alice', 80), ('Bob', 41), ('Charlie', 70), ('Alice', -60), ('Alice', -60)]], [[('Alice', 80), ('Bob', 90), ('Alice', 81), ('Charlie', 70), ('Alice', 80), ('Bob', 70)]], [[('Alice', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 100), ('Alice', 80), ('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Alice', -60)]], [[('Bob', 41), ('Charlie', 70), ('Alice', -60)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bob', 50), ('Charlie', 70)]], [[('AlDavidice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50), ('Alice', -50)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), ('Bob', 50), ('Charlie', 40), ('Bob', 50), ('Charlie', 70), ('Charlie', 70)]], [[('Alice', 80), ('Charlie', 70), ('Bob', 50), ('Charlie', 40)]], [[('Alice', -50), ('AlDavidice', -49), ('Alice', -50), ('Alice', -50)]], [[('Alice', 80), ('Charlie', 69), ('Bob', -90), ('Charlie', 70), ('Charlie', 70), ('Charlie', 70)]], [[('Alice', 50), ('Bob', 60), ('Charlie', 70), ('David', 80), ('Alice', 90), ('Bob', 100), ('Charlie', 110), ('Bob', 140), ('Charlie', 150), ('David', 160), ('David', 80)]], [[('Alice', -50), ('AlDavidice', -49), ('Alice', -50), ('Alice', -50), ('AlDavidice', -49), ('Alice', -50)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('BoDavid', 50)]], [[('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 70)]], [[('Charli', 70)]], [[('Alice', 80), ('Bob', 40), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bob', 40)]], [[('Alice', 80), ('Bob', 40), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bob', -90)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bobb', 50), ('Bob', -90), ('Bob', -90)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('BoDavid', 50), ('Bob', 50), ('Bob', -90)]], [[('Alice', 80), ('Charlie', 70), ('Bob', 50), ('Charlie', 70), ('BoDavid', 70)]], [[('Alice', 80), ('Charlie', 70), ('Bob', 50), ('Charlie', 70), ('Charlie', 70), ('Charlie', 70)]], [[('Alice', 80), ('Alice', 81), ('Charlie', 70), ('Alice', 80), ('Bob', 70), ('Alice', 80), ('Alice', 80), ('Alice', 80)]], [[('Alice', 80), ('Bob', -90), ('Alice', -60), ('Bob', 50), ('Charlie', 70), ('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Charlie', 40), ('Bob', -90), ('Alice', 80)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bob', 50), ('Bob', 50)]], [[('Bob', 110), ('Alice', 80), ('Bob', -90), ('Bob', -90), ('Bob', 110)]], [[('Ali', 80), ('Bob', 90), ('Charlie', 70), ('Alice', 60), (41, 40), ('Charlie', 40), ('Bob', 50), ('Bob', 50)]], [[('Alice', 80), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Bob', -90), ('Bob', 50)]], [[('Bob', -90), ('Charlie', 70), ('Bo', -90), ('Bobb', 50), ('Charlie', 40)]], [[('Alice', 50), ('Bob', 60), ('David', 80), ('Alice', 90), ('Bob', 100), ('Charlie', 110), ('Bob', 140), ('Charlie', 150), ('David', 160), ('David', 80)]], [[('Alice', 80), ('Bob', -90), ('Alice', -60), ('Bob', 50), ('BoDavid', 50), ('Bob', 50), ('Bob', -90)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Bobb', 50), ('Bob', -90), ('BoBob', -90)]], [[('Alice', 80), ('Bob', 90), ('Alice', 80), ('Bob', 70), ('Charlie', 70), ('Bob', 70), ('Bob', 70), ('Bob', 70)]], [[('Alice', 80), ('Bob', -90), ('Bob', -89), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('Alice', 80)]], [[('Alice', 80), ('Bob', 40), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Charlie', 40), ('Bob', 40), ('Charlie', 40)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bobb', 50), ('Alice', 80), ('Charlie', 70)]], [[('AlDavidice', 70), ('AlDavidice', 70)]], [[('Charlie', 70), ('Alice', -60)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Charlie', 70)]], [[('Alice', 80), ('Bob', -90), ('Charlie', 70), ('Alice', -60), ('Bob', 50), ('BoDavid', 50), ('Charlie', 70)]]]
results = [('Juan Whelan', 212), ('Juan Whelan', 72), ('Sabah Colley', 70), ('Alice', 140), ('Alice', -50), ('Charlie', 110), ('Alice', 160), ('David', 360), ('Charlie', 70), ('Charlie', 110), ('Alice', -100), ('Alice', 80), ('Charlie', 110), ('Charlie', 70), ('Charlie', 210), ('Bob', 190), ('Charlie', 110), ('Charlie', 70), ('Alice', -50), ('Charlie', 150), ('Charlie', 150), ('AlDavidice', -50), ('Alice', 80), ('Charlie', 70), ('Bob', 190), ('AlDavidice', -50), ('Charlie', 70), ('Charlie', 70), ('Charlie', 140), ('Alice', -150), ('AlDavidice', -50), ('Bob', 230), ('Alice', -200), ('Charlie', 70), ('Charlie', 110), ('AlDavidice', -50), ('Charlie', 70), ('AlDavidice', 70), ('Bob', 190), ('AlDavidice', -50), ('Charlie', 110), ('Charlie', 70), ('Bob', 190), ('Charlie', 110), ('Charlie', 140), ('Bobb', 150), ('David', 440), ('Bob', 300), ('Bob', 160), ('Bob', 190), ('Charlie', 110), ('Bob', 190), ('Charlie', 210), ('Alice', 160), ('Charlie', 70), ('BoBob', 110), ('Alice', -101), ('Alice', 160), ('Charlie', 110), ('AlDavidice', -49), ('Alice', 100), ('Charlie', 150), ('Charlie', 110), ('Charlie', 70), ('Alice', 240), ('David', 440), ('Alice', 120), ('Charlie', 70), ('Alice', 241), ('Alice', 260), ('Charlie', 70), ('Charlie', 70), ('Charlie', 140), ('AlDavidice', -50), ('Charlie', 250), ('Charlie', 110), ('AlDavidice', -49), ('Charlie', 279), ('Charlie', 330), ('AlDavidice', -98), ('Charlie', 70), ('Charlie', 140), ('Charli', 70), ('Charlie', 110), ('Charlie', 110), ('Alice', 80), ('Charlie', 70), ('Charlie', 140), ('Charlie', 280), ('Alice', 481), ('Charlie', 140), ('Charlie', 110), ('Alice', 80), ('Alice', 80), ('Bob', 190), ('Charlie', 70), ('Charlie', 110), ('David', 320), ('BoDavid', 50), ('Alice', 80), ('Bob', 370), ('Alice', 100), ('Charlie', 150), ('Charlie', 140), ('AlDavidice', 140), ('Charlie', 70), ('Charlie', 140), ('Charlie', 140)]

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
        func_name = "max_aggregate"
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
        for test_case in ["assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)", "assert max_aggregate([('Juan Whelan',50),('Sabah Colley',48),('Peter Nichols',37),('Juan Whelan',22),('Sabah Colley',14)])==('Juan Whelan', 72)", "assert max_aggregate([('Juan Whelan',10),('Sabah Colley',20),('Peter Nichols',30),('Juan Whelan',40),('Sabah Colley',50)])==('Sabah Colley', 70)"]:
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
