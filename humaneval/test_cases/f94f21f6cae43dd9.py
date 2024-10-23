
def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361


def run_tests():
    check(get_max_triples)

if __name__ == "__main__":
    run_tests()
