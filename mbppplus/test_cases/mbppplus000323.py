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
inputs = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 4], [[5, 15, 25, 35, 45, 55, 65, 75, 85, 95], 5], [[11, 22, 33, 44, 55, 66, 77, 88, 99, 110], 7], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3], [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 2], [['apple', 'banana', 'cherry', 'date', 'elderberry'], 3], [['cat', 'dog', 'elephant', 'fish', 'giraffe'], 4], [[100], 1], [[1000000000, 2000000000, 3000000000, 4000000000], 2], [[1, 'two', 3.0, [4, 5], {'six': 7}, [8, 9]], 1], [[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 3], [[True, 2.5, 'hello', [1, 2, 3], {'a': 1, 'b': 2}], 2], [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1], [['apple', 2, True, [1, 2, 3]], 2], [[], 0], [[1000000000, 3000000000, 4000000000], 2], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 6], 3], [[9, 2, 4, 6, 8, 10, 12, 14, 16, 2000000000, 20], 3], [[5, 15, 25, 45, 55, 65, 75, 85, 95], 5], [[8, 15, 25, 45, 55, 65, 75, 85, 95], 6], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 16], 3], [[2, 4, 6, 8, 10, 12, 14, 6, 16, 18, 20, 6], 3], [[1, 'two', [4, 5], {'six': 7}, [8, 9]], 1], [[[1, 2, 3], [4, 5, 6, 6], [7, 8, 9]], 1], [[2, 4, 13, 6, 8, 10, 12, 14, 16, 30, 18, 20], 3], [['cat', 'dog', 'two', 'elephant', 'fish', 'giraffe'], 5], [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 19], 2], [[2, 4, 6, 8, 10, 12, 16, 18, 1, 20, 6], 3], [[5, 15, 25, 35, 45, 55, 65, 75, 85, 4000000000], 5], [[2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16], 11], [[[1, 2, 3], [4, 5, 6, 6], [7, 8, 100, 9], [7, 8, 100, 9]], 1], [['cat', 'dog', 'elephant', 'fish', 'giraffe'], 3], [[5, 15, 25, 45, 55, 65, 75, 95], 5], [['cat', 'dog', 'two', 'elephant', 'fish', 'giraffe', 'two'], 5], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 6], 4], [['giraffe', 'RGSFieqfEz', 'date', 'aPof', 'elderberry', '', 'JGvUdQh'], 0], [[2, 4, 6, 8, 10, 12, 14, 6, 16, 18, 20, 6], 5], [[2, 45, 19, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16], 11], [[[1, 2, 3], [7, 8, 9]], 1], [[3.0], 0], [[0, 3, 5, 7, 9, 11, 15, 17, 19, 19, 15], 2], [['cat', 'dog', 'two', 'fish', 'giraffe'], 5], [[5, 15, 45, 55, 65, 75, 85, 95], 5], [[9, 2, 1999999999, 4, 6, 8, 10, 12, 14, 16, 2000000000, 20], 3], [[5, 15, 25, 45, 66, 65, 75, 95], 5], [[2, 4, 6, 8, 10, 12, 16, 18, 1, 20, 6], 4], [[4, 6, 8, 10, 12, 16, 18, 1, 20, 6], 4], [[17, 2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16], 11], [[11, 22, 12, 33, 44, 55, 66, 77, 88, 99, 110], 7], [[True, 2.5, 'hello', [1, 2, 3], {'a': 1, 'b': 2}, [1, 2, 3]], 2], [[2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2], 11], [[[1, 2, 3], [7, 8, 9], [7, 8, 9], [1, 2, 3]], 1], [[2000000000, 3000000000, 4000000000], 2], [['apple', 'banana', 'chery', 'date', 'elderberry'], 3], [[[1, 2, 3, 1], [7, 8, 9], [7, 8, 9], [1, 2, 3, 1]], 1], [[2, 45, 19, 6, 8, 11, 12, 14, 16, 18, 20, 16], 11], [[100], 0], [[2, [1, 2, 99, 3, 1], True, [1, 2, 99, 3, 1]], 2], [['cat', 'dog', 'elephant', 'fish', 'giraffe'], 2], [[5, 45, 55, 75, 85, 95], 5], [[2, 4, 6, 8, 10, 14, 16, 18, 20, 6], 4], [[1, 3, 12, 5, 7, 9, 11, 13, 15, 17, 19, 19], 2], [[2, 4, 6, 8, 12, 16, 18, 1, 20], 4], [[5, 15, 45, 66, 65, 75, 95], 5], [[5, 15, 45, 55, 65, 110, 75, 85, 95], 5], [[[3, 1, 2, 3], [7, 8, 9], [7, 8, 9], [3, 1, 2, 3]], 1], [[17, 2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2], 11], [[2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2, 4], 11], [[1, 3, 12, 5, 7, 9, 11, 13, 17, 19, 19], 2], [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 13], 2], [[[1, 2, 3, 1], [7, 8, 9], [7, 8, 9]], 1], [[True, 2.5, 'hello', [1, 2, 3], {'a': 1, 'b': 2}], 4], [[1, 'two', 3.0, [4, 5], {'six': 7}, [8, 9], 3.0], 1], [['giraffe', 'echerylderberry', 'RGSFieqfEz', 'date', 'aPof', 'elderberry', '', 'JGvUdQh'], 0], [['cat', 'elephant', 'fish', 'girafffe'], 2], [[8, 15, 25, 45, 55, 65, 75, 85, 20, 95], 6], [[1, 3, 12, 7, 11, 13, 17, 19, 19], 2], [[[1, 2, 3], [7, 8, 9], [7, 8, 9], [1, 2, 3]], 2], [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 10], 3], [[2, 4, 13, 6, 8, 10, 12, 14, 16, 3, 30, 18, 20], 3], [[2, 4, 6, 8, 10, 12, 25, 16, 18, 20, 6], 3], [[10, 20, 30, 40, 50, 70, 80, 90, 100], 4], [['giraffe', 'RGSFieqfEz', 'date', 'elderberry', '', 'JGvUdQh'], 1], [[2, [1, 2, 99, 3, 1], True, [1, 2, 99, 3, 1]], 3], [[11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 11], 7], [[5, 15, 25, 45, 66, 65, 75, 99], 5], [[2, 4, 6, 8, 10, 12, 14, 6, 16, 18, 20, 6], 11], [[[1, 2, 3], [7, 8, 9], [7, 8, 9], [1, 2, 3]], 0], [[2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 12], 11], [['a', 'dog', 'two', 'elephant', 'fish', 'giraffe', 'two'], 5], [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 11], 3], [[[7, 8, 9], [7, 8, 9], [1, 2, 3, 1]], 0], [[2, 4, 6, 8, 10, 12, 16, 18, 1, 6], 4], [[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 9], [['cat', 'dog', 'two', 'eelephant', 'fish', 'giraffe'], 5], [[2, 4, 6, 8, 10, 12, 14, 6, 16, 18, 20, 6], 7], [[1, 'two', [4, 5], {'six': 7}, [8, 9]], 5], [[5, 15, 25, 45, 55, 65, 75, 95], 6], [[5, 15, 25, 45, 55, 65, 75, 85, 95], 4], [[True, 2.5, {'a': 1, 'b': 2, 'six': 2}, [1, 2, 3, 1], 'hello', [1, 2, 3, 1], {'a': 1, 'b': 2, 'six': 2}], 2], [[1, 'two', 3.0, [4, 5], {'six': 7}, [8, 9], [4, 5], [4, 5]], 1], [[[7, 8, 9]], 0], [[5, 15, 25, 45, 66, 65, 99, 75, 25], 5], [[2, 4, 6, 8, 10, 12, 14, 6, 16, 18, 20, 6], 2], [[2, 4, 6, 8, 10, 12, 25, 16, 18, 20, 6], 2], [[5, 15, 45, 55, 65, 75, 85, 95, 55], 5], [[1, 3, 12, 5, 7, 9, 11, 13, 17, 19, 19], 1], [[[1, 2, 3, 1], [7, 8, 9, 9], [7, 8, 9, 9], [7, 8, 9, 9]], 2], [[2, 4, 8, 10, 12, 16, 18, 1, 20, 6], 4], [[[1, 3], [1, 3], [3, 4], [5, 6], [7, 8], [9, 10]], 3], [['apple', 2, True, [1, 2, 3]], 3], [[1, 3, 5, 7, 9, 11, 15, 17, 19, 11], 3], [[[1, 2, 3, 3], [4, 5, 6, 6], [1, 2, 3, 3], [7, 8, 9]], 1], [['cat', 'dog', 'two', 'fish', 'giraffe', 'dog'], 5], [[True, 2.5, [1, 2, 3], {'a': 1, 'b': 2}, {'a': 1, 'b': 2}], 4]]
results = [[8, 9, 10, 1, 2, 3, 4, 5, 6, 7], [9, 10, 1, 2, 3, 4, 5, 6, 7, 8], [6, 7, 8, 9, 10, 1, 2, 3, 4, 5], [70, 80, 90, 100, 10, 20, 30, 40, 50, 60], [55, 65, 75, 85, 95, 5, 15, 25, 35, 45], [44, 55, 66, 77, 88, 99, 110, 11, 22, 33], [16, 18, 20, 2, 4, 6, 8, 10, 12, 14], [17, 19, 1, 3, 5, 7, 9, 11, 13, 15], ['cherry', 'date', 'elderberry', 'apple', 'banana'], ['dog', 'elephant', 'fish', 'giraffe', 'cat'], [100], [3000000000, 4000000000, 1000000000, 2000000000], [[8, 9], 1, 'two', 3.0, [4, 5], {'six': 7}], [[5, 6], [7, 8], [9, 10], [1, 2], [3, 4]], [[1, 2, 3], {'a': 1, 'b': 2}, True, 2.5, 'hello'], [[7, 8, 9], [1, 2, 3], [4, 5, 6]], [True, [1, 2, 3], 'apple', 2], [], [3000000000, 4000000000, 1000000000], [18, 20, 6, 2, 4, 6, 8, 10, 12, 14, 16], [16, 2000000000, 20, 9, 2, 4, 6, 8, 10, 12, 14], [55, 65, 75, 85, 95, 5, 15, 25, 45], [45, 55, 65, 75, 85, 95, 8, 15, 25], [18, 20, 16, 2, 4, 6, 8, 10, 12, 14, 16], [18, 20, 6, 2, 4, 6, 8, 10, 12, 14, 6, 16], [[8, 9], 1, 'two', [4, 5], {'six': 7}], [[7, 8, 9], [1, 2, 3], [4, 5, 6, 6]], [30, 18, 20, 2, 4, 13, 6, 8, 10, 12, 14, 16], ['dog', 'two', 'elephant', 'fish', 'giraffe', 'cat'], [19, 19, 1, 3, 5, 7, 9, 11, 13, 15, 17], [1, 20, 6, 2, 4, 6, 8, 10, 12, 16, 18], [55, 65, 75, 85, 4000000000, 5, 15, 25, 35, 45], [2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16], [[7, 8, 100, 9], [1, 2, 3], [4, 5, 6, 6], [7, 8, 100, 9]], ['elephant', 'fish', 'giraffe', 'cat', 'dog'], [45, 55, 65, 75, 95, 5, 15, 25], ['two', 'elephant', 'fish', 'giraffe', 'two', 'cat', 'dog'], [16, 18, 20, 6, 2, 4, 6, 8, 10, 12, 14], ['giraffe', 'RGSFieqfEz', 'date', 'aPof', 'elderberry', '', 'JGvUdQh'], [6, 16, 18, 20, 6, 2, 4, 6, 8, 10, 12, 14], [19, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2, 45], [[7, 8, 9], [1, 2, 3]], [3.0], [19, 15, 0, 3, 5, 7, 9, 11, 15, 17, 19], ['cat', 'dog', 'two', 'fish', 'giraffe'], [55, 65, 75, 85, 95, 5, 15, 45], [16, 2000000000, 20, 9, 2, 1999999999, 4, 6, 8, 10, 12, 14], [45, 66, 65, 75, 95, 5, 15, 25], [18, 1, 20, 6, 2, 4, 6, 8, 10, 12, 16], [18, 1, 20, 6, 4, 6, 8, 10, 12, 16], [2, 4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 17], [44, 55, 66, 77, 88, 99, 110, 11, 22, 12, 33], [{'a': 1, 'b': 2}, [1, 2, 3], True, 2.5, 'hello', [1, 2, 3]], [4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2, 2], [[1, 2, 3], [1, 2, 3], [7, 8, 9], [7, 8, 9]], [3000000000, 4000000000, 2000000000], ['chery', 'date', 'elderberry', 'apple', 'banana'], [[1, 2, 3, 1], [1, 2, 3, 1], [7, 8, 9], [7, 8, 9]], [45, 19, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2], [100], [True, [1, 2, 99, 3, 1], 2, [1, 2, 99, 3, 1]], ['fish', 'giraffe', 'cat', 'dog', 'elephant'], [45, 55, 75, 85, 95, 5], [16, 18, 20, 6, 2, 4, 6, 8, 10, 14], [19, 19, 1, 3, 12, 5, 7, 9, 11, 13, 15, 17], [16, 18, 1, 20, 2, 4, 6, 8, 12], [45, 66, 65, 75, 95, 5, 15], [65, 110, 75, 85, 95, 5, 15, 45, 55], [[3, 1, 2, 3], [3, 1, 2, 3], [7, 8, 9], [7, 8, 9]], [4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 2, 17, 2], [6, 8, 11, 12, 14, 16, 18, 20, 16, 2, 4, 2, 4], [19, 19, 1, 3, 12, 5, 7, 9, 11, 13, 17], [19, 13, 1, 3, 5, 7, 9, 11, 13, 15, 17], [[7, 8, 9], [1, 2, 3, 1], [7, 8, 9]], [2.5, 'hello', [1, 2, 3], {'a': 1, 'b': 2}, True], [3.0, 1, 'two', 3.0, [4, 5], {'six': 7}, [8, 9]], ['giraffe', 'echerylderberry', 'RGSFieqfEz', 'date', 'aPof', 'elderberry', '', 'JGvUdQh'], ['fish', 'girafffe', 'cat', 'elephant'], [55, 65, 75, 85, 20, 95, 8, 15, 25, 45], [19, 19, 1, 3, 12, 7, 11, 13, 17], [[7, 8, 9], [1, 2, 3], [1, 2, 3], [7, 8, 9]], [18, 20, 10, 2, 4, 6, 8, 10, 12, 14, 16], [30, 18, 20, 2, 4, 13, 6, 8, 10, 12, 14, 16, 3], [18, 20, 6, 2, 4, 6, 8, 10, 12, 25, 16], [70, 80, 90, 100, 10, 20, 30, 40, 50], ['JGvUdQh', 'giraffe', 'RGSFieqfEz', 'date', 'elderberry', ''], [[1, 2, 99, 3, 1], True, [1, 2, 99, 3, 1], 2], [55, 66, 77, 88, 99, 110, 11, 11, 22, 33, 44], [45, 66, 65, 75, 99, 5, 15, 25], [4, 6, 8, 10, 12, 14, 6, 16, 18, 20, 6, 2], [[1, 2, 3], [7, 8, 9], [7, 8, 9], [1, 2, 3]], [4, 6, 8, 11, 12, 14, 16, 18, 20, 16, 12, 2], ['two', 'elephant', 'fish', 'giraffe', 'two', 'a', 'dog'], [17, 19, 11, 1, 3, 5, 7, 9, 11, 13, 15], [[7, 8, 9], [7, 8, 9], [1, 2, 3, 1]], [16, 18, 1, 6, 2, 4, 6, 8, 10, 12], [20, 30, 40, 50, 60, 70, 80, 90, 100, 10], ['dog', 'two', 'eelephant', 'fish', 'giraffe', 'cat'], [12, 14, 6, 16, 18, 20, 6, 2, 4, 6, 8, 10], [1, 'two', [4, 5], {'six': 7}, [8, 9]], [25, 45, 55, 65, 75, 95, 5, 15], [65, 75, 85, 95, 5, 15, 25, 45, 55], [[1, 2, 3, 1], {'a': 1, 'b': 2, 'six': 2}, True, 2.5, {'a': 1, 'b': 2, 'six': 2}, [1, 2, 3, 1], 'hello'], [[4, 5], 1, 'two', 3.0, [4, 5], {'six': 7}, [8, 9], [4, 5]], [[7, 8, 9]], [66, 65, 99, 75, 25, 5, 15, 25, 45], [20, 6, 2, 4, 6, 8, 10, 12, 14, 6, 16, 18], [20, 6, 2, 4, 6, 8, 10, 12, 25, 16, 18], [65, 75, 85, 95, 55, 5, 15, 45, 55], [19, 1, 3, 12, 5, 7, 9, 11, 13, 17, 19], [[7, 8, 9, 9], [7, 8, 9, 9], [1, 2, 3, 1], [7, 8, 9, 9]], [18, 1, 20, 6, 2, 4, 8, 10, 12, 16], [[5, 6], [7, 8], [9, 10], [1, 3], [1, 3], [3, 4]], [2, True, [1, 2, 3], 'apple'], [17, 19, 11, 1, 3, 5, 7, 9, 11, 15], [[7, 8, 9], [1, 2, 3, 3], [4, 5, 6, 6], [1, 2, 3, 3]], ['dog', 'two', 'fish', 'giraffe', 'dog', 'cat'], [2.5, [1, 2, 3], {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, True]]

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
        func_name = "rotate_right"
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
        for test_case in ['assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]', 'assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]', 'assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5]']:
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