METADATA = {
    "entry_point": "bf"
}

def check(candidate):
    assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(candidate("Jupiter", "Neptune")))
    assert candidate("Earth", "Mercury") == ("Venus",), "Second test error: " + str(candidate("Earth", "Mercury"))
    assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(candidate("Mercury", "Uranus"))
    assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(candidate("Neptune", "Venus"))
    assert candidate("Earth", "Earth") == ()
    assert candidate("Mars", "Earth") == ()
    assert candidate("Jupiter", "Makemake") == ()

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
