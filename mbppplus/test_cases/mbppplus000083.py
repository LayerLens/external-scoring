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
inputs = [[[[3, 4, 5], [4, 5, 7], [1, 4]]], [[[1, 2, 3], [4, 2, 3], [7, 8]]], [[[7, 8, 9], [10, 11, 12], [10, 11]]], [[[]]], [[[1, 2, 3], [4, 5], [6, 7, 8, 9]]], [[]], [[[1, 2, 3], [4, 2, 3], [7, 8, 9], [4, 2, 3]]], [[[1, 2, 3], [4, 5], [], [6, 7, 8, 9]]], [[[1, 2, 3, 4], [5, 6], [7], [8, 9, 10]]], [[[1, 2, 3], [], [4, 5], [], [6, 7, 8]]], [[[1, 2, 3], [2, 3, 4], [4, 2, 3], [7, 8, 9], [4, 2, 3]]], [[[10000000, 20000000, 30000000], [40000000, 50000000], [60000000], [70000000, 80000000, 90000000]]], [[[4, 5], [6, 7, 8, 9]]], [[[6, 7, 8, 9, 8], [4, 5], [6, 7, 8, 9, 8], [6, 7, 8, 9, 8]]], [[[1, 2, 3, 4], [5, 6], [8, 9, 10, 8], [1, 2, 3, 4]]], [[[1, 2, 3, 4], [5, 6], [7], [9, 10]]], [[[1, 1, 3], [4, 2, 3], [7, 8, 9], [4, 2, 3]]], [[[1, 2, 3], [3, 2, 3], [7, 8, 9], [4, 2, 3]]], [[[8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8], [4, 5], [8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8]]], [[[6, 7, 8, 9, 8], [4, 5], [6, 7, 8, 9, 8], [6, 7, 8, 9, 8], [6, 7, 8, 9, 8]]], [[[70000000, 80000000, 80000001, 90000000], [10000000, 20000000, 30000000], [40000000, 50000000], [], [70000000, 80000000, 80000001, 90000000]]], [[[2, 3], [2, 3], [], [4, 5], [], [6, 7, 8]]], [[[2, 3], [2, 3], [], [4, 5], [], [False, False, True, False]]], [[[8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8], [4, 5], [8, 6, 7, 8, 9, 8, 8, 8]]], [[[70000000, 4, 5], [70000000, 4, 5], [6, 7, 8, 9]]], [[[1, 2, 3], [4, 40000000, 2, 3], [4, 2, 3], [7, 8, 9], [4, 40000000, 2, 3]]], [[[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]], [[[8, 6, 7, 9, 8, 8, 8], [8, 6, 7, 9, 8, 8, 8], [8, 6, 7, 9, 8, 8, 8], [8, 6, 7, 9, 8, 8, 8], [8, 6, 7, 9, 8, 8, 8], [4, 5], [8, 6, 7, 9, 8, 8, 8]]], [[[6, 7, 8, 10], [6, 7, 8, 10]]], [[[6, 7, 8, 9, 8], [6, 7, 8, 9, 8], [6, 7, 8, 9, 8]]], [[[1, 2, 3], [4, 5], [7, 8, 9], [7, 8, 9]]], [[[1, 2, 3], [4, 5], [6, 7, 8, 9, 6], [4, 5]]], [[[8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [4, 5], [8, 6, 7, 8, 9, 8, 8, 8, 8]]], [[[1, 2, 3], [], [4, 5], [True, False, True, False, True, True, False], [], [6, 7, 8], []]], [[[2, 3], [2, 3], [5, 4, 5], [5, 4, 5], [], [6, 7, 8, 7]]], [[[1, 2, 3, 4], [5, 6], [9, 10, 10], [7], [9, 10, 10], [9, 10, 10]]], [[[1, 2, 3, 4], [5, 6], [9, 10, 10], [7], [9, 10, 10], [9, 10, 10], [9, 10, 10], [9, 10, 10]]], [[[70000000, 80000000, 80000001, 90000000], [10000000, 20000000, 30000000], [9, 50000000], [9, 50000000], [], [70000000, 80000000, 80000001, 90000000], [9, 50000000]]], [[[2, 3], [2, 3], [5, 4, 5], [5, 4, 5], [], [6, 7, 8, 7], []]], [[[1, 2], [4, 40000000, 2, 3, 3], [4, 2, 3], [7, 8, 9], [4, 40000000, 2, 3, 3]]], [[[1, 1, 3], [4, 2, 3], [7, 8, 9], [4, 2, 3], [4, 2, 3]]], [[[4, 5], [6, 7, 8, 9, 6], [4, 5], [4, 5]]], [[[0, 2, 3, 4], [5, 6], [7], [0, 2, 3, 4], [9, 10]]], [[[70000000, 80000000, 20000000, 90000000], [10000000, 20000000, 30000000], [40000000, 50000000], [], [70000000, 80000000, 20000000, 90000000]]], [[[1, 2, 3], [], [6, 7, 8, 9], []]], [[[1, 2, 3], [6, 7, 8, 9, 6], [4, 5]]], [[[6, 7, 8, 10], [6, 7, 8, 10], [6, 7, 8, 10]]], [[[1, 2, 3], [6, 7, 8, 9]]], [[[2, 3, 2], [2, 3, 2], [5, 4, 5], [2, 3, 2], [5, 4, 5], [], [6, 7, 8, 7]]], [[[1, 2, 3], [], [6, 7, 8, 9], [], []]], [[[4, 2], [1, 1, 3], [4, 2], [4, 2, 3], [4, 2]]], [[[1, 2, 3], [], [4, 5], [], [False, False, False, False, False, False, True], [6, 7, 8], []]], [[[1, 2, 3, 4], [5, 6], [7], [9, 10, 9], [9, 10, 9]]], [[[1, 2, 3], [4, 5], [7, 8, 8], [7, 8, 8], [4, 5]]], [[[1, 2, 3], [], [], [6, 7, 8], []]], [[[1, 2, 3, 4], [5, 6], [10, 10], [10, 10], [10, 10]]], [[[4, 40000000, 2, 3, 3], [4, 2, 3], [7, 8, 9], [4, 40000000, 2, 3, 3], [4, 40000000, 2, 3, 3]]], [[[1, 2, 3, 3], [4, 5], [], [6, 7, 8, 9]]], [[[1, 30000000, 3], [], [], [6, 7, 8], [True, False, True, False, False, True, True], [1, 30000000, 3]]], [[[4, 7, 8, 9]]], [[[2, 3], [5, 4, 5], [5, 4, 5], [], [6, 7, 8, 7], []]], [[[1, 2, 3], [4], [4], [6, 90000000, 8, 9], [], [6, 90000000, 8, 9]]], [[[1, 2, 3, 3], [4, 5], [False, False], [], [6, 7, 8, 9], [6, 7, 8, 9]]], [[[1, 2, 3, 4], [11, 10], [5, 6], [11, 10], [11, 10], [11, 10]]], [[[4, 2], [1, 1, 3], [4, 30000000, 2, 3], [4, 2], [1, 1, 3]]], [[[1, 2, 3, 4], [5, 6], [8, 9, 10, 8, 8], [1, 2, 3, 4]]], [[[7, 8, 11], [7, 8, 11], [7, 8, 11]]], [[[1, 2, 3, 3], [], [-16, 80000000, 5, 1, 70000000, -1, 3, 50000000], [], [False, False], [], [6, 7, 8, 9], [6, 7, 8, 9]]], [[[1, 2, 3, 4, 4], [5, 6], [8, 9, 10, 8], [1, 2, 3, 4, 4], [5, 6]]], [[[8, 6, 8, 7, 8, 9, 8, 8, 8, 8], [8, 6, 8, 7, 8, 9, 8, 8, 8, 8], [8, 6, 8, 7, 8, 9, 8, 8, 8, 8], [8, 6, 8, 7, 8, 9, 8, 8, 8, 8], [4, 5], [8, 6, 8, 7, 8, 9, 8, 8, 8, 8]]], [[[1, 2, 3], [7, 8, 9, 6], [4, 5]]], [[[8, 6, 8, 8, 9, 8, 8, 8], [8, 6, 8, 8, 9, 8, 8, 8], [8, 6, 8, 8, 9, 8, 8, 8], [8, 6, 8, 8, 9, 8, 8, 8], [4, 5], [8, 6, 8, 8, 9, 8, 8, 8]]], [[[1, 2], [4, 40000000, 2, 3, 3], [7, 8, 9]]], [[[1, 30000000, 3], [], [], [6, 7, 8], [True, False, True, False, False, True, True], [1, 30000000, 3], []]], [[[6, 7, 8, 9, 8], [5, 4, 5], [6, 7, 8, 9, 8], [5, 4, 5]]], [[[1, 2, 3, 3], [6, 7, 8, 9, 6], [4, 5], [], [6, 7, 8, 9, 6]]], [[[1, 2, 3, 4], [5, 6], [8, 9, 10, 8, 8, 9], [1, 2, 3, 4], [1, 2, 3, 4], [5, 6]]], [[[1, 2, 3], [6, 7, 8, 9, 6], [4, 5], [4, 5]]], [[[1, 2, 3], [4, 40000000, 2, 3, 3], [4, 2, 3], [7, 8, 9], [4, 40000000, 2, 3, 3]]], [[[1, 2, 3], [], [], [False, False, False, False, False, False, True], [6, 7, 8], [], []]], [[[2, 4, 3], [2, 4, 3], [], [4, 5], []]], [[[1, 2, 3], [5, 6], [8, 9, 10, 8, 8], [1, 2, 3]]], [[[7, 8, 80000001], [7, 8, 80000001], [7, 8, 80000001]]], [[[1, 2], [4, 40000000, 2, 3, 3]]], [[[1, 2]]], [[[7, 8, 10], [7, 8, 10], [7, 8, 10]]], [[[], []]], [[[1, 2, 3, 4, 4], [5, 6], [8, 9, 10, 8, 8, 9], [1, 2, 3, 4, 4], [1, 2, 3, 4, 4], [5, 6]]], [[[70000000, 4, 5], [70000000, 4, 5]]], [[[2, 3], [5, 4, 5], [5, 4, 5], [6, 7, 8, 7], []]], [[[1, 2, 3], [4, 2, 3], [4, 40000000, 2, 3, 3], [4, 2, 3], [7, 8, 9], [4, 40000000, 2, 3, 3]]], [[[1, 2, 3, 4, 4], [5, 6], [8, 9, 10, 8, 8, 9], [1, 2, 3, 4, 4], [5, 6]]], [[[0, 2, 3, 4], [5, 6], [9, 10, 9], [7], [0, 2, 3, 4], [9, 10, 9]]], [[[1, 2], [4, 40000000, 2, 3], [4, 2, 3], [4, 40000000, 2, 3], [7, 8, 9], [4, 40000000, 2, 3]]], [[[1, 2, 3, 3], [4, 5], [], [6, False, 7, 8, 9]]], [[[2, 3], [5, 4, 5], [5, 4, 5], [], [79, 10, -79, False], [6, 7, 8, 7], []]], [[[1, 2, 3, 3], [], [False, False, False], [-16, 80000000, 5, 1, 70000000, -1, 3, 50000000], [], [False, False, False], [], [6, 7, 8, 9], [6, 7, 8, 9]]], [[[1, 1, 3], [2, 3], [7, 8, 9], [3, 2, 3], [1, 1, 3]]], [[[2, 3], [5, 4, 5], [5, 4, 5], [6, 7, 8, 5, 7], []]], [[[1, 2, 3, 3], [], [False, False, False], [-16, 80000000, 5, 1, 70000000, -1, 3, 50000000], [], [False, False, False], [True, True], [6, 7, 8, 9], [6, 7, 8, 9], [1, 2, 3, 3]]], [[[1, 2, 3], [], [4, 5], [], [6, 7, 8], [6, 7, 8]]], [[[1, 2, 3], [-67.78782247261685, 83.24602733926832, -64.83209224493669, -32.228902651098196, 69.90886379841328, -35.80770870297867, 93.05813550801312, -42.59408393983315], [4, 5], [], [6, 7, 8], [-67.78782247261685, 83.24602733926832, -64.83209224493669, -32.228902651098196, 69.90886379841328, -35.80770870297867, 93.05813550801312, -42.59408393983315]]], [[[1, 2, 3, 90000000, 4], [5, 6], [7], [8, 9, 10]]], [[[False, 1, 2, 3], [], [4, 5], [], [6, 7, 8], []]], [[[6, 7], [1, 2, 3], [], [], [False, False, False, False, False, False, True], [6, 7], [], [], [1, 2, 3]]], [[[1, 2, 3, 3], [4, 10000000, 5], [6, 7, 8, 9, 6], [1, 2, 3, 3], [4, 10000000, 5]]], [[[1, 2, 3], [4, 40000000, 2, 3, 3], [4, 6, 3], [7, 8, 9], [4, 40000000, 2, 3, 3]]], [[[1, 2, 3], [4, 5], [], [6, 7, 8], [6, 7, 8]]], [[[1, 2, 3], [6, 7, 8, 9], [], [1, 2, 3]]], [[[2, 3], [2, 3], [], [4, 5], [93.05813550801312, -34.32335254187532, 69.90886379841328], [6, 7, 8]]], [[[2, 3, 2], [2, 3, 2], [3, 5, 4, 5], [2, 3, 2], [3, 5, 4, 5], [], [6, 7, 8, 7]]], [[[8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [8, 6, 7, 8, 9, 8, 8, 8, 8], [4, 5], [8, 6, 7, 8, 9, 8, 8, 8, 8]]]]
results = [{1, 3, 4, 5, 7}, {1, 2, 3, 4, 7, 8}, {7, 8, 9, 10, 11, 12}, set(), {1, 2, 3, 4, 5, 6, 7, 8, 9}, set(), {1, 2, 3, 4, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {1, 2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 4, 7, 8, 9}, {10000000, 20000000, 40000000, 30000000, 50000000, 60000000, 70000000, 80000000, 90000000}, {4, 5, 6, 7, 8, 9}, {4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 8, 9, 10}, {1, 2, 3, 4, 5, 6, 7, 9, 10}, {1, 2, 3, 4, 7, 8, 9}, {1, 2, 3, 4, 7, 8, 9}, {4, 5, 6, 7, 8, 9}, {4, 5, 6, 7, 8, 9}, {70000000, 80000000, 90000000, 80000001, 10000000, 20000000, 30000000, 40000000, 50000000}, {2, 3, 4, 5, 6, 7, 8}, {False, True, 2, 3, 4, 5}, {4, 5, 6, 7, 8, 9}, {70000000, 4, 5, 6, 7, 8, 9}, {40000000, 1, 2, 3, 4, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8}, {4, 5, 6, 7, 8, 9}, {8, 10, 6, 7}, {8, 9, 6, 7}, {1, 2, 3, 4, 5, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {4, 5, 6, 7, 8, 9}, {False, 1, 2, 3, 4, 5, 6, 7, 8}, {2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 9, 10}, {1, 2, 3, 4, 5, 6, 7, 9, 10}, {70000000, 80000000, 90000000, 80000001, 10000000, 20000000, 30000000, 50000000, 9}, {2, 3, 4, 5, 6, 7, 8}, {40000000, 1, 2, 3, 4, 7, 8, 9}, {1, 2, 3, 4, 7, 8, 9}, {4, 5, 6, 7, 8, 9}, {0, 2, 3, 4, 5, 6, 7, 9, 10}, {70000000, 80000000, 20000000, 90000000, 10000000, 30000000, 40000000, 50000000}, {1, 2, 3, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {8, 10, 6, 7}, {1, 2, 3, 6, 7, 8, 9}, {2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 6, 7, 8, 9}, {1, 2, 3, 4}, {False, 1, 2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 9, 10}, {1, 2, 3, 4, 5, 7, 8}, {1, 2, 3, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 10}, {40000000, 2, 3, 4, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {30000000, 1, False, 3, 6, 7, 8}, {8, 9, 4, 7}, {2, 3, 4, 5, 6, 7, 8}, {90000000, 1, 2, 3, 4, 6, 8, 9}, {False, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 10, 11}, {30000000, 1, 2, 3, 4}, {1, 2, 3, 4, 5, 6, 8, 9, 10}, {8, 11, 7}, {80000000, 1, 2, 3, 70000000, 5, 50000000, False, 6, 7, 8, 9, -16, -1}, {1, 2, 3, 4, 5, 6, 8, 9, 10}, {4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {4, 5, 6, 8, 9}, {40000000, 1, 2, 3, 4, 7, 8, 9}, {30000000, 1, False, 3, 6, 7, 8}, {4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 8, 9, 10}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {40000000, 1, 2, 3, 4, 7, 8, 9}, {False, 1, 2, 3, 6, 7, 8}, {2, 3, 4, 5}, {1, 2, 3, 5, 6, 8, 9, 10}, {8, 80000001, 7}, {40000000, 1, 2, 3, 4}, {1, 2}, {8, 10, 7}, set(), {1, 2, 3, 4, 5, 6, 8, 9, 10}, {70000000, 4, 5}, {2, 3, 4, 5, 6, 7, 8}, {40000000, 1, 2, 3, 4, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 8, 9, 10}, {0, 2, 3, 4, 5, 6, 7, 9, 10}, {40000000, 1, 2, 3, 4, 7, 8, 9}, {False, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {False, 2, 3, 4, 5, 6, 7, 8, 10, 79, -79}, {False, 1, 2, 3, 80000000, 5, 70000000, 50000000, 6, 7, 8, 9, -16, -1}, {1, 2, 3, 7, 8, 9}, {2, 3, 4, 5, 6, 7, 8}, {False, 1, 2, 3, 80000000, 5, 70000000, 50000000, 6, 7, 8, 9, -16, -1}, {1, 2, 3, 4, 5, 6, 7, 8}, {-64.83209224493669, 1, 2, 3, -32.228902651098196, 69.90886379841328, 4, 5, 6, 7, 8, -67.78782247261685, 83.24602733926832, 93.05813550801312, -42.59408393983315, -35.80770870297867}, {90000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {False, 1, 2, 3, 4, 5, 6, 7, 8}, {False, 1, 2, 3, 6, 7}, {10000000, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {40000000, 1, 2, 3, 4, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 6, 7, 8, 9}, {2, 3, 4, 5, 69.90886379841328, 6, 7, 8, 93.05813550801312, -34.32335254187532}, {2, 3, 4, 5, 6, 7, 8}, {4, 5, 6, 7, 8, 9}]

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
        func_name = "extract_singly"
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
        for test_case in ['assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])', 'assert set(extract_singly([(1, 2, 3), (4, 2, 3), (7, 8)])) == set([1, 2, 3, 4, 7, 8])', 'assert set(extract_singly([(7, 8, 9), (10, 11, 12), (10, 11)])) == set([7, 8, 9, 10, 11, 12])']:
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
