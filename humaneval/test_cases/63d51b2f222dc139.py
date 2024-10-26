METADATA = {
    "entry_point": "digits"
}

def check(candidate):
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625
    assert candidate(2468) == 0

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
