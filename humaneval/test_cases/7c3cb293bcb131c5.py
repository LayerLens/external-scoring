


METADATA = {}


def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124


def run_tests():
    check(max_element)

if __name__ == "__main__":
    run_tests()
