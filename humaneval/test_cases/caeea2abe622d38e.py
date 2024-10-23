


METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29



def run_tests():
    check(largest_prime_factor)

if __name__ == "__main__":
    run_tests()
