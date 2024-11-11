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
inputs = [[['python', 'PHP', 'bigdata']], [['a', 'ab', 'abc']], [['small', 'big', 'tall']], [['Longest', 'word', 'length']], [['This', 'is', 'a', 'complex', 'example', 'to', 'test', 'the', 'function']], [['elephant', 'fox', 'monkey', 'zebra', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['fox', 'monkey', 'zebra', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['elephant', 'fox', 'monkey', 'zebra', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['fox', 'Longest', 'zebra', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['fox', 'monkey', 'zebra', 'lion', 'This', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'monkey']], [['elephant', 'fox', 'monkey', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['elephant', 'fox', 'monkey', 'zebra', 'tiger', 'giraffe', 'p', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['i', 'This', 'is', 'a', 'complex', 'example', 'to', 'test', 'the', 'ttoo', 'function']], [['elephant', 'fox', 'monkey', 'zebra', 'lion', 'tiger', 'gireaffe', 'kangaroo', 'panda', 'hippopotamus']], [['elephant', 'fox', 'monkey', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger', 'tiger']], [['elephant', 'fox', 'monkey', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangamonkeyroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['fox', 'monkey', 'zebra', 'tiger', 'giraffe', 'p', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['This', 'is', 'a', 'complex', 'example', 'to', 'test', 'the', 'function', 'a']], [['Longest', 'length']], [['fox', 'Longest', 'zebra', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['fox', 'monkey', 'zebra', 'tiger', 'giraffe', '', 'p', 'kangaroo', 'foelephantx', 'bear', 'panda', 'hippopotamus']], [['fox', 'Longest', 'zebra', 'pandaa', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['Longest', 'zebra', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['Longest', 'length', 'Longest']], [['fox', 'monkey', 'zebra', 'tiger', 'giraffe', '', 'p', 'kangaroo', 'foelephantx', 'bear', 'panda', 'hippopotamus', 'giraffe']], [['elephant', 'fox', 'monkey', 'function', 'zebra', 'lion', 'tiger', 'gireaffe', 'kangaroo', 'panda', 'hippopotamus']], [['length', 'LongestThis', 'Longest']], [['elephant', 'fox', 'monkey', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['This', 'is', '', 'a', 'complex', 'example', 'to', 'test', 'the', 'function', 'the']], [['This', 'is', 'a', 'complex', 'example', 'to', 'the', 'aa', 'function', 'a']], [['This', 'is', 'a', 'complex', 'example', 'to', 'test', 'the', 'function', 'a', 'a']], [['elephant', 'fox', 'teiger', 'monkey', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['elephant', 'fox', 'monkey', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['elephant', 'fx', 'monkey', 'zebra', 'lion', 'tiger', 'giraffe', 'giraff', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['elephant', 'fox', 'zebra', 'monkey', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['This', 'is', 'a', 'complex', 'example', 'is', 'test', 'the', 'function', 'a', 'a']], [['This', 'is', '', 'a', 'complex', 'example', 'to', 'test', 'the']], [['fox', 'monkey', 'zebra', 'lion', 'tigttooer', 'giraffe', 'kangaroo', 'bear', 'hippopotamus']], [['Longest', 'word', 'length', 'Longest']], [['This', 'a', 'complex', 'example', 'to', 'test', 'thte', 'function', 'a', 'a']], [['monkey', 'zebra', 'tiger', 'giraffe', '', 'p', 'kangaroo', 'foelephantx', 'bear', 'panda', 'hippopotamus']], [['Longest', 'Lonngest', 'length', 'Longest']], [['leth', 'LongestThis', 'Longest']], [['fnunction', 'This', 'is', 'a', 'complex', 'example', 'to', 'the', 'aa', 'function', 'a']], [['elephant', 'fox', 'monkey', 'LongestThis', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger', 'tiger']], [['This', 'is', 'elephant', 'complex', 'example', 'is', 'test', 'the', 'function', 'a', 'a']], [['fox', 'monkey', 'zebra', 'lion', 'This', 'giraffe', 'kangaroo', 'bear', 'panda', 'giraffbeare', 'hippopotamus', 'monkey']], [['elephant', 'fox', 'monkey', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'hippopotamus', 'tiger']], [['This', 'a', 'complex', 'giraffbeare', 'to', 'test', 'thte', 'function', 'a', 'a']], [['Longest', 'word', 'Lonpgest', 'length', 'Longest', 'Longest']], [['Longest', 'word', 'length', 'word']], [['This', 'is', 'a', 'complex', 'example', 'to', 'test', 'function', 'a', 'a']], [['This', 'is', 'a', 'complex', 'example', 'to', 'test', 'oto', 'function', 'a', 'a', 'is']], [['Longest']], [['fox', 'monkey', 'zebra', 'lion', 'giraffe', 'kangaroo', 'bear', 'hippopotamus']], [['leth', 'LongestThis', 'leelephantth', 'Longest']], [['Lot', 'word', 'length', 'word']], [['Longest', 'fnunction', 'lion', 'tigerLongest', 'giraffe', 'kangaroo', 'bear', 'hippopotamus']], [['elephant', 'fx', 'monkey', 'zebra', 'foelephantx', 'lion', 'tiger', 'giraffe', 'giraff', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['This', 'a', 'example', 'to', 'test', 'thte', 'function', 'a', 'a']], [['This', 'a', 'complex', 'the', 'to', 'test', 'thte', 'function', 'a', 'a']], [['is', 'a', 'complex', 'example', 'to', 'test', 'the', 'function', 'a', 'a']], [['This', 'a', 'complex', 'the', 'to', 'apandaa', 'test', 'thte', 'function', 'a', 'a']], [['Longest', 'word', 'length', 'Longest', 'Longest']], [['Lonpgest', 'monkey', '', 'length', 'length']], [['lgth', 'Longest', 'length', 'Longest', 'length']], [['elephant', 'fox', 'monkey', 'zebra', 'zebralengthn', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger', 'tiger', 'elephant']], [['is', 'a', 'complex', 'word', 'to', 'test', 'the', 'function', 'a', 'a']], [['This', 'TThis', 'is', 'a', 't', 'complex', 'example', 'to', 'test', 'the', 'function', 'the']], [['LLot', 'word', 'length', 'word', 'word']], [['Longest', 'fnunction', 'lion', 'tigerLongest', 'giraffe', 'bear', 'hippopotamus']], [['is', 'a', 'complex', '', 'example', 'to', 'test', 'the', 'function', 'a', 'a']], [['This', 'a', 'complex', 'the', 'to', 'apandaa', 'test', 'thtte', 'function', '', 'a']], [['Longest', 'lion', 'tigerLongest', 'giraffe', 'bbr', 'kangaroo', 'bbear', 'bear', 'hippopotamus']], [['Longest', 'word', 'length', 'Longest', 'Longest', 'word', 'Longest']], [['Lot', 'fox', 'monkey', 'zebra', 'zera', 'giraffe', 'hiippopotamus', 'kangaroo', 'bear', 'hippopotamus']], [['This', 'is', 'elephant', 'example', 'is', 'test', 'the', 'function', 'a', 'a']], [['Longest', 'fnunction', 'lion', 'tigerLongest', 'giraffe', 'bearr', 'hippopotamus', 'fnunction']], [['LLot', 'word', 'length', 'word', 'panda']], [['fox', 'LongestThis', 'Longsest', 'example']], [['elephant', 'giraff', 'monkey', 'lion', 'tiger', 'mlengthonkey', 'giraffe', 'kangaroo', 'bear', 'panda', 'pada', 'hippopotamus']], [['elephant', 'fox', 'zebra', 'zebra', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger']], [['This', 'a', 'complex', 'the', 'to', 'apandaa', 'length', 'test', 'thtte', 'function', '', 'a']], [['Longest', 'fnunction', 'lion', 'tigerLongest', 'giraffe', 'kangaroo', 'bear', 'hippopotamus', 'fnunction']], [['Longetst', 'zebra', 'lion', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['a', 'complex', 'giraffbeare', 'to', 'test', 'thte', 'function', 'a', 'a']], [['zera', 'Lot', 'word', 'length', 'word', 'zera']], [['oto', 'This', 'is', 'a', 'complex', 'example', 'to', 'the', 'aa', 'function', 'a']], [['Longest', 'fnunction', 'lion', 'tigerLongest', 'giraffe', 'fnuncction', 'bear', 'hippopotamus']], [['oto', 'This', 'a', 'complex', 'example', 'aa', 'to', 'aa', 'function', 'a']], [['This', 'is', 'elephant', 'example', 'is', 'test', 'the', 'function', 'elephant', 'a']], [['lgth', 'Longest', 'length', 'Longest', 'length', 'Longest']], [['elephant', 'fox', 'monkey', 'LongestThis', 'zebran', 'tiger', 'giraffe', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger', 'kangamonkeyroo']], [['oto', 'This', 'is', 'a', 'complex', 'exampl', 'to', 'the', 'aa', 'function', 'hthe', 'a']], [['fox', 'p', 'zebra', 'tiger', 'giraffe', 'p', 'kangaroo', 'foelephantx', 'bear', 'panda', 'hippopotamus', 'giraffe']], [['elephant', 'fox', 'monkey', 'LongestThis', 'zebran', 'tiger', 'kangaroo', 'bear', 'panda', 'hippopotamus', 'tiger', 'kangamonkeyroo', 'monkey']], [['fox', 'Longest', 'zebra', 'lion', 'tiger', 'girafffoelephantx', 'kangaroo', 'bear', 'panda', 'hippopotamus']], [['elephant', 'fox', 'monkey', 'function', 'zebra', 'lion', 'tiger', 'gireaffe', 'to', 'kangaroo', 'panda', 'hippopotamus']], [['This', 'a', 'complex', 'the', 'to', 'apandaa', 'test', 'thte', 'function', 'a', 'a', 'apandaa']], [['fnunction', 'This', 'is', 'a', 'complex', 'example', 'to', 'the', 'aa', 'function', 'a', 'to', 'to']], [['is', 'a', 'complex', '', 'to', 'test', 'the', 'function', 'a', 'a']], [['This', 'a', 'complex', 'the', 'to', 'apandaa', 'test', 'thtte', 'function', '', 'a', 'complex']], [['This', 'is', '', 'a', 'complex', 'example', 'to', 'test', 'the', 'function', 'the', 'th', 'a']], [['elephant', 'fox', 'monkey', 'function', 'zebra', 'lion', 'tiger', 'gireaffe', 'kangaroo', 'panda', 'girafffoelephantx', 'hippopotamus']], [['Longest', 'fnunction', 'lion', 'tigerLongest', 'giraffe', 'bearr', 'fnunction']], [['Longest', 'lion', 'tigerLongest', 'giraffe', 'bearr', 'fnunction']]]
results = [7, 3, 5, 7, 8, 12, 12, 12, 12, 12, 12, 12, 8, 12, 12, 14, 12, 8, 7, 12, 12, 12, 12, 7, 12, 12, 11, 12, 8, 8, 8, 12, 12, 12, 12, 8, 7, 12, 7, 8, 12, 8, 11, 9, 12, 8, 12, 12, 11, 8, 7, 8, 8, 7, 12, 12, 6, 12, 12, 8, 8, 8, 8, 7, 8, 7, 12, 8, 8, 6, 12, 8, 8, 12, 7, 13, 8, 12, 6, 11, 12, 12, 8, 12, 12, 11, 6, 8, 12, 8, 8, 7, 14, 8, 12, 14, 17, 12, 8, 9, 8, 8, 8, 17, 12, 12]

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
        func_name = "len_log"
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
        for test_case in ['assert len_log(["python","PHP","bigdata"]) == 7', 'assert len_log(["a","ab","abc"]) == 3', 'assert len_log(["small","big","tall"]) == 5']:
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
