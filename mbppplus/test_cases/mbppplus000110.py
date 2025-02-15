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
inputs = [[[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]], [[1, 2, 3, 4, 5], [5, 6, 7, 8]], [['red', 'blue', 'green'], ['yellow']], [[1, 2, 3, 4], []], [[1, 2, 3], []], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12]], [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]], [[5], [1, 2, 3, 4, 5]], [[1, 3, 5, 7, 9, 11, 13, 15], [2, 4, 6, 8, 10, 12, 14, 16]], [[1, 2], [3, 4, 5]], [[10, 50, 100, 500, 1000], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 3, [5, [7, [9], 10]], [2, [4, [6, [8]]]]], [[11, [13, [15]]], [12, [14, [16]]]]], [[1, [2, [3, [4, [5]]]]], [[6, [7, [8]]], [9, [10, [11]]]]], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13], [14, 15]]], [[1, 'two', True, 4.5], ['five', False, 6, 'seven']], [[{'1': 'one'}, [2, 'two'], {'three': 3}], [[4, 'four'], {'five': 5}]], [['red', 'blue', 'green'], [[]]], [[['apple', 1], ['banana', 2]], [None, ['cherry', 3]]], [[1, 'two', True, 4.5, True], ['five', False, 6, 'seven']], [[10, 50, 100, 500, 1000], [1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12]], [[1, 3, 5, 7, 9], [4, 6, 8]], [[1, 'two', True, 4.5], ['five', False, 6, 'cherryfive', 'seven']], [[1, 2, 3, 4], [-9, 1, 6, 91, 9, 56]], [[10, 50, 1000], [10, 50, 1000]], [[1, 3, 5, 7, 9], [1, 3, 5, 7, 9]], [[2, 4, 6, 8, 10, 12, 14, 16, 10], [2, 4, 6, 8, 10, 12, 14, 16, 10]], [[1, 3, 5, 7, 9, 7], [1, 3, 5, 7, 9, 7]], [[3, 4, 5, 3], [3, 4, 5, 3]], [[{'three': 3}, {'three': 3}], [{'three': 3}, {'three': 3}]], [[3, 4], [3, 4]], [[{'1': 'one'}, [2, 'two'], {'three': 3}], [{'five': 5, 'fifve': 14}, [4, 'four'], {'five': 5, 'fifve': 14}]], [[3, 5, 7, 9], [3, 5, 7, 9]], [[2, 4, 6, 8, 10, 12, 14, 11], [2, 4, 6, 8, 10, 12, 14, 11]], [[10, 999], [10, 999]], [[{'five': 5, 'red': 9}, [4, 'four'], {'five': 5, 'red': 9}], [{'1': 'one'}, [2, 'two'], {'three': 3}]], [[3, 5, 2, 7, 4, 9], [3, 5, 2, 7, 4, 9]], [[-9, 1, 6, 91, 9, 56], [-9, 1, 6, 91, 9, 56]], [[1, 3, 5, 7, 9, 9, 9, 3], [1, 3, 5, 7, 9, 9, 9, 3]], [[['apple', 1], ['banana', 2]], [['cherry', 3]]], [[2, 4, 6, 8, 10, 12, 11, 8], [2, 4, 6, 8, 10, 12, 11, 8]], [[3, 1, 5, 2, 7, 4, 9], [3, 1, 5, 2, 7, 4, 9]], [[3, 4, 3], [3, 4, 3]], [[1, 3, 5, 7, 9], [4, 5, 8]], [[4, 6, 9, 8], [4, 6, 9, 8]], [[10, 50, 1000, 10], [10, 50, 1000, 10]], [[{'1': 'one'}, [2, 'two'], {'three': 3}], [[4, 'four']]], [[0, 1, 2, 3], [4, False, 'vBHB', -94, 46.84204088708893, False, 80.50554519978891, 59]], [[[False, False]], [[False, False]]], [[10, 50, 2, 100, 500, 1000], [1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12]], [[{'1': 'one'}, [2, 'two'], {'three': 3}], [{'1': 'one'}, [2, 'two'], {'three': 3}]], [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]], [[{'five': 5, 'red': 9}, [4, 'four'], {'five': 5, 'red': 9}], [{'five': 5, 'red': 9}, [4, 'four'], {'five': 5, 'red': 9}]], [[1, 3, 5, 7, 9], [9, 4, 6, 8]], [[{'three': 10}, {'three': 10}], [{'three': 10}, {'three': 10}]], [[2, 4, 6, 8, 10, 12, 14], [1, 3, 14, 5, 7, 9, 11, 13, 15]], [[1, False, True, 4.5, True], [1, False, True, 4.5, True]], [[10, 1000, 10, 10], [10, 1000, 10, 10]], [[499, 10, 50, 100, 500, 1000], [499, 10, 50, 100, 500, 1000]], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]], [[7, 2, 4, 6, 8, 10, 12, 14], [1, 3, 14, 5, 7, 9, 11, 13, 15]], [[{'1': 'one'}, [2, 'two'], {}], [[4, 'four'], {}]], [[1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12], [1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12]], [[10, 999, 998, 999], [10, 999, 998, 999]], [[{'1': 'one'}, [2, 'two'], {'three': 3}], [{'five': 5, 'fifve': 14}, [4, 'four'], {'five': 5, 'fifve': 14}, [4, 'four']]], [[4, False, 'vBHB', -94, 46.84204088708893, False, 80.50554519978891, 59], [4, False, 'vBHB', -94, 46.84204088708893, False, 80.50554519978891, 59]], [[499, 9, 50, 51, 100, 500, 1000, 50], [499, 9, 50, 51, 100, 500, 1000, 50]], [[4], [4]], [[4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 59, 4, 80.50554519978891], [4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 59, 4, 80.50554519978891]], [[4, False, 'cherryfive', 46.84204088708893, False, 80.50554519978891, 59], [4, False, 'cherryfive', 46.84204088708893, False, 80.50554519978891, 59]], [[10, 1000, 10], [10, 1000, 10]], [[1, 2, 3, 16, 4, 5, 6, 7, 8, 9], [1, 2, 3, 16, 4, 5, 6, 7, 8, 9]], [[4, 6, 10, 8], [4, 6, 10, 8]], [[[3, 2, 'two'], {'1': 'one'}, [3, 2, 'two'], {'three': 3}], [[3, 2, 'two'], {'1': 'one'}, [3, 2, 'two'], {'three': 3}]], [[51, 3, 5, 7, 9, 11, 13, 15], [2, 4, 6, 8, 10, 12, 14, 16]], [[2, 4, 6, 8, 10, 12, 14, 11, 6], [2, 4, 6, 8, 10, 12, 14, 11, 6]], [[4, 4.5, False, 'vBHB', -94, 46.84204088708893, True, 80.50554519978891, 59], [4, 4.5, False, 'vBHB', -94, 46.84204088708893, True, 80.50554519978891, 59]], [[4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891], [4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891]], [[1, 3, 6, 5, 7, 9, 11, 13, 15], [2, 4, 6, 8, 10, 12, 14, 16]], [[4, 6, 8, 10, 14, 11], [4, 6, 8, 10, 14, 11]], [[3, 14, 5, 2, 7, 4, 9], [3, 14, 5, 2, 7, 4, 9]], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[15], [11, 12, 13], [15]]], [[10, 9, 1000, 10], [10, 9, 1000, 10]], [[10, 50, 1000, 9, 10], [10, 50, 1000, 9, 10]], [[499, 999, 10, 100, 500, 1000], [499, 999, 10, 100, 500, 1000]], [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[15, 11, 12, 60], [15, 11, 12, 60], [14, 15]]], [[1, [[3, [4, [3], [3]], [4, [3], [3]]], 2, [3, [4, [3], [3]], [4, [3], [3]]]]], [1, [[3, [4, [3], [3]], [4, [3], [3]]], 2, [3, [4, [3], [3]], [4, [3], [3]]]]]], [[4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB'], [4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB']], [[{'three': 9}, {'three': 9}], [{'three': 9}, {'three': 9}]], [[4, 6, 4, 8], [4, 6, 4, 8]], [[-9, 1, 6, 91, 9, 56, 1], [-9, 1, 6, 91, 9, 56, 1]], [[5, 5], [1, 2, 3, 4, 5]], [[2, 4, 6, 50, 7, 10, 12, 14, 11, 6], [2, 4, 6, 50, 7, 10, 12, 14, 11, 6]], [[499, 10, 100, 500, 1000], [499, 10, 100, 500, 1000]], [[{'three': 3, 't': 499}, {'three': 3, 't': 499}], [{'three': 3, 't': 499}, {'three': 3, 't': 499}]], [[4, False, 'vBHB', -94, True, 46.84204088708893, False, 16, False, 80.50554519978891, 59, 'vBHB'], [4, False, 'vBHB', -94, True, 46.84204088708893, False, 16, False, 80.50554519978891, 59, 'vBHB']], [[1, 3, 5, 7, 9, 11, 13, 15], [1, 3, 5, 7, 9, 11, 13, 15]], [[10, 50, 100, 500, 1000], [10, 50, 100, 500, 1000]], [[2, 4, 6, 13, 7, 10, 12, 13, 14, 11, 6, 6], [2, 4, 6, 13, 7, 10, 12, 13, 14, 11, 6, 6]], [[3, 6, 5, 15, 9, 11, 13, 15], [3, 6, 5, 15, 9, 11, 13, 15]], [[4, 4], [4, 4]], [[4, 'vBvHB', -94, 80.4210480089324, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891, 4], [4, 'vBvHB', -94, 80.4210480089324, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891, 4]], [[1, 2, 3, 4, 5, 6, 14, 8, 9, 12, 14], [1, 2, 3, 4, 5, 6, 14, 8, 9, 12, 14]], [[499, 10, 100, 100, 1000, 499], [499, 10, 100, 100, 1000, 499]], [[1, 'two', True, 4.5, True], [1, 'two', True, 4.5, True]], [[1, 3, 14, 5, 7, 9, 11, 13, 15, 9], [1, 3, 14, 5, 7, 9, 11, 13, 15, 9]], [[4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB', 59, 'vBHB'], [4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB', 59, 'vBHB']], [[{}, {}], [{}, {}]], [[1, 3, 14, 5, 7, 9, 11, 15], [1, 3, 14, 5, 7, 9, 11, 15]], [[1, 2, 3, 4], [-9, 1, 6, 91, 9, 56, 56]], [[56, 4], [56, 4]], [[2, 4, 6, 8, 10, 12, 14, 16, 60, 10, 10], [2, 4, 6, 8, 10, 12, 14, 16, 60, 10, 10]], [['Mhrbldw', None, 29.04635642164004, 'two', ['vBvHB', 'red', 'banana', 'fzAKPhIsu'], 4.5, False, 17, 'cdL'], []], [[[[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [9, [10, [11]]]], [[[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [9, [10, [11]]]]], [[4, 10, 1, 3, 5, 7, 9], [4, 10, 1, 3, 5, 7, 9]], [[1, 3, 14, 5, 7, 9, 13, 15, 9], [1, 3, 14, 5, 7, 9, 13, 15, 9]], [[4, 6, 8, 10, 14, 11, 8], [4, 6, 8, 10, 14, 11, 8]], [[2, 4, 8, 10, 12, 14, 16], [2, 4, 8, 10, 12, 14, 16]], [[{'1': 'one'}, [2, 'two'], {'three': 3}], [{'five': 5, 'fifve': 14, 'fivfe': 5}, [4, 'four'], {'five': 5, 'fifve': 14, 'fivfe': 5}, [4, 'four']]]]
results = [[1, 3, 5, 7, 9, 2, 4, 6, 8], [1, 2, 3, 4, 5, 6, 7, 8], ['red', 'blue', 'yellow'], [1, 2, 3], [1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], [1, 3, 5, 7, 2, 4, 6, 8, 10], [1, 2, 3, 4, 5], [1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 14, 16], [1, 3, 4, 5], [10, 50, 100, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, [5, [7, [9], 10]], [11, [13, [15]]], [12, [14, [16]]]], [1, [6, [7, [8]]], [9, [10, [11]]]], [[1, 2, 3, 4, 5], [11, 12, 13], [14, 15]], [1, 'two', True, 'five', False, 6, 'seven'], [{'1': 'one'}, [2, 'two'], [4, 'four'], {'five': 5}], ['red', 'blue', []], [['apple', 1], None, ['cherry', 3]], [1, 'two', True, 4.5, 'five', False, 6, 'seven'], [10, 50, 100, 500, 1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12], [1, 3, 5, 7, 4, 6, 8], [1, 'two', True, 'five', False, 6, 'cherryfive', 'seven'], [1, 2, 3, -9, 1, 6, 91, 9, 56], [10, 50, 10, 50, 1000], [1, 3, 5, 7, 1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14, 16, 2, 4, 6, 8, 10, 12, 14, 16, 10], [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 7], [3, 4, 5, 3, 4, 5, 3], [{'three': 3}, {'three': 3}, {'three': 3}], [3, 3, 4], [{'1': 'one'}, [2, 'two'], {'five': 5, 'fifve': 14}, [4, 'four'], {'five': 5, 'fifve': 14}], [3, 5, 7, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12, 14, 2, 4, 6, 8, 10, 12, 14, 11], [10, 10, 999], [{'five': 5, 'red': 9}, [4, 'four'], {'1': 'one'}, [2, 'two'], {'three': 3}], [3, 5, 2, 7, 4, 3, 5, 2, 7, 4, 9], [-9, 1, 6, 91, 9, -9, 1, 6, 91, 9, 56], [1, 3, 5, 7, 9, 9, 9, 1, 3, 5, 7, 9, 9, 9, 3], [['apple', 1], ['cherry', 3]], [2, 4, 6, 8, 10, 12, 11, 2, 4, 6, 8, 10, 12, 11, 8], [3, 1, 5, 2, 7, 4, 3, 1, 5, 2, 7, 4, 9], [3, 4, 3, 4, 3], [1, 3, 5, 7, 4, 5, 8], [4, 6, 9, 4, 6, 9, 8], [10, 50, 1000, 10, 50, 1000, 10], [{'1': 'one'}, [2, 'two'], [4, 'four']], [0, 1, 2, 4, False, 'vBHB', -94, 46.84204088708893, False, 80.50554519978891, 59], [[False, False]], [10, 50, 2, 100, 500, 1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12], [{'1': 'one'}, [2, 'two'], {'1': 'one'}, [2, 'two'], {'three': 3}], [2, 4, 6, 8, 1, 3, 5, 7, 9], [{'five': 5, 'red': 9}, [4, 'four'], {'five': 5, 'red': 9}, [4, 'four'], {'five': 5, 'red': 9}], [1, 3, 5, 7, 9, 4, 6, 8], [{'three': 10}, {'three': 10}, {'three': 10}], [2, 4, 6, 8, 10, 12, 1, 3, 14, 5, 7, 9, 11, 13, 15], [1, False, True, 4.5, 1, False, True, 4.5, True], [10, 1000, 10, 10, 1000, 10, 10], [499, 10, 50, 100, 500, 499, 10, 50, 100, 500, 1000], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [7, 2, 4, 6, 8, 10, 12, 1, 3, 14, 5, 7, 9, 11, 13, 15], [{'1': 'one'}, [2, 'two'], [4, 'four'], {}], [1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 1, 2, 3, 4, 5, 6, 7, 12, 8, 9, 12], [10, 999, 998, 10, 999, 998, 999], [{'1': 'one'}, [2, 'two'], {'five': 5, 'fifve': 14}, [4, 'four'], {'five': 5, 'fifve': 14}, [4, 'four']], [4, False, 'vBHB', -94, 46.84204088708893, False, 80.50554519978891, 4, False, 'vBHB', -94, 46.84204088708893, False, 80.50554519978891, 59], [499, 9, 50, 51, 100, 500, 1000, 499, 9, 50, 51, 100, 500, 1000, 50], [4], [4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 59, 4, 4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 59, 4, 80.50554519978891], [4, False, 'cherryfive', 46.84204088708893, False, 80.50554519978891, 4, False, 'cherryfive', 46.84204088708893, False, 80.50554519978891, 59], [10, 1000, 10, 1000, 10], [1, 2, 3, 16, 4, 5, 6, 7, 8, 1, 2, 3, 16, 4, 5, 6, 7, 8, 9], [4, 6, 10, 4, 6, 10, 8], [[3, 2, 'two'], {'1': 'one'}, [3, 2, 'two'], [3, 2, 'two'], {'1': 'one'}, [3, 2, 'two'], {'three': 3}], [51, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 14, 16], [2, 4, 6, 8, 10, 12, 14, 11, 2, 4, 6, 8, 10, 12, 14, 11, 6], [4, 4.5, False, 'vBHB', -94, 46.84204088708893, True, 80.50554519978891, 4, 4.5, False, 'vBHB', -94, 46.84204088708893, True, 80.50554519978891, 59], [4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 60, 4, 4, False, 'vBvHB', -94, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891], [1, 3, 6, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10, 12, 14, 16], [4, 6, 8, 10, 14, 4, 6, 8, 10, 14, 11], [3, 14, 5, 2, 7, 4, 3, 14, 5, 2, 7, 4, 9], [[1, 2, 3, 4, 5], [15], [11, 12, 13], [15]], [10, 9, 1000, 10, 9, 1000, 10], [10, 50, 1000, 9, 10, 50, 1000, 9, 10], [499, 999, 10, 100, 500, 499, 999, 10, 100, 500, 1000], [[1, 2, 3, 4, 5], [15, 11, 12, 60], [15, 11, 12, 60], [14, 15]], [1, 1, [[3, [4, [3], [3]], [4, [3], [3]]], 2, [3, [4, [3], [3]], [4, [3], [3]]]]], [4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB'], [{'three': 9}, {'three': 9}, {'three': 9}], [4, 6, 4, 4, 6, 4, 8], [-9, 1, 6, 91, 9, 56, -9, 1, 6, 91, 9, 56, 1], [5, 1, 2, 3, 4, 5], [2, 4, 6, 50, 7, 10, 12, 14, 11, 2, 4, 6, 50, 7, 10, 12, 14, 11, 6], [499, 10, 100, 500, 499, 10, 100, 500, 1000], [{'three': 3, 't': 499}, {'three': 3, 't': 499}, {'three': 3, 't': 499}], [4, False, 'vBHB', -94, True, 46.84204088708893, False, 16, False, 80.50554519978891, 59, 4, False, 'vBHB', -94, True, 46.84204088708893, False, 16, False, 80.50554519978891, 59, 'vBHB'], [1, 3, 5, 7, 9, 11, 13, 1, 3, 5, 7, 9, 11, 13, 15], [10, 50, 100, 500, 10, 50, 100, 500, 1000], [2, 4, 6, 13, 7, 10, 12, 13, 14, 11, 6, 2, 4, 6, 13, 7, 10, 12, 13, 14, 11, 6, 6], [3, 6, 5, 15, 9, 11, 13, 3, 6, 5, 15, 9, 11, 13, 15], [4, 4, 4], [4, 'vBvHB', -94, 80.4210480089324, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891, 4, 'vBvHB', -94, 80.4210480089324, 46.84204088708893, False, 80.50554519978891, 60, 4, 80.50554519978891, 4], [1, 2, 3, 4, 5, 6, 14, 8, 9, 12, 1, 2, 3, 4, 5, 6, 14, 8, 9, 12, 14], [499, 10, 100, 100, 1000, 499, 10, 100, 100, 1000, 499], [1, 'two', True, 4.5, 1, 'two', True, 4.5, True], [1, 3, 14, 5, 7, 9, 11, 13, 15, 1, 3, 14, 5, 7, 9, 11, 13, 15, 9], [4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB', 59, 4, False, 'vBHB', -94, 46.84204088708893, False, 16, 80.50554519978891, 59, 'vBHB', 59, 'vBHB'], [{}, {}, {}], [1, 3, 14, 5, 7, 9, 11, 1, 3, 14, 5, 7, 9, 11, 15], [1, 2, 3, -9, 1, 6, 91, 9, 56, 56], [56, 56, 4], [2, 4, 6, 8, 10, 12, 14, 16, 60, 10, 2, 4, 6, 8, 10, 12, 14, 16, 60, 10, 10], ['Mhrbldw', None, 29.04635642164004, 'two', ['vBvHB', 'red', 'banana', 'fzAKPhIsu'], 4.5, False, 17], [[[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [[[8, 8], 7, [8, 8]], 5, [[8, 8], 7, [8, 8]]], [9, [10, [11]]]], [4, 10, 1, 3, 5, 7, 4, 10, 1, 3, 5, 7, 9], [1, 3, 14, 5, 7, 9, 13, 15, 1, 3, 14, 5, 7, 9, 13, 15, 9], [4, 6, 8, 10, 14, 11, 4, 6, 8, 10, 14, 11, 8], [2, 4, 8, 10, 12, 14, 2, 4, 8, 10, 12, 14, 16], [{'1': 'one'}, [2, 'two'], {'five': 5, 'fifve': 14, 'fivfe': 5}, [4, 'four'], {'five': 5, 'fifve': 14, 'fivfe': 5}, [4, 'four']]]

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
        func_name = "replace_list"
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
        for test_case in ['assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]', 'assert replace_list([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]', 'assert replace_list(["red","blue","green"],["yellow"])==["red","blue","yellow"]']:
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
