METADATA = {
    "entry_point": "string_to_md5",
    "description": "Test function solution for string_to_md5"
}
def check(candidate):

    # Check some simple cases
    assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert candidate('') == None
    assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
    assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'

    # Check some edge cases that are easy to work out by hand.
    assert True


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
