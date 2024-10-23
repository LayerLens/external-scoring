


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == 0
    assert candidate('x') == 1
    assert candidate('asdasnakj') == 9


def run_tests():
    check(strlen)

if __name__ == "__main__":
    run_tests()
