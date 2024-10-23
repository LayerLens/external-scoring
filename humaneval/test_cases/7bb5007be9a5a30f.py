


METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100



def run_tests():
    check(car_race_collision)

if __name__ == "__main__":
    run_tests()
