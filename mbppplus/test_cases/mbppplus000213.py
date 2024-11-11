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
inputs = [[[[1], [1, 2], [1, 2, 3]]], [[[1, 1], [1, 1, 1], [1, 2, 7, 8]]], [[['x'], ['x', 'y'], ['x', 'y', 'z']]], [[[], [], []]], [[['x']]], [[['x'], ['x', 'y']]], [[['x'], ['x', 'y'], ['x', 'y', 'z'], ['x', 'y', 'z', 'a']]], [[['x'], ['x', 'y'], ['x', 'y', 'z'], ['x', 'y', 'z', 'a'], ['x', 'y', 'z', 'a', 'b']]], [[[], ['x', 'y'], [], ['x', 'y', 'z']]], [[[[1]], [[1, 2]], [[1, 2, 3]]]], [[[[1]], [[1, 2], [3, 4]], [[1, 2, 3, 4, 5]]]], [[[[1]], [[1, 2], [3, 4]], [[1, 2, 3, 4, 5]], [[0, 1, 2, 3]]]], [[[[1]], [[1, 2], [3, 4]], [[1, 2, 3, 4, 5]], [[0, 1, 2, 3]], []]], [[[], ['a', 'b', 'c'], ['d', 'e', 'f'], [], [], ['g'], [], ['h', 'i']]], [[[[1, 2, 3], [4, 5, 6]], [], [[7, 8, 9, 10], [11, 12], [13]], [[14, 15]], []]], [[['apple', 'banana'], ['carrot', 'potato'], ['orange'], [], ['grapefruit', 'watermelon']]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p']]]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['m', 'n']]]], [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10], [11, 12]], [[13, 14, 15, 16, 17], [18, 19], [20, 21, 22]]]], [[['x', 'y'], ['a', 'b'], ['i', 'j'], ['u', 'v', 'w'], ['m', 'n', 'o', 'p']]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], [[10, 11]], [[12, 13, 14], [15, 16, 17], [18, 19, 20]], [[21, 22], [23, 24], [25, 26], [27, 28]]]], [[['apple', 'banana', 'cherry'], ['doughnut'], ['elephant', 'fox'], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango']]], [[['x'], ['y'], ['z', 'a'], ['b', 'c', 'd'], ['e', 'f', 'g', 'h']]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9, 10], [11, 12], [13]], [[1, 2, 3], [4, 5, 6]], [[14, 15]], [[1, 2, 3], [4, 5, 6]]]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']]]], [[['x'], [], [], ['z', 'a'], ['b', 'c', '', 'd'], ['e', 'f', 'g', 'h']]], [[[], []]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm'], ['e', 'f', 'g', 'h']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm'], ['e', 'f', 'g', 'h']]]], [[[['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[['g', 'h'], ['i', 'j', 'k', 'l']], [['g', 'h'], ['i', 'j', 'k', 'l']]]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k'], ['e', 'f', 'g', 'h']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k'], ['e', 'f', 'g', 'h']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k'], ['e', 'f', 'g', 'h']]]], [[[], [], ['l', 'tFbRBOk', 'cfOPt', 'fox', 'grape', 'mango', 'bURovwB', 'lemon', 'ZRkprFsNlc', 'BdjtDHroYE'], []]], [[[['a'], ['b'], ['c']], [['dd']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p']], [['dd']]]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], [[12, 13, 14], [15, 16, 17], [18, 19, 20]], [[21, 22], [23, 24], [25, 26], [27, 28]]]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['dd', 'e', 'f']], [['dd', 'e', 'f']], [['m', 'n']]]], [[[], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], []]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['g', 'h'], ['i', 'j', 'k', 'l']]]], [[[['a'], ['b'], ['c']], [], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k'], ['e', 'f', 'g', 'h']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k'], ['e', 'f', 'g', 'h']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k'], ['e', 'f', 'g', 'h']]]], [[[], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], [], [], []]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['m', 'n', 'm'], ['m', 'n', 'm']]]], [[[], [], [], ['eqmZrrw', 'NUksHJFgXB', 'B', 'u', 'j', 'BdjtDHroYE', 'LONOBOhF', '', 'qIZtur', 'grape']]], [[[], [], [], []]], [[['x'], [], [], ['z', 'a'], ['b', 'c', '', 'd']]], [[['apple', 'banana', 'cherry'], [], ['elephant', 'fox'], [], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango']]], [[['apple', 'banana'], [-85.491799009766, -28.429789067892102, -13.346744109726245, -58.44119256953919, 60.7668803444335, 47.68813139253385, -7.5873331040208, 47.72732136154761, -85.491799009766, -28.429789067892102], ['carrot', 'potato'], ['orange'], [], ['grapefruit', 'watermelon']]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], [[12, 13, 14], [15, 16, 17], [18, 19, 20]], [[21, 22], [23, 24], [25, 26], [27, 28]], [[1, 2, 3], [4, 5, 6]]]], [[[True, True, True, True], [False, True, False]]], [[['apple', 'banana', 'cherry'], [], ['elephant', 'fox'], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango'], ['ice cream']]], [[[], ['a', 'b', 'c'], ['d', 'e', 'f'], [], [], ['g'], [], ['h', 'i'], []]], [[[True, True, True, True], [True, True, True, True], [True, True, True, True], [False, True, False]]], [[[['cf', 'c'], ['a'], ['b'], ['cf', 'c']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p']], [['dd']], [['dd']]]], [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10], [11, 12]], [[13, 14, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 14, 15, 16, 17], [18, 19], [20, 21, 22]]]], [[[], ['eqtKS'], [['g', 'h'], ['i', 'j', 'k', 'l']]]], [[[], [], ['l', 'tFbRBOk', 'cfOPt', 'fox', 'grape', 'mango', 'bURovwB', 'lemon', 'ZRkprFsNlc', 'BdjtDHroYE'], [], []]], [[[], [], [], ['eqmZrrw', 'NUksHJFgXB', 'B', 'u', 'c', 'j', 'BdjtDHroYE', 'LONOBOhF', '', 'qIZtur', 'grape']]], [[[], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], [], [], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], []]], [[['x', 'x'], ['x', 'x'], ['x', 'y']]], [[[], ['a', 'b', 'c'], ['d', 'e', 'f'], [], [], ['g'], [], ['h', 'i'], [], []]], [[[True, True, False, False, False], [], []]], [[[], ['a', 'b', 'c'], ['d', 'e', 'f'], [], [], ['g'], [], [], ['h', 'i'], [], [], [], []]], [[['x'], [], [], ['zz', 'a'], ['b', 'c', '', 'd'], ['e', 'f', 'g', 'h']]], [[[-70.45849814287817, -79.72463141052742], ['x', 'y'], [], ['x', 'y', 'z']]], [[[-89.56928478588684, 69.15039976127599, -58.61307409762566, -70.45849814287817, 63.11673272639632], [], [], [], []]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['m', 'n', 'm'], ['m', 'n', 'm']], [['x', 'y', 'z'], ['a', 'b', 'c']]]], [[['apple', 'baanana', 'cherry'], [], ['elephant', 'fox'], [], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango'], []]], [[['apple', 'banana', 'cherry'], [False, True], [], ['elephant', 'fox'], [], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango']]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['m', 'n']], [['m', 'n']]]], [[[], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], [], [True, False, True, True, False], [], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], []]], [[[['a', 'b', 'c']], [['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['m', 'n', 'm'], ['m', 'n', 'm']], [['a', 'b', 'c']]]], [[[False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, False]]], [[[[0], [0]], [[0], [0]], [[1, 2], [3, 4]], [[1, 2, 3, 4, 5]]]], [[[['a'], ['b'], ['c']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k']], [['n', 'o', 'p', 'p', 'o'], ['n', 'o', 'p', 'p', 'o']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm', 'k']]]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['i', 'j', 'k', 'l']]]], [[[False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, False, True]]], [[['x'], [], [], ['z', 'a'], ['b', 'c', '', 'd'], ['e', 'f', 'g', 'jh']]], [[[-70.45849814287817, -79.72463141052742], ['x', 'y'], [], ['x', 'y', 'z'], ['x', 'y'], []]], [[[-89.56928478588684, 69.15039976127599, -58.61307409762566, -70.45849814287817, 63.11673272639632], [], [], [], [], []]], [[[True, True], [True, True], [True, True], [True, True], [False, True, False], [True, True]]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], [[12, 13, 14], [15, 16, 17], [18, 19, 20]], [[21, 22], [23, 24], [25, 26], [27, 28], [27, 28]]]], [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10], [11, 12]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]]]], [[[['a'], ['by', 'b'], ['c']], [['d']], [['a'], ['by', 'b'], ['c']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p'], ['n', 'o', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[], ['elephant', 'fox'], [], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango'], ['ice cream']]], [[[[1]], [[1, 2], [3, 4]], [[1, 2, 3, 4, 5]], [[0, 1, 2, 3]], [], [[1, 2, 3, 4, 5]]]], [[[[1, 2, 3], [4, 5, 6]], [96, 61], [[7, 8, 9, 10], [11, 12], [13]], [[14, 15]], [], [[7, 8, 9, 10], [11, 12], [13]]]], [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10], [11, 12]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22]]]], [[[], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], [], []]], [[['x'], [], [], ['e', 'f', 'g', 'h', 'f'], ['z', 'a'], ['b', 'c', '', 'd'], ['e', 'f', 'g', 'h', 'f']]], [[[['g', 'h'], ['i', 'j', 'k', 'l']]]], [[[], [], ['l', 'tFbRBOk', 'cfOPt', 'fox', 'grape', 'mango', 'bURovwB', 'lemon', 'ZRkprFsNlc', 'BdjtDHroYE'], [], [], ['l', 'tFbRBOk', 'cfOPt', 'fox', 'grape', 'mango', 'bURovwB', 'lemon', 'ZRkprFsNlc', 'BdjtDHroYE']]], [[[], ['l', 'tFbRBOk', 'cfOPt', 'fox', 'grape', 'mango', 'bURovwB', 'lemon', 'ZRkprFsNlc', 'BdjtDHroYE'], [], [True, False, False, False, True], [], ['l', 'tFbRBOk', 'cfOPt', 'fox', 'grape', 'mango', 'bURovwB', 'lemon', 'ZRkprFsNlc', 'BdjtDHroYE']]], [[[], ['x', 'y', 'x'], [], ['x', 'y', 'z']]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h']], [['e', 'f', 'g', 'h']]]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h']], [['n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h']], [['e', 'f', 'g', 'h']], [['d']]]], [[[], [], ['x', 'y', 'z']]], [[[False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, False], [False, True, True, True]]], [[[], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], [], [True, False, True, True, False], [], [], [-58.44119256953919, -85.491799009766, 69.15039976127599, -28.429789067892102, 22.405065830734472, 63.11673272639632], []]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'll']], [['g', 'h'], ['i', 'j', 'k', 'll']]]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['d', 'e', 'f']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['m', 'n']], [['m', 'n']], [['m', 'n']]]], [[[False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, True, True], [False, True, False], [False, True, True, True], [False, True, True, True]]], [[[['a'], ['by', 'b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['plemon', 'n', 'o', 'p', 'p'], ['plemon', 'n', 'o', 'p', 'p'], ['plemon', 'n', 'o', 'p', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[['x', 'y', 'z'], ['a', 'b', 'c']], [['e', 'f'], ['e', 'f']], [['i', 'j', 'k', 'll']], [['i', 'j', 'k', 'll']], [['i', 'j', 'k', 'll']]]], [[['grape', 'apple', 'baanana', 'cherry', 'grape'], ['grape', 'apple', 'baanana', 'cherry', 'grape'], [], ['elephant', 'fox'], [], ['grape', 'honey'], ['ice cream'], ['juice'], ['kiwi', 'lemon', 'mango'], [], ['ice cream']]], [[[], [], [False, False, False, True, True, True, False, False], [-4, -79, 15, 11, 18, 14, -1, -59, 11], []]], [[[[1, 2, 3], [4, 5, 6]], [96, 61], [[14, 15], [14, 15]], [[7, 8, 9, 10], [11, 12], [13]], [[14, 15], [14, 15]], [], [[7, 8, 9, 10], [11, 12], [13]], [[7, 8, 9, 10], [11, 12], [13]]]], [[['grapefruit'], ['apple', 'banana'], ['carrot', 'potato'], ['orange'], [], ['grapefruit']]], [[[['a'], ['b'], ['c']], [['d'], ['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p']]]], [[[], [], ['Icky', 'g', 'sRzEiFHz', 'kT', 'aoLcOFLFH', 'tFbRBOk', 'RaynjY', 'MCUQiO', 'OgmzNgy'], ['eqmZrrw', 'NUksHJFgXB', 'B', 'u', 'j', 'BdjtDHroYE', 'LONOBOhF', '', 'qIZtur', 'grape']]], [[[[1]], [[1, 2, 3, 4, 5]], [[0, 1, 2, 3]], [[1, 2], [3, 4]]]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], [[10, 11]], [[12, 13, 14, 13], [12, 13, 14, 13], [15, 16, 17], [18, 19, 20]], [[12, 13, 14, 13], [12, 13, 14, 13], [15, 16, 17], [18, 19, 20]], [[21, 22], [23, 24], [25, 26], [27, 28]]]], [[[['a'], ['cc', 'c'], ['b'], ['cc', 'c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p', 'p']], [['a'], ['cc', 'c'], ['b'], ['cc', 'c']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[['a'], ['by', 'b'], ['c']], [['d']], [['a'], ['by', 'b'], ['c']], [['n', 'o', 'p'], ['n', 'o', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']]]], [[[['a', 'b', 'c']], [['a', 'b', 'c']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['a', 'b', 'c']], [['m', 'n', 'm'], ['m', 'n', 'm']], [['a', 'b', 'c']], [['a', 'b', 'c']]]], [[[], ['a', 'b', 'c'], ['d', 'e', 'f'], [], [], ['g'], [], ['h', 'i'], [], [-28, 94, 16, -11, 9, -4], []]], [[[], [], ['z', 'a'], ['b', 'c', '', 'd']]], [[['x', 'y', 'z'], ['x'], ['x', 'y'], ['x', 'y', 'z'], ['x', 'y', 'z']]], [[[['a'], ['b'], ['c']], [['d']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['n', 'o', 'p']], [['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l', 'm']], [['a'], ['b'], ['c']]]], [[[], [], [], ['x', 'y', 'z']]], [[[['g', 'h'], ['i', 'j', 'k', 'l']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['g', 'h'], ['i', 'j', 'k', 'l']]]], [[['ejuiceqtKS'], [['g', 'h'], ['i', 'j', 'k', 'l']]]], [[[False, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True], [False, True, False], [False, True, True, True, True], [False, True, True, True, True], [False, True, True, True, True]]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], [[10, 11]], [[12, 13, 14], [15, 16, 17], [18, 19, 20]], [[21, 22], [23, 24], [25, 26], [27, 28]], [[21, 22], [23, 24], [25, 26], [27, 28]]]], [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10], [11, 12]], [[13, 15, 16, 17], [18, 19], [20, 21, 22], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22], [20, 21, 22]], [[13, 15, 16, 17], [18, 19], [20, 21, 22], [20, 21, 22]]]]]
results = [[1], [1, 1], ['x'], [], ['x'], ['x'], ['x'], ['x'], [], [[1]], [[1]], [[1]], [], [], [], [], [['d']], [['d', 'e', 'f']], [[10], [11, 12]], ['x', 'y'], [[7, 8, 9]], ['doughnut'], ['x'], [[14, 15]], [['d']], [['d']], [['d', 'e', 'f']], [], [], [['d']], [['d']], [['g', 'h'], ['i', 'j', 'k', 'l']], [['d']], [], [['dd']], [[7, 8, 9]], [['dd', 'e', 'f']], [], [['d', 'e', 'f']], [], [], [['d', 'e', 'f']], [], [], [], [], [], [[7, 8, 9]], [False, True, False], [], [], [False, True, False], [['n', 'o', 'p']], [[10], [11, 12]], [], [], [], [], ['x', 'x'], [], [], [], [], [], [], [['d', 'e', 'f']], [], [], [['d', 'e', 'f']], [], [['a', 'b', 'c']], [False, True, False], [[1, 2, 3, 4, 5]], [['d']], [['d', 'e', 'f']], [False, True, True, True], [], [], [], [True, True], [[7, 8, 9]], [[10], [11, 12]], [['d']], [], [], [], [[10], [11, 12]], [], [], [['g', 'h'], ['i', 'j', 'k', 'l']], [], [], [], [['d']], [['d']], [], [False, True, False], [], [['d', 'e', 'f']], [['d', 'e', 'f']], [False, True, False], [['d']], [['i', 'j', 'k', 'll']], [], [], [], [], [['n', 'o', 'p']], [], [[1]], [[7, 8, 9]], [['d']], [['d']], [['a', 'b', 'c']], [], [], ['x'], [['d']], [], [['g', 'h'], ['i', 'j', 'k', 'l']], ['ejuiceqtKS'], [False, True, False], [[7, 8, 9]], [[10], [11, 12]]]

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
        func_name = "Find_Min"
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
        for test_case in ['assert Find_Min([[1],[1,2],[1,2,3]]) == [1]', 'assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]', "assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']"]:
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