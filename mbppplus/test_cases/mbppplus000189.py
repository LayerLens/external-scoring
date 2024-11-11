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
inputs = [[[[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1], [[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'A'], [[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'E'], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']], 'A'], [[], 'A'], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']], 'G'], [[['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H'], ['I', 'J', 'K', 'L']], 'F'], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], 'L'], [[['A', 'B', 'C'], ['D', 'E'], ['F', 'G', 'H', 'I', 'J']], 'K'], [[['A', 'B', 'C', 'D'], ['E', 'F'], ['G', 'H', 'I', 'J'], ['K'], ['L', 'M', 'N']], 'D'], [[['A', 'B'], ['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J']], 'I'], [[['A', 'B'], ['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J']], 'J'], [[['A', 'B'], ['C', 'D'], ['F', 'G', 'H', 'IB', 'J'], ['E'], ['F', 'G', 'H', 'IB', 'J']], 'J'], [[['A', 'B', 'C', 'D'], ['E', 'F'], ['G', 'H', 'I', 'J'], ['K']], ''], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']], 'GG'], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H']], 'GG'], [[['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J']], 'J'], [[['A', 'B', 'C', 'D'], ['E', 'F'], ['G', 'H', 'I', 'J'], ['K']], 'IB'], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H'], ['H']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['H'], ['H']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']], ''], [[['A', 'B'], ['D'], ['E', 'F'], ['G', 'H'], ['A', 'B']], 'A'], [[['A', 'B', 'C', 'D'], ['G', 'H', 'I', 'J'], ['K']], 'E'], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], 'LL'], [[['B'], ['C', 'D'], ['B'], ['E', 'F'], ['G', 'H']], 'GG'], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H']], 'C'], [[['BB', 'A', 'B'], ['C', 'D'], ['F', 'G', 'H', 'IB', 'J'], ['E'], ['F', 'G', 'H', 'IB', 'J']], 'J'], [[['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H'], ['I', 'J', 'K', 'L']], 'I'], [[['A', 'B', 'C', 'D', 'E'], ['F', 'G', '', 'H'], ['F', 'G', '', 'H'], ['I', 'J', 'K', 'L']], [['A', 'B', 'C', 'D', 'E'], ['F', 'G', '', 'H'], ['F', 'G', '', 'H'], ['I', 'J', 'K', 'L']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H']], ''], [[['A'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], 'L'], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], [['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']]], [[['D'], ['E'], ['D'], ['F', 'G', 'H', 'I', 'J']], [['D'], ['E'], ['D'], ['F', 'G', 'H', 'I', 'J']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['H']]], [[['A', 'B'], ['LLF', 'C', 'D'], ['E', 'F'], ['H', 'H']], [['A', 'B'], ['LLF', 'C', 'D'], ['E', 'F'], ['H', 'H']]], [[['A', 'B', 'C', 'D', 'E'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['I', 'J', 'K', 'L']], [['A', 'B', 'C', 'D', 'E'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['I', 'J', 'K', 'L']]], [[['A', 'B'], ['LLF', 'C', 'D'], ['F'], ['F'], ['H', 'H']], [['A', 'B'], ['LLF', 'C', 'D'], ['F'], ['F'], ['H', 'H']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['G', 'H'], ['C', 'D']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['G', 'H'], ['C', 'D']]], [[['B'], ['C', 'D'], ['E', 'F'], ['G', 'H']], 'GG'], [[['C', 'D'], ['E', 'F'], ['H']], [['C', 'D'], ['E', 'F'], ['H']]], [[['A', 'B'], ['C', 'D'], ['G', 'H']], 'GG'], [[['A', 'B', 'C', 'D'], ['E', 'F'], ['G', 'H', 'I', 'J'], ['K']], 'K'], [[['A', 'B'], ['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J']], 'H'], [[['A', 'B'], ['C', 'D'], ['E'], ['F', 'IB', 'H', 'I', 'J']], 'H'], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M'], ['B', 'C', 'D']], 'L'], [[['D'], ['E']], [['D'], ['E']]], [[['B'], ['G', 'IBH'], ['C', 'D'], ['B'], ['E', 'F'], ['G', 'IBH']], [['B'], ['G', 'IBH'], ['C', 'D'], ['B'], ['E', 'F'], ['G', 'IBH']]], [[['A', 'B'], ['E', 'F'], ['H', 'H']], [['A', 'B'], ['E', 'F'], ['H', 'H']]], [[['A', 'B'], ['C', 'D', 'D'], ['E', 'F'], ['G', 'H']], [['A', 'B'], ['C', 'D', 'D'], ['E', 'F'], ['G', 'H']]], [[['A', 'B'], ['H', 'H', 'H'], ['E', 'F'], ['H', 'H', 'H']], [['A', 'B'], ['H', 'H', 'H'], ['E', 'F'], ['H', 'H', 'H']]], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M'], ['B', 'C', 'D']], 'LL'], [[['A', 'B'], ['LLF', 'C', 'D'], ['F'], ['H', 'H']], [['A', 'B'], ['LLF', 'C', 'D'], ['F'], ['H', 'H']]], [[['DD', 'DD'], ['E'], ['DD', 'DD'], ['DD', 'DD'], ['F', 'G', 'H', 'I', 'J'], ['DD', 'DD']], [['DD', 'DD'], ['E'], ['DD', 'DD'], ['DD', 'DD'], ['F', 'G', 'H', 'I', 'J'], ['DD', 'DD']]], [[['A', 'B', 'C', 'D'], ['G', 'H', 'I', 'J'], ['K'], ['A', 'B', 'C', 'D']], [['A', 'B', 'C', 'D'], ['G', 'H', 'I', 'J'], ['K'], ['A', 'B', 'C', 'D']]], [[['D'], []], [['D'], []]], [[['A', 'IBH', 'B', 'C', 'D', 'E'], ['F', 'G', 'H'], ['A', 'IBH', 'B', 'C', 'D', 'E'], ['I', 'J', 'K', 'L']], 'I'], [[['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'DH'], ['I', 'J', 'K', 'L']], 'F'], [[['DD', 'DD'], ['E'], ['DD', 'DD'], ['DD', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'DD']], [['DD', 'DD'], ['E'], ['DD', 'DD'], ['DD', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'DD']]], [[['A', 'IBH', 'B', 'C', 'D', 'E'], ['F', 'G', 'H'], ['I', 'LL', 'J', 'K', 'L'], ['A', 'IBH', 'B', 'C', 'D', 'E'], ['I', 'LL', 'J', 'K', 'L']], 'I'], [[['DD', 'E', 'DD'], ['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD']], [['DD', 'E', 'DD'], ['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD']]], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['KK', 'K', 'L', 'M']], 'L'], [[['A', 'B'], ['C', 'D', 'D'], ['F'], ['GG', 'G', 'H'], ['GG', 'G', 'H'], ['GG', 'G', 'H']], [['A', 'B'], ['C', 'D', 'D'], ['F'], ['GG', 'G', 'H'], ['GG', 'G', 'H'], ['GG', 'G', 'H']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['G', 'H'], ['C', 'D'], ['E', 'F']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['G', 'H'], ['C', 'D'], ['E', 'F']]], [[['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J', 'F'], ['F', 'G', 'H', 'I', 'J', 'F']], [['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J', 'F'], ['F', 'G', 'H', 'I', 'J', 'F']]], [[['A', 'B', 'C', 'D'], ['KE'], ['KE'], ['A', 'B', 'C', 'D']], [['A', 'B', 'C', 'D'], ['KE'], ['KE'], ['A', 'B', 'C', 'D']]], [[['A', 'B', 'D'], ['G', 'H', 'I', 'J'], ['K'], ['A', 'B', 'D']], [['A', 'B', 'D'], ['G', 'H', 'I', 'J'], ['K'], ['A', 'B', 'D']]], [[['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD']], [['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD']]], [[['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD'], ['E']], [['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD'], ['E']]], [[['A', 'B'], ['E', 'EE', 'F'], ['H', 'H']], [['A', 'B'], ['E', 'EE', 'F'], ['H', 'H']]], [[['A', 'B', 'C', 'A'], ['D', 'E'], ['F', 'G', 'H', 'I', 'J']], 'K'], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['K', 'L', 'M', 'K']], [['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['K', 'L', 'M', 'K']]], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], ''], [[['D'], ['BB', 'A', 'B'], ['D'], ['F', 'G', 'H', 'IB', 'J'], ['E'], ['F', 'G', 'H', 'IB', 'J']], 'J'], [[['C', 'D', 'C'], ['A', 'B'], ['C', 'D', 'C'], ['E', 'F'], ['H'], ['C', 'D', 'C']], [['C', 'D', 'C'], ['A', 'B'], ['C', 'D', 'C'], ['E', 'F'], ['H'], ['C', 'D', 'C']]], [[['A', 'B'], ['C', 'D', 'D'], ['E', 'F'], ['G', 'H'], ['E', 'F']], [['A', 'B'], ['C', 'D', 'D'], ['E', 'F'], ['G', 'H'], ['E', 'F']]], [[['A', 'B'], ['E', 'F'], ['H', 'H', 'H']], [['A', 'B'], ['E', 'F'], ['H', 'H', 'H']]], [[['AI', 'A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['AI', 'A', 'B', 'C', 'D', 'E']], [['AI', 'A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['AI', 'A', 'B', 'C', 'D', 'E']]], [[['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD'], ['E']], [['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD'], ['E']]], [[['A', 'B'], ['E']], 'I'], [[['A', 'B', 'C', 'D', 'E'], ['F', 'G', '', 'N'], ['F', 'G', '', 'N'], ['F', 'G', '', 'N'], ['I', 'J', 'K', 'L']], [['A', 'B', 'C', 'D', 'E'], ['F', 'G', '', 'N'], ['F', 'G', '', 'N'], ['F', 'G', '', 'N'], ['I', 'J', 'K', 'L']]], [[['A', 'B'], ['D'], ['E', 'F'], ['G', 'H'], ['A', 'B']], [['A', 'B'], ['D'], ['E', 'F'], ['G', 'H'], ['A', 'B']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['E', 'F']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['E', 'F']]], [[['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J'], ['F', 'G', 'H', 'I', 'J']], 'DDJ'], [[['C', 'F'], ['A', 'B'], ['C', 'F'], ['H', 'H', 'H']], [['C', 'F'], ['A', 'B'], ['C', 'F'], ['H', 'H', 'H']]], [[['A', 'B'], ['E', 'GGF'], ['C', 'D'], ['E', 'GGF'], ['H']], [['A', 'B'], ['E', 'GGF'], ['C', 'D'], ['E', 'GGF'], ['H']]], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], 'BB'], [[['A'], ['E', 'F', 'G', 'H'], ['K', 'L', 'M', 'K']], [['A'], ['E', 'F', 'G', 'H'], ['K', 'L', 'M', 'K']]], [[['A', 'B', 'C', 'D'], ['E', 'F'], ['G', 'H', 'I', 'J'], ['K']], [['A', 'B', 'C', 'D'], ['E', 'F'], ['G', 'H', 'I', 'J'], ['K']]], [[['H', 'H', 'H'], ['E', 'F']], [['H', 'H', 'H'], ['E', 'F']]], [[['BB', 'A', 'B'], ['C', 'D'], ['F', 'G', '', 'H', 'IB', 'J'], ['F', 'G', '', 'H', 'IB', 'J'], ['E'], ['F', 'G', '', 'H', 'IB', 'J']], [['BB', 'A', 'B'], ['C', 'D'], ['F', 'G', '', 'H', 'IB', 'J'], ['F', 'G', '', 'H', 'IB', 'J'], ['E'], ['F', 'G', '', 'H', 'IB', 'J']]], [[['A', 'B', 'C', 'D', 'E'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['I', 'J', 'K', 'L'], ['F', 'FF', '', 'H']], [['A', 'B', 'C', 'D', 'E'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['F', 'FF', '', 'H'], ['I', 'J', 'K', 'L'], ['F', 'FF', '', 'H']]], [[['I', 'J', 'K', 'L', 'K'], ['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'DH'], ['I', 'J', 'K', 'L', 'K']], [['I', 'J', 'K', 'L', 'K'], ['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'DH'], ['I', 'J', 'K', 'L', 'K']]], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M'], ['K', 'L', 'M']], [['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M'], ['K', 'L', 'M']]], [[['A', 'B', 'C', 'A'], ['D', 'E'], ['F', 'G', 'H', 'I', 'J'], ['F', 'G', 'H', 'I', 'J']], 'AA'], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H'], ['H'], ['E', 'F']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['H'], ['H'], ['E', 'F']]], [[['AI', 'A', 'B', 'C', 'D', 'BB', 'E'], ['F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['AI', 'A', 'B', 'C', 'D', 'BB', 'E']], [['AI', 'A', 'B', 'C', 'D', 'BB', 'E'], ['F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['AI', 'A', 'B', 'C', 'D', 'BB', 'E']]], [[['A', 'B'], ['C', 'D']], 'GG'], [[['A'], ['E', 'F', 'G', 'GG', 'H'], ['I', 'J'], ['E', 'F', 'G', 'GG', 'H'], ['K', 'L', 'M']], [['A'], ['E', 'F', 'G', 'GG', 'H'], ['I', 'J'], ['E', 'F', 'G', 'GG', 'H'], ['K', 'L', 'M']]], [[['A', 'B'], [], ['C', 'D'], ['F', 'G', 'H', 'I', 'J']], [['A', 'B'], [], ['C', 'D'], ['F', 'G', 'H', 'I', 'J']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['H']], 'IBH'], [[['F', 'G', 'H'], ['A', 'IBH', 'B', 'C', 'D', 'E']], [['F', 'G', 'H'], ['A', 'IBH', 'B', 'C', 'D', 'E']]], [[['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['G', 'H'], ['E', 'F'], ['C', 'D'], ['C', 'D']], [['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H'], ['G', 'H'], ['E', 'F'], ['C', 'D'], ['C', 'D']]], [[['A', 'B', 'C', 'BB'], ['KE'], ['KE'], ['A', 'B', 'C', 'BB']], [['A', 'B', 'C', 'BB'], ['KE'], ['KE'], ['A', 'B', 'C', 'BB']]], [[['B'], ['B'], ['C', 'D'], ['E'], ['F', 'G', 'H', 'I', 'J'], ['B']], 'J'], [[['B', 'C', 'D'], ['E', 'N', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], [['B', 'C', 'D'], ['E', 'N', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']]], [[['A'], ['I', 'J'], ['K', 'L', 'M']], [['A'], ['I', 'J'], ['K', 'L', 'M']]], [[['E', 'EE', 'F'], ['H', 'H'], ['H', 'H']], [['E', 'EE', 'F'], ['H', 'H'], ['H', 'H']]], [[['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD']], [['E'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD'], ['GG', 'F', 'G', 'H', 'I', 'J'], ['DD', 'E', 'DD'], ['DD', 'E', 'DD']]], [[['A', 'B'], [False, True], ['C', 'D'], ['F', 'G', 'H', 'I', 'J']], [['A', 'B'], [False, True], ['C', 'D'], ['F', 'G', 'H', 'I', 'J']]], [[['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M'], ['E', 'F', 'G', 'H']], [['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M'], ['E', 'F', 'G', 'H']]], [[['A'], ['B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J'], ['K', 'L', 'M']], 'EKE'], [[['D'], ['AE'], ['AE'], ['AE']], [['D'], ['AE'], ['AE'], ['AE']]]]
results = [3, 3, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

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
        func_name = "count_element_in_list"
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
        for test_case in ['assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3', "assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'A')==3", "assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']],'E')==1"]:
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
