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
inputs = [[('Mers', 'for', 'Vers')], [('Avenge', 'for', 'People')], [('Gotta', 'get', 'go')], [('Lorem', 'ipsum', 'dolor', 'sit', 'amet')], [('Quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')], [('Python', 'is', 'a', 'widely', 'used', 'programming', 'language')], [('This', 'is', 'a', 'test', 'for', 'the', 'function')], [('Complex', 'input', 'to', 'test', 'the', 'function', 'with')], [('I', 'love', 'writing', 'code', 'in', 'Python')], [('The', 'function', 'should', 'handle', 'both', 'strings', 'and', 'numbers')], [('We', 'expect', 'the', 'output', 'to', 'be', 'a', 'list', 'of', 'characters')], [()], [('Hello', 'World!', '12345')], [('123', 'abc', '456')], [('Hello World', 'This is a test', 'for the function')], [('apple', 'banana', 'cherry', 'durian')], [('apple', 'orange', 'mango', 'kiwi', 'papaya')], [('dog', 'cat', 'hamster', 'guinea pig', 'rabbit', 'gerbil')], [('The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog!')], [('hello123', 'world456', 'python789')], [('1', '2', '3', '4', '5')], [('-1', '-2', '-3', '-4', '-5')], [('9', 'a', 'b', '1', '2')], [('input', 'kiwi', 'app4le', 'papaya')], [('Hello', 'World!', '12345', 'He', '12345')], [('apple', 'banana', 'mango', 'cherry', 'durian', 'bananna', 'durian', 'durian')], [('The', 'function', 'over', 'should', 'handle', 'both', 'strings', 'and', 'numbers')], [('strings', 'This is a test', 'for the function')], [('banana', 'durian', 'apple')], [('Hello World', 'This is a test')], [('The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'World', 'lazy', 'dog!')], [('banana', 'durian', 'fox')], [('The', 'quic', 'brown', 'fox', 'jumps', 'over', 'the', 'World', 'lazy', 'dgd!')], [('The', 'function', 'over', 'should', 'handle', 'both', 'strings', 'and', 'numbers', 'strings')], [('dog', 'cat', 'hamster', 'guinea pig', 'rabbit', 'gerbil', 'guinea pig')], [('brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')], [('dog', 'cat', 'love', 'used', 'hamster', 'guinea pig', 'rabbit', 'gerbil')], [('strings', 'This is a test', 'for the function', 'strings')], [('apple', 'orange', 'maoutputngo', 'kiwi', 'papaya')], [('1', '2', '3', '4', 'dolor')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings')], [('brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'fox')], [('The', 'function', 'over', 'should', 'handle', 'dgd!', 'strings', 'and', 'numbers')], [('uswidelyed', 'dog', 'cat', 'love', 'used', 'hamster', 'guinea pig', 'rabbit', 'gerbil')], [('The', 'quick', 'brown', 'fox', 'expect', 'jumps', 'over', 'the', 'lazy', 'dog!')], [('dog', 'cat', 'love', 'used', 'guinea pig', 'rabbit')], [('This', 'is', 'a', 'test', 'for', 'function')], [('This', 'is', 'a', 'sit', 'test', 'for', 'function')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'strings')], [('4', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'doog', 'fox')], [('1', '2rabbit', '3', '4', 'handle', 'dolor')], [('The', 'quic', 'brown', 'fox', 'jumps', 'the', 'World', 'd!gd!', 'abc', 'dgd!')], [('The', 'function', 'over', 'should', 'handle', 'ThTe', 'both', 'strings', 'and', 'numbers', 'strings')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('dog', 'cat', 'hamster', 'guinea pig', 'rabbit', 'gerbil', 'guinea pig', 'guinea pig')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'string', 'strings', 'strings')], [('Quick', 'brown', 'fox', 'jumps', 'over', 'laazy', 'the', 'lazy', 'dog')], [('dog', 'ctI', 'hamster', 'guinea pig', 'rabbit', 'gerbil', 'guinea pig', 'guinea pig')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', '-2', 'numbers', 'strings', 'handle')], [('This', 'is', 'a', 'test', 'for', 'the', 'function', 'for', 'for')], [('apple', 'laazy', 'banana', 'mango', 'cherry', 'durian', 'bananna', 'durian', 'durian')], [('This', 'is', 'a', 'test', 'for', 'function', 'for')], [('apple', 'laazy', 'banana', 'mango', 'cherry', 'durian', 'bananna', 'durian', 'durian', 'cherry')], [('The', 'function', 'over', 'should', 'handle', 'ThTe', 'both', 'and', 'numbers', 'strings', 'over')], [('input', 'kiwi', 'pappaya', 'gerbil', 'papaya')], [('dog', 'cat', 'hamsterof', 'guinea pig', 'rabbit', 'gerbil')], [('The', 'function', 'over', 'should', 'handle', 'both', 'strings', 'anjumpsd', 'numbers', 'strings')], [('The', 'quick', 'brown', 'fox', 'brown', 'jumps', 'over', 'the', 'lazy', 'dog!')], [('dtheog', 'love', 'used', 'guinea pig', 'rabbit')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle', 'and')], [('dog', 'cat', 'guinea pig', 'rabbit', 'gerbil', 'dog')], [('kiwi', 'app4le', 'papaya')], [('Complex', '-5', 'love', 'used', 'hamster', 'guinea pig', 'rabbit', 'gerbil', 'guinea pig')], [('Lorem', 'dolor', 'cat', 'sit', 'amet', 'amet')], [('The', 'function', 'over', 'should', 'handle', 'dgd!', 'strings', 'and', 'numbers', 'numbers', 'The')], [('The', 'functon', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('apple', 'orange', 'mango', 'kiwi', 'papaya', 'kiwi')], [('brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'fox', 'fox')], [('Hello World', 'This is a test', 'for the function', 'Hello World')], [('This', 'test', 'for', 'function')], [('dtheog', 'love', 'used', 'guinea pig', 'rabbit', 'guinea pig')], [('This', 'a', 'test', 'for', 'the', 'function')], [('uswidelyed', 'dog', 'cat', 'used', 'hamster', 'guinea pig', 'rabbit', 'gerbil')], [('The', 'function', 'should', 'handle', 'both', 'strings', 'botd!gd!h', 'and', 'numbers')], [('The', 'funnction', 'over', 'should', 'handle', 'dgd!', 'strings', 'and', 'numbers')], [('-3The', 'function', 'over', 'should', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('rrabbit', 'dog', 'ctI', 'hamster', 'guinea pig', 'rabbit', 'gerbil', 'guinea pig', 'guinea pig')], [('banana', 'apple', 'apple')], [('dog', 'cat', 'used', 'hamter', 'guinea pig', 'rabbit', 'gerbil')], [('-3The', 'function', 'over', 'd!gd!', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('dog', 'cat', 'guinea pig', '123', 'gerbil', 'dog')], [('We', 'expect', 'pappaya', 'output', 'to', 'be', 'a', 'list', 'of', 'characters')], [('banana', 'durian', 'fox', 'durian')], [('The', 'function', 'over', 'should', 'ThTe', 'handale', 'both', 'strings', 'and', 'numbers', 'strings', 'strings', 'The')], [('dtheog', 'love', 'used', 'guinea pig', 'rabbit', 'guinea pig', 'guinea pig')], [('This', 'is', 'a', 'for', 'function')], [('1', '3', '4', 'handle', 'dolor')], [('Imango', 'love', 'writing', 'code', 'in', 'Python', 'Python')], [('The', 'function', 'over', 'should', 'ThTe', 'numipsumrs', 'handle', 'both', 'brown', 'and', 'numbers', 'strings')], [('I', 'love', 'writing', 'code', 'in', 'Python', 'I')], [('Thloveis', 'is', 'a', 'sit', 'test', 'for', 'function')], [('rOdbYFwfQl', 'TI', 'hamter', 'jumps')], [('input', 'kiwi', 'pappaya')], [('dtheog', 'love', 'used', 'guinea pig', 'rabbit', 'guinea pigwriting', 'guinea pig', 'guinea pig')], [('The', 'brown', 'fox', 'jumps', 'the', 'World', 'd!gd!', 'abc', 'dgd!')], [('The', 'function', 'over', 'should', 'ThTe', '3', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('ctI', 'banana', 'apple', 'apple')], [('input', 'kiwi', 'app4le', 'papaya', 'app4le')], [('The', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('The', 'brown', 'fox', 'Wrld', 'jumps', 'the', 'World', 'd!gd!', 'abc', 'dgd!')], [('apple', 'orange', 'maoutputngo', 'kiwi', 'papaya', 'apple')], [('We', 'expect', 'the', 'output', 'to', 'be', 'a', 'list', 'of', 'characters', 'expecct')], [('1', '2', '3', '4', 'dolor', '2')], [('apple', 'banana', 'durian', 'durian')], [('The', 'function', 'over', 'shoduld', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'strings')], [('The', 'function', 'over', 'should', 'ThTe', 'handle', 'both', 'strings', 'and', 'numbers', 'used')], [('brown', 'ddog', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog')], [('-33The', 'function', 'over', 'd!gd!', 'handle', 'both', 'strings', 'and', 'numbers', 'strings', 'handle')], [('We', 'expect', 'papWorldpaya', 'output', 'to', 'be', 'a', 'of', 'characters')], [('input', 'kiwi', 'app4le')], [('9', 'a', '1', '2')], [('love', '9', 'TI', 'hamter', 'jumps')], [('The', 'funnction', 'over', 'nmangoumbers', 'should', 'handle', 'dgd!', 'strings', 'and', 'numbers')]]
results = [['s', 'r', 's'], ['e', 'r', 'e'], ['a', 't', 'o'], ['m', 'm', 'r', 't', 't'], ['k', 'n', 'x', 's', 'r', 'e', 'y', 'g'], ['n', 's', 'a', 'y', 'd', 'g', 'e'], ['s', 's', 'a', 't', 'r', 'e', 'n'], ['x', 't', 'o', 't', 'e', 'n', 'h'], ['I', 'e', 'g', 'e', 'n', 'n'], ['e', 'n', 'd', 'e', 'h', 's', 'd', 's'], ['e', 't', 'e', 't', 'o', 'e', 'a', 't', 'f', 's'], [], ['o', '!', '5'], ['3', 'c', '6'], ['d', 't', 'n'], ['e', 'a', 'y', 'n'], ['e', 'e', 'o', 'i', 'a'], ['g', 't', 'r', 'g', 't', 'l'], ['e', 'k', 'n', 'x', 's', 'r', 'e', 'y', '!'], ['3', '6', '9'], ['1', '2', '3', '4', '5'], ['1', '2', '3', '4', '5'], ['9', 'a', 'b', '1', '2'], ['t', 'i', 'e', 'a'], ['o', '!', '5', 'e', '5'], ['e', 'a', 'o', 'y', 'n', 'a', 'n', 'n'], ['e', 'n', 'r', 'd', 'e', 'h', 's', 'd', 's'], ['s', 't', 'n'], ['a', 'n', 'e'], ['d', 't'], ['e', 'k', 'n', 'x', 's', 'r', 'e', 'd', 'y', '!'], ['a', 'n', 'x'], ['e', 'c', 'n', 'x', 's', 'r', 'e', 'd', 'y', '!'], ['e', 'n', 'r', 'd', 'e', 'h', 's', 'd', 's', 's'], ['g', 't', 'r', 'g', 't', 'l', 'g'], ['n', 'x', 's', 'r', 'e', 'y', 'g'], ['g', 't', 'e', 'd', 'r', 'g', 't', 'l'], ['s', 't', 'n', 's'], ['e', 'e', 'o', 'i', 'a'], ['1', '2', '3', '4', 'r'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's'], ['n', 'x', 's', 'r', 'e', 'y', 'g', 'x'], ['e', 'n', 'r', 'd', 'e', '!', 's', 'd', 's'], ['d', 'g', 't', 'e', 'd', 'r', 'g', 't', 'l'], ['e', 'k', 'n', 'x', 't', 's', 'r', 'e', 'y', '!'], ['g', 't', 'e', 'd', 'g', 't'], ['s', 's', 'a', 't', 'r', 'n'], ['s', 's', 'a', 't', 't', 'r', 'n'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 's'], ['4', 'n', 'x', 's', 'r', 'e', 'y', 'g', 'x'], ['1', 't', '3', '4', 'e', 'r'], ['e', 'c', 'n', 'x', 's', 'e', 'd', '!', 'c', '!'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 'e'], ['g', 't', 'r', 'g', 't', 'l', 'g', 'g'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 'g', 's', 's'], ['k', 'n', 'x', 's', 'r', 'y', 'e', 'y', 'g'], ['g', 'I', 'r', 'g', 't', 'l', 'g', 'g'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', '2', 's', 's', 'e'], ['s', 's', 'a', 't', 'r', 'e', 'n', 'r', 'r'], ['e', 'y', 'a', 'o', 'y', 'n', 'a', 'n', 'n'], ['s', 's', 'a', 't', 'r', 'n', 'r'], ['e', 'y', 'a', 'o', 'y', 'n', 'a', 'n', 'n', 'y'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 'd', 's', 's', 'r'], ['t', 'i', 'a', 'l', 'a'], ['g', 't', 'f', 'g', 't', 'l'], ['e', 'n', 'r', 'd', 'e', 'h', 's', 'd', 's', 's'], ['e', 'k', 'n', 'x', 'n', 's', 'r', 'e', 'y', '!'], ['g', 'e', 'd', 'g', 't'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 'e', 'd'], ['g', 't', 'g', 't', 'l', 'g'], ['i', 'e', 'a'], ['x', '5', 'e', 'd', 'r', 'g', 't', 'l', 'g'], ['m', 'r', 't', 't', 't', 't'], ['e', 'n', 'r', 'd', 'e', '!', 's', 'd', 's', 's', 'e'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 'e'], ['e', 'e', 'o', 'i', 'a', 'i'], ['n', 'x', 's', 'r', 'e', 'y', 'g', 'x', 'x'], ['d', 't', 'n', 'd'], ['s', 't', 'r', 'n'], ['g', 'e', 'd', 'g', 't', 'g'], ['s', 'a', 't', 'r', 'e', 'n'], ['d', 'g', 't', 'd', 'r', 'g', 't', 'l'], ['e', 'n', 'd', 'e', 'h', 's', 'h', 'd', 's'], ['e', 'n', 'r', 'd', 'e', '!', 's', 'd', 's'], ['e', 'n', 'r', 'd', 'e', 'h', 's', 'd', 's', 's', 'e'], ['t', 'g', 'I', 'r', 'g', 't', 'l', 'g', 'g'], ['a', 'e', 'e'], ['g', 't', 'd', 'r', 'g', 't', 'l'], ['e', 'n', 'r', '!', 'e', 'h', 's', 'd', 's', 's', 'e'], ['g', 't', 'g', '3', 'l', 'g'], ['e', 't', 'a', 't', 'o', 'e', 'a', 't', 'f', 's'], ['a', 'n', 'x', 'n'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 's', 'e'], ['g', 'e', 'd', 'g', 't', 'g', 'g'], ['s', 's', 'a', 'r', 'n'], ['1', '3', '4', 'e', 'r'], ['o', 'e', 'g', 'e', 'n', 'n', 'n'], ['e', 'n', 'r', 'd', 'e', 's', 'e', 'h', 'n', 'd', 's', 's'], ['I', 'e', 'g', 'e', 'n', 'n', 'I'], ['s', 's', 'a', 't', 't', 'r', 'n'], ['l', 'I', 'r', 's'], ['t', 'i', 'a'], ['g', 'e', 'd', 'g', 't', 'g', 'g', 'g'], ['e', 'n', 'x', 's', 'e', 'd', '!', 'c', '!'], ['e', 'n', 'r', 'd', 'e', '3', 'h', 's', 'd', 's', 's', 'e'], ['I', 'a', 'e', 'e'], ['t', 'i', 'e', 'a', 'e'], ['e', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 'e'], ['e', 'n', 'x', 'd', 's', 'e', 'd', '!', 'c', '!'], ['e', 'e', 'o', 'i', 'a', 'e'], ['e', 't', 'e', 't', 'o', 'e', 'a', 't', 'f', 's', 't'], ['1', '2', '3', '4', 'r', '2'], ['e', 'a', 'n', 'n'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 's', 's'], ['e', 'n', 'r', 'd', 'e', 'e', 'h', 's', 'd', 's', 'd'], ['n', 'g', 'x', 's', 'r', 'e', 'y', 'g'], ['e', 'n', 'r', '!', 'e', 'h', 's', 'd', 's', 's', 'e'], ['e', 't', 'a', 't', 'o', 'e', 'a', 'f', 's'], ['t', 'i', 'e'], ['9', 'a', '1', '2'], ['e', '9', 'I', 'r', 's'], ['e', 'n', 'r', 's', 'd', 'e', '!', 's', 'd', 's']]

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
        func_name = "extract_rear"
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
        for test_case in ["assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']", "assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']", "assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']"]:
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
