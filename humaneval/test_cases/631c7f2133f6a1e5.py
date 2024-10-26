METADATA = {
    "entry_point": "multiply"
}

def check(candidate):
    assert candidate(148, 412) == 16, "First test error: " + str(candidate(148, 412))
    assert candidate(19, 28) == 72, "Second test error: " + str(candidate(19, 28))
    assert candidate(2020, 1851) == 0, "Third test error: " + str(candidate(2020, 1851))
    assert candidate(14,-15) == 20, "Fourth test error: " + str(candidate(14,-15))
    assert candidate(76, 67) == 42, "Fifth test error: " + str(candidate(76, 67))
    assert candidate(17, 27) == 49, "Sixth test error: " + str(candidate(17, 27))
    assert candidate(0, 1) == 0, "1st edge test error: " + str(candidate(0, 1))
    assert candidate(0, 0) == 0, "2nd edge test error: " + str(candidate(0, 0))

def run_tests(response_data):
    try:
        # Create namespace and execute response code
        namespace = {}
        exec(response_data.get('parsed_result', response_data.get('result')), namespace)
        
        # Find the candidate function
        candidate_name = None
        for name, obj in namespace.items():
            if callable(obj) and name not in ('__builtins__', 'check', 'run_tests'):
                candidate_name = name
                break
                
        if not candidate_name:
            return False
            
        # Run the checks
        check(namespace[candidate_name])
        return True
    except Exception as e:
        print(f"Test failed: {str(e)}")
        return False
