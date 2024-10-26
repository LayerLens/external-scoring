METADATA = {
    "entry_point": "total_match"
}

def check(candidate):
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([], []) == []
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([], ['this']) == []
    assert candidate(['this'], []) == []

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
