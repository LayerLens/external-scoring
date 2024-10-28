METADATA = {
    "entry_point": "x_or_y",
    "description": "Test function solution for x_or_y"
}
def check(candidate):

    # Check some simple cases
    assert candidate(7, 34, 12) == 34
    assert candidate(15, 8, 5) == 5
    assert candidate(3, 33, 5212) == 33
    assert candidate(1259, 3, 52) == 3
    assert candidate(7919, -1, 12) == -1
    assert candidate(3609, 1245, 583) == 583
    assert candidate(91, 56, 129) == 129
    assert candidate(6, 34, 1234) == 1234
    

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 2, 0) == 0
    assert candidate(2, 2, 0) == 2


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
