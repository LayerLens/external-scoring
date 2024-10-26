METADATA = {
    "entry_point": "sort_array"
}

def check(candidate):
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([]) == [], "Error"
    assert candidate([5]) == [5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], "Error"
    assert candidate([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], "Error"
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([2, 1]) == [1, 2], "Error"
    assert candidate([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87], "Error"
    assert candidate([21, 14, 23, 11]) == [23, 21, 14, 11], "Error"

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
