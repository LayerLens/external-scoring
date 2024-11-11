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
inputs = [[(3, 4, 5, 6), (5, 7, 4, 10)], [(1, 2, 3, 4), (7, 2, 3, 9)], [(21, 11, 25, 26), (26, 34, 21, 36)], [(3, 4, 5, 6, 7, 8, 9), (5, 7, 4, 10, 12, 14, 16)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), (7, 2, 3, 9, 14, 18, 21, 25)], [(21, 11, 25, 26, 30, 35, 40), (26, 34, 21, 36, 40, 45, 50)], [(), ()], [(), (1, 2, 3)], [(1, 2, 3), ()], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)], [(1, 1, 1, 1, 2, 2, 2, 2), (2, 2, 2, 2, 3, 3, 3, 3)], [(1, 2, 3, 4, 5, 5, 5, 5), (5, 5, 5, 5, 6, 6, 6, 6)], [(10, 20, 30, 40, 50, 60, 70, 80, 90, 100), (10, 10, 20, 20, 30, 30, 40, 40, 50, 50)], [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], [(1, 2, 3, 4, 5), (1, 2, 3, 4, 5)], [(1, 2, 3, 4, 5, 6), (7, 8, 9, 10, 11)], [(1, 1, 2, 2, 3, 3, 4, 4, 5, 5), (2, 2, 4, 4, 6, 6, 8, 8, 10, 10)], [('a', 'b', 'c', 'd', 'e', 'f', 'g'), ('h', 'i', 'j', 'k', 'l', 'm', 'n')], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)], [('apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig'), ('apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig')], [('a', 'b', 'c', 'd', 'e', 'f', 'g'), ('c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')], [(1, 2, 3, 4, 5, 6, 7, 8), (2, 4, 6, 8, 10, 12, 14, 16)], [(1, 2, 3, 4, 5, 6, 7), (2, 4, 6, 8, 10, 12, 14, 16)], [('apple', 'banana', 'cucumber', 'dragonfruit'), ('banana', 'dragonfruit', 'eggplant', 'fig')], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20)], [('apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig'), ('apple', 'banana', 'cherry', 'guava', 'kiwi', 'mango')], [(1, 2, 3, 1), (1, 2, 3, 1)], [('', 'apple', 'banana'), ('banana', 'apple', '')], [(1, 2, 3, 4, 5), (5, 6, 7, 8, 9)], [('a', 'b', 'c', 'd'), ('d', 'e', 'f', 'g')], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)], [(1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')], [(1, 2, 3, 1), (1, 16, 3, 1)], [(1, 1, 2, 1, 2, 2, 2, 2, 2, 2), (2, 2, 2, 3, 3, 3, 3)], [('apple', 'banana', 'cucumber', 'dragonfruit'), ('banana', 'dragonfruit', 'egcherrygplant', 'eggplant', 'fig', 'dragonfruit')], [(1, 2, 3, 4, 5, 6, 15, 7, 8, 9, 10), (1, 2, 3, 4, 30, 6, 7, 9, 10)], [(1, 16, 3, 1), (1, 16, 3, 1)], [(1, 2, 3, 1, 3), (1, 2, 3, 1)], [('', 'apple', 'elderberry', 'banana', ''), ('', 'apple', 'banana')], [('', 'apple'), ('banana', 'apple', '')], [(21, 11, 25, 26, 30, 35, 40, 40), (26, 34, 21, 36, 40, 45, 50)], [(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20), (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20)], [(10, 10, 20, 20, 30, 30, 40, 50, 40, 50, 50), (10, 10, 20, 20, 30, 30, 40, 40, 50, 50)], [('apple', 'banana', 'cucumber', 'dragonfruit'), ('banana', 'dragonfruit', 'fig')], [(26, 34, 21, 36, 40, 45, 50), (26, 34, 21, 36, 40, 45, 50)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 17, 16, 17, 18, 19, 20)], [(1, 2, 3, 4, 7), (1, 2, 3, 4, 5)], [('', 'apple', 'banana'), ('', 'apple', 'banana')], [(1, 2, 3, 4, 5, 2), (6, 7, 8, 9, 10)], [(21, 11, 25, 26, 30, 35, 40, 40, 21), (26, 34, 21, 36, 40, 45, 50)], [(1, 2, 3, 1, 1), (1, 2, 3, 1)], [('a', 'b', 'c', 'd', 'e', 'f', 'gg'), ('h', 'i', 'j', 'k', 'l', 'm', 'n')], [('', 'apple', 'a'), ('', 'apple', 'apple')], [(1, 2, 3, 4, 5, 6, 15, 7, 8, 9, 10, 6), (1, 2, 3, 4, 30, 6, 7, 9, 10)], [('', 'apple', 'banana'), ('egcherrygplant', 'a', 'banana')], [(1, 2, 3), (1, 2, 3)], [(1, 2, 3, 4, 5), (1, 2, 15, 3, 4, 5, 1)], [(1, 2, 3, 4, 5, 6, 7, 2), (2, 4, 6, 8, 10, 12, 14, 16)], [(1, 16, 3, 1), (2, 1, 16, 3, 1)], [('a', 'b', 'c', 'd', 'e', 'f', 'g'), ('durian', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')], [(), (32.93260841054931, -74.09499781125828, -54.49719674608351, -59.91254473588992, 66.77507074495682)], [('apple',), ('apple',)], [(10, 9, 21, 8, 7, 6, 5, 4, 3, 2, 1, 11, 16, 17, 18, 19, 20), (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 16, 17, 18, 19, 20)], [(10, 20, 30, 40, 50, 60, 70, 80, 90, 100), (10, 20, 20, 30, 30, 40, 40, 50, 50)], [(10, 20, 30, 40, 50, 60, 70, 80, 90, 100), (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)], [(5, 60, 18, 10, 11, 8, 26, -35, 2, 34), (5, 60, 18, 10, 11, 8, 26, -35, 2, 34, 18)], [(1, 2, 3, 90, 5, 2, 7, 8, 9, 10, 11, 12), (1, 2, 3, 90, 5, 2, 7, 8, 9, 10, 11, 12)], [('n', '', 'cherry'), ('banana', 'apple', '')], [('banana', 'apple', '', ''), ('banana', 'apple', '', '')], [(10, 3, 9, 8, 7, 6, 4, 3, 2, 1), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)], [(1, 2, 3, 4, 9, 5), (1, 2, 15, 3, 4, 35, 5, 1)], [(1, 1, 1, 1, 2, 2, 2, 2, 2, 2), (1, 1, 1, 1, 2, 2, 2, 2)], [('apple', 'banana', 'n', 'cucumber', 'dragonfruit'), ('apple', 'banana', 'cucumber', 'dragonfruit')], [(1, 2, 3, 4, 5, 2), (1, 2, 3, 4, 5, 2)], [('apple', 'banana', 'f', 'guava', 'm', 'kiwi', 'mango', 'guava'), ('banana', 'f', 'guava', 'kiwi', 'mango')], [(1, 2, 3, 4, 80, 5), (2, 15, 35, 3, 60, 4, 5, 1)], [('a', 'b', 'c', 'c', 'd', 'e', 'gg'), ('a', 'b', 'c', 'd', 'e', 'gg')], [(False,), ()], [(21, 11, 25, 26, 30, 35, 40, 40), (21, 11, 25, 26, 30, 35, 40, 40)], [(1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7)], [('', 'appple', 'a', 'apple'), ('', 'apple', 'apple')], [(5, 60, 18, 10, 11, 8, 26, -35, 34), (5, 60, 18, 10, 11, 8, 26, -35, 2, 34, 18)], [('apple', 'banana', 'cherry', 'durian', 'elderberry', 'eggplant', 'fig', 'durian'), ('apple', 'banana', 'cherrappple', 'guava', 'kiwi', 'mango')], [(5, 5, 5, 5, 6, 6, 6, 6, 5), (5, 5, 5, 5, 6, 6, 6, 6)], [(1, 2, 3, 4, 30, 6, 7, 9, 10, 9), (1, 3, 4, 30, 6, 7, 9, 10, 9)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15), (10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 18, 19, 20)], [('apple', 'guva', 'banana', 'guava', 'kiwi', 'mango'), ('apple', 'banana', 'guava', 'kiwi', 'mango')], [('', 'apple', ''), ('', 'apple')], [('a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'), ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')], [(7, 8, 10, 9, 10, 11), (7, 8, 9, 10, 11)], [(5, 5, 5, 5, 6, 5, 6, 6, 5), (5, 5, 5, 5, 6, 6, 6, 6, 5, 5)], [(1, 1, 1, 1, 2, 2, 2, 2), (1, 1, 1, 1, 2, 2, 2, 2)], [(21, 11, 25, 26, 30, 35, 40, 40, 21), (26, 34, 21, 36, 50, 40, 45, 50)], [(1, 2, 3, 90, 5, 2, 7, 8, 9, 10, 11, 12), (1, 2, 3, 90, 5, 12, 7, 8, 9, 10, 11, 12)], [('apple', 'banana', 'egcherrygplant', 'guava', 'kiwi', 'mango', 'kiwi'), ('apple', 'banana', 'egcherrygplant', 'guava', 'kiwi', 'mango')], [('e', 'f', 'g'), ('d', 'e', 'f', 'g')], [(1, 1, 60, 2, 3, 3, 4, 4, 5, 5), (2, 2, 4, 4, 6, 6, 8, 8, 10, 10)], [(1, 2, 3, 4, 5, 2), (1, 2, 3, 4, 5, 2, 1)], [(1, 2, 3, 19, 5), (1, 2, 3, 4, 7)], [(1, 2, 3, 4, 5, 7, 8, 9, 10), (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)], [(21, 11, 25, 26, 30, 35, 40), (26, 34, 21, 40, 45, 50)], [('', 'apple', 'banana'), ('egcherrygplant', 'a', 'banana', 'egcherrygplant')], [(10, 9, 8, 5, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15)], [(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6, 7)], [(11, 20, 30, 40, 50, 60, 70, 80, 90, 100), (10, 20, 30, 40, 50, 60, 70, 9, 90, 100)], [(1, 2, 90, 5, 12, 7, 8, 9, 10, 11, 12), (1, 2, 90, 5, 12, 7, 8, 9, 10, 11, 12)], [(10, 20, 15, 40, 50, 60, 70, 9, 90, 100), (10, 20, 15, 40, 50, 60, 70, 9, 90, 100)], [(2, 4, 6, 8, 10, 12, 1, 14, 25, 16), (2, 4, 6, 8, 10, 12, 14, 16)], [(10, 9, 8, 7, 6, 5, 4, 3, 1, 11, 16, 17, 18, 19, 20), (10, 9, 21, 8, 7, 6, 5, 4, 3, 2, 1, 11, 16, 17, 18, 19, 20)], [(1, 2, 3, 1, 3), (1, 2, 1)], [('apple', 'banana', 'cherry', 'guava', 'kiwi', 'mango'), ('apple', 'banana', 'cherry', 'guava', 'kiwi', 'mango')], [(10, 10, 20, 20, 30, 30, 7, 40, 50, 50), (10, 10, 20, 20, 30, 30, 40, 40, 50, 50)], [(1, 2, 3, 90, 5, 2, 7, 8, 9, 10, 11, 12), (1, 2, 3, 90, 5, 2, 7, 8, 9, 60, 10, 11, 12)], [(1, 2, 3, 0, 4, 5, 5, 5, 5, 5), (1, 2, 3, 4, 5, 5, 5, 5, 5)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 2), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6)], [('banana', 'dragonfruit', 'j'), ('banana', 'dragonfruit', 'fig')], [('', 'banana', 'banana'), ('banana', 'apple', '')], [(1, 2, 3, 2, 4, 5, 1, 1), (1, 2, 3, 4, 7)], [('a', 'b', 'c'), ('d', 'e', 'f', 'g')], [(1, 2, 3, 4, 30, 6, 7, 9, 10, 9), (1, 3, 4, 30, 6, 7, 9, 10, 9, 4)], [(1, 2, 3, 4, 30, 6, 7, 9, 10), (1, 2, 3, 4, 30, 6, 7, 9, 10)], [(1, 2, 25, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7)], [(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25, 13, 14), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25, 13, 14, 15)], [(1, 2, 3, 4, 5, 2), (1, 2, 3, 4, 5)], [('apple',), ('kiwi', 'pple', 'apple')], [(16, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), (7, 2, 3, 9, 13, 14, 18, 21, 25)], [('a', 'b', 'c', 'd'), ('a', 'b', 'c', 'd')], [('egcherrygplantbanana', 'apple', ''), ('banana', 'apple', '')], [('apple', 'banana', 'cherry', 'dian', 'elderberry', 'fig'), ('apple', 'banana', 'cherry', 'daurian', 'elderberry', 'fig')], [('a', 'b', 'c', 'd', 'e', 'f'), ('h', 'i', 'j', 'k', 'l', 'm', 'n')], [('ebanana', '', 'apple', 'banana'), ('', 'apple', 'banana')], [(26, 34, 21, 36, 50, 40, 45, 50), (26, 34, 21, 36, 50, 40, 45, 50, 45)]]
results = [(3, 6, 7, 10), (1, 4, 7, 9), (34, 36, 11, 25), (3, 6, 8, 9, 10, 12, 14, 16), (1, 4, 5, 6, 8, 10, 11, 12, 14, 18, 21, 25), (11, 25, 30, 34, 35, 36, 45, 50), (), (1, 2, 3), (1, 2, 3), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), (1, 3), (1, 2, 3, 4, 6), (100, 70, 80, 90, 60), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), (1, 3, 5, 6, 8, 10), ('b', 'e', 'l', 'j', 'h', 'k', 'g', 'c', 'i', 'd', 'f', 'a', 'm', 'n'), (), (), ('b', 'a', 'i', 'h', 'j', 'k', 'l'), (1, 3, 5, 7, 10, 12, 14, 16), (1, 3, 5, 7, 8, 10, 12, 14, 16), ('eggplant', 'cucumber', 'fig', 'apple'), (11, 12, 13, 14, 15, 16, 17, 18, 19, 20), ('kiwi', 'durian', 'guava', 'elderberry', 'fig', 'mango'), (), (), (1, 2, 3, 4, 6, 7, 8, 9), ('b', 'e', 'c', 'f', 'g', 'a'), (), (1, 2, 3, 4, 5, 'f', 'i', 'g', 'h', 'j'), (16, 2), (1, 3), ('eggplant', 'fig', 'cucumber', 'apple', 'egcherrygplant'), (5, 8, 15, 30), (), (), ('elderberry',), ('banana',), (11, 25, 30, 34, 35, 36, 45, 50), (), (), ('cucumber', 'fig', 'apple'), (), (11, 12, 13, 14, 15, 16, 17, 18, 19, 20), (5, 7), (), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (11, 25, 30, 34, 35, 36, 45, 50), (), ('b', 'e', 'l', 'j', 'h', 'k', 'c', 'i', 'd', 'f', 'a', 'm', 'n', 'gg'), ('a',), (5, 8, 15, 30), ('a', '', 'apple', 'egcherrygplant'), (), (15,), (1, 3, 5, 7, 8, 10, 12, 14, 16), (2,), ('b', 'durian', 'a', 'i', 'h', 'j', 'k', 'l'), (32.93260841054931, 66.77507074495682, -59.91254473588992, -74.09499781125828, -54.49719674608351), (), (21,), (100, 70, 80, 90, 60), (), (), (), ('cherry', 'banana', 'apple', 'n'), (), (5,), (35, 9, 15), (), ('n',), (), ('apple', 'm'), (35, 15, 80, 60), (), (False,), (), (), ('a', 'appple'), (2,), ('eggplant', 'durian', 'cherry', 'cherrappple', 'kiwi', 'guava', 'elderberry', 'fig', 'mango'), (), (2,), (11, 12, 13, 14, 15, 16, 18, 19, 20), ('guva',), (), ('b',), (), (), (), (11, 25, 30, 34, 35, 36, 45, 50), (), (), ('d',), (1, 3, 5, 6, 8, 10, 60), (), (19, 4, 5, 7), (1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), (34, 35, 11, 45, 50, 25, 30), ('a', '', 'apple', 'egcherrygplant'), (11, 12, 13, 15, 16, 17, 18, 19, 20), (7,), (9, 10, 11, 80), (), (), (1, 25), (2, 21), (3,), (), (7,), (60,), (0,), (), ('j', 'fig'), ('apple',), (5, 7), ('b', 'e', 'd', 'f', 'c', 'g', 'a'), (2,), (), (3, 25), (15,), (), ('kiwi', 'pple'), (4, 5, 6, 8, 10, 11, 12, 13, 14, 16, 18, 21, 25), (), ('banana', 'egcherrygplantbanana'), ('daurian', 'dian'), ('b', 'e', 'l', 'j', 'h', 'k', 'c', 'i', 'd', 'f', 'a', 'm', 'n'), ('ebanana',), ()]

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
        func_name = "find_dissimilar"
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
        for test_case in ['assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)', 'assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)', 'assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25)']:
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
