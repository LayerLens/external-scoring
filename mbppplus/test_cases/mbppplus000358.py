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
inputs = [['ac'], ['dc'], ['abbbba'], ['caacabbbba'], [''], ['gHZZiSWmTL'], ['gHZZiSWmgHZZiSWmTLL'], ['gHZZiSWmgHZZiSWgmTLL'], ['gHZgHZZiSWmgHZZiSWmTLLZSWmTL'], ['gHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLL'], ['gHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLL'], ['gHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWm'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['gHZgHZgHZZiSWmTLZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['ggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTL'], ['gHZZigHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTLSWmgHZZiSWmTLL'], ['gHZZiSWmgHZZiSWmTgHZZimgHZZiSWgmTLLLL'], ['gHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWm'], ['gHZZiSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLL'], ['gZHZgHZZiSWmgHZZiSWmTLLZSWmTL'], ['gZHZgHZZiSWmgHZZigHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSWmTL'], ['gZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTL'], ['gHZgHZZiSWmgHZZiSWTLLZSWmTL'], ['gHZgHZgHZZiSWmTLZiSWmgggHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmHZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['gHZgHZgHZZiSWmTLZiSWmgggHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLgZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLHZZiSWmTLLZSWmTL'], ['gHZgHZZiSWgZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZSZiSWmTLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLgHZZiSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTL'], ['gHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTL'], ['gHZZiSWmgHZZiSWmTgHZZimgHZgHZZiSWmgHZZgHZZiSWmgHZZiSWmTLLiSWmTgHZZiSWmgHZZiSWgmTLLLLZiSWgmTLLLL'], ['gHZZiSWmgHZgHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmZiSWmTLL'], ['gHZZiSWmggHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLL'], ['gHZgHZgHZZgHZZiSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLLiSWmTLZiSWmgggHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['gHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZigSWm'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWiSWmTL'], ['gHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTmLL'], ['AyLkNrPEwE'], ['wah'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTLZiSWmTLgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSgHZZiSWmgHZZiSWgmTLLTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmLZSWmTL'], ['gZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWLgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTL'], ['gHZgHZZiSWmgHZZiSWTgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTLSWmTL'], ['ggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZgHZZiSWmgHZgHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmZiSWmTLLZiSWgmTLL'], ['gHZZiSWmgHZZiSWmgHZZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLHZZiSWm'], ['gHZgHZWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWgmTLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWWSgmTLWLHZZiSWmTLLZSWmTL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWgZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTLWmgHZZiSWgmTLLWmTLSWTLLZSWmTLZiSWmTLgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTLZiSWmTLgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZgHZgHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLZiSWmgHZZiSWTLLZSHWmTL'], ['gHZZiSWmgHZZiSWimTLL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTgHZZiSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLLHZZiSWmTLZSWmTL'], ['gZHZgHZZiSWmgHZZigHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSTL'], ['gHZgHZgHZZiSgHZZiSWmgHZgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLZiSWgmTLLWmgHZZiSWgmTLLZiSWmgHZZiSWTLLZSHWmTL'], ['gHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmggHZZiSWgmTLLLLHZZiSgHZZigHZZiSWmgHZgHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmZiSWmTLLSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmLZSWmTgZHZgHZZiSWmgHZZigHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSTLL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLgHZZiSWmTLSWTLLZSWmTLZiSWmTLgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZZigHZgHZZiSWmggHZZiSWmgHZHZiSWgmTLLHZZiSWmTLLZSWmTLWSWHZZiSWmTLL'], ['gHgZHZgHZZiSWmgHZZiSWmTLLZSWmTLZgHZgHZZgHZZiSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLLiSWmTLZiSWmgggHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['gHZZZiS'], ['gHZZiSWmgHZZiSWmgHZZgHZZiSWmggHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWiSWmTLgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLHZZiSWm'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLgZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWggmTLLWmgHZZiSWgmTLLWmTLHZZiSWmTLLZSWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWgmTgHZZiSWmggHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLLLHZZiSWmTLZSWmTL'], ['gHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSgHZZiSZWmgHZgHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmZiSWmTLLWgmTmLL'], ['gHZZigHZgHZZiSWmggHZZiSWmgHZHZiwahSWgmTLLHSZZiSWmTLLZSWmTLWSWHZZiSWmTLL'], ['gHZZigHZZiSWmgHZZiSWmTLLSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLL'], ['gHZgHZZiSWmgggHZgHZgHZZiSgHZZiSWmgHZgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLZiSWgmTLLWmgHZZiSWgmTLLZiSWmgHZZiSWTLLZSHWmTLHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTL'], ['gHZZiSWmgHZZiSgWgmTL'], ['gZHZgHZZiSWmgHZZigHZZiSWmgHZZiSWmgHZgHgHZgHZWmTLZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSWmTL'], ['gHZZiSWSmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWm'], ['gZHZgHZZiSgHZZiSWmgHZZiSWmTgHZZimgHZZiSWgmTLLLLWmgHZZigHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSWmTL'], ['gHZgHZZiSWmggWHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTL'], ['gHZZigHZZiSWmgHZZiSWmTLLSWmgHZZiSWmTLgHZZiSgHZgHZgHZZiSWmTLZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWgZHZgHZZiSWmgHZZigHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSTLmTLZSWmTLWmgHZZiSWgmTLLLL'], ['ggHZZiSWmgHZZiSWmTgHZZiSWmgWHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLL'], ['gHZZigHZgHZZiWSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTLSWmgHZZiSWmTLL'], ['gHZgHZgHZZiZZiSWmTLZSWmTL'], ['gHZgHZZiSWgZHZgHZZiSWmgHZZigHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmTLSWmTLLZSTLmggHZZiSWmgHZZiSWgmLZSWmTL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWgZHZgHZZiSWggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTLWmgHZZiSWgmTLLWmTLSWTLLZSWTmTLZiSWmTLgHZZiSWmgHZZiSWgmTLLgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZgHZLLZiSWmgHZZiSWTLLZSHWmTL'], ['gHZgHZZiSWmggHZZiSWmgHZgHZZiSWmggWHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSWmTLgHZZiSWgmLZSWmTL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLgHZgHZZigHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZigHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLLZSgHZZiSWmgHZZiSWgmTLLTLSWmTLLZSWmTL'], ['gHZZiSWmgHZZiSWgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLmTLL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmTLLWmTLSWTLLZSWmTLZiSWmTLgHZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLLL'], ['gHZZiSWmggHZgHZZiSWmggHZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTLHZZiSWmTLL'], ['gHZZiSWmgHZZiSWmgHZZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSgZHZgHZZiSWmgHZZiSWmTLLZSWmTLWmTLiSWmgHZZiSWgmTLiLHZZiSWm'], ['gHZgHZgHZZiSWmTLZiSWmgggHZZgHZZiSWmgHZZiSgWgmTLgHZZiSWgmTLWLHZZiSWmTLTLiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmHZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTL'], ['gHZZiSWmggHZgHZgHZZiSWgZHZgHZZiSWggHZmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLgHZgHZZigHZZiSWmgHZ'], ['gHgHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWmgHZZiSWmgHZZiSWmTLLSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLL'], ['gHZgHZZiSWmggWHZZiSWmgHZZiSWgmTLLHTZZiSWmTLLZSWmTL'], ['gHZgHZgHZZiSWmTLZiSWmgggHZZiSWmgHZZiSWmgHZgHZZiSWmgggHZZiSWmgHZZiSWmgHZZgHZZiSWmggHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWiSWmTLgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWmgHZZiSWgmTLiLHZZiSWmHZZiSWmgHZZiSWgmTLWLHZZiSWmTLLZSWmTLiSWZZiSWmgHSZZiSWgmTLLHZZiSWmTLZSWmTL'], ['ggHZZiSWmgHZZiSWmTgHZZiSWmgHZZiSWgmTLLLLHZZiSgHZZiSWmgHZZiSWgmTLLWmgHZZiSWgmmTLL'], ['gHZZiSWmgHZZgiSWmTgHZZiSWmgHZZiSWgmTLiLLLgHZZiSWmgHZZiSWm'], ['gHZZiSWmgHZZiSgWgmTgHZZigHZgHZZiSWmggHZZiSWmgHZHZiSWgmTLLHZZiSWmTLLZSWmTLWSWHZZiSWmTLLL'], ['gHZZiSWmgHZZiSWmgHZZgHZZiSWmggHZZiSWmgHZZiSWgmTLWLHZgHgZHZgHZZiSWmgHZZiSWmTLLZSWmTLZgHZgHZZgHZZiSWmgHZZiSWmTLgHZZiSWmgHZZiSWgmTLLLLiSWmTLZiSWmgggHZZiSWmgHZZiSWmgHZgHZZiSWmggHZZiSWmgHZZiSWgmgHZZiSWgmTLLHZZiSWmTLZSWmTLZiHSWmTLLZSgZHZgHZZiSWmgHZZiSWmTLLZSWmTLWmTLiSWmgHZZiSWgmTLiLHZZiSWm'], ['gHZZiSWTLLZSWmTL'], ['gHZgHZZiSWmggWHZZiSWmgHmZZiSWgmTLLHTZZiSWmTLLZSWmTL'], ['wahh'], ['gHZZiSWmggHZgHZZiSWmggHgZHZgHZZiSWmgHZZiSWmTLLZSWmTLZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTLHZZiSWmTLL'], ['gHZZiSWmggHZgHZZiSWmggHgZHZgHZZiSWmgHZZiSWmTLLZSWmTLZZiSWmgHZZiSWgmTLLHZZiSWmTLZSWmTgHZgHZgHZZiSgHZZiSWmgHZgHZgHZZiSWmggHZZiSWmgHZZiSWWgmTLWLHZZiSWmTLLZSWmTLZiSWgmTLLWmgHZZiSWgmTLLZiSWmgHZZiSWTLLZSHWmTLLHZZiSWmTLL']]
results = [False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

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
        func_name = "text_match_three"
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
        for test_case in ['assert not text_match_three("ac")', 'assert not text_match_three("dc")', 'assert text_match_three("abbbba")', 'assert text_match_three("caacabbbba")']:
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
