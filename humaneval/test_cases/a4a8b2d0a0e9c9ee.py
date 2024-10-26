METADATA = {
    "entry_point": "factorize"
}

def check(candidate):
    assert candidate(2) == [2]
    assert candidate(4) == [2, 2]
    assert candidate(8) == [2, 2, 2]
    assert candidate(3 * 19) == [3, 19]
    assert candidate(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert candidate(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
    assert candidate(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert candidate(3 * 2 * 3) == [2, 3, 3]

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
