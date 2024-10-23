


METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386



def run_tests():
    check(fib4)

if __name__ == "__main__":
    run_tests()
