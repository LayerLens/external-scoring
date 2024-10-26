METADATA = {
    "entry_point": "hex_key"
}

def check(candidate):
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))
    assert candidate([]) == 0

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
