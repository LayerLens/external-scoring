METADATA = {
    "entry_point": "double_the_difference"
}

def check(candidate):
    assert candidate([]) == 0 , "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([5, 4]) == 25 , "This prints if this assert fails 2 (good for debugging!)"
    assert candidate([0.1, 0.2, 0.3]) == 0 , "This prints if this assert fails 3 (good for debugging!)"
    assert candidate([-10, -20, -30]) == 0 , "This prints if this assert fails 4 (good for debugging!)"
    assert candidate([-1, -2, 8]) == 0, "This prints if this assert fails 5 (also good for debugging!)"
    assert candidate([0.2, 3, 5]) == 34, "This prints if this assert fails 6 (also good for debugging!)"
    assert candidate(lst) == odd_sum , "This prints if this assert fails 7 (good for debugging!)"

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
