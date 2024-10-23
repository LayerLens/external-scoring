


METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144



def run_tests():
    check(fib)

if __name__ == "__main__":
    run_tests()
