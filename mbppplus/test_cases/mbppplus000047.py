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
inputs = [[[('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]], [[('Yash', 185), ('Dawood', 125), ('Sanya', 175)]], [[('Sai', 345), ('Salman', 145), ('Ayesha', 96)]], [[('John', 100)]], [[('Alice', 100), ('Bob', 100), ('Charlie', 100)]], [[('Alice', 100), ('Bob', 200), ('Charlie', 300), ('John', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False)]], [[('Adam', 150), ('Benjamin', 100), ('Charlie', 100), ('David', 125)]], [[('John', 100), ('Jane', 150), ('Jim', 200), ('Jill', 175)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', False)]], [[('John', 100, 100), ('John', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True, 'Chicago'), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False)]], [[('John', 100), ('Jane', 150), ('Jim', 200)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', True, False, 100), ('David', 125, 'Miami', False)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True, 'Charlie'), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False)]], [[('Adam', 150), ('Benjamin', 100), ('Charlie', 100), ('Adam', 150, 150)]], [[('Alice', 100), ('Bob', 200), ('John', 100), ('John', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True, 'Charlie'), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Adam', 150), ('Benjamin', 100), ('Charlie', 100), ('Benjamin', 100, 'Benjamin'), ('David', 125)]], [[('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bob', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False)]], [[('Adam', 150, 'NYC', 'NYBenjamin', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', True, False, 100), ('David', 125, 'Miami', False)]], [[('John', 100), ('Jane', 150), ('Jim', 200), ('Jill', 175), ('John', 100), ('Jim', 200)]], [[('Charlie', 101), ('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bob', 100)]], [[('Adam', 150, 'NYC', True), ('Charlie', 200, 'Chicago', True)]], [[('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bob', 100), ('Bob', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True, 'Chicago'), ('David', 125, 'Miami', False)]], [[('Alice', 100), ('Bob', 200), ('John', 100), ('John', 100), ('John', 100)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Benjamin', True, 100), ('Charlie', 300), ('Benjamin', 100), ('John', 100)]], [[('Alice', 100), ('Bob', 200), ('John', 100), ('John', 100), ('John', 100), ('John', 100)]], [[('Alice', 100), ('Charlie', 101), ('Alice', 100), ('John', 100), ('Charlie', 100)]], [[('Alice', 100), ('Bob', 200), ('John', 100), ('John', 100), ('John', 100), ('John', 100), ('John', 100)]], [[('Alice', 100), ('Alice', 101), ('Bob', 200), ('John', 100), ('John', 100), ('John', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Benjamin', 100)]], [[('Alice', 100), ('Charlie', 100), ('Alice', 100)]], [[('John', 100), ('Jim', 200), ('Jill', 175)]], [[('John', 100), ('John', 100)]], [[('Charlie', 101), ('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bobb', 100), ('Alice', 100)]], [[('Alice', 101, 100), ('John', 300), ('Alice', True, 100), ('Bob', 200), ('John', 100), ('John', 100), ('Bob', 200)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False, False)]], [[('Adam', 150, 'NYC', 'NYBenjamin', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', True, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', False, False)]], [[('Bob', 100), ('Charlie', 100), ('Bob', 100)]], [[('Adam', 150, 'NYC', True), ('Adam', 150, 'NYC', True)]], [[('Adam', 150, 'NYC', 'NYBenjamin', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', True, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Bob', 100), ('Charlie', 100), ('Bob', 100), ('Bob', 100)]], [[('Adam', 150, 'NYC', True), ('Adam', False, 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True), ('Charlie', 200, 'Chicago', True, 'Charlie'), ('David', 125, 'Miami', False)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Alice', 175), ('Benjamin', 100)]], [[('Alice', 100), ('Bob', 200), ('Charlie', 300), ('John', 100), ('Bob', 200)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Charlie', 300, 300), ('Benjamin', 100)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('John', 100)]], [[('Charlie', 100), ('Adam', 150, 150)]], [[('Adam', 150), ('Benjamin', 100), ('David', 125)]], [[('AlNYCice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Charlie', 300, 300), ('Alice', 100)]], [[('Charlie', 100), ('Bob', 100)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Benjamin', True, 100), ('Charlie', 300), ('Benjamin', 100), ('Bob', 200, 'Bob')]], [[('Alice', 100), ('Alice', 175), ('Benjamin', 100)]], [[('Adam', 150, 'NYC', 'NYBenjamin', True), ('Benjamin', 100, 'LA', False, False), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', True, False, 100), ('Benjamin', 100, 'LA', False, False)]], [[('Alice', 100), ('Bob', 100)]], [[('Alice', 100), ('Bob', 200, 'oBob', 'Bob'), ('Charlie', 300), ('Alice', 175), ('Benjamin', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True, 'Chicago'), ('Charlie', 200, 'Chicago', True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA', False)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Benjamin', True, 100, True), ('Charlie', 300), ('Benjamin', 100), ('Bob', 200, 'Bob')]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True), ('Charlie', 200, 'Chicago', True, 'Charlie'), ('David', 125, 'Miami', False)]], [[('Alice', 100), ('Charlie', 300)]], [[('John', 100), ('Jane', 150), ('Jim', 200), (300, 175)]], [[('Bob', 200, 'Bob'), ('Charlie', 300), ('Charlie', 300, 300), ('Benjamin', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True), ('Charlie', 200, 'Chicago', True, 'Charlie'), ('David', 125, 'Miami', True)]], [[('AlNYCice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Charlie', 300, 300), ('Alice', 100), ('Bob', 200, 'Bob')]], [[('Alice', 100), ('Bob', 200), ('John', 100), ('John', 100), ('John', 100), ('John', 100), ('John', 100), ('John', 100), ('Alice', 100)]], [[('Alice', 100), ('Alice', 101), ('Bob', 200, 'Bob'), ('Charlie', 300), ('John', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True, 'Chicago', 'Charlie'), ('David', 125, 'Miami', False)]], [[('Alice', 100), ('BoAlNYCiceb', 100), ('Bob', 100), ('Bob', 100)]], [[('Alice', 101, 100, 'Alice'), ('John', 300), ('Alice', True, 100), ('Bob', 200), ('John', 100), ('John', 100), ('Bob', 200)]], [[('Charlie', 101), ('Alice', 100), ('Bob', 100, 100), ('Charlie', 100), ('Bobb', 100), ('Alice', 100), ('Bob', 100, 100)]], [[('Adam', 150, 'NYC', True, 'Adam'), ('AdaJanem', 150, 'NYC', True, 150), ('AdaJanem', 150, 'NYC', True), ('Adam', 150, 'NYC', True)]], [[('Alice', 100), ('Bob', 200), ('Charlie', 300), ('John', 100), ('Bob', 200), ('Charlie', 300), ('Charlie', 300)]], [[('Charlie', 100), ('Adam', 150, 149)]], [[('Charlie', 101), ('Alice', 100), ('Bob', 100, 100), ('Charlie', 100), ('Bobb', 100), ('Alice', 100), ('Bob', 100, 100), ('Charlie', 101), ('Charlie', 100), ('Bob', 100, 100)]], [[('Charlie', 300), ('John', 100), ('Bob', 200)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False), ('David', 125, 'Miami', False)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, False), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Bob', 300, 300), ('Charlie', 300, 300), ('Benjamin', 100)]], [[('Adam', 150, 'NYC', True), ('Charlie', 200, 'Chicago', True), ('Adam', 150, 'NYC', True)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, False), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Alice', 100), ('John', 100), ('John', 100), ('John', 100)]], [[('John', True), ('Alice', 100), ('Bob', 200), ('John', 100), ('John', 100), ('John', 100)]], [[('Adam', 150), ('Benjamin', 100), ('Charlie', 100), ('David', 124, 125)]], [[('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False)]], [[('Jane', 150), ('Jim', 200)]], [[('AlNYCice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Charlie', 300, 300), ('Alice', 100), ('Bob', 200, 'Bob'), ('AlNYCice', 100)]], [[('Charlie', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, False), ('Adam', 150, 'NYC', True, True), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Charlie', 101), ('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bobb', 100), ('Alice', 100), ('Bobb', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('BenLAjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('John', 100), ('Jane', 150), ('Jill', 175)]], [[('Adam', 150, 'NYC', True, 'Adam'), ('Benjamin', 100, 'LA', False), ('Charlie', 200, 'Chicago', True), ('Charlie', 200, 'Chicago', True, 'Charlie')]], [[('John', 100, 100), ('John', 100), ('John', 100, 100)]], [[('John', 100), ('Jill', 175)]], [[('Jane', 150), ('Jill', 175), ('Jane', 150)]], [[('AlNYCice', 100), ('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bob', 100)]], [[('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False), ('LA', 150, 'NYC', True), ('Charlie', 200, 'Chicago', True, 'Chicago'), ('David', 125, 'Miami', False)]], [[('Bob', 100), ('Charlie', 100), ('Bob', 100), ('Bob', 100), ('Bob', 100), ('Bob', 100)]], [[('Charlie', 101), ('Alice', 100), ('Bob', 100), ('Charlie', 100), ('Bobb', 100), ('Alice', 100), ('Bobb', 100), ('Bobb', 100)]], [[('Alice', 100), ('Charlie', 300), ('Benjamin', 100)]], [[('Alice', 100), ('Bob', 200, 'Bob'), ('Charlie', 300), ('Bob', 300, 300), ('Benjamin', 100)]], [[('Bob', 200, 'Bob'), ('Charlie', 300), ('Charlie', 300, 300), ('Benjamin', 100), ('Benjamin', 100, 'Benjamin')]], [[('Benjamin', 100, 'LA', False, False, 100), ('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, False), ('BenLAjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('NYBenjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]], [[('Benjamin', 100, 'LA', False, False, 100), ('Adam', 150, 'NYC', True), ('Benjamin', 100, 'LA', False, 100), ('Benjamin', 100, 'LA', False, False), ('BenLAjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False, 100), ('David', 125, 'Miami', False), ('NYBenjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA'), ('Benjamin', 100, 'LA', False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False), ('Benjamin', 100, 'LA', False, False)]]]
results = ['Varsha', 'Dawood', 'Ayesha', 'John', 'Alice', 'Alice', 'Benjamin', 'Benjamin', 'John', 'Benjamin', 'John', 'Benjamin', 'John', 'Benjamin', 'Benjamin', 'Benjamin', 'Alice', 'Benjamin', 'Benjamin', 'Alice', 'Benjamin', 'Benjamin', 'John', 'Alice', 'Adam', 'Alice', 'Benjamin', 'Alice', 'Benjamin', 'Alice', 'Alice', 'Alice', 'Alice', 'Benjamin', 'Alice', 'Alice', 'John', 'John', 'Alice', 'Alice', 'Benjamin', 'Benjamin', 'Bob', 'Adam', 'Benjamin', 'Bob', 'Adam', 'Alice', 'Alice', 'Alice', 'Alice', 'Charlie', 'Benjamin', 'AlNYCice', 'Charlie', 'Benjamin', 'Alice', 'Benjamin', 'Alice', 'Alice', 'Benjamin', 'Benjamin', 'Benjamin', 'Benjamin', 'Alice', 'John', 'Benjamin', 'Benjamin', 'AlNYCice', 'Alice', 'Alice', 'Benjamin', 'Alice', 'Alice', 'Alice', 'Adam', 'Alice', 'Charlie', 'Alice', 'John', 'Benjamin', 'Benjamin', 'Alice', 'Adam', 'Benjamin', 'Alice', 'John', 'Benjamin', 'Benjamin', 'Jane', 'AlNYCice', 'Charlie', 'Benjamin', 'Alice', 'Benjamin', 'John', 'Benjamin', 'John', 'John', 'Jane', 'AlNYCice', 'Benjamin', 'Bob', 'Alice', 'Alice', 'Alice', 'Benjamin', 'Benjamin', 'Benjamin']

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
        func_name = "index_minimum"
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
        for test_case in ["assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'", "assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'", "assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'"]:
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
