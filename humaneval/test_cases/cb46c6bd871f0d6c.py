METADATA = {
    "entry_point": "valid_date"
}

def check(candidate):
    assert candidate('03-11-2000') == True
    assert candidate('15-01-2012') == False
    assert candidate('04-0-2040') == False
    assert candidate('06-04-2020') == True
    assert candidate('01-01-2007') == True
    assert candidate('03-32-2011') == False
    assert candidate('') == False
    assert candidate('04-31-3000') == False
    assert candidate('06-06-2005') == True
    assert candidate('21-31-2000') == False
    assert candidate('04-12-2003') == True
    assert candidate('04122003') == False
    assert candidate('20030412') == False
    assert candidate('2003-04') == False
    assert candidate('2003-04-12') == False
    assert candidate('04-2003') == False

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
