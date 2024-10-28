METADATA = {
    "entry_point": "count_up_to",
    "description": "Test function solution for count_up_to"
}
def check(candidate):

    assert candidate(5) == [2,3]
    assert candidate(6) == [2,3,5]
    assert candidate(7) == [2,3,5]
    assert candidate(10) == [2,3,5,7]
    assert candidate(0) == []
    assert candidate(22) == [2,3,5,7,11,13,17,19]
    assert candidate(1) == []
    assert candidate(18) == [2,3,5,7,11,13,17]
    assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


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
