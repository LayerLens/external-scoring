METADATA = {
    "entry_point": "prod_signs",
    "description": "Test function solution for prod_signs"
}
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 1]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([]) == None
    assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
    assert candidate([-1, 1, -1, 1]) == 4
    assert candidate([-1, 1, 1, 1]) == -4
    assert candidate([-1, 1, 1, 0]) == 0

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


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
