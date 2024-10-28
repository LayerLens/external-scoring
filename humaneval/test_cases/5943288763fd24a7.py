METADATA = {
    "entry_point": "same_chars",
    "description": "Test function solution for same_chars"
}
def check(candidate):
    assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert candidate('abcd', 'dddddddabc') == True
    assert candidate('dddddddabc', 'abcd') == True
    assert candidate('eabcd', 'dddddddabc') == False
    assert candidate('abcd', 'dddddddabcf') == False
    assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert candidate('aabb', 'aaccc') == False


def ll_run_tests(response_data):
    """
    Main test function for code evaluation.
    Args:
        response_data: Dict containing response code
    Returns:
        bool: True if all test cases pass
    """
    try:
        # Create namespace and execute response code
        namespace = {}
        response_code = response_data.get('parsed_result', response_data.get('result', ''))
        exec(response_code, namespace)

        # Get the candidate function name from metadata
        candidate_name = METADATA["entry_point"]
        if candidate_name not in namespace:
            print(f"Function '{candidate_name}' not found in response")
            return False

        # Run test cases
        check(namespace[candidate_name])
        return True

    except AssertionError as e:
        print(f"Test case failed")
        return False
    except Exception as e:
        print(f"Execution failed: {str(e)}")
        return False
