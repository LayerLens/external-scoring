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
inputs = [[[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 0], [[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 2], [[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)], 1], [[], 0], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 91, 89)], 1], [[], 1], [[('John Doe', 78, 90, 82)], 0], [[('A', 1), ('B', 1), ('C', 1)], 1], [[], 84], [[], 85], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1), (1, 'C', 1)], 1], [[('A', 1), ('C', 1)], 1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1), (1, 'C', 1)], 0], [[('A', 1), ('B', 1), ('C', 1), ('C', 1)], 0], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1)], 0], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1)], 1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1)], 1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1)], -1], [[('A', 1), ('B', 1), (2, 'A', 1), ('C', 1), ('C', 1), ('A', 1)], 0], [[('A', 1), ('B', 1), ('C', 1), ('C', 1)], -1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1), (1, 'C', 1)], -1], [[('B', 1), ('C', 1), ('C', 1)], 0], [[('EEmily BrownownA', 1), (1, 'C', 1), ('B', 1), ('C', 1), (1, 'C', 1)], 1], [[('A', 1), ('C', 1), ('C', 1)], 1], [[('B', 1), ('C', 1), ('Mark Johnson', 1), ('C', 1)], 0], [[('A', 1), ('B', 1), ('C', 'C', 1), ('C', 1), ('C', 1)], 1], [[('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('B', 1), ('C',), ('Mark Johnson', 1), ('C', 1)], 0], [[('AA', 'A', 1), ('B', 1), ('C', 1)], 1], [[('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Jane Smith', 0, 87, 84), ('Emily Brown', 88, 91, 89)], 0], [[('A', 1), ('B', 1), ('C',), ('C', 1), ('C', 1)], 0], [[('C', 1)], 1], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('John Doe', 78, 90, 82)], -1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1)], -2], [[], 83], [[('A', 1), ('C', 1, 1), ('C', 1)], 1], [[('C', 92), ('A', 1), ('B', 1), ('C', 1), ('C', 1), ('A', 1)], -1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('A', 1)], -1], [[('A', 1), ('B', 1), ('C', 'CC', 1)], 1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1)], 0], [[('John Doe', 78, 90, 82), ('John Doe', 78, 90, 82), ('John Doe', 78, 90, 82)], 0], [[('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Jane Smith', 0, 87, 84), ('Emily Brown', 88, 91, 89), (79, 'Emily Brown', 88, 91, 89), ('Jane Smith', 92, 87, 84)], 0], [[('A', 1), ('C', 1, 1), ('C', 1)], 0], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), ('C', 1), (1, 'C', 1)], -1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), ('C', 1), (1, 'C', 1), ('C',)], -1], [[('A', 1), ('C', 1), ('BrownA', 1)], 1], [[('A', 1), ('B', 1), ('C', 'CC', 1), ('A', 1)], 1], [[('A', 1), ('C', 1), ('BrownA', 1)], -1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('A', 1), (1,)], -1], [[('Emily BrownA', 1), ('Emilyy BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1)], 0], [[], 89], [[('Emily BrownA', 1), ('Emilyy BrownA', 1), (1, 'C', 1), ('B', 1)], 1], [[('A', 1), ('C', 1, 1), ('C', 1)], -1], [[('A', 1), ('', 1), ('B', 1), ('C', 1), ('C', 1)], 0], [[('John Doe', 78, 90, 82, 'John Doe'), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('A', 1), ('C', 1), ('BrownA', 1)], 0], [[('A', 1), ('B', 1), ('C', 'CC', 1), ('B', 1)], 1], [[('A', 1), ('A', 92), ('B', 1), ('C', 1), ('A', 1)], 1], [[('Emily BrownA', 1), ('Emilyy BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1), ('Emilyy BrownA', 1)], 0], [[('A', '', 1), ('B', 1), ('C', 1), ('C', 1)], 1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), ('C', 1), (1, 'C', 0, 1), ('C',)], -1], [[('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Jane Smith', 0, 87, 84), ('Jane Smith', 1, 87, 84), ('Emily Brown', 88, 91, 89)], 0], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 91, 89), ('John Doe', 78, 90, 82)], 0], [[('A', 1), ('C', 1), ('BrownA', 1), ('BrownA', 1)], -1], [[('Emily BrownA', 1), ('Emilyy BrownA', 1), (1, 'C', 1), ('B', 2), ('C', 1)], 0], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('Jane Smith',), ('C', 1), (1, 'C', 0, 1), ('C',)], -1], [[('A', 1), ('C', 1), ('BrownA', 1)], -2], [[('BrownownAA', 1), ('C', 1), ('BrownA', 1), ('BrownA', 1)], -1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), ('C', 1), (1, 'C', 1)], 0], [[('AA', 'A', 1), ('C', 1)], 1], [[('A', 1), ('C', 1, 1), ('C', 1), ('C', 1)], 1], [[('B', 1), ('C', 1), ('Mark Johnson', 1), ('C', 1), ('C', 1)], -1], [[('Emily BrownA', 1), ('Emilyy BrownA', 1), (1, 'C', 1), ('B', 2)], -1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1), ('C', 1)], -1], [[('A', 1), ('', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1)], 0], [[('A', 1), ('', 1), ('B', 1), ('C', 1), ('C', 1), (1,), ('C', 1)], -1], [[('B', 1, 'B'), ('B', 1), ('C', 1), ('Mark Johnson', 1), ('C', 1), ('C', 1)], -1], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1), ('C', 1)], 1], [[('BrownownAA', 1), ('EEmily BrownownA', 'BrownA', 1), ('C', 1), ('BrownA', 1), ('BrownA', 1)], -2], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), (90, 'Mark Johnson', 79, 85, 91), ('Mark Johnson', 79, 85, 91, 85), ('Emily Brown', 88, 91, 89), ('Mark Johnson', 'Mark Jokhnson', 79, 85, 91, 85), ('John Doe', 78, 90, 82)], 0], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1), (1, 'C', 1, 1)], -1], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 91, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('A', 1), ('B', 1), ('C', 'C', 1), ('C', 1), ('C', 1)], 0], [[('A', 1), ('AA', 'A', 1), ('C', 1)], 1], [[('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Jane Smith', 0, 87, 84), ('Emily Brown', 88, 91, 89), (79, 'Emily Brown', 88, 91, 89), ('Jane Smith', 92, 87, 84)], -2], [[('BA', 'A', 1), ('A', 1), ('B', 'A', 1), ('C', 1), ('BrownA', 1), ('B', 'A', 1)], 1], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 85, 91), ('Emily Brown', 88, 91, 89), ('Jane Smith', 92, 87, 84)], 0], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), ('C', 1), (1, 'C', 1), ('C',), ('C',)], -1], [[(1,), (1, 'C', 1), ('B', 1), ('C', 1)], 0], [[('A', 1), ('B', 2), ('C', 'CC', 1)], 1], [[('A', 1), ('CC', 1), ('C', 1)], 0], [[('AA', 'A', 1), ('B', 1), ('AA', 'A'), ('C', 1)], 0], [[('A', 1), ('A', 92), ('B', 1), ('C', 1, 1), ('A', 1)], 1], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), (1, '', 'C', 1), ('C', 1), (1, 'C', 1)], 0], [[('Emily BrownA', 1), ('B', 1), ('Jane Smith',), ('C', 1), (1, 'C', 0, 1), (1, 'C', 0, 0), ('C',)], -1], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 91, 89)], -2], [[('Emily BrownA', 1), (1, 'C', 1), ('B', 1), ('C',), ('C', 1), (1, 'C', 1), (1, 'C', 1)], -1], [[('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Mark Johnson', 78, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('A', 1), ('B', 1), ('C', 1), ('C', 1), ('C', 1), ('B', 1)], 0], [[('John Doe', 78, 90, 82), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Emily Brown', 88, 78, 91, 89), ('John Doe', 78, 90, 82)], 0], [[('A', 1), ('', 1), ('C', 1), ('C', 1)], 0], [[('A', 1), ('B', 1), ('C', 1)], -2], [[('Mark Johnson', 79, 85, 91), ('Mark Johnson', 78, 85, 91), ('Emily Brown', 88, 91, 89)], 0], [[('A', 1), ('C', 1), ('BrownA', 1), ('A', 1)], -1], [[('Jane Smith', 91, 87, 84), ('Jane Smith', 92, 87, 84), ('Mark Johnson', 79, 85, 91), ('Jane Smith', 0, 87, 84), ('Emily Brown', 88, 91, 89), (79, 'Emily Brown', 88, 91, 89), ('Jane Smith', 92, 87, 84)], -2], [[('Emily BrownA', 1), ('B', 90, 1), ('Emilyy BrownA', 1), (1, 'C', 1), ('B', 1), ('C', 1)], 0]]
results = [['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'], [99, 96, 94, 98], [98, 97, 91, 94], [], [78, 92, 79, 88], [], ['John Doe'], [1, 1, 1], [], [], [1, 'C', 1, 1, 'C'], [1, 1], ['Emily BrownA', 1, 'B', 'C', 1], ['A', 'B', 'C', 'C'], ['A', 'B', 'C', 'C', 'C'], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown'], [1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], ['A', 'B', 2, 'C', 'C', 'A'], [1, 1, 1, 1], [1, 1, 1, 1, 1], ['B', 'C', 'C'], [1, 'C', 1, 1, 'C'], [1, 1, 1], ['B', 'C', 'Mark Johnson', 'C'], [1, 1, 'C', 1, 1], ['Jane Smith', 'Mark Johnson', 'Emily Brown'], ['B', 'C', 'Mark Johnson', 'C'], ['A', 1, 1], ['Jane Smith', 'Mark Johnson', 'Jane Smith', 'Emily Brown'], ['A', 'B', 'C', 'C', 'C'], [1], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown'], [82], ['A', 'B', 'C', 'C'], [], [1, 1, 1], [92, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 'CC'], ['Emily BrownA', 1, 'B', 'C'], ['John Doe', 'John Doe', 'John Doe'], ['Jane Smith', 'Mark Johnson', 'Jane Smith', 'Emily Brown', 79, 'Jane Smith'], ['A', 'C', 'C'], [1, 1, 1, 'C', 1, 1], [1, 1, 1, 'C', 1, 1, 'C'], [1, 1, 1], [1, 1, 'CC', 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], ['Emily BrownA', 'Emilyy BrownA', 1, 'B', 'C'], [], [1, 1, 'C', 1], [1, 1, 1], ['A', '', 'B', 'C', 'C'], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown'], ['A', 'C', 'BrownA'], [1, 1, 'CC', 1], [1, 92, 1, 1, 1], ['Emily BrownA', 'Emilyy BrownA', 1, 'B', 'C', 'Emilyy BrownA'], ['', 1, 1, 1], [1, 1, 1, 'C', 1, 1, 'C'], ['Jane Smith', 'Mark Johnson', 'Jane Smith', 'Jane Smith', 'Emily Brown'], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown', 'John Doe'], [1, 1, 1, 1], ['Emily BrownA', 'Emilyy BrownA', 1, 'B', 'C'], [1, 1, 1, 'Jane Smith', 1, 1, 'C'], ['A', 'C', 'BrownA'], [1, 1, 1, 1], ['Emily BrownA', 1, 'B', 'C', 'C', 1], ['A', 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 1, 1, 1, 1], ['A', '', 'B', 'C', 'C', 'C'], [1, 1, 1, 1, 1, 1, 1], ['B', 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], ['BrownownAA', 'BrownA', 'C', 'BrownA', 'BrownA'], ['John Doe', 'Jane Smith', 90, 'Mark Johnson', 'Emily Brown', 'Mark Johnson', 'John Doe'], [1, 1, 1, 1, 1], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown'], ['A', 'B', 'C', 'C', 'C'], [1, 'A', 1], [87, 85, 87, 91, 91, 87], ['A', 1, 'A', 1, 1, 'A'], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown', 'Jane Smith'], [1, 1, 1, 'C', 1, 1, 'C', 'C'], [1, 1, 'B', 'C'], [1, 2, 'CC'], ['A', 'CC', 'C'], ['AA', 'B', 'AA', 'C'], [1, 92, 1, 1, 1], ['Emily BrownA', 1, 'B', 'C', 1, 'C', 1], [1, 1, 'Jane Smith', 1, 1, 0, 'C'], [90, 87, 85, 91], [1, 1, 1, 'C', 1, 1, 1], ['Jane Smith', 'Mark Johnson', 'Mark Johnson', 'Emily Brown'], ['A', 'B', 'C', 'C', 'C', 'B'], ['John Doe', 'Jane Smith', 'Mark Johnson', 'Emily Brown', 'John Doe'], ['A', '', 'C', 'C'], ['A', 'B', 'C'], ['Mark Johnson', 'Mark Johnson', 'Emily Brown'], [1, 1, 1, 1], [87, 87, 85, 87, 91, 91, 87], ['Emily BrownA', 'B', 'Emilyy BrownA', 1, 'B', 'C']]

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
        func_name = "extract_nth_element"
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
        for test_case in ["assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']", "assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,2)==[99, 96, 94, 98]", "assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)],1)==[98, 97, 91, 94]"]:
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
