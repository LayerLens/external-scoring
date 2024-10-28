METADATA = {
    "entry_point": "sorted_list_sum",
    "description": "Test function solution for sorted_list_sum"
}
def check(candidate):

    # Check some simple cases
    assert candidate(["aa", "a", "aaa"]) == ["aa"]
    assert candidate(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert candidate(["d", "b", "c", "a"]) == []
    assert candidate(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(["AI", "ai", "au"]) == ["AI", "ai", "au"]
    assert candidate(["a", "b", "b", "c", "c", "a"]) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]


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
