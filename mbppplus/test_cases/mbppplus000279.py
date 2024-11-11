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
inputs = [[[['x', 'y'], ['a', 'b'], ['m', 'n']]], [[[1, 2], [3, 4], [5, 6], [7, 8]]], [[[[1], [2]], [[3], [4]], [[5], [6]], [[7], [8]]]], [[['x', 1], ['y', 2], [True, 'z']]], [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]]]], [[[['hello', 'world'], ['foo', 'bar']], [['baz', 'qux'], ['python', 'programming']]]], [[['y', 2], [True, 'z']]], [[[['a', 'b', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]]]], [[[['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[['y', 2], ['y', 2]]], [[[['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 2]]]], [[['y', 2]]], [[[['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['c', 'd'], [3, 4]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 2]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4, 4]], [['c', 'd'], [3, 4, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[[['a', 'b', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['c', 'd'], [3, 4]]]], [[['y', 2], [True, 'z'], [True, 'z']]], [[[['hello', 'world'], ['foo', 'bar']], [['baz', 'qux'], ['python', 'programming']], [['hello', 'world'], ['foo', 'bar']]]], [[[['hello', 'world'], ['foo', 'bar']], [['hello', 'world'], ['foo', 'bar']]]], [[[['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']]]], [[[['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 6, 2]]]], [[['y', 1], ['y', 1]]], [[['y', 2], ['y', 2], ['y', 2]]], [[[['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['hello', 'world'], ['foo', 'bbar']]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 2]], [['a', 'b'], [1, 2]]]], [[[True, 'z'], [True, 'z']]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[[['c', 'd'], [3, 4]], [['e', 'ff', 'f'], ['e', 'ff', 'f']], [['e', 'ff', 'f'], ['e', 'ff', 'f']], [['c', 'd'], [3, 4]]]], [[[['a', 'b', 'b'], [1]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1]]]], [[[['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar'], ['foo', 'bbar']]]], [[[['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]]]], [[[['hello', 'world'], ['foo', 'bar']], [['hello', 'world'], ['foo', 'bar']], [['hello', 'world'], ['foo', 'bar']]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [[5, 6], [5, 6]], [[5, 6], [5, 6]], [[5, 6], [5, 6]], [['a', 'b'], [1, 2]], [['a', 'b'], [1, 2]]]], [[['yy', 1], ['yy', 1]]], [[['z', 2]]], [[[['e', ''], [5, 6]], [['a', 'b', 'b'], [1, 2]], [['e', ''], [5, 6]]]], [[['x', 1], [True, 'z']]], [[[['c', 'd'], [3, 4]], [['c', 'd'], [3, 4]]]], [[['y', 2], ['y', 2], ['y', 2], ['y', 2]]], [[[['a', 'b', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]]]], [[[['e', 'f'], [5, 6, 6]], [['a', 'b', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6, 6]], [['e', 'f'], [5, 6, 6]]]], [[['x', 1], [True, 'z'], ['x', 1]]], [[[['hello', 'world'], ['foo', 'bar']], [['hello', 'world'], ['foo', 'bar']], [['hello', 'world'], ['foo', 'bar']], [['hello', 'world'], ['foo', 'bar']]]], [[[['baz', 'qux'], ['python', 'python', 'programming']], [['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'python', 'programming']]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4, 4]], [['c', 'd'], [3, 4, 4]], [[5, 6], ['e', 'f']], [[5, 6], ['e', 'f']]]], [[[['e', 'f'], [5, 6, 6]], [['a', 'b', 'b'], [1, 2]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6, 6]]]], [[['z', 2], ['z', 2]]], [[['y', 1], ['y', 1], ['y', 1]]], [[[['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar'], ['foo', 'bbar']]]], [[[['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[[['c', 'd'], [3, 4, 4]], [['c', 'd'], [3, 4, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[[['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']]]], [[['y', 2], [True, 'z'], [True, 'z'], ['y', 2]]], [[[['a', 'b', 'b'], [1]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1]], [['a', 'b', 'b'], [1]]]], [[[['a', 'b', 'b'], [1, 2]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]]]], [[[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4, 4]], [['c', 'd'], [3, 4, 4]], [[5, 6], ['e', 'f']], [[5, 6], ['e', 'f']], [['c', 'd'], [3, 4, 4]]]], [[[['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']]]], [[[['c', 'd'], [3, 4]], [['e', 'f'], [5, 5, 6]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b'], [1, 2]]]], [[[['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']]]], [[[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['baz', 'qux'], ['python', 'programming', 'programming']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']]]], [[[['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]]]], [[['y', 2], [True, 'z'], ['y', 2]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 10]], [['e', 'f'], [5, 10]], [['e', 'f'], [5, 10]], [['e', 'f'], [5, 10]], [['e', 'f'], [5, 10]]]], [[[['e', 'f'], [5, 6, 6]], [['a', 'b', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6, 6]], [['e', 'f'], [5, 6, 6]], [['a', 'b', 'b'], [1, 2]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b'], [1, 2]], [['a', 'b'], [1, 2]]]], [[[['e', ''], [5, 6]], [['a', 'b', 'b'], [1, 2]], [['e', ''], [5, 6]], [['e', ''], [5, 6]]]], [[[['a', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[[['c', 'd'], [3, 4]], [['a', 'b', 'b'], [8, 2]], [['a', 'b', 'b'], [8, 2]], [['e', 'f'], [5, 6]]]], [[['y', 2], [True, 'yy'], [True, 'yy'], ['y', 2], ['y', 2]]], [[[['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['c', 'd'], [3, 4]]]], [[[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['baz', 'qux'], ['python', 'programming', 'programming']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']]]], [[[['e'], [5, 6]], [['a', 'b', 'b'], [1, 2]], [['e'], [5, 6]], [['e'], [5, 6]]]], [[[['hello', 'world'], ['foo', 'bar']]]], [[[['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar']]]], [[[['a', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]]]], [[['x', 1], [True, 'z'], ['x', 1], [True, 'z']]], [[[['a', 'b'], [1, 2, 1]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 2, 1]], [['a', 'b'], [1, 2, 1]], [['a', 'b'], [1, 2, 1]]]], [[[['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['hello', 'world', 'hello'], ['foo', 'bbar']]]], [[[['e', 'f'], [5, 6, 6]], [['a', 'b', 'b'], [1, 2]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6, 6]], [['a', 'b', 'b'], [1, 2]]]], [[[['hello', 'world'], ['foo', 'bbar']], [['hello', 'world'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['hello', 'world'], ['foo', 'bbar']]]], [[[['c', 'd'], [3, 4]]]], [[[['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]], [['c', 'd'], [3, 4]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 6, 2]], [['c', 'd'], [3, 4]]]], [[[['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['hello', 'world', 'hello'], ['foo', 'bbar']], [['hello', 'world', 'hello'], ['foo', 'bbar']]]], [[[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['baz', 'qux'], ['python', 'programming', 'programming']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']]]], [[[['e', ''], [5, 6]], [['a', 'b', 'b'], [1, 2]]]], [[[['e'], [5, 6]], [['a', 'b', 'b'], [1, 2]], [['e'], [5, 6]], [['e'], [5, 6]], [['e'], [5, 6]]]], [[[['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar'], ['foo', 'bbar']]]], [[['y', 2], [True, 'z'], [True, 'z'], [True, 'z']]], [[[['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar'], ['foo', 'bbar']], [['baz', 'qux'], ['python', 'programming']], [['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar']]]], [[[['a', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 2]]]], [[[['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]], [['d'], [3, 4]], [['e', 'f'], [5, 6]], [['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]], [['a', 'b'], [1, 6, 2]]]], [[['e', 2], ['e', 2], [True, 'z'], [True, 'z'], [True, 'z']]], [[[['a', 'b', 'b'], [1, 2]], [['c', 'd'], [3, 4]], [['a', 'b', 'b'], [1, 2]], [['e', 'f'], [5, 6]], [['c', 'd'], [3, 4]]]], [[[['e', ''], [5, 6]], [['a', 'b', 'b'], [1, 2]], [['a', 'b', 'b'], [1, 2]]]], [[[[1, 2, 3], [4, 5, 6]]]], [[[['c', 'd'], [3, 4]], [['c', 'd'], [3, 4]], [['c', 'd'], [3, 4]]]], [[[['a', 'b'], [1, 2]], [['c', 'd'], [3, 4, 4, 4]], [['c', 'd'], [3, 4, 4, 4]], [[5, 6], ['e', 'f']], [[5, 6], ['e', 'f']], [['c', 'd'], [3, 4, 4, 4]], [['c', 'd'], [3, 4, 4, 4]]]], [[['yy', 1]]], [[['y', 8], ['y', 8], ['y', 8], ['y', 8]]], [[[['e'], [5, 7]], [['a', 'b', 'b'], [1, 2]], [['e'], [5, 7]], [['e'], [5, 7]], [['e'], [5, 7]]]], [[[['a', 'b'], [1, 2]], [['e', 'f'], [5, 6]]]]]
results = [[['x', 'a', 'm'], ['y', 'b', 'n']], [[1, 3, 5, 7], [2, 4, 6, 8]], [[[1], [3], [5], [7]], [[2], [4], [6], [8]]], [['x', 'y', True], [1, 2, 'z']], [[[1, 2, 3], [7, 8, 9]], [[4, 5, 6], [10, 11, 12]]], [[['a', 'b'], ['c', 'd'], ['e', 'f']], [[1, 2], [3, 4], [5, 6]]], [[['hello', 'world'], ['baz', 'qux']], [['foo', 'bar'], ['python', 'programming']]], [['y', True], [2, 'z']], [[['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b'], ['e', 'f']], [[1, 2], [3, 4], [1, 2], [5, 6]]], [[['hello', 'world'], ['hello', 'world'], ['hello', 'world'], ['baz', 'qux']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming']]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f']], [[1, 2], [3, 4], [5, 6], [5, 6]]], [['y', 'y'], [2, 2]], [[['c', 'd'], ['a', 'b', 'b'], ['e', 'f']], [[3, 4], [1, 2], [5, 6]]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f'], ['a', 'b']], [[1, 2], [3, 4], [5, 6], [5, 6], [1, 2]]], [['y'], [2]], [[['c', 'd'], ['a', 'b', 'b'], ['e', 'f'], ['c', 'd']], [[3, 4], [1, 2], [5, 6], [3, 4]]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['a', 'b']], [[1, 2], [3, 4], [5, 6], [1, 2]]], [[['a', 'b'], ['c', 'd'], ['c', 'd'], ['e', 'f'], ['e', 'f']], [[1, 2], [3, 4, 4], [3, 4, 4], [5, 6], [5, 6]]], [[['a', 'b', 'b'], ['c', 'd'], ['e', 'f'], ['c', 'd']], [[1, 2], [3, 4], [5, 6], [3, 4]]], [['y', True, True], [2, 'z', 'z']], [[['hello', 'world'], ['baz', 'qux'], ['hello', 'world']], [['foo', 'bar'], ['python', 'programming'], ['foo', 'bar']]], [[['hello', 'world'], ['hello', 'world']], [['foo', 'bar'], ['foo', 'bar']]], [[['hello', 'world'], ['hello', 'world'], ['baz', 'qux']], [['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming']]], [[['a', 'b'], ['a', 'b'], ['c', 'd'], ['e', 'f'], ['a', 'b']], [[1, 6, 2], [1, 6, 2], [3, 4], [5, 6], [1, 6, 2]]], [['y', 'y'], [1, 1]], [['y', 'y', 'y'], [2, 2, 2]], [[['hello', 'world'], ['hello', 'world'], ['hello', 'world'], ['baz', 'qux'], ['hello', 'world']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar']]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f'], ['a', 'b'], ['a', 'b']], [[1, 2], [3, 4], [5, 6], [5, 6], [1, 2], [1, 2]]], [[True, True], ['z', 'z']], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f'], ['e', 'f']], [[1, 2], [3, 4], [5, 6], [5, 6], [5, 6]]], [[['c', 'd'], ['e', 'ff', 'f'], ['e', 'ff', 'f'], ['c', 'd']], [[3, 4], ['e', 'ff', 'f'], ['e', 'ff', 'f'], [3, 4]]], [[['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b']], [[1], [3, 4], [1]]], [[['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['baz', 'qux'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar']]], [[['a', 'b'], ['a', 'b'], ['c', 'd'], ['e', 'f'], ['a', 'b'], ['a', 'b']], [[1, 6, 2], [1, 6, 2], [3, 4], [5, 6], [1, 6, 2], [1, 6, 2]]], [[['hello', 'world'], ['hello', 'world'], ['hello', 'world']], [['foo', 'bar'], ['foo', 'bar'], ['foo', 'bar']]], [[['a', 'b'], ['c', 'd'], [5, 6], [5, 6], [5, 6], ['a', 'b'], ['a', 'b']], [[1, 2], [3, 4], [5, 6], [5, 6], [5, 6], [1, 2], [1, 2]]], [['yy', 'yy'], [1, 1]], [['z'], [2]], [[['e', ''], ['a', 'b', 'b'], ['e', '']], [[5, 6], [1, 2], [5, 6]]], [['x', True], [1, 'z']], [[['c', 'd'], ['c', 'd']], [[3, 4], [3, 4]]], [['y', 'y', 'y', 'y'], [2, 2, 2, 2]], [[['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b']], [[1, 2], [3, 4], [1, 2]]], [[['e', 'f'], ['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b'], ['e', 'f'], ['e', 'f']], [[5, 6, 6], [1, 2], [3, 4], [1, 2], [5, 6, 6], [5, 6, 6]]], [['x', True, 'x'], [1, 'z', 1]], [[['hello', 'world'], ['hello', 'world'], ['hello', 'world'], ['hello', 'world']], [['foo', 'bar'], ['foo', 'bar'], ['foo', 'bar'], ['foo', 'bar']]], [[['baz', 'qux'], ['hello', 'world'], ['hello', 'world'], ['baz', 'qux']], [['python', 'python', 'programming'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'python', 'programming']]], [[['a', 'b'], ['c', 'd'], ['c', 'd'], [5, 6], [5, 6]], [[1, 2], [3, 4, 4], [3, 4, 4], ['e', 'f'], ['e', 'f']]], [[['e', 'f'], ['a', 'b', 'b'], ['a', 'b', 'b'], ['e', 'f']], [[5, 6, 6], [1, 2], [1, 2], [5, 6, 6]]], [['z', 'z'], [2, 2]], [['y', 'y', 'y'], [1, 1, 1]], [[['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['baz', 'qux'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar']]], [[['c', 'd'], ['a', 'b', 'b'], ['e', 'f'], ['e', 'f']], [[3, 4], [1, 2], [5, 6], [5, 6]]], [[['c', 'd'], ['c', 'd'], ['e', 'f'], ['e', 'f']], [[3, 4, 4], [3, 4, 4], [5, 6], [5, 6]]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f'], ['e', 'f'], ['e', 'f']], [[1, 2], [3, 4], [5, 6], [5, 6], [5, 6], [5, 6]]], [[['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['baz', 'qux']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming']]], [['y', True, True, 'y'], [2, 'z', 'z', 2]], [[['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b'], ['a', 'b', 'b']], [[1], [3, 4], [1], [1]]], [[['a', 'b', 'b'], ['a', 'b', 'b'], ['e', 'f']], [[1, 2], [1, 2], [5, 6]]], [[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['baz', 'qux'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['python', 'programming'], ['foo', 'bbar', 'foo']]], [[['a', 'b'], ['c', 'd'], ['c', 'd'], [5, 6], [5, 6], ['c', 'd']], [[1, 2], [3, 4, 4], [3, 4, 4], ['e', 'f'], ['e', 'f'], [3, 4, 4]]], [[['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['baz', 'qux'], ['foo', 'bbar', 'bbar'], ['baz', 'qux'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['python', 'programming'], ['foo', 'bbar', 'bbar'], ['python', 'programming'], ['foo', 'bbar', 'bbar']]], [[['c', 'd'], ['e', 'f']], [[3, 4], [5, 5, 6]]], [[['a', 'b'], ['c', 'd'], ['a', 'b']], [[1, 2], [3, 4], [1, 2]]], [[['hello', 'world'], ['hello', 'world'], ['hello', 'world'], ['hello', 'world']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar']]], [[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['baz', 'qux'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['python', 'programming', 'programming'], ['foo', 'bbar', 'foo']]], [[['c', 'd'], ['a', 'b', 'b'], ['e', 'f'], ['e', 'f'], ['a', 'b', 'b'], ['e', 'f']], [[3, 4], [1, 2], [5, 6], [5, 6], [1, 2], [5, 6]]], [['y', True, 'y'], [2, 'z', 2]], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f'], ['e', 'f'], ['e', 'f'], ['e', 'f']], [[1, 2], [3, 4], [5, 10], [5, 10], [5, 10], [5, 10], [5, 10]]], [[['e', 'f'], ['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b'], ['e', 'f'], ['e', 'f'], ['a', 'b', 'b']], [[5, 6, 6], [1, 2], [3, 4], [1, 2], [5, 6, 6], [5, 6, 6], [1, 2]]], [[['a', 'b'], ['c', 'd'], ['a', 'b'], ['a', 'b']], [[1, 2], [3, 4], [1, 2], [1, 2]]], [[['e', ''], ['a', 'b', 'b'], ['e', ''], ['e', '']], [[5, 6], [1, 2], [5, 6], [5, 6]]], [[['a', 'b'], ['e', 'f'], ['e', 'f']], [[1, 2], [5, 6], [5, 6]]], [[['c', 'd'], ['a', 'b', 'b'], ['a', 'b', 'b'], ['e', 'f']], [[3, 4], [8, 2], [8, 2], [5, 6]]], [['y', True, True, 'y', 'y'], [2, 'yy', 'yy', 2, 2]], [[['c', 'd'], ['e', 'f'], ['c', 'd']], [[3, 4], [5, 6], [3, 4]]], [[['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['baz', 'qux'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['python', 'programming', 'programming'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']]], [[['e'], ['a', 'b', 'b'], ['e'], ['e']], [[5, 6], [1, 2], [5, 6], [5, 6]]], [[['hello', 'world']], [['foo', 'bar']]], [[['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['baz', 'qux'], ['foo', 'bbar', 'bbar'], ['baz', 'qux'], ['foo', 'bbar', 'bbar']], [['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['foo', 'bbar', 'bbar'], ['python', 'programming'], ['foo', 'bbar', 'bbar'], ['python', 'programming'], ['foo', 'bbar', 'bbar']]], [[['a', 'b'], ['e', 'f'], ['e', 'f'], ['e', 'f']], [[1, 2], [5, 6], [5, 6], [5, 6]]], [['x', True, 'x', True], [1, 'z', 1, 'z']], [[['a', 'b'], ['c', 'd'], ['e', 'f'], ['e', 'f'], ['a', 'b'], ['a', 'b'], ['a', 'b']], [[1, 2, 1], [3, 4], [5, 6], [5, 6], [1, 2, 1], [1, 2, 1], [1, 2, 1]]], [[['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['baz', 'qux'], ['hello', 'world', 'hello']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar']]], [[['e', 'f'], ['a', 'b', 'b'], ['a', 'b', 'b'], ['e', 'f'], ['a', 'b', 'b']], [[5, 6, 6], [1, 2], [1, 2], [5, 6, 6], [1, 2]]], [[['hello', 'world'], ['hello', 'world'], ['baz', 'qux'], ['hello', 'world']], [['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar']]], [[['c', 'd']], [[3, 4]]], [[['a', 'b'], ['a', 'b'], ['c', 'd'], ['e', 'f'], ['a', 'b'], ['c', 'd']], [[1, 6, 2], [1, 6, 2], [3, 4], [5, 6], [1, 6, 2], [3, 4]]], [[['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello'], ['baz', 'qux'], ['hello', 'world', 'hello'], ['hello', 'world', 'hello']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar'], ['foo', 'bbar']]], [[['foo', 'bbar', 'foo'], ['baz', 'qux'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']], [['foo', 'bbar', 'foo'], ['python', 'programming', 'programming'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo'], ['foo', 'bbar', 'foo']]], [[['e', ''], ['a', 'b', 'b']], [[5, 6], [1, 2]]], [[['e'], ['a', 'b', 'b'], ['e'], ['e'], ['e']], [[5, 6], [1, 2], [5, 6], [5, 6], [5, 6]]], [[['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['baz', 'qux'], ['foo', 'bbar'], ['baz', 'qux'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar']]], [['y', True, True, True], [2, 'z', 'z', 'z']], [[['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['baz', 'qux'], ['foo', 'bbar'], ['baz', 'qux'], ['foo', 'bbar'], ['foo', 'bbar']], [['foo', 'bbar'], ['foo', 'bbar'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar'], ['python', 'programming'], ['foo', 'bbar'], ['foo', 'bbar']]], [[['a', 'b'], ['e', 'f'], ['a', 'b']], [[1, 2], [5, 6], [1, 2]]], [[['a', 'b'], ['a', 'b'], ['d'], ['e', 'f'], ['a', 'b'], ['a', 'b'], ['a', 'b']], [[1, 6, 2], [1, 6, 2], [3, 4], [5, 6], [1, 6, 2], [1, 6, 2], [1, 6, 2]]], [['e', 'e', True, True, True], [2, 2, 'z', 'z', 'z']], [[['a', 'b', 'b'], ['c', 'd'], ['a', 'b', 'b'], ['e', 'f'], ['c', 'd']], [[1, 2], [3, 4], [1, 2], [5, 6], [3, 4]]], [[['e', ''], ['a', 'b', 'b'], ['a', 'b', 'b']], [[5, 6], [1, 2], [1, 2]]], [[[1, 2, 3]], [[4, 5, 6]]], [[['c', 'd'], ['c', 'd'], ['c', 'd']], [[3, 4], [3, 4], [3, 4]]], [[['a', 'b'], ['c', 'd'], ['c', 'd'], [5, 6], [5, 6], ['c', 'd'], ['c', 'd']], [[1, 2], [3, 4, 4, 4], [3, 4, 4, 4], ['e', 'f'], ['e', 'f'], [3, 4, 4, 4], [3, 4, 4, 4]]], [['yy'], [1]], [['y', 'y', 'y', 'y'], [8, 8, 8, 8]], [[['e'], ['a', 'b', 'b'], ['e'], ['e'], ['e']], [[5, 7], [1, 2], [5, 7], [5, 7], [5, 7]]], [[['a', 'b'], ['e', 'f']], [[1, 2], [5, 6]]]]

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
        func_name = "merge"
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
        for test_case in ["assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]", 'assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]', "assert merge([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]"]:
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