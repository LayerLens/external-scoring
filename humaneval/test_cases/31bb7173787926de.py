


METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0



def run_tests():
    check(triangle_area)

if __name__ == "__main__":
    run_tests()
