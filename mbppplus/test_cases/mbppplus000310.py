import numpy as np
[]

def is_floats(x) -> bool:
    """Helper function to check float values for comparison"""
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False

def assertion(out, exp, atol):
    """Custom assertion function that handles float comparisons"""
    # Special handling for booleans
    if isinstance(out, bool) or isinstance(exp, bool):
        assert out == exp, f"out: {out}, exp: {exp}"
        return
        
    # Float comparison setup
    if atol == 0 and is_floats(exp):
        atol = 1e-6
    
    # Handle set conversion for sequences
    if isinstance(out, (list, tuple)) and isinstance(exp, (list, tuple)):
        out = set(out)
        exp = set(exp)
    
    # Do the actual comparison
    if out != exp and atol != 0:
        assert np.allclose(out, exp, rtol=1e-07, atol=atol)
    else:
        assert out == exp, f"out: {out}, exp: {exp}"

# Test data
inputs = [[[10, 20, 30], [15, 25, 35]], [[1, 2, 3], [5, 6, 7]], [[15, 20, 30], [15, 45, 75]], [[], []], [[1, 2, 3], [4, 5, 6]], [[10, 20, 30, 40], [5, 3, 2, 1]], [[0.5, 0.8, 1.2], [1.2, 0.3, 1.8]], [['a', 'b', 'c'], ['d', 'e', 'f']], [[0.1, 0.2, 0.3, 0.4], [1, 2, 3, 4]], [[-1, -2, -3, -4], [1, 2, 3, 4]], [[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[0.1, 0.2, 0.3, 0.4], [1, 2, 2, 4]], [[1, 30, 2, 4, 2], [1, 30, 2, 4, 2]], [[1, 3, 4], [1, 3, 4]], [[-1, -2, -3, -4, -3], [1, 2, 3, 4, 3]], [[0.1, 0.2, 0.3, 0.4, 0.4], [0.1, 0.2, 0.3, 0.4, 0.4]], [[3, 3, 4], [3, 3, 4]], [[0.1, 0.2, 0.4, 0.4, 0.1], [0.1, 0.2, 0.4, 0.4, 0.1]], [[10, 20, 30, 40], [6, 3, 2, 1]], [[5, 3, 2, 1], [5, 3, 2, 1]], [[10, 20, 30, 40], [20, 3, 2, 1]], [[0.1, 0.2, 0.4, 0.4, -5.070116511374234e-05, 0.1, 0.1], [0.1, 0.2, 0.4, 0.4, -5.070116511374234e-05, 0.1, 0.1]], [[-1, -2, -3, -4, -5, -6, -7, -4, -9, -10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[1, 2, 3, 4], [1, 2, 3, 4]], [[10, 20, 30, 40], [10, 20, 30, 40]], [[0.1, -5.070116511374234e-05, 0.2, 0.4, 0.4, -5.070116511374234e-05, 0.1, 0.1], [0.1, -5.070116511374234e-05, 0.2, 0.4, 0.4, -5.070116511374234e-05, 0.1, 0.1]], [[-1, -2, -3, -4], [-1, -2, -3, -4]], [[1, 3, 4, 5, 6, 7, 8, 9, 10, 7], [1, 3, 4, 5, 6, 7, 8, 9, 10, 7]], [[1, 40, 1, 4], [1, 40, 1, 4]], [[11, 20, 30, 40], [11, 20, 30, 40]], [[-1, -2, -3, -4, -5, -6, -7, -4, -9, -10], [-1, -2, -3, -4, -5, -6, -7, -4, -9, -10]], [[-1, -2, -3, -4, 3, -6, -7, -4, -9, -10], [-1, -2, -3, -4, 3, -6, -7, -4, -9, -10]], [[0.1, 0.2, 0.4, 0.2682347250149916, 0.4, -5.070116511374234e-05, 0.1], [0.1, 0.2, 0.4, 0.2682347250149916, 0.4, -5.070116511374234e-05, 0.1]], [[-1, -2, -3, -4, 3, -6, -7, 3, -4, -9, -10, -4], [-1, -2, -3, -4, 3, -6, -7, 3, -4, -9, -10, -4]], [[0.1, 0.12680036984068382, 0.3, 0.4], [1, 2, 2, 4]], [[-1, -3, -5, 3, -6, -7, 3, -4, -9, -10, -4], [-1, -3, -5, 3, -6, -7, 3, -4, -9, -10, -4]], [[-1, -2, -3, -4, 3, -6, -4, -9, -10], [-1, -2, -3, -4, 3, -6, -4, -9, -10]], [[-5, 11, 20, 20, 30, 40, 30, 11], [-5, 11, 20, 20, 30, 40, 30, 11]], [['a', 'a', 'b', 'c', 'b'], ['a', 'a', 'b', 'c', 'b']], [[0.5, 0.8, 1.2, 0.8], [0.5, 0.8, 1.2, 0.8]], [[-1, -2, -3, -4, 3, -6, -4, -9, -10, -1], [-1, -2, -3, -4, 3, -6, -4, -9, -10, -1]], [[-1, -2, -3, -4, -6, 11, -4, -9, -10, -1], [-1, -2, -3, -4, -6, 11, -4, -9, -10, -1]], [[5, 3, 2, 2], [5, 3, 2, 2]], [[-5.070116511374234e-05, 0.5, 0.8, 1.4877489589365553, 0.8, 1.4877489589365553], [-5.070116511374234e-05, 0.5, 0.8, 1.4877489589365553, 0.8, 1.4877489589365553]], [[-1, -6, -2, -3, -4, 3, -6, -7, -4, -3, -9], [-1, -6, -2, -3, -4, 3, -6, -7, -4, -3, -9]], [[1, -2, -3, -4, -2], [1, -2, -3, -4, -2]], [[-1, -2, -3, -4, -6, 11, 40, -9, -10, -1], [-1, -2, -3, -4, -6, 11, 40, -9, -10, -1]], [[-1, -2, -3, -4, -5, -6, -7, -8, -10], [1, 2, 4, 5, 6, 7, 8, 9, 10]], [[-1, -6, -2, -3, -4, 3, -6, -7, -4, -3, -9, 3, -3], [-1, -6, -2, -3, -4, 3, -6, -7, -4, -3, -9, 3, -3]], [[1, -9, 3, 2, 4], [0.1, 0.5, 0.12680036984068382, 0.3, 0.4]], [[1, 3, 4, 1], [1, 3, 4, 1]], [[0.1, 0.2, 0.3, 1.020982984611004, 0.4], [0.1, 0.2, 0.3, 1.020982984611004, 0.4]], [[-1, -2, -4, -5, -6, -7, -4, -9, -11], [-1, -2, -4, -5, -6, -7, -4, -9, -11]], [[-1, -3, -5, 3, -6, -7, -4, -9, -10, -4], [-1, -3, -5, 3, -6, -7, -4, -9, -10, -4]], [[5, 3, 2, 2, 5], [5, 3, 2, 2, 5]], [[1, 3, 4, 5, 7, 7, 8, 9, 10, 7], [1, 3, 4, 5, 7, 7, 8, 9, 10, 7]], [[20, 3, 2, 1, 2], [20, 3, 2, 1, 2]], [[0.1, 0.2, 0.4, 0.2682347250149916, -5.070116511374234e-05, 0.1], [0.1, 0.2, 0.4, 0.2682347250149916, -5.070116511374234e-05, 0.1]], [[2, 3, 3, 4], [2, 3, 3, 4]], [[0, 6, -7, -4, -5, -6, -7, -8, -9, -10], [0, 6, -7, -4, -5, -6, -7, -8, -9, -10]], [[0.2, 0.4, 0.4910844678602658, 0.1, 0.4], [0.2, 0.4, 0.4910844678602658, 0.1, 0.4]], [[-1, -6, -2, -4, 3, -6, -7, -4, -3, -9, 3, -3], [-1, -6, -2, -4, 3, -6, -7, -4, -3, -9, 3, -3]], [[3, 2, 2, 5], [3, 2, 2, 5]], [[-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -7], [-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -7]], [[0.1, 0.3, 0.4], [0.1, 0.3, 0.4]], [[-1, -2, -3, -4, -5, -6, -7, -4, -9, -10, -4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 8]], [[3, 2, 1], [3, 2, 1]], [[0.1, 0.2, 0.3, 0.3394475696956425, 0.2], [0.1, 0.2, 0.3, 0.3394475696956425, 0.2]], [[1, 5, 2, 3, 4, 3], [1, 5, 2, 3, 4, 3]], [[1, 5, -7, 2, -10, 3, 4, 3], [1, 5, -7, 2, -10, 3, 4, 3]], [[-2, -3, -4, 3, -6, -4, -9, -10, -1], [-2, -3, -4, 3, -6, -4, -9, -10, -1]], [[2, 3, 4], [2, 3, 4]], [[1, 4, 40], [1, 4, 40]], [[-1, -2, -3, -4, -6, -7, 3, -4, -9, -10, -4], [-1, -2, -3, -4, -6, -7, 3, -4, -9, -10, -4]], [[11, 20, -5, 30, 30, 40], [11, 20, -5, 30, 30, 40]], [[1, 2, 3, 4, 4], [1, 2, 3, 4, 4]], [[1, 3, 2, 2], [1, 3, 2, 2]], [[-2, -3, -4, 3, -6, -4, -9, -10, -1, -6], [-2, -3, -4, 3, -6, -4, -9, -10, -1, -6]], [[-1, -2, -4, -5, 0, -6, -7, -4, -11, -7], [-1, -2, -4, -5, 0, -6, -7, -4, -11, -7]], [[2, 4, 4], [2, 4, 4]], [['a', 'a', 'b', 'aa', 'b', 'b'], ['a', 'a', 'b', 'aa', 'b', 'b']], [[2, 4], [2, 4]], [[11, 20, -5, 30, 30, 40, 30], [11, 20, -5, 30, 30, 40, 30]], [[-1, -6, -4, -5, -6, -7, -4, -9, -11], [-1, -6, -4, -5, -6, -7, -4, -9, -11]], [[-1, -3, -5, 3, -6, -7, 3, -4, -8, -10, -4], [-1, -3, -5, 3, -6, -7, 3, -4, -8, -10, -4]], [[0.24244486712234534, 0.4, 0.4910844678602658, 0.1, 0.4, 0.1], [0.24244486712234534, 0.4, 0.4910844678602658, 0.1, 0.4, 0.1]], [[1, 2, 3], [5, 5, 6]], [['', 'aa', 'a', 'a', 'b', 'c', 'b'], ['', 'aa', 'a', 'a', 'b', 'c', 'b']], [[-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -5, -7, -6, 2], [-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -5, -7, -6, 2]], [[0.24244486712234534, 0.4, 0.4910844678602658, 0.1, 0.4, 0.1, 0.4910844678602658], [0.24244486712234534, 0.4, 0.4910844678602658, 0.1, 0.4, 0.1, 0.4910844678602658]], [[-1, -2, -3, 9, -6, 11, -4, -9, -5, -10, -1, -1], [-1, -2, -3, 9, -6, 11, -4, -9, -5, -10, -1, -1]], [[0.1, 0.2, 0.3, 0.4], [1, 3, 4, 4]], [[-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -7, 1, -2], [-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -7, 1, -2]], [[0.1, 1.4877489589365553, 0.3, 0.2], [0.1, 1.4877489589365553, 0.3, 0.2]], [[-5.070116511374234e-05, 0.5, 0.8, 1.4877489589365553, 0.8, 1.4877489589365553, 1.4877489589365553, 1.4877489589365553], [-5.070116511374234e-05, 0.5, 0.8, 1.4877489589365553, 0.8, 1.4877489589365553, 1.4877489589365553, 1.4877489589365553]], [[2, 4, 3, 4], [2, 4, 3, 4]], [[3, 4], [3, 4]], [[-1, -3, -5, 3, -6, -7, 3, -3, -8, -10, -4, -4], [-1, -3, -5, 3, -6, -7, 3, -3, -8, -10, -4, -4]], [[3], [3]], [[1, -6, 3, 4, 4], [1, -6, 3, 4, 4]], [[0.2, 0.4, 0.4910844678602658, 0.4], [0.2, 0.4, 0.4910844678602658, 0.4]], [[-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -7, 1, -2, -3], [-1, 2, -6, -2, -3, 6, 3, -6, -7, -4, -3, -9, -7, 1, -2, -3]], [[2, 5, 4], [2, 5, 4]], [[2, -5, 11, 20, 20, 30, 40, 30, 11, 11], [2, -5, 11, 20, 20, 30, 40, 30, 11, 11]], [['d', 'e', 'f', 'd', 'd'], ['d', 'e', 'f', 'd', 'd']], [[-5, 11, 20, 20, 30, 40, 30, 21, 11], [-5, 11, 20, 20, 30, 40, 30, 21, 11]], [[-5, 11, 20, 30, 40, 30, 11, 30], [-5, 11, 20, 30, 40, 30, 11, 30]], [[-9, -2, -3, -4, 3, -6, -4, -9, -10, -1, -6], [-9, -2, -3, -4, 3, -6, -4, -9, -10, -1, -6]], [[2, 3, 4, 4], [2, 3, 4, 4]], [[-1, -8, -6, -2, -3, -4, 3, -6, -7, -4, -3, -9, 3, -3], [-1, -8, -6, -2, -3, -4, 3, -6, -7, -4, -3, -9, 3, -3]], [[-1, -2, -3, -4, 3, -6, -4, -9, -10, -9], [-1, -2, -3, -4, 3, -6, -4, -9, -10, -9]]]
results = [[25, 45, 65], [6, 8, 10], [30, 65, 105], [], [5, 7, 9], [15, 23, 32, 41], [1.7, 1.1, 3.0], ['ad', 'be', 'cf'], [1.1, 2.2, 3.3, 4.4], [0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [7, 9, 11, 13, 15], [1.1, 2.2, 2.3, 4.4], [2, 60, 4, 8, 4], [2, 6, 8], [0, 0, 0, 0, 0], [0.2, 0.4, 0.6, 0.8, 0.8], [6, 6, 8], [0.2, 0.4, 0.8, 0.8, 0.2], [16, 23, 32, 41], [10, 6, 4, 2], [30, 23, 32, 41], [0.2, 0.4, 0.8, 0.8, -0.00010140233022748468, 0.2, 0.2], [0, 0, 0, 0, 0, 0, 0, 4, 0, 0], [2, 4, 6, 8], [20, 40, 60, 80], [0.2, -0.00010140233022748468, 0.4, 0.8, 0.8, -0.00010140233022748468, 0.2, 0.2], [-2, -4, -6, -8], [2, 6, 8, 10, 12, 14, 16, 18, 20, 14], [2, 80, 2, 8], [22, 40, 60, 80], [-2, -4, -6, -8, -10, -12, -14, -8, -18, -20], [-2, -4, -6, -8, 6, -12, -14, -8, -18, -20], [0.2, 0.4, 0.8, 0.5364694500299833, 0.8, -0.00010140233022748468, 0.2], [-2, -4, -6, -8, 6, -12, -14, 6, -8, -18, -20, -8], [1.1, 2.1268003698406837, 2.3, 4.4], [-2, -6, -10, 6, -12, -14, 6, -8, -18, -20, -8], [-2, -4, -6, -8, 6, -12, -8, -18, -20], [-10, 22, 40, 40, 60, 80, 60, 22], ['aa', 'aa', 'bb', 'cc', 'bb'], [1.0, 1.6, 2.4, 1.6], [-2, -4, -6, -8, 6, -12, -8, -18, -20, -2], [-2, -4, -6, -8, -12, 22, -8, -18, -20, -2], [10, 6, 4, 4], [-0.00010140233022748468, 1.0, 1.6, 2.9754979178731107, 1.6, 2.9754979178731107], [-2, -12, -4, -6, -8, 6, -12, -14, -8, -6, -18], [2, -4, -6, -8, -4], [-2, -4, -6, -8, -12, 22, 80, -18, -20, -2], [0, 0, 1, 1, 1, 1, 1, 1, 0], [-2, -12, -4, -6, -8, 6, -12, -14, -8, -6, -18, 6, -6], [1.1, -8.5, 3.1268003698406837, 2.3, 4.4], [2, 6, 8, 2], [0.2, 0.4, 0.6, 2.041965969222008, 0.8], [-2, -4, -8, -10, -12, -14, -8, -18, -22], [-2, -6, -10, 6, -12, -14, -8, -18, -20, -8], [10, 6, 4, 4, 10], [2, 6, 8, 10, 14, 14, 16, 18, 20, 14], [40, 6, 4, 2, 4], [0.2, 0.4, 0.8, 0.5364694500299833, -0.00010140233022748468, 0.2], [4, 6, 6, 8], [0, 12, -14, -8, -10, -12, -14, -16, -18, -20], [0.4, 0.8, 0.9821689357205317, 0.2, 0.8], [-2, -12, -4, -8, 6, -12, -14, -8, -6, -18, 6, -6], [6, 4, 4, 10], [-2, 4, -12, -4, -6, 12, 6, -12, -14, -8, -6, -18, -14], [0.2, 0.6, 0.8], [0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 4], [6, 4, 2], [0.2, 0.4, 0.6, 0.678895139391285, 0.4], [2, 10, 4, 6, 8, 6], [2, 10, -14, 4, -20, 6, 8, 6], [-4, -6, -8, 6, -12, -8, -18, -20, -2], [4, 6, 8], [2, 8, 80], [-2, -4, -6, -8, -12, -14, 6, -8, -18, -20, -8], [22, 40, -10, 60, 60, 80], [2, 4, 6, 8, 8], [2, 6, 4, 4], [-4, -6, -8, 6, -12, -8, -18, -20, -2, -12], [-2, -4, -8, -10, 0, -12, -14, -8, -22, -14], [4, 8, 8], ['aa', 'aa', 'bb', 'aaaa', 'bb', 'bb'], [4, 8], [22, 40, -10, 60, 60, 80, 60], [-2, -12, -8, -10, -12, -14, -8, -18, -22], [-2, -6, -10, 6, -12, -14, 6, -8, -16, -20, -8], [0.4848897342446907, 0.8, 0.9821689357205317, 0.2, 0.8, 0.2], [6, 7, 9], ['', 'aaaa', 'aa', 'aa', 'bb', 'cc', 'bb'], [-2, 4, -12, -4, -6, 12, 6, -12, -14, -8, -6, -18, -10, -14, -12, 4], [0.4848897342446907, 0.8, 0.9821689357205317, 0.2, 0.8, 0.2, 0.9821689357205317], [-2, -4, -6, 18, -12, 22, -8, -18, -10, -20, -2, -2], [1.1, 3.2, 4.3, 4.4], [-2, 4, -12, -4, -6, 12, 6, -12, -14, -8, -6, -18, -14, 2, -4], [0.2, 2.9754979178731107, 0.6, 0.4], [-0.00010140233022748468, 1.0, 1.6, 2.9754979178731107, 1.6, 2.9754979178731107, 2.9754979178731107, 2.9754979178731107], [4, 8, 6, 8], [6, 8], [-2, -6, -10, 6, -12, -14, 6, -6, -16, -20, -8, -8], [6], [2, -12, 6, 8, 8], [0.4, 0.8, 0.9821689357205317, 0.8], [-2, 4, -12, -4, -6, 12, 6, -12, -14, -8, -6, -18, -14, 2, -4, -6], [4, 10, 8], [4, -10, 22, 40, 40, 60, 80, 60, 22, 22], ['dd', 'ee', 'ff', 'dd', 'dd'], [-10, 22, 40, 40, 60, 80, 60, 42, 22], [-10, 22, 40, 60, 80, 60, 22, 60], [-18, -4, -6, -8, 6, -12, -8, -18, -20, -2, -12], [4, 6, 8, 8], [-2, -16, -12, -4, -6, -8, 6, -12, -14, -8, -6, -18, 6, -6], [-2, -4, -6, -8, 6, -12, -8, -18, -20, -18]]

def ll_run_tests(response_data):
    """
    Main test function for code evaluation.
    Args:
        response_data: Dict containing response code
    Returns:
        bool: True if all test cases pass
    """
    try:
        # Initialize test environment
        global_namespace = {
            'np': np,
            'assertion': assertion,
            'is_floats': is_floats,
            'inputs': inputs,
            'results': results
        }
        
        # Execute solution code
        response_code = response_data.get('parsed_result', response_data.get('result', ''))
        exec(response_code, global_namespace)
        
        # Verify function exists
        func_name = "sum_list"
        if func_name not in global_namespace:
            print(f"Function '{func_name}' not found in response")
            return False
        
        # Execute tests
        solution_func = global_namespace[func_name]
        
        # Run input/output tests
        for i, (test_input, expected) in enumerate(zip(inputs, results)):
            try:
                result = solution_func(*test_input)
                assertion(result, expected, 0)
            except AssertionError as e:
                print(f"Test case {i} failed: {str(e)}")
                print(f"Input: {test_input}")
                print(f"Expected: {expected}")
                print(f"Got: {result}")
                return False
        
        # Run assertion-based tests if any
        for test_case in ['assert sum_list([10,20,30],[15,25,35])==[25,45,65]', 'assert sum_list([1,2,3],[5,6,7])==[6,8,10]', 'assert sum_list([15,20,30],[15,45,75])==[30,65,105]']:
            try:
                exec(test_case, global_namespace)
            except AssertionError as e:
                print(f"Assertion test failed: {str(e)}")
                print(f"Test case: {test_case}")
                return False
            
        return True
            
    except Exception as e:
        print(f"Error during test execution: {str(e)}")
        return False
