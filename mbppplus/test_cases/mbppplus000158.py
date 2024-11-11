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
inputs = [[['Python PHP', 'Java JavaScript', 'c c++']], [['Python Programming', 'Java Programming']], [['Pqrst Pqr', 'qrstuv']], [['Python Programming', 'Java Programming', 'Perl Programming', 'Ruby Programming', 'PHP Programming', 'C Programming']], [[]], [['apple', 'banana', 'carrot', 'dog', 'elephant']], [['python Programming', 'Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Programming', 'C Programming']], [['Python PHP', 'Java JavaScript', 'C C++', 'Perl Python', 'Ruby R']], [['Python', 'Programming', 'Java', 'Programming', 'Perl', 'Programming', 'Ruby', 'Programming', 'PHP', 'Programming', 'C', 'Programming']], [['Apple', 'Banana', 'Carrot', 'Dog', 'Elephant']], [['Python', 'Programming', 'Java', 'Programming', 'PBananaerl', 'Programming', 'Ruby', 'Programming', 'PHP', 'Programming', 'C', 'Programming']], [['python Programming', 'Elephant', 'Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Programming', 'C Programming']], [['Python PHP', 'Java JavaScript', 'C C++', 'Perl Python', 'Ruby R', 'Java JavaScript']], [['python Programming', 'Elephant', 'Java Programming', 'perl Programming', 'PHP Programming', 'C Programming', 'Elephant']], [['python Programming', 'Elephant', 'python', 'perl Programming', 'PHP Programming', 'C Programming', 'Elephant']], [['Apple', 'Banana', 'Carrort', 'Carrot', 'Dog', 'Elephant']], [['Apple', 'Banana', 'Carrort', 'Dog', 'Elephant']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'PHP Programming', 'C Programming', 'carrot', 'Elephant']], [['Apple', 'Banana', 'Python Programming', 'Carrot', 'Dog', 'Elephant']], [['Apple', 'Banana', 'Crrort', 'Dog', 'Elephant']], [['python Programming', 'Java Programming', 'perl Programming', 'PHP Programming', 'C Programming', 'python Programming']], [['python Programming', 'Elephant', 'Java Programming', 'perl Progrgamming', 'Ruby Programming', 'PHP Programming', 'C Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'PHP Programming', 'carrot', 'Elephant']], [['python Programming', 'Elephant', 'python', 'Python', 'perl Programming', 'PHP Programming', 'C Programming', 'Elephant']], [['Elephant', 'Java Programming', 'perl Progrgamming', 'Ruby Programming', 'PHP Programming', 'C Programming']], [['Python Programming', 'Java Programming', 'Perl Programming', 'Ruby Programming', 'PHP Programming', 'PHP Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Promgramming', 'C Programming']], [['Python', 'Programming', 'Java', 'Programming', 'PBananaerl', 'C Programming', 'Programming', 'Ruby', 'Programming', 'PHP', 'Programming', '', 'Programming', 'C']], [['Apple', 'Banana', 'Banan', 'Crrort', 'Dog', 'Elephant']], [['python Programming', 'Elephant', 'perl Programming', 'Java Programming', 'perl Progrgamming', 'Ruby Programming', 'PHP Programming', 'C Programming']], [['Banana', 'Apple', 'Banan', 'Crrort', 'Dog', 'Elephant']], [['Java Programming', 'perl Programming', 'PHP Programming', 'C Programming', 'python Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'PHP Programming', 'C Programming', 'Elephant']], [['python Programming', 'Elephant', 'Python', 'perl Programming', 'PHP Programming', 'C Programming', 'Elephant']], [['apple', 'banana', 'carrot', 'apBananple', 'dog', 'elephant', 'banana']], [['python Programming', 'Elephant', 'Java Programming', 'pperlerl Progrgamming', 'Ruby Programming', 'PHP Programming']], [['Apple', 'Banana', 'Perl Python', 'Crrort', 'Dog', 'Elephant']], [['Carrort', 'Dog', 'Elephant', 'Carrort']], [['Apple', 'Banana', 'Perl Python', 'Dog', 'Elephant']], [['Python', 'Programming', 'Java', 'Programming', 'PBananaerl', 'C Programming', 'Programming', 'Ruby', 'Programming', 'PHP', 'Programming', '', 'Programming', 'C', 'Programming']], [['apple', 'banana', 'carrot', 'dog', 'etlephant']], [['Apple', 'Banana', 'Carrot', 'Dg', 'Elephant']], [['Apple', 'Banana', 'Crrort', 'Dog', 'Appe', 'Banana']], [['apple', 'banana', 'carrot', 'Java', 'dog', 'elephant', 'banana']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'perl ProgrammC Programminging', 'PHP Programming', 'Elephant']], [['python Programming', 'Elephant', 'python', 'Python', 'perl Programming', 'PHP Programming', 'C ramming', 'Elephant', 'python Programming']], [['Apple', 'Banana', 'Carrort', 'Dog', 'Elephant', 'apBananple']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'PHP Progiramming', 'C Programming', 'Elephant']], [['python Programming', 'Java Programming', 'Crrort', 'Ruby Programming', 'ProgrammC', 'PHP Promgramming', 'C Programming']], [['Apple', 'Bannana', 'Banana', 'Perl Python', 'Dog', 'Elephant']], [['perl Programmming', 'python Programming', 'Java Programming', 'perl Programming', 'perl ProgrammC Programminging', 'PHP Programming', 'Elephant']], [['Python', 'Programming', 'Java', 'Programming', 'PBananaerl', 'Programming', 'Programming', 'PHP', 'Programming', 'C', 'Programming']], [['python Programming', 'etlephant', 'Java Programming', 'perl Programming', 'perl Programming', 'PHP Programming', 'C Programming', 'Elephant']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'perl ProgrammC Programminging', 'Ruby', 'Elephant']], [['Apple', 'Banana', 'Carrot', 'Programmming', 'Dog', 'Progiramming', 'Elephant']], [['Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Programming', 'Ruby ProgrammingJava', 'C Programming']], [['Elephant', 'Java Programming', 'perl Progrgamming', 'Ruby Programming', 'R', 'C Programming']], [['Java Programming', 'Perl Programming', 'Ruby Programming', 'PHP Programming', 'PHP Programming']], [['python Programming', 'Elephant', 'Java Programming', 'perl Programming', 'PHP Programming', 'Elephant']], [['apple', 'carrot', 'apBananple', 'Javadog', 'elephant', 'banana']], [['apple', 'banana', 'carrot', 'Bannana', 'dog', 'etlephant']], [['Apple', 'Banana', 'Crrort', 'Dog', 'Elephant', 'Banana']], [['Dogg', 'Carrort', 'Dog', 'Elephant']], [['perl Programmming', 'python Programming', 'Java Programming', 'perl Programming', 'perl ProgrammC Programminging', 'PHP Programming', 'Elephant', 'perl Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'PHP Programming', 'Elephant']], [['Apple', 'Banana', 'Carrot', 'Dg', 'Perl Python']], [['Apple', 'Banana', 'Dog', 'Elephant']], [['Elephant', 'Promgramming', 'perl Progrgamming', 'Ruby Programming', 'R', 'C Programming']], [['Apple', 'Banana', 'Carrot', 'Dg', 'Detlephantg', 'Elephant']], [['Elephant', 'Promgramming', 'perl Progrgamming', 'Ruby Programming', 'R']], [['Python', 'Programming', 'Java', 'Programming', 'PBananaerl', 'C Programming', 'Programming', 'Ruby', 'Programming', 'PHP', 'ProPgramming', '', 'Programming', 'C', 'Programming']], [['python Programming', 'Elephant', 'Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Programming', 'C Programming', 'perl Programming', 'Elephant']], [['Elephant', 'Java Programming', 'perl Progrgamming', 'perl Programming', 'R', 'C Programming']], [['Apple', 'Dog', 'Elephant']], [['Perl Programming', 'Ruby Programming', 'PHP Programming', 'Ruby ProgrammiRuby Rng', 'PHP Programming', 'PHP Programming']], [['Apple', 'Banana', 'Python Programming', 'Carrot', 'ProgrammiRubyDog', 'Elephant']], [['apple', 'carrot', 'apBananple', 'Javadog', 'elephant', 'banana', 'banana']], [['banana', 'carrot', 'Bannana', 'dog', 'etlephan']], [['Programming', 'Java', 'Programming', 'PBananaerl', 'C Programming', 'Programming', 'Ruby', 'Programming', 'PHP', 'ProPgramming', '', 'Programming', 'C', 'Programming']], [['Elephant', 'PromgrammingJava Programming', 'perl Progrgamming', 'Ruby Programming', 'R', 'C Programming', 'perl Progrgamming']], [['Carrort', 'Dog', 'Elephant', 'oDog', 'Carrort']], [['Apple', 'Banana', 'Carrort', 'Dog', 'ElephantCarrort', 'apBananple', 'Banana']], [['python Programming', 'Java Programming', 'perl Programming', 'perl Programming', 'perl ProgrammC Programminging', 'Ruby', 'Elephant', 'perl ProgrammC Programminging']], [['python Programming', 'Elephant', 'Java Programming', 'perl Programming', 'PHP Programming', 'C Programming']], [['Apple', 'Bannana', 'Banana', 'Perl Python', 'Elephpant', 'Elephant']], [['python Programming', 'Java Programming', 'perl Programming', 'PHP Programming', 'C Progmramming', 'python Programming']], [['Elephant', 'Promgramming', 'perl', 'perl Progrgamming', 'Apple', 'Ruby Programming', 'prl', 'C Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'perl ProgrammC Programminging', 'Ruby', 'Elephant', 'perl ProgrammC Programminging', 'perl Programming', 'perl ProgrammC Programminging']], [['Python PHP', 'Java JavaScript', 'Perl Python', 'Ruby R']], [['Dogg', 'Dog', 'Elephant']], [['Java Programming', 'perl Programming', 'perl', 'PHP Programming', 'C Programming', 'python Programming']], [['Carrort', 'Dog', 'Elephant', 'og', 'Carrort']], [['python Programming', 'Elephant', 'Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Programming', 'C Programming', 'Java Programming']], [['python Programming', 'pperlerl Progrgamming', 'Ruby Programming', 'PHP Programming']], [['Java Programming', 'Perl Programming', 'Ruby Programming', 'C Programming', 'PHP Programming']], [['python Programming', 'Java Programming', 'Crrort', 'Ruby Programming', 'Pramming', 'ProgrammC', 'PHP Promgramming', 'C Programming', 'PHP Promgramming']], [['Java Programming', 'Perl Programming', 'Ruby Programming', 'PHP Programming']], [['Promgramming', 'Python Programming', 'perl Progrgamming', 'Ruby Programming', 'R']], [['Apple', 'Banana', 'Python Programming', 'ProgrammiRuby', 'Dog', 'Elephant']], [['python Programming', 'PHP ProCrrortgramming', 'Elephant', 'python', 'Python', 'perl Programming', 'PHP Programming', 'C ramming', 'Elephant', 'python Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'PHP PrPHP ProCrrortgrammingogramming', 'C Programming', 'python Programming']], [['', 'python Programming', 'Java Programming', 'Crrort', 'Ruby Programming', 'ProgrammC', 'PHP Promgramming', 'C Programming']], [['Java Programming', 'Perl Programming', 'PHnP Programming', 'Ruby Programming', 'PHP Programming', 'PHP Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'Ruby Programming', 'PHP Promgramming', 'C Programming', 'C Programming', 'Java Programming']], [['python Programming', 'Java Programming', 'perl Programming', 'PHP Programming', 'carrot', 'Elephant']], [['carrot', 'apBananple', 'Javadog', 'elephant', 'Python', 'banana', 'banana']], [['apple', 'banana', 'carrot', 'dRog', 'apBananple', 'dog', 'elephant', 'banana']], [['PHP PrPBananaerling', 'Python Programming', 'Java Programming', 'Perl Programming', 'Ruby Programming', 'PHP Programming', 'PHP Programming']], [['Elephant', 'PromgramminC Progmrammingg', 'perl Progrgamming', 'Ruby Programming', 'R']], [['python Programming', 'Elephant', 'Java Programming', 'pperlerl Progrgammicarrotng', 'Ruby Programming', 'PHP Programming']]]
results = [('Python', 'PHP'), ('Python', 'Programming'), ('Pqrst', 'Pqr'), ('Python', 'Programming'), None, None, ('PHP', 'Programming'), ('Python', 'PHP'), None, None, None, ('PHP', 'Programming'), ('Python', 'PHP'), ('PHP', 'Programming'), ('PHP', 'Programming'), None, None, ('PHP', 'Programming'), ('Python', 'Programming'), None, ('PHP', 'Programming'), ('PHP', 'Programming'), ('PHP', 'Programming'), ('PHP', 'Programming'), ('PHP', 'Programming'), ('Python', 'Programming'), ('PHP', 'Promgramming'), None, None, ('PHP', 'Programming'), None, ('PHP', 'Programming'), ('PHP', 'Programming'), ('PHP', 'Programming'), None, ('PHP', 'Programming'), ('Perl', 'Python'), None, ('Perl', 'Python'), None, None, None, None, None, ('PHP', 'Programming'), ('PHP', 'Programming'), None, ('PHP', 'Progiramming'), ('PHP', 'Promgramming'), ('Perl', 'Python'), ('PHP', 'Programming'), None, ('PHP', 'Programming'), None, None, ('PHP', 'Programming'), None, ('Perl', 'Programming'), ('PHP', 'Programming'), None, None, None, None, ('PHP', 'Programming'), ('PHP', 'Programming'), ('Perl', 'Python'), None, None, None, None, None, ('PHP', 'Programming'), None, None, ('Perl', 'Programming'), ('Python', 'Programming'), None, None, None, ('PromgrammingJava', 'Programming'), None, None, None, ('PHP', 'Programming'), ('Perl', 'Python'), ('PHP', 'Programming'), None, None, ('Python', 'PHP'), None, ('PHP', 'Programming'), None, ('PHP', 'Programming'), ('PHP', 'Programming'), ('Perl', 'Programming'), ('PHP', 'Promgramming'), ('Perl', 'Programming'), ('Python', 'Programming'), ('Python', 'Programming'), ('PHP', 'ProCrrortgramming'), ('PHP', 'PrPHP'), ('PHP', 'Promgramming'), ('Perl', 'Programming'), ('PHP', 'Promgramming'), ('PHP', 'Programming'), None, None, ('PHP', 'PrPBananaerling'), ('PromgramminC', 'Progmrammingg'), ('PHP', 'Programming')]

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
        func_name = "start_withp"
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
        for test_case in ['assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==(\'Python\', \'PHP\')', 'assert start_withp(["Python Programming","Java Programming"])==(\'Python\',\'Programming\')', 'assert start_withp(["Pqrst Pqr","qrstuv"])==(\'Pqrst\',\'Pqr\')']:
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
